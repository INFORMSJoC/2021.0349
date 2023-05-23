#!/usr/bin/python3

from argparse import ArgumentParser
from pathlib import Path
from typing import List, Tuple, Union

import numpy
import pandas
from tabulate import tabulate


def print_with_descriptive_rows(frame: pandas.DataFrame, headers: List[str], floatfmt: Union[str, Tuple[str, ...]]) -> None:
    epilogue = frame.agg(['min', 'max', 'median', 'mean'])
    print(tabulate(frame.append(epilogue), headers=headers, floatfmt=floatfmt))


def check_counts(costs: pandas.DataFrame, expectation: int) -> None:
    all_values = costs['len'].values.flatten('K')
    all_present_values = map(int, filter(pandas.notna, all_values))
    distinct_values = set(all_present_values)
    if distinct_values == {expectation}: return
    explanation = 'values include {}; expected to only see {}'.format(distinct_values, expectation)
    raise ValueError(explanation)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument('results_directory', help='directory containing results CSV files; defaults to directory containing this script', nargs='?', type=Path, default=Path(__file__).parent)
    options = parser.parse_args()

    ###################################################################
    #
    #  load various data tables for later use
    #

    def read_csv(path_stem: str) -> pandas.DataFrame:
        return pandas.read_csv(options.results_directory / (path_stem + '.csv'))

    # per_build_index_columns = ('application', 'version', 'instrumentor')
    # per_function_index_columns = per_build_index_columns + ('trial', 'function')
    # lemon_coarse = read_csv('lemon-coarse', index_col=per_function_index_columns)
    # lemon_fine = read_csv('lemon-fine', index_col=per_function_index_columns + ('iteration',))

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
    #  show facts of interest, derived from the above data tables
    #

    print('Compilation times for LEMON relative to local; lower is better:\n')
    timings = compile_results.pivot_table(index='application', values='compiletime', columns='instrumentor', aggfunc=[len, numpy.mean])
    relative = pandas.DataFrame(index=timings.index)
    for site_kind in 'bb', 'cc':
        relative[site_kind] = timings['mean', site_kind + '-lemon'] / timings['mean', site_kind + '-local']
    print_with_descriptive_rows(relative, headers=['application'] + relative.columns.tolist(), floatfmt='.0%')
    print('\n')

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


if __name__ == '__main__':
    main()
