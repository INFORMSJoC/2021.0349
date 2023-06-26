[![INFORMS Journal on Computing Logo](https://INFORMSJoC.github.io/logos/INFORMS_Journal_on_Computing_Header.jpg)](https://pubsonline.informs.org/journal/ijoc)

# A Set Covering Approach to Customized Coverage Instrumentation

This archive is distributed in association with the [INFORMS Journal on
Computing](https://pubsonline.informs.org/journal/ijoc) under the [Apache 2.0 License](LICENSE).

The software and data in this repository are a snapshot of the software and data that were used in the research reported on in the paper [A Set Covering Approach to Customized Coverage Instrumentation](https://doi.org/10.1287/ijoc.2019.0000) by Michini et al. The snapshot is based on [tag v1.4.0](https://github.com/liblit/csi-cc/releases/tag/v1.4.0) in the development repository. 

**Important: This code is being developed on an on-going basis at [https://github.com/liblit/csi-cc](https://github.com/liblit/csi-cc). Please go there if you would like to get a more recent version.**

## Cite

To cite the contents of this repository, please cite both the paper and this repo, using their respective DOIs.

https://doi.org/10.1287/ijoc.2021.0349

https://doi.org/10.1287/ijoc.2019.0349.cd

Below is the BibTex for citing this snapshot of the repository

```
@misc{michini.et.al-22,
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
Just running the command 
```build-llvm```
in the scripts/ directory should be sufficient to download and build all necessary software.  If users have these tools already installed on their system, this step may be omitted. 


### Building csi-cc

The main program csi-cc uses the [Scons](https://scons.org/) software construction tool for building.
Building csi-cc with the integer-programming based optimal program instrumentation requires both the LEMON and Gurobi to be installed. 
Lemon may be obtained from [the Lemon Graph Library Web Site](https://lemon.cs.elte.hu/trac/lemon).  Gurobi is available for academic use from the [Gurobi Academic Program and Liicenses page](https://www.gurobi.com/academia/academic-program-and-licenses/).

There are instructions for building and running the csi-cc code in the src/docs directory.  For most users, the command 
```
scons LLVM_CONFIG=/path/to/llvm-config LEMONDIR=/path/to/lemon GUROBIDIR=/path/to/gurobi
```
should build the compiler, assuming all necessary dependencies are installed.  The compiler will be created in the src/Release directory with the executable/compiler csi-cc and associated library libCSI.so.


## Results

In the data directory, we have placed many of the C codes that we used 

Other applications from the paper may be retrieved from the 
[Software-artifact Infrastructure Repository](https://sir.csc.ncsu.edu/portal/index.php). 

Also in the data directory, there is a script run-all.sh that demonstrates how to compile the example codes using the csi-cc compiler, instrumented with the integer-programming-based to optimize program coverage.  The sample script makes use of a special ijoc-{bb,cc}.schema files (located in the src/schemas directory) that will allow for complete compilation of all the sample programs, by 'bypassing' instrumentation of functions that take too long to compile.  Note that this is not the same configuration used in generating results for the paper, where instead, comiles were allowed to time out after 3 hours. 


## Replicating

Replicating all of the results would be an incredibly time-consuming process.  Instead, we have put the raw text files containing results from each run in the results/ directory. 
The figures can be created by running the scripts in the results directory.  There is a README file in that directory explaining how to generate all figures and tables from the paper.



## Ongoing Development

This code is being developed on an on-going basis at 
[https://github.com/liblit/csi-cc](https://github.com/liblit/csi-cc). Please go there if you would like to get a more recent version of the packages. 
