# Working Notes

These are working notes for Peter and Jeff to write up instructions for the README.

Users are likely to need a version of llvm compiled from scratch (to ensure assertions are active) in order to get debug/print support

## Dependencies 

llvm
clang
compiler-rt   
Also needed to install libopt-dev 

(Need all with assertions enabled, so use the make script to build that is in your llvm)

Jeff -- put the doc

Someone needs to tell the compiler the following flags
LLVM_CONFIG=/path/to/llvm-config


~/llvm/5.10.60.1-microsoft-standard-WSL2/install
(???) I am not sure what this was...

## Folders 

src/
Peter will make a release snapshot and move the code into our src dir

results/
Essentially be a copy of pldi-2019/results folder.

scripts/
(This will contain the 'make' -> Rename, to download and build LLVM)

data/
This contains the source code for the applications that are *not* part of the SIR infrastructure repository

docs/
README.md  -> Nothing to see here.  See csi-cc documentation.


# Jeff compiling notes 

For bc, setting 
export CC="${HOME}/git-mods/csi-cc-private/Release/csi-cc";
export CFLAGS="--trace=${HOME}/git-mods/csi-cc-private/schemas/bb.schema -csi-opt=3 -opt-style=lemon -log-stats"
./configure
(Ran with turning off yyparse)

Try this for bc 
./configure "CC=${HOME}/git-mods/csi-cc-private/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -fno-builtin --trace=${HOME}/git-mods/csi-cc-private/schemas/bb.schema -csi-opt=3 -opt-style=lemon -log-stats" 


For ccrypt need
./configure "CC=${HOME}/git-mods/csi-cc-private/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -fno-builtin --trace=${HOME}/git-mods/csi-cc-private/schemas/bb.schema -csi-opt=3 -opt-style=lemon -log-stats" 
make


For libexif do 
./configure "CC=${HOME}/git-mods/csi-cc-private/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -fno-builtin --trace=${HOME}/git-mods/csi-cc-private/schemas/bb.schema -csi-opt=3 -opt-style=lemon -log-stats"  --prefix=${PWD}/install
make
make install



For exif try  
./configure "CC=${HOME}/git-mods/csi-cc-private/Release/csi-cc -g -std=gnu89 --trace=${HOME}/git-mods/csi-cc-private/schemas/bb.schema -csi-opt=3 -opt-style=lemon -log-stats -I../libexif-0.6.10/install/include" "PKG_CONFIG_PATH=../libexif-0.6.10/install/lib/pkgconfig"

Also needed to install pkg-config 
Also needed to install libopt-dev 


For gcc
This you built with scons 
'-std=gnu89', '-Wno-unused-value', '-Wno-parentheses',
                '-Wno-switch', '-Wno-conversion', '-Wno-format',
                '-Wno-return-type'

export CC="${HOME}/git-mods/csi-cc-private/Release/csi-cc";
export CFLAGS="-std=gnu89 -Wno-tautological-constant-out-of-range-compare -Wno-switch -Wno-implicit-function-declaration -Wno-parentheses -Wno-enum-conversion -Wno-format --trace=${HOME}/git-mods/csi-cc-private/schemas/bb.schema -csi-opt=3 -opt-style=lemon -log-stats"
Then just do scons 

Add your SConstruct (edited SConctrcuted to build)
Then just scons 


##  


jeff -> Turn off Gurobi license stuff (in C++)
Also, maybe not MaxDepth print 

https://support.gurobi.com/hc/en-us/articles/360044784552-How-do-I-suppress-all-console-output-from-Gurobi-