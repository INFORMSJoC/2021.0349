#!/usr/bin/python3

from argparse import ArgumentParser
from pathlib import Path
from sys import stdout
from typing import List, Tuple, Union

import numpy
import pandas

def print_with_descriptive_rows(frame: pandas.DataFrame, headers: List[str], floatfmt: Union[str, Tuple[str, ...]]) -> None:
    # imports in here, so extra libraries aren't required to generate CSV
    from tabulate import tabulate
    import warnings
    warnings.simplefilter(action='ignore', category=FutureWarning)

    epilogue = frame.agg(['min', 'max', 'median', 'mean'])
    print(tabulate(frame.append(epilogue), headers=headers, floatfmt=floatfmt))

def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('results_directory', help='directory containing results CSV files; defaults to directory containing this script', nargs='?', type=Path, default=Path(__file__).parent)
    parser.add_argument('--prettyprint', dest='pprint', help='produce human-readable output (rather than CSV)', action='store_true')
    options = parser.parse_args()

    ###################################################################
    #
    #  load various data tables for later use
    #

    def read_csv(path_stem: str) -> pandas.DataFrame:
        return pandas.read_csv(options.results_directory / (path_stem + '.csv'))

    # discard compile results where success is False; these failed to compile
    # discard compile results for simple and none instrumentors; we don't subsequently use these
    compile_results = read_csv('compile-results')
    compile_results = compile_results[compile_results['success'] & compile_results['instrumentor'].str.contains('-l')]
    compile_results.set_index(['application', 'version', 'instrumentor'], inplace=True)

    # for this CSV file, nothing can ever vary from one trial to another, making the "trial" column useless
    # also, discard any rows corresponding to failed or ignored compilations
    solution = read_csv('solution')
    solution = solution[solution['trial'] == 1]
    solution.drop(columns='trial', inplace=True)
    solution.set_index(['application', 'version', 'instrumentor'], inplace=True)
    first_compilation = compile_results[compile_results['trial'] == 1]
    solution = solution.join(first_compilation, how='inner')

    ###################################################################
    #
    # Relative timings (only used for filtering in this script)
    #

    timings = compile_results.pivot_table(index='application', values='compiletime', columns='instrumentor', aggfunc=[len, numpy.mean])
    relative = pandas.DataFrame(index=timings.index)
    for site_kind in 'bb', 'cc':
        relative[site_kind] = timings['mean', site_kind + '-lemon'] / timings['mean', site_kind + '-local']

    ###################################################################
    #
    #  Count how often lemon gets a more optimal solution than
    #  local (both absolute and percentage of functions).
    #

    costs = solution.pivot_table(index=['application', 'version', 'function', 'file'], values='objectiveValue', columns='instrumentor', aggfunc=[len, numpy.mean])
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
    combined = pandas.concat([different_count, different_fraction], axis=1, keys=('count', 'percent'))
    if options.pprint:
        print('Functions where costs of LEMON and local solutions differ; higher is better:\n')
        headers = ['\napplication'] + list(map('\n'.join, combined.columns.tolist()))
        print_with_descriptive_rows(combined, headers=headers, floatfmt=('s', '.0f', '.0f', '.1%', '.1%'))
    else:
        # flatten column names
        combined.columns = ['%s-%s' % (instr_type, agg_style) \
                            for agg_style, instr_type in combined.columns]
        combined = combined.reindex(sorted(combined.columns), axis=1)
        # remove decimal points in integer columns by converting to strings; ignore NaNs
        for col in combined.columns:
            if 'count' in col:
                combined[col] = combined[col].map(lambda n : '' if pandas.isna(n) else '%.0f' % n)
        combined.to_csv(stdout, float_format='%.3f')

if __name__ == '__main__':
    main()
