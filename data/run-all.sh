#!/bin/bash

# You need to set this to point to your csi-cc installation
CSI_CC_DIR=${HOME}/git-mods/2021.0349/src


cd tcas/src
echo "Making tcas with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats tcas.c > ../../tcas-bb.out 2>&1
echo "Making tcas with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats tcas.c > ../../tcas-cc.out 2>&1
cd ../..

cd schedule2/src
echo "Making schedule2 with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-parentheses -Wno-implicit --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats schedule2.c > ../../schedule2-bb.out 2>&1
echo "Making schedule2 with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-parentheses -Wno-implicit --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats schedule2.c > ../../schedule2-cc.out 2>&1
cd ../..

cd schedule/src
echo "Making schedule with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-return-type -Wno-macro-redefined -Wno-implicit --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats schedule.c > ../../schedule-bb.out 2>&1
echo "Making schedule with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-return-type -Wno-macro-redefined -Wno-implicit --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats schedule.c > ../../schedule-cc.out 2>&1
cd ../..

cd replace/src
echo "Making replace with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats replace.c > ../../replace-bb.out 2>&1
echo "Making replace with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats replace.c > ../../replace-cc.out 2>&1
cd ../..

cd totinfo/src
echo "Making totinfo with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -lm -g -std=gnu89 -Wno-comment -Wno-return-type --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats tot_info.c > ../../totinfo-bb.out 2>&1
echo "Making totinfo with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -lm -g -std=gnu89 -Wno-comment -Wno-return-type --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats tot_info.c > ../../totinfo-cc.out 2>&1
cd ../..

cd printtokens2/src
echo "Making printtokens2 with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89  -Wno-return-type -Wno-implicit --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats print_tokens2.c > ../../printtokens2-bb.out 2>&1
echo "Making printtokens2 with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-return-type -Wno-implicit --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats print_tokens2.c > ../../printtokens2-cc.out 2>&1
cd ../..

cd printtokens/src
echo "Making printtokens with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89  -Wno-return-type -Wno-implicit -Wno-empty-body --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats print_tokens.c > ../../printtokens-bb.out 2>&1
echo "Making printtokens with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-return-type -Wno-implicit -Wno-empty-body --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats print_tokens.c > ../../printtokens-cc.out 2>&1
cd ../..

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

cd gzip/src
echo "Making gzip with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89  -DSTDC_HEADERS=1 -DHAVE_UNISTD_H=1 -DDIRENT=1 -DHAVE_ALLOCA_H=1 --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats allfile.c > ../../gzip-bb.out 2>&1
echo "Making gzip with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -DSTDC_HEADERS=1 -DHAVE_UNISTD_H=1 -DDIRENT=1 -DHAVE_ALLOCA_H=1 --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats allfile.c > ../../gzip-cc.out 2>&1
cd ../..

cd space/src
echo "Making space with basic block coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-parentheses -Wno-deprecated-declarations -Wno-unused-comparison -Wno-format --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats space.c > ../../space-bb.out 2>&1
echo "Making space with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-parentheses -Wno-deprecated-declarations -Wno-unused-comparison -Wno-format --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats space.c > ../../space-cc.out 2>&1
cd ../..


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


cd sed/src
# echo "Making sed with basic block coverage"
# ${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-dangling-else -Wno-non-literal-null-conversion -Wno-int-to-pointer-cast --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats sed.c > ../../sed-bb.out 2>&1
echo "Making sed with call site coverage"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-dangling-else -Wno-non-literal-null-conversion -Wno-int-to-pointer-cast --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats sed.c > ../../sed-cc.out 2>&1
cd ../..

cd flex/src
# echo "Making sed with basic block coverage"
# ${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-dangling-else -Wno-non-literal-null-conversion -Wno-int-to-pointer-cast --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats sed.c > ../../sed-bb.out 2>&1
echo "Making flex with call site coverage. (Won't link as needs library)"
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-implicit -Wno-incompatible-library-redeclaration  --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats flex.c > ../../flex-cc.out 2>&1
cd ../..

cd grep/src
echo "Making grep with basic block coverage."
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-format -Wno-dangling-else -Wno-non-literal-null-conversion -Wno-int-to-pointer-cast -Wno-switch -Wno-logical-op-parentheses --trace=${CSI_CC_DIR}/schemas/ijoc-bb.schema -csi-opt=3 -opt-style=lemon -log-stats grep.c > ../../grep-bb.out 2>&1
echo "Making grep with call site coverage."
${CSI_CC_DIR}/Release/csi-cc -g -std=gnu89 -Wno-format -Wno-dangling-else -Wno-non-literal-null-conversion -Wno-int-to-pointer-cast -Wno-switch -Wno-logical-op-parentheses --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats grep.c > ../../grep-cc.out 2>&1
cd ../..

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

# bash 
cd bash/src
echo "Making bash with call site coverage"
./configure "CC=/home/jeff/git-mods/2021.0339/src/Release/csi-cc -g -std=gnu89 --trace=${CSI_CC_DIR}/schemas/ijoc-cc.schema -csi-opt=3 -opt-style=lemon -log-stats"
make > ../../bash-cc.out 2>&1
make clean
cd ../..


