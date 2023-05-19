[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# A Set Covering Approach to Customized Coverage Instrumentation

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [Apache 2.0 License](LICENSE).

The software and data in this repository are a snapshot of the software and data
that were used in the research reported on in the paper 
[A Set Covering Approach to Customized Coverage Instrumentation](https://doi.org/10.1287/ijoc.2019.0000) by Michini et al. 
The snapshot is based on 
[tag v1.4.0](https://github.com/liblit/csi-cc/releases/tag/v1.4.0) 
in the development repository. 

**Important: This code is being developed on an on-going basis at 
[https://github.com/liblit/csi-cc](https://github.com/liblit/csi-cc). Please go there if you would like to
get a more recent version.**

## Cite

To cite the contents of this repository, please cite both the paper and this repo, using their respective DOIs.

https://doi.org/10.1287/ijoc.2019.0000

https://doi.org/10.1287/ijoc.2019.0000.cd

Below is the BibTex for citing this snapshot of the repository

```
@article{CacheTest,
  author =        {Carla Michini and Peter Ohmann and Ben Liblit and Jeff Linderoth},
  publisher =     {INFORMS Journal on Computing},
  title =         {{A Set Covering Approach to
Customized Coverage Instrumentation}},
  year =          {2022},
  doi =           {10.1287/ijoc.2021.0349.cd},
  url =           {https://github.com/INFORMSJoC/2021.0349},
}  
```

## Description

This software is an instrumenting compiler for lightweight, customizable control-flow tracing.  The compiler has embedded within it calls to the mixed-integer programming package Gurobi to implement the cutting plane method as described in the paper.

## Building

First, one needs to build the csi-cc compiler.  Entering the src directory and typing 
```
scons
```
should build the compiler, assuming all necessary dependencies are installed.  

* scons
* llvm 
* clang 
* pkg-config 
* libopt-dev 

(This should make in src a Release directory) with the executable/compiler csi-cc and associated library libCSI.so



## Results

Figure 1 in the paper shows the results of the multiplication test with different
values of K using `gcc` 7.5 on an Ubuntu Linux box.

![Figure 1](results/mult-test.png)

Figure 2 in the paper shows the results of the sum test with different
values of K using `gcc` 7.5 on an Ubuntu Linux box.

![Figure 1](results/sum-test.png)

## Replicating

To replicate the results in [Figure 1](results/mult-test), do either

```
make mult-test
```
or
```
python test.py mult
```
To replicate the results in [Figure 2](results/sum-test), do either

```
make sum-test
```
or
```
python test.py sum
```

## Ongoing Development

This code is being developed on an on-going basis at the author's
[Github site](https://github.com/tkralphs/JoCTemplate).

## Support

For support in using this software, submit an
[issue](https://github.com/tkralphs/JoCTemplate/issues/new).
