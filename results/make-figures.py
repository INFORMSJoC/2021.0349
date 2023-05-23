from argparse import ArgumentParser
from pathlib import Path
from scipy.stats import mstats

import os
import numpy
import pandas


###################################################################
#
#      load compile time/memory results
#
def group_and_csv(results_table, agg_style, output_dir, file_name):
    summary = results_table.fillna(numpy.nan).groupby(['application', 'version', 'instrumentor']).agg(agg_style)
    summary = summary.fillna(numpy.nan).groupby(['application', 'instrumentor']).agg(agg_style)
    summary.to_csv(os.path.join(output_dir, file_name), float_format='%.6g')

def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('results_directory', help='directory containing results CSV files; defaults to directory containing this script', nargs='?', type=Path, default=Path(__file__).parent)
    parser.add_argument('output_directory', help='directory in which to place generated CSV files; defaults to cwd', nargs='?', type=Path, default=os.getcwd())
    parser.add_argument('--failures', dest='do_all_agg', help='produce percent time/memory out CSV file (all_agg.csv)', action='store_true')
    parser.add_argument('--successes', dest='do_success_only', help='produce relative-time CSV file including only success runs (success_only.csv)', action='store_true')
    parser.add_argument('--saturated', dest='do_saturated', help='produce relative-time CSV file with saturated timeouts (saturated.csv)', action='store_true')
    options = parser.parse_args()

    ###################################################################
    #
    #  load compile time/memory results
    #

    def read_csv(path_stem: str) -> pandas.DataFrame:
        return pandas.read_csv(options.results_directory / (path_stem + '.csv'))

    compile_results = read_csv('compile-results')
    compile_results['failurereason'].fillna('', inplace=True)
    compile_results['failurereason'] = compile_results['failurereason'].str.strip()
    compile_results.drop(compile_results.loc[compile_results['instrumentor'] == 'clang'].index, inplace=True)

    ###################################################################
    #
    #  add columns for summarizing
    #

    # add columns for percent time/memory out
    compile_results['percenttimeout'] = 0.0
    compile_results['percentmemout'] = 0.0
    compile_results.loc[compile_results['failurereason'] == 'TIMEOUT', 'percenttimeout'] = 1.0
    compile_results.loc[compile_results['failurereason'] == 'MEMOUT', 'percentmemout'] = 1.0

    # verify only failures have failure reasons
    assert (compile_results[compile_results['success']]['failurereason'] == '').all()
    assert compile_results[~compile_results['success']]['failurereason'].isin(['TIMEOUT', 'MEMOUT']).all()

    # add column for base (none instrumentor) time
    instrumentor_prefixes = compile_results['instrumentor'].str.slice(stop=2)
    assert instrumentor_prefixes.isin(['bb', 'cc']).all()
    compile_results['baseinstrumentor'] = instrumentor_prefixes + '-none'
    compile_results = compile_results.merge(compile_results, 'left',
                                            left_on=['application', 'version', 'trial', 'baseinstrumentor'],
                                            right_on=['application', 'version', 'trial', 'instrumentor'],
                                            suffixes=('', '_BASE'), validate='many_to_one')

    compile_results['relativetime'] = compile_results['compiletime'] / compile_results['compiletime_BASE']


    agg_style = {'relativetime': mstats.gmean,
                 'percenttimeout': numpy.average,
                 'percentmemout': numpy.average}


    ###################################################################
    #
    #  Straight aggregation (trials, then versions).
    #  Likely most useful for percent timeout and memout, since
    #  "time relative to unoptimized" is meaningless
    #

    if options.do_all_agg:
        group_and_csv(compile_results,
                      {'percenttimeout': numpy.average, 'percentmemout': numpy.average},
                      str(options.output_directory), 'all_agg.csv')

    ###################################################################
    #
    #  Filter to results for only successful runs (dropping all
    #  *versions* that have a time or memory out for LEMON, LOCAL,
    #  or SIMPLE)
    #  One possible comparison for time relative to unoptimized.
    #

    if options.do_success_only:
        successful_results = compile_results[compile_results['success']].copy()
        for (row_num, row_data) in compile_results.iterrows():
            opt_style = row_data['instrumentor'].split('-')[-1].strip()
            if opt_style in ('lemon', 'local', 'simple') and row_data['success'] == False:
                # drop *all* rows for this app.version, so we only compare
                # times for versions that completed for *all* relevant solvers
                # see these pages for explanation of how the next line works:
                # https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression#answer-27360130
                # https://stackoverflow.com/questions/36921951/truth-value-of-a-series-is-ambiguous-use-a-empty-a-bool-a-item-a-any-o#answer-36922103
                successful_results.drop(successful_results[(successful_results.application == row_data['application']) & \
                                                               (successful_results.version == row_data['version'])].index,
                                        inplace=True)
        group_and_csv(successful_results,
                      {'relativetime': mstats.gmean},
                      str(options.output_directory), 'success_only.csv')


    ###################################################################
    #
    #  Set all timeout to MAX time.  Then aggregate.
    #  Another possible comparison for time relative to unoptimized.
    #  Gives a *lower bound* on the improvement from local to lemon.
    #

    if options.do_saturated:
        # 3 hours in seconds
        MAX_TIME = 3 * 60 * 60

        # filter out MEMOUT results
        mem_outs_mask = compile_results['failurereason'] == 'MEMOUT'
        mem_outs = compile_results[mem_outs_mask]
        assert(mem_outs['instrumentor'].str.contains('gams').all())
        max_time_results = compile_results[~mem_outs_mask]

        # new column for compile time (saturated to MAX time)
        time_outs_mask = compile_results['failurereason'] == 'TIMEOUT'
        compile_results['saturatedcompiletime'] = compile_results['compiletime'].where(~time_outs_mask, MAX_TIME)
        compile_results['saturatedrelativetime'] = compile_results['saturatedcompiletime'] / compile_results['compiletime_BASE']
        group_and_csv(compile_results[~mem_outs_mask],
                      {'saturatedrelativetime' : mstats.gmean},
                      str(options.output_directory), 'saturated.csv')

    ###################################################################
    #
    #  Count how often lemon gets a more optimal solution than
    #  local (both absolute and percentage of functions).
    #

    """ TODO """

    """
    print('Functions where costs of LEMON and local solutions differ; higher is better:\n')
    costs = solution.pivot_table(index=['application', 'version', 'function', 'file'], values='objectiveValue', columns='instrumentor', aggfunc=[len, numpy.mean])
    check_counts(costs, 1)
    different = pandas.DataFrame(index=costs.index)
    for site_kind in 'bb', 'cc':
        lemon_costs = costs['mean', site_kind + '-lemon']
        local_costs = costs['mean', site_kind + '-local']
        same_costs = lemon_costs.isna() | local_costs.isna() | (lemon_costs == local_costs)
        different[site_kind] = ~same_costs
    different = different.groupby(level=['application'])
    different_count = different.sum()
    different_count = different_count.mask(relative.isna())
    different_fraction = different_count / different.count()
    combined = pandas.concat([different_count, different_fraction], axis=1, keys=('count', 'fraction'))
    headers = ['\napplication'] + list(map('\n'.join, combined.columns.tolist()))
    print_with_descriptive_rows(combined, headers=headers, floatfmt=('s', '.0f', '.0f', '.0%', '.0%'))
    """


if __name__ == '__main__':
    main()
