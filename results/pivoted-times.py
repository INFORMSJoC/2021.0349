from itertools import product
from pandas import read_csv
from pathlib import Path
from scipy.stats.mstats import gmean
from sys import stdout


def main() -> None:
    results_dir = Path(__file__).parent

    wanted_instrumentors = list(map('-'.join, product(
        ('bb', 'cc'),
        ('local', 'lemon'),
    )))

    times = read_csv(results_dir / 'saturated.csv')
    times = times[times['instrumentor'].isin(wanted_instrumentors)]

    pivoted = times.pivot(
        index='application',
        columns='instrumentor',
        values='saturatedrelativetime',
    ).join(
        read_csv(
            results_dir / 'c-applications.csv',
            index_col='Application',
            usecols=['Application', 'Description', 'Mean LOC'],
            squeeze=True,
        ),
    )
    pivoted = pivoted[pivoted['Description'] != 'Siemens']
    pivoted = pivoted.sort_values('Mean LOC').drop(columns=['Description', 'Mean LOC'])

    mean_label = r'geom.\\mean'
    pivoted.index = pivoted.index.str.replace('_', '\\_')
    pivoted.loc[mean_label] = gmean(pivoted)

    # A hack (due to time): re-calculate the geometric mean for BB, ignoring missing data.
    # Specifically, manually edit those applications that run out of time on
    # *all* tests for both LOCAL and LEMON.
    # Unfortunately, we are setting these to 1.0.  NaN would be cleaner, but
    # I'm not sure how to handle it well in tikz.
    missingApps = ('gcc', 'grep')
    missingColumns = ('bb-local', 'bb-lemon')
    for column in missingColumns:
        for app in missingApps:
            # set it to 1.0, since this is the closest I could get to a "missing
            # bar" while still showing the x label in TeX
            pivoted.loc[app, column] = 1.0
        pivoted.loc[mean_label, column] = gmean(pivoted[~pivoted.index.isin(missingApps+(mean_label,))][column])

    pivoted['position'] = range(len(pivoted))
    pivoted.loc[mean_label, 'position'] += 1
    pivoted.to_csv(stdout, columns=['position'] + wanted_instrumentors, float_format='%.6g')


if __name__ == '__main__':
    main()
