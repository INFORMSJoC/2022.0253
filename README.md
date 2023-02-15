[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# Boot-sp

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [3-clause BSD License](LICENSE).

The software and data in this repository are a snapshot of the software and data
described in the paper
["Software for data-based stochastic programming using bootstrap estimation"](https://doi.org/aa.bbbb/ijoc.yyy.zzzz) by X. Chen and D.L. Woodruff.
The snapshot corresponds to tag v0.1.0-beta on [boot-sp github](https://github.com/boot-sp/boot-sp)


**Important: This code is being developed on an on-going basis at 
https://github.com/boot-sp/boot-sp) Please go there if you would like to
get a more recent version or would like support**

## Cite

To cite this software, please cite the [paper](https://doi.org/aa.bbbb/ijoc.yyy.zzzz) using its DOI and the software itself, using the following DOI.

[![DOI](https://zenodo.org/badge/cccc.svg)](https://zenodo.org/badge/latestdoi/cccc)

Below is the BibTex for citing this snapshot version of the code.

```
@article{boot-sp,
  author =        {X.\ Chen and D.L.\ Woodruff},
  publisher =     {INFORMS Journal on Computing},
  title =         {{boot-sp} tag v0.1.0-beta},
  year =          {2023},
  doi =           {10.5281/zenodo.cccc},
  url =           {https://github.com/INFORMSJoC/2022.0253},
}  
```

## Description

Data-based, two-stage stochastic programming using bootstrap and bagging for confidence intervals.

## Building

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

From the directory where you downloaded boot-sp, which for this archive is 2022.0253,
give the command

- python setup.py develop

or

- python setup.py install


## Documentation

There is documentation on [readthedocs](https://boot-sp.readthedocs.io/en/latest/). Note: If
you want to use this archive instead of the current version, the directory named
mpi-sppy will not exist. That directory name is 2022.0253 for this archive.

## Running Examples in the online supplement

If you want to run the examples (either with this archive version or the current version)
see the file README.md and the slurm scripts in the examples/paper_runs directory.



