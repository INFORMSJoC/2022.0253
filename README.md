[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# Boot-sp

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [3-clause BSD License](LICENSE).

The software and data in this repository are a snapshot of the software and data
described in the paper
["Software for data-based stochastic programming using bootstrap estimation"](https://doi.org/10.128/ijoc.2022.0253) by X. Chen and D.L. Woodruff.
The snapshot corresponds to [tag v0.1.0-beta](https://github.com/boot-sp/boot-sp/releases/tag/v0.1.0-beta)


**Important: This code is being developed on an on-going basis at 
https://github.com/boot-sp/boot-sp Please go there if you would like to
get a more recent version or would like support.**

## Cite

To cite the contents of this respository, please cite both the paper and this repo, using their respective DOIs.

https://doi.org/10.1287/ijoc.2022.0253

https://doi.org/10.1287/ijoc.2022.0253.cd

Below is the BibTex for citing this snapshot version of the code.

```
@article{boot-sp,
  author =        {X.\ Chen and D.L.\ Woodruff},
  publisher =     {INFORMS Journal on Computing},
  title =         {{boot-sp} v2022.0253},
  year =          {2023},
  doi =           {10.1287/ijoc.2022.0253.cd},
  url =           {https://github.com/INFORMSJoC/2022.0253},
}  
```

## Description

Data-based, two-stage stochastic programming using bootstrap and bagging for confidence intervals.

## Building

## Dependencies

This snapshot version should work with

- Python 3.8-3.11
- Pyomo 6.4.2
- mpi-sppy: release 0.11.1 should work, but tag 0.11.1.1 might be better

If you really want to run this snapshot version and not the current version of boot-sp, then
you probably should make sure you have these versions of Pyomo and mpi-sppy
before you run setup.py for boot-sp because setup.py will get current versions of these
dependencies, which might not work with this snapshot in the future.

There are various dependencies for mpi-sppy; most importantly, it would like to have mpi4py available, but can do some things without it.

This software could work on Windows machines in principle, but it has only been tested on *nix machines.
Installation (particularly of MPI and mpi4py) on Windows may be challenging.

## Running setup.py

From the directory where you downloaded boot-sp, which for this shapshot is 2022.0253,
give the command

```
python setup.py develop
```

or

```
python setup.py install
```

## Documentation

There is documentation on [readthedocs](https://boot-sp.readthedocs.io/en/latest/). Note: If
you want to use this snapshot instead of the current version, the directory named
mpi-sppy will not exist. That directory name is 2022.0253 for this snapshot.

## Running Examples in the online supplement

If you want to run the examples (either with this snapshot version or the current version)
see the file README.md and the slurm scripts in the examples/paper_runs directory.



