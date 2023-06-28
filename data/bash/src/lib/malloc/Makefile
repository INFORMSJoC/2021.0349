# Generated automatically from Makefile.in by configure.
# Skeleton Makefile for the GNU malloc code
#

srcdir = .
VPATH = .:.
topdir = ../..
BUILD_DIR = /home/jeff/git-mods/2021.0349/data/bash/src

INSTALL = /usr/bin/install -c
INSTALL_PROGRAM = ${INSTALL}
INSTALL_DATA = ${INSTALL} -m 644

CC = gcc
RANLIB = ranlib
AR = ar
RM = rm -f
CP = cp
MV = mv

CFLAGS = -g -O2
LOCAL_CFLAGS = 
CPPFLAGS = 
LDFLAGS = 

DEFS = -DHAVE_CONFIG_H

INCLUDES = -I. -I../.. -I$(topdir) -I$(topdir)/lib

CCFLAGS = ${INCLUDES} $(DEFS) $(LOCAL_CFLAGS) $(CFLAGS) $(MALLOC_CFLAGS) $(CPPFLAGS)

.c.o:
	$(CC) $(CCFLAGS) -c $<

.s.o:
	$(CC) $(CCFLAGS) -c $<

MALLOC_SOURCE = malloc.c

ALLOCA_SOURCE = alloca.c
ALLOCA_OBJECT = alloca.o

MALLOC_SRC = $(ALLOC_LIBSRC)/malloc.c
MALLOC = malloc.o
ALLOCA = 

libmalloc.a:	$(MALLOC) $(ALLOCA) stub.o
	$(RM) $@
	$(AR) cr $@ $(MALLOC) $(ALLOCA) stub.o
	-test -n "$(RANLIB)" && $(RANLIB) $@

malloc.o: malloc.c getpagesize.h

alloca.o:	$(ALLOCA_SOURCE)
	$(CC) $(CCFLAGS) -c $(ALLOCA_SOURCE)
	@- if test "$(ALLOCA_OBJECT)" != alloca.o ; then \
		mv $(ALLOCA_OBJECT) alloca.o >/dev/null 2>&1 ; \
	fi

mostlyclean clean:
	$(RM) *.o libmalloc.a

distclean realclean maintainer-clean: clean
	$(RM) Makefile

alloca.o: $(BUILD_DIR)/config.h
malloc.o: $(BUILD_DIR)/config.h
xmalloc.o: $(BUILD_DIR)/config.h
gmalloc.o: $(BUILD_DIR)/config.h
