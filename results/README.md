# Raw Data and Plot Generation for "A Set Covering Approach to Customized Coverage Instrumentation"

This directory contains the raw data and scripts used to generate all result
plots and figures in the paper 
[A Set Covering Approach to Customized Coverage Instrumentation](https://doi.org/10.1287/ijoc.2021.0349)
by Michini et al.

## Table 2

This table is generated directly from file [c-applications.csv](c-applications.csv).

## Table 3

This table is generated in two steps from the raw data.  First, to generate a CSV
file containing the percentage of compilations for each application that ran out of
time and (separately) the percentage of compilations that ran out of memory, run
the command:
```
python3 make-figures.py --failures
```
This will produce a file named `all_agg.csv` containing the percentage of time- and
memory-out runs for each application.

To summarize and pivot this data into a CSV file that matches the table from the
paper, run the command:
```
python3 pivoted-failures.py
```
Columns prefixed with `bb-` refer to `Basic Blocks` results; those with `cc-` refer
to `Call Sites`.  Columns labeled with `-gams` refer to the `netflow` solver; those
labeled with `-local` refer to the locally-optimal solver; those labeled with
`-lemon` refer to the new `set-cover` solver.

Both scripts to generate this table require [Python 3](https://www.python.org/)
,the [pandas](https://pandas.pydata.org/) library,
the [NumPy](https://numpy.org/) library, and the
[SciPy](https://scipy.org/) library.

The raw data used for this table is provided in
[compile-results.csv](compile-results.csv), which contains the raw measured
timings and memory usage for each compilation, per section 4.1 of
[the paper](https://doi.org/10.1287/ijoc.2021.0349).

## Table 4

To generate a CSV file containing the results for this table,
simply run the [compile-times.py](compile-times.py) script.
This script requires [Python 3](https://www.python.org/)
and the [pandas](https://pandas.pydata.org/) library.

The raw data used for this table is provided in
[compile-results.csv](compile-results.csv), which contains the raw measured
timings for each compilation, per section 4.1 of
[the paper](https://doi.org/10.1287/ijoc.2021.0349).

## Figure 5

TODO

## Table 5

TODO

## Table 6

TODO
