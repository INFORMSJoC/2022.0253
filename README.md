# 2022.0253

## Archive version of boot-sp for the paper in IJOC

Data-based, two-stage stochastic programming using bootstrap and bagging for confidence intervals.

## Active version

This archive version corresponds to tag v0.1.0-beta on [boot-sp github](https://github.com/boot-sp/boot-sp)

## To cite:

Chen, X. and Woodruff, D.L., "Software for data-based stochastic programming using bootstrap estimation" to appear in
The INFORMS Journal on Computing, 2023.

## Documentation

There is documentation on [readthedocs](https://boot-sp.readthedocs.io/en/latest/)

## Running Examples in the online supplement

If you want to run the examples (either with this archive version or the current version)
see the file README.md and the slurm scripts in the examples/paper_runs directory.

## Dependencies

This archive version should work with

- Python 3.8-3.11
- Pyomo 6.4.2
- mpi-sppy: release 0.11.1 should work, but tag 0.11.1.1 might be better

If you really want to run this archive version and not the current version of boot-sp, then
you probably should make sure you have these versions of Pyomo and mpi-sppy
before you run setup.py because setup.py will get current versions of these
programs, which might not work with this archive in the future.

There are various dependencies for mpi-sppy; most importantly, it would like to have mpi4py available.

This software could work on Windows machines in principle, but it has only been tested on *nix machines.
Installation (particularly of mpi4py) on Windows may be challenging.

## Running setup.py

From the directory where you downloaded boot-sp, which has the name
boot-sp, give the command

$ python setup.py develop
or
$ python setup.py install

