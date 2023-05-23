from itertools import product
from pandas import read_csv
from pathlib import Path
from sys import stdout


def main() -> None:
    results_dir = Path(__file__).parent

    wanted_instrumentors = list(map('-'.join, product(
        ('bb', 'cc'),
        ('gams', 'local', 'lemon'),
    )))

    failures = read_csv(results_dir / 'all_agg.csv')
    failures = failures[failures['instrumentor'].isin(wanted_instrumentors)]
    failures['percent-any-out'] = failures['percenttimeout'] + failures['percentmemout']

    pivoted = failures.pivot(
        index='application',
        columns='instrumentor',
        values='percent-any-out',
    ).join(
        read_csv(
            results_dir / 'c-applications.csv',
            index_col='Application',
            usecols=['Application', 'Mean LOC'],
            squeeze=True,
        ),
    ).sort_values('Mean LOC').drop(columns='Mean LOC')

    pivoted.loc['mean'] = pivoted.mean()
    pivoted.to_csv(stdout, columns=wanted_instrumentors)


if __name__ == '__main__':
    main()
