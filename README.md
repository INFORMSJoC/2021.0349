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

https://doi.org/10.1287/ijoc.2021.0349

https://doi.org/10.1287/ijoc.2019.0349.cd

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

This is a large software infrastructure, so building and testing is a somewhat laborious process.


First, one needs to build the csi-cc compiler, which is based on the [llvm compiler infrastructure](https://llvm.org/).  To ensure that assertions are active and to get debug/print support, the user will need to build the tools from source using appropriate compiler flags. 

### Building LLVM 

In the scripts subdirectory, we have provided a "build-llvm" script that downloads and builds clang CFE internals (cfe), the compielr runtime (compiler-rt), and llvm.


### Building csi-cc

Building csi-cc with the integer-programming based optimal program instrumentation requires both the LEMON and Gurobi to be installed. 

(Jeff doesn't see how/where to )

```
scons
```
should build the compiler, assuming all necessary dependencies are installed.   Dependencies may include the following:

```
scons LLVM_CONFIG=??? (What is this)  LEMONDIR=/path/to/lemon GUROBIDIR=/path/to/gurobi
```


(This should make in src a Release directory with the executable/compiler csi-cc and associated library libCSI.so)



## Results

In the results directory, we put the log output from running compilation of a variety of test instances. 

Most of the test instances can be obtained from (site where Peter told Jeff)

Other applications are given in the data directory 


## Replicating

Replicating all of the results will be incredibly time consuming, 
The figures can be created by running the scripts XXX


## Ongoing Development

This code is being developed on an on-going basis at 
[https://github.com/liblit/csi-cc](https://github.com/liblit/csi-cc). Please go there if you would like to
get a more recent version
