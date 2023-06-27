#!/bin/bash

# You need to set this to point to your csi-cc installation
CSI_CC_DIR=${HOME}/git-mods/2021.0349/src

# cd bc/src 
# make clean
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -fno-builtin --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats"
# echo "Compiling bc with basic block"
# make > ../../bc-bb.out 2>&1
# make clean
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -Wno-implicit -fno-builtin --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats"
# echo "Compiling bc with call site"
# make > ../../bc-cc.out 2>&1
# cd ../..

# cd ccrypt/src
# make clean
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -Wno-implicit -fno-builtin --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats"
# echo "Compiling ccrypt with basic block"
# make > ../../ccrypt-bb.out 2>&1
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -Wno-implicit -fno-builtin --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats"
# echo "Compiling ccrypt with call site"
# make > ../../ccrypt-cc.out 2>&1
# make clean
# cd ../..

# cd exif/libexif-0.6.10
# make clean
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -Wno-format -fno-builtin --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats"
# echo "Compiling libexif with basic block"
# make > ../../libexif-bb.out 2>&1
# make install 
# cd ../..
# cd exif/exif-0.6.9
# make clean
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-enum-conversion -Wno-format --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats -I../libexif-0.6.10/install/include" "PKG_CONFIG_PATH=../libexif-0.6.10/install/lib/pkgconfig"
# echo "Making exif with basic block"
# make > ../../exif-bb.out 2>&1
# cd ../..

# cd exif/libexif-0.6.10
# make clean
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-pointer-sign -Wno-format -fno-builtin --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats"
# echo "Compiling libexif with call site"
# make > ../../libexif-cc.out 2>&1
# make install 
# cd ../..
# cd exif/exif-0.6.9
# make clean
# ./configure "CC=${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-enum-conversion -Wno-format --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats -I../libexif-0.6.10/install/include" "PKG_CONFIG_PATH=../libexif-0.6.10/install/lib/pkgconfig"
# echo "Making exif with call site"
# make > ../../exif-cc.out 2>&1
# cd ../..


# cd gcc/src
# scons --clean 
# export CC="${CSI_CC_DIR}/Release/csi-cc"
# export CFLAGS="-g -std=gnu89 -Wno-tautological-constant-out-of-range-compare -Wno-switch -Wno-implicit -Wno-parentheses -Wno-enum-conversion -Wno-format --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats"
# echo "Making gcc with basic block coverage"
# scons --no-cache > ../../gcc-bb.out 2>&1
# scons --clean 
# export CC="${CSI_CC_DIR}/Release/csi-cc"
# export CFLAGS="-g -std=gnu89 -Wno-tautological-constant-out-of-range-compare -Wno-switch -Wno-implicit -Wno-parentheses -Wno-enum-conversion -Wno-format --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats"
# echo "Making gcc with call site coverage"
# scons --no-cache > ../../gcc-cc.out 2>&1
# cd ../..


cd tcas/src
echo "Making tcas with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats tcas.c > tcas-bb.out 2>&1
echo "Making tcas with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats tcas.c > tcas-cc.out 2>&1
cd ../..

cd schedule2/src
echo "Making schedule2 with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats schedule2.c > schedule2-bb.out 2>&1
echo "Making schedule2 with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats schedule2.c > schedule2-cc.out 2>&1
cd ../..

