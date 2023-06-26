#!/bin/bash

# You need to set this to point to your csi-cc installation
CSI_CC_DIR=${HOME}/git-mods/2021.0349/src

# Run bc 
cd bc/src 
./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -Wno-implicit-function-declaration -fno-builtin --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats"
make
cd ../..

# Run ccrypt
# cd ccrypt/src
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -Wno-implicit-function-declaration -fno-builtin --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats"
# make
# cd ../..

# cd exif/libexif-0.6.10
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -Wno-format -fno-builtin --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats"
# make 
# make install 
# cd ../..

# cd exif/exif-0.6.9
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-enum-conversion -Wno-format --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats -I../libexif-0.6.10/install/include" "PKG_CONFIG_PATH=../libexif-0.6.10/install/lib/pkgconfig"
# make 
# cd ../..

cd gcc/src
export CC="${CSI_CC_DIR}/Release/csi-cc"
export CFLAGS="-g -std=gnu89 -Wno-tautological-constant-out-of-range-compare -Wno-switch -Wno-implicit-function-declaration -Wno-parentheses -Wno-enum-conversion -Wno-format --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats"
scons 
cd ../..


