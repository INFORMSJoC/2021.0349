# Generated automatically from Makefile.in by configure.
# Make sure the first target in the makefile is the right one
all: .made

# Include some boilerplate Gnu makefile definitions.
prefix = /usr/local

exec_prefix = ${prefix}
bindir = ${exec_prefix}/bin
libdir = ${exec_prefix}/lib
infodir = ${prefix}/info
includedir = ${prefix}/include

mandir = ${prefix}/man
manpfx = man

man1ext = 1
man1dir = $(mandir)/$(manpfx)$(man1ext)
man3ext = 3
man3dir = $(mandir)/$(manpfx)$(man3ext)

topdir = .
BUILD_DIR = /home/jeff/git-mods/2021.0349/data/bash/src
srcdir = .
VPATH = .:.


CC = gcc
YACC = yacc
SHELL=/bin/sh
CP = cp
RM = rm -f
AR = ar
RANLIB = ranlib

INSTALL = /usr/bin/install -c
INSTALL_PROGRAM = ${INSTALL}
INSTALL_DATA = ${INSTALL} -m 644

COMPRESS = gzip
COMPRESS_EXT = .gz

#If you have purify, and want to use it, uncomment this definition or
# run the make as `make PURIFY=purify'
# or run configure with the --with-purify argument.
PURIFY = 

# Here is a rule for making .o files from .c files that does not
# force the type of the machine (like -M_MACHINE) into the flags.
.c.o:
	$(RM) $@
	$(CC) $(CCFLAGS) -c $<

# The name of this program.
Program = bash
Machine = 
OS = 
MACHTYPE = 

RELSTATUS = release

THIS_SH = $(BUILD_DIR)/$(Program)

# PROFILE_FLAGS is either -pg, to generate profiling info for use
# with gprof, or nothing (the default).
PROFILE_FLAGS=

# set to alloca.o if we are using the C alloca in lib/malloc
ALLOCA = 
ALLOCA_SOURCE = 
ALLOCA_OBJECT = 

# The GNU coding standards don't recognize the possibility that
# other information besides optimization and debugging might be
# passed to cc.  A different name should have been used.
CFLAGS = -g -O2
LOCAL_CFLAGS = 
DEFS = -DHAVE_CONFIG_H
LOCAL_LIBS = 
LIBS = $(BUILTINS_LIB) $(LIBRARIES) $(LOCAL_LIBS) -ldl 
LDFLAGS =  $(LOCAL_LDFLAGS) $(PROFILE_FLAGS) $(CFLAGS)
LOCAL_LDFLAGS = 

SYSTEM_FLAGS = -DPROGRAM='"$(Program)"' -DHOSTTYPE='"$(Machine)"' -DOSTYPE='"$(OS)"' -DMACHTYPE='"$(MACHTYPE)"'

CCFLAGS	= $(PROFILE_FLAGS) $(SYSTEM_FLAGS) -DSHELL \
	  $(DEFS) $(LOCAL_CFLAGS) $(CPPFLAGS) $(INCLUDES) $(CFLAGS)

INCLUDES = -I. -I$(srcdir) -I$(LIBSRC)

GCC_LINT_FLAGS = -ansi -Wall -Wshadow -Wpointer-arith -Wcast-qual \
		 -Wwrite-strings -Werror -Wstrict-prototypes \
		 -Wmissing-prototypes
GCC_LINT_CFLAGS = $(CCFLAGS) $(GCC_LINT_FLAGS)

#
# Support libraries
# 

dot = .

LIBSUBDIR = lib
LIBSRC = $(srcdir)/$(LIBSUBDIR)

SUBDIR_INCLUDES = -I. -I$(topdir) -I$(topdir)/$(LIBSUBDIR) -I$(includedir)

# we assume for now that readline source is being shipped with bash
RL_LIBSRC = $(LIBSRC)/readline
RL_LIBDOC = $(RL_LIBSRC)/doc
RL_LIBDIR = $(dot)/$(LIBSUBDIR)/readline
RL_ABSSRC = ${topdir}/$(RL_LIBDIR)

READLINE_LIB = -lreadline
READLINE_LIBRARY = $(RL_LIBDIR)/libreadline.a
READLINE_LDFLAGS = -L${RL_LIBDIR}
READLINE_DEP = $(READLINE_LIBRARY)

# The source, object and documentation of the GNU Readline library.
READLINE_SOURCE	= $(RL_LIBSRC)/rldefs.h $(RL_LIBSRC)/rlconf.h \
		  $(RL_LIBSRC)/readline.h $(RL_LIBSRC)/tcap.h \
		  $(RL_LIBSRC)/chardefs.h $(RL_LIBSRC)/keymaps.h \
		  $(RL_LIBSRC)/history.h $(RL_LIBSRC)/histlib.h \
		  $(RL_LIBSRC)/posixstat.h $(RL_LIBSRC)/tilde.h \
		  $(RL_LIBSRC)/funmap.c $(RL_LIBSRC)/emacs_keymap.c \
		  $(RL_LIBSRC)/search.c $(RL_LIBSRC)/vi_keymap.c \
		  $(RL_LIBSRC)/keymaps.c $(RL_LIBSRC)/parens.c \
		  $(RL_LIBSRC)/vi_mode.c $(RL_LIBSRC)/callback.c \
		  $(RL_LIBSRC)/readline.c $(RL_LIBSRC)/tilde.c \
		  $(RL_LIBSRC)/rltty.c $(RL_LIBSRC)/complete.c \
		  $(RL_LIBSRC)/bind.c $(RL_LIBSRC)/isearch.c \
		  $(RL_LIBSRC)/display.c $(RL_LIBSRC)/signals.c \
		  $(RL_LIBSRC)/util.c $(RL_LIBSRC)/kill.c \
		  $(RL_LIBSRC)/undo.c $(RL_LIBSRC)/macro.c \
		  $(RL_LIBSRC)/terminal.c $(RL_LIBSRC)/nls.c \
		  $(RL_LIBSRC)/input.c $(RL_LIBSRC)/xmalloc.c \
		  $(RL_LIBSRC)/histexpand.c $(RL_LIBSRC)/history.c \
		  $(RL_LIBSRC)/histsearch.c $(RL_LIBSRC)/histfile.c

READLINE_OBJ	= $(RL_LIBDIR)/readline.o $(RL_LIBDIR)/funmap.o \
		  $(RL_LIBDIR)/parens.o $(RL_LIBDIR)/search.o \
		  $(RL_LIBDIR)/keymaps.o $(RL_LIBDIR)/xmalloc.o \
		  $(RL_LIBDIR)/rltty.o $(RL_LIBDIR)/complete.o \
		  $(RL_LIBDIR)/bind.o $(RL_LIBDIR)/isearch.o \
		  $(RL_LIBDIR)/display.o $(RL_LIBDIR)/signals.o \
		  $(RL_LIBDIR)/tilde.o $(RL_LIBDIR)/util.o \
		  $(RL_LIBDIR)/kill.o $(RL_LIBDIR)/undo.o $(RL_LIBDIR)/nls.o \
		  $(RL_LIBDIR)/macro.o $(RL_LIBDIR)/input.o \
		  $(RL_LIBDIR)/terminal.o $(RL_LIBDIR)/callback.o \
		  $(RL_LIBDIR)/history.o $(RL_LIBDIR)/histexpand.o \
		  $(RL_LIBDIR)/histsearch.o $(RL_LIBDIR)/histfile.o

HIST_LIBSRC = $(LIBSRC)/readline
HIST_LIBDIR = $(dot)/$(LIBSUBDIR)/readline
HIST_ABSSRC = ${topdir}/$(HIST_LIBDIR)

HISTORY_LIB = -lhistory
HISTORY_LIBRARY = $(HIST_LIBDIR)/libhistory.a
HISTORY_LDFLAGS = -L$(HIST_LIBDIR)
HISTORY_DEP = $(HISTORY_LIBRARY)

# The source, object and documentation of the history library.
HISTORY_SOURCE	= $(HIST_LIBSRC)/history.c $(HIST_LIBSRC)/histexpand.c \
		  $(HIST_LIBSRC)/histsearch.c $(HIST_LIBSRC)/histfile.c \
		  $(HIST_LIBSRC)/history.h $(HIST_LIBSRC)/histlib.h
HISTORY_OBJ	= $(HIST_LIBDIR)/history.o $(HIST_LIBDIR)/histexpand.o \
		  $(HIST_LIBDIR)/histsearch.o $(HIST_LIBDIR)/histfile.o

# You only need termcap (or curses) if you are linking with GNU Readline.
TERM_LIBSRC = $(LIBSRC)/termcap
TERM_LIBDIR = $(dot)/$(LIBSUBDIR)/termcap
TERM_ABSSRC = ${topdir}/$(TERM_LIBDIR)

TERMCAP_LIB = -ltermcap
TERMCAP_LIBRARY = $(TERM_LIBDIR)/libtermcap.a
TERMCAP_LDFLAGS = -L$(TERM_LIBDIR)
TERMCAP_DEP = 

TERMCAP_SOURCE	= $(TERM_LIBSRC)/termcap.c $(TERM_LIBSRC)/tparam.c
TERMCAP_OBJ	= $(TERM_LIBDIR)/termcap.o $(TERM_LIBDIR)/tparam.o

GLOB_LIBSRC = $(LIBSRC)/glob
GLOB_LIBDIR = $(dot)/$(LIBSUBDIR)/glob
GLOB_ABSSRC = ${topdir}/$(GLOB_LIBDIR)

GLOB_LIB     = -lglob
GLOB_LIBRARY = $(GLOB_LIBDIR)/libglob.a
GLOB_LDFLAGS = -L$(GLOB_LIBDIR)
GLOB_DEP = $(GLOB_LIBRARY)

GLOB_SOURCE = $(GLOB_LIBSRC)/glob.c $(GLOB_LIBSRC)/fnmatch.c \
	      $(GLOB_LIBSRC)/glob.h $(GLOB_LIBSRC)/fnmatch.h
GLOB_OBJ    = $(GLOB_LIBDIR)/glob.o $(GLOB_LIBDIR)/fnmatch.o

# The source, object and documentation for the GNU Tilde library.
TILDE_LIBSRC = $(LIBSRC)/tilde
TILDE_LIBDIR = $(dot)/$(LIBSUBDIR)/tilde
TILDE_ABSSRC = ${topdir}/$(TILDE_LIBDIR)

TILDE_LIB = -ltilde
TILDE_LIBRARY = $(TILDE_LIBDIR)/libtilde.a
TILDE_LDFLAGS = -L$(TILDE_LIBDIR)
TILDE_DEP = $(TILDE_LIBRARY)

TILDE_SOURCE	= $(TILDE_LIBSRC)/tilde.c $(TILDE_LIBSRC)/tilde.h
TILDE_OBJ	= $(TILDE_LIBDIR)/tilde.o

# Our malloc.
ALLOC_LIBSRC = $(LIBSRC)/malloc
ALLOC_LIBDIR = $(dot)/$(LIBSUBDIR)/malloc
ALLOC_ABSSRC = ${topdir}/$(ALLOC_LIBDIR)

ALLOCA_DEP = $(ALLOC_LIBDIR)/

MALLOC_OBJ = $(ALLOC_LIBDIR)/malloc.o
MALLOC_SRC = $(ALLOC_LIBSRC)/malloc.c
MALLOC_CFLAGS = -Drcheck -Dbotch=programming_error

MALLOC_LIB     = -lmalloc
MALLOC_LIBRARY = $(ALLOC_LIBDIR)/libmalloc.a
MALLOC_LDFLAGS = -L$(ALLOC_LIBDIR)
MALLOC_DEP = $(MALLOC_LIBRARY)

ALLOC_HEADERS = $(ALLOC_LIBSRC)/getpagesize.h

$(MALLOC_LIBRARY): $(MALLOC_SRC)
		@$(RM) $@
		@(cd $(ALLOC_LIBDIR) && \
		 $(MAKE) $(MFLAGS) \
		 MALLOC_CFLAGS="$(MALLOC_CFLAGS)" libmalloc.a ) || exit 1

BASHPOSIX_LIB     = $(LIBSRC)/posixheaders
BASHPOSIX_SUPPORT = $(BASHPOSIX_LIB)/posixstat.h $(BASHPOSIX_LIB)/ansi_stdlib.h \
		    $(BASHPOSIX_LIB)/memalloc.h $(BASHPOSIX_LIB)/stdc.h

LIBRARIES = $(READLINE_LIB) $(HISTORY_LIB) $(TERMCAP_LIB) $(GLOB_LIB) \
	    $(TILDE_LIB) $(MALLOC_LIB) $(LOCAL_LIBS)

LIBDEP = $(READLINE_DEP) $(TERMCAP_DEP) $(GLOB_DEP) $(HISTORY_DEP) \
	 $(TILDE_DEP) $(MALLOC_DEP)

LIBRARY_LDFLAGS = $(READLINE_LDFLAGS) $(HISTORY_LDFLAGS) $(TILDE_LDFLAGS) \
		  $(GLOB_LDFLAGS) $(MALLOC_LDFLAGS)

#
# The shell itself
#

# The main source code for the Bourne Again SHell.
CSOURCES = shell.c eval.c parse.y general.c make_cmd.c print_cmd.c y.tab.c \
	   dispose_cmd.c execute_cmd.c variables.c $(GLOBC) version.c \
	   expr.c copy_cmd.c flags.c subst.c hashlib.c mailcheck.c \
	   test.c trap.c jobs.c nojobs.c $(ALLOC_FILES) braces.c \
	   vprint.c input.c bashhist.c array.c sig.c pathexp.c oslib.c \
	   unwind_prot.c siglist.c getcwd.c $(RL_SUPPORT_SRC) error.c \
	   list.c stringlib.c locale.c xmalloc.c

HSOURCES = shell.h flags.h trap.h hashlib.h jobs.h builtins.h alias.c y.tab.h \
	   general.h variables.h config.h $(ALLOC_HEADERS) alias.h maxpath.h \
	   quit.h posixstat.h filecntl.h unwind_prot.h \
	   command.h input.h error.h bashansi.h dispose_cmd.h make_cmd.h \
	   subst.h externs.h siglist.h bashhist.h bashline.h bashtypes.h \
	   array.h sig.h mailcheck.h bashtty.h

SOURCES	 = $(CSOURCES) $(HSOURCES) $(BUILTIN_DEFS)

# object files chosen based on running of configure
JOBS_O = jobs.o

# Matching object files.
OBJECTS	 = shell.o eval.o y.tab.o general.o make_cmd.o print_cmd.o $(GLOBO) \
	   dispose_cmd.o execute_cmd.o variables.o copy_cmd.o error.o \
	   expr.o flags.o $(JOBS_O) subst.o hashlib.o mailcheck.o test.o \
	   trap.o input.o unwind_prot.o pathexp.o sig.o version.o \
	   alias.o array.o braces.o bracecomp.o bashhist.o bashline.o \
	   getcwd.o siglist.o vprint.o oslib.o list.o stringlib.o \
	   locale.o xmalloc.o

# Where the source code of the shell builtins resides.
BUILTIN_SRCDIR=$(srcdir)/builtins
DEFSRC=$(BUILTIN_SRCDIR)
BUILTIN_ABSSRC=${topdir}/builtins
DEFDIR = $(dot)/builtins

BUILTIN_DEFS = $(DEFSRC)/alias.def $(DEFSRC)/bind.def $(DEFSRC)/break.def \
	       $(DEFSRC)/builtin.def $(DEFSRC)/cd.def $(DEFSRC)/colon.def \
	       $(DEFSRC)/command.def $(DEFSRC)/declare.def \
	       $(DEFSRC)/echo.def $(DEFSRC)/enable.def $(DEFSRC)/eval.def \
	       $(DEFSRC)/exec.def $(DEFSRC)/exit.def $(DEFSRC)/fc.def \
	       $(DEFSRC)/fg_bg.def $(DEFSRC)/hash.def $(DEFSRC)/help.def \
	       $(DEFSRC)/history.def $(DEFSRC)/jobs.def $(DEFSRC)/kill.def \
	       $(DEFSRC)/let.def $(DEFSRC)/read.def $(DEFSRC)/return.def \
	       $(DEFSRC)/set.def $(DEFSRC)/setattr.def $(DEFSRC)/shift.def \
	       $(DEFSRC)/source.def $(DEFSRC)/suspend.def $(DEFSRC)/test.def \
	       $(DEFSRC)/times.def $(DEFSRC)/trap.def $(DEFSRC)/type.def \
	       $(DEFSRC)/ulimit.def $(DEFSRC)/umask.def $(DEFSRC)/wait.def \
	       $(DEFSRC)/getopts.def $(DEFSRC)/reserved.def \
	       $(DEFSRC)/pushd.def $(DEFSRC)/shopt.def
BUILTIN_C_SRC  = $(DEFSRC)/mkbuiltins.c $(DEFSRC)/common.c \
		 $(DEFSRC)/evalstring.c $(DEFSRC)/evalfile.c \
		 $(DEFSRC)/bashgetopt.c $(GETOPT_SOURCE) \
		 $(DEFSRC)/hashcom.h 
BUILTIN_C_OBJ  = $(DEFDIR)/common.o $(DEFDIR)/evalstring.o \
		 $(DEFDIR)/evalfile.o $(DEFDIR)/bashgetopt.o
BUILTIN_OBJS = $(DEFDIR)/alias.o $(DEFDIR)/bind.o $(DEFDIR)/break.o \
	       $(DEFDIR)/builtin.o $(DEFDIR)/cd.o $(DEFDIR)/colon.o \
	       $(DEFDIR)/command.o $(DEFDIR)/declare.o \
	       $(DEFDIR)/echo.o $(DEFDIR)/enable.o $(DEFDIR)/eval.o \
	       $(DEFDIR)/exec.o $(DEFDIR)/exit.o $(DEFDIR)/fc.o \
	       $(DEFDIR)/fg_bg.o $(DEFDIR)/hash.o $(DEFDIR)/help.o \
	       $(DEFDIR)/history.o $(DEFDIR)/jobs.o $(DEFDIR)/kill.o \
	       $(DEFDIR)/let.o $(DEFDIR)/pushd.o $(DEFDIR)/read.o \
	       $(DEFDIR)/return.o $(DEFDIR)/shopt.o \
	       $(DEFDIR)/set.o $(DEFDIR)/setattr.o $(DEFDIR)/shift.o \
	       $(DEFDIR)/source.o $(DEFDIR)/suspend.o $(DEFDIR)/test.o \
	       $(DEFDIR)/times.o $(DEFDIR)/trap.o $(DEFDIR)/type.o \
	       $(DEFDIR)/ulimit.o $(DEFDIR)/umask.o $(DEFDIR)/wait.o \
	       $(DEFDIR)/getopts.o $(BUILTIN_C_OBJ)
GETOPT_SOURCE   = $(DEFSRC)/getopt.c $(DEFSRC)/getopt.h
PSIZE_SOURCE	= $(DEFSRC)/psize.sh $(DEFSRC)/psize.c

BUILTINS_LIBRARY = builtins/libbuiltins.a
BUILTINS_LIB = -lbuiltins
BUILTINS_LDFLAGS = -L$(DEFDIR)
BUILTINS_DEP = $(BUILTINS_LIBRARY)

# Documentation for the shell.
DOCSRC = $(srcdir)/doc
DOCDIR = ./doc

SIGNAMES_SUPPORT = $(SUPPORT_SRC)mksignames.c

SUPPORT_SRC = $(srcdir)/support/
SDIR = ./support/

CREATED_SUPPORT = signames.h recho zecho tests/recho tests/zecho \
		  tests/printenv mksignames mkversion 
CREATED_CONFIGURE = config.h config.cache config.status config.log \
		    stamp-h
CREATED_MAKEFILES = Makefile builtins/Makefile doc/Makefile \
		    lib/readline/Makefile lib/glob/Makefile \
		    lib/tilde/Makefile lib/malloc/Makefile \
		    lib/termcap/Makefile

# Keep GNU Make from exporting the entire environment for small machines.
.NOEXPORT:

.made: $(Program) bashbug
	cp .machine .made

$(Program):  .build $(OBJECTS) $(BUILTINS_DEP) $(LIBDEP) $(srcdir)/.distribution
	$(RM) $@
	$(PURIFY) $(CC) $(LDFLAGS) $(BUILTINS_LDFLAGS) $(LIBRARY_LDFLAGS) -o $(Program) $(OBJECTS) $(LIBS)
	ls -l $(Program)
	size $(Program)

.build:	$(SOURCES) config.h Makefile mkversion version.h .machine
	@echo
	@echo "	  ***********************************************************"
	@echo "	  *                                                         *"
	@echo "	  * Making Bash-`cat $(srcdir)/.distribution`.`cat $(srcdir)/.patchlevel`-$(RELSTATUS) for a $(Machine) running $(OS)"
	@echo "	  *                                                         *"
	@echo "	  ***********************************************************"
	@echo

.machine: $(SOURCES) config.h Makefile mkversion version.h
	@echo "$(Program) last made for a $(Machine) running $(OS)" >.machine

bashbug: $(SUPPORT_SRC)bashbug.sh mkversion config.h Makefile
	@sed -e "s:!MACHINE!:$(Machine):" -e "s:!OS!:$(OS):" \
	     -e "s:!CFLAGS!:$(CCFLAGS):" -e "s:!CC!:$(CC):" \
	     -e "s:!RELEASE!:`cat $(srcdir)/.distribution`:" \
	     -e "s:!PATCHLEVEL!:`cat $(srcdir)/.patchlevel`:" \
	     -e "s:!MACHTYPE!:$(MACHTYPE):" -e "s:!RELSTATUS!:$(RELSTATUS):" \
	     $(SUPPORT_SRC)bashbug.sh > $@
	@chmod a+rx bashbug

strip:	$(Program) .made
	strip $(Program)
	ls -l $(Program)
	size $(Program)

version.h:  $(SOURCES) config.h Makefile mkversion .patchlevel .distribution
	if ./mkversion -dir $(srcdir) -build -status $(RELSTATUS); then mv -f newversion.h version.h; fi

# old rules
y.tab.o: y.tab.c parser-built
y.tab.c: parser-built
y.tab.h: parser-built
parser-built:	parse.y command.h stdc.h input.h
	$(RM) $@
	-if test -f y.tab.h; then mv -f y.tab.h old-y.tab.h; fi
	$(YACC) -d $(srcdir)/parse.y
	-if cmp -s old-y.tab.h y.tab.h; then mv old-y.tab.h y.tab.h; fi
	touch $@

# experimental new rules - work with GNU make but not BSD (or OSF) make
#y.tab.o: y.tab.c y.tab.h
#y.tab.c y.tab.h: parse.y command.h stdc.h input.h
#	-if test -f y.tab.h; then mv -f y.tab.h old-y.tab.h; fi
#	$(YACC) -d $(srcdir)/parse.y
#	-if cmp -s old-y.tab.h y.tab.h; then mv old-y.tab.h y.tab.h; fi

$(READLINE_LIBRARY): config.h $(READLINE_SOURCE)
	@echo making $@ in ${RL_LIBDIR}
	@(cd ${RL_LIBDIR} && \
		$(MAKE) $(MFLAGS) APP_CFLAGS=-DSHELL libreadline.a) || exit 1

$(HISTORY_LIBRARY): config.h $(HISTORY_SOURCE)
	@echo making $@ in ${HIST_LIBDIR}
	@(cd ${HIST_LIBDIR} && \
		$(MAKE) $(MFLAGS) libhistory.a) || exit 1

$(GLOB_LIBRARY): config.h $(GLOB_SOURCE)
	@echo making $@ in ${GLOB_LIBDIR}
	@(cd ${GLOB_LIBDIR} && \
		$(MAKE) $(MFLAGS) libglob.a) || exit 1

$(TILDE_LIBRARY): config.h $(TILDE_SOURCE)
	@echo making $@ in ${TILDE_LIBDIR}
	@(cd ${TILDE_LIBDIR} && \
		$(MAKE) $(MFLAGS) libtilde.a) || exit 1

$(TERMCAP_LIBRARY): config.h ${TERMCAP_SOURCE}
	@echo making $@ in ${TERMCAP_LIBDIR}	
	@(cd ${TERMCAP_LIBDIR} && \
		$(MAKE) $(MFLAGS) libtermcap.a) || exit 1

mksignames:	$(SUPPORT_SRC)mksignames.c
	$(CC) $(CCFLAGS) $(CPPFLAGS) -o $@ $(SUPPORT_SRC)mksignames.c

signames.h:   mksignames
	$(RM) $@
	./mksignames $@

$(BUILTINS_LIBRARY): $(BUILTIN_DEFS) $(BUILTIN_C_SRC) config.h memalloc.h
	@(cd $(DEFDIR) && $(MAKE) $(MFLAGS) libbuiltins.a ) || exit 1

# these require special rules to circumvent make builtin rules
builtins/common.o:	$(BUILTIN_SRCDIR)/common.c
	@(cd $(DEFDIR) && $(MAKE) $(MFLAGS) common.o) || exit 1

builtins/bashgetopt.o:	$(BUILTIN_SRCDIR)/bashgetopt.c
	@(cd $(DEFDIR) && $(MAKE) $(MFLAGS) bashgetopt.o) || exit 1

builtins/builtext.h: $(BUILTIN_DEFS)
	@(cd $(DEFDIR) && $(MAKE) $(MFLAGS) builtext.h ) || exit 1

# For the justification of the following Makefile rules, see node
# `Automatic Remaking' in GNU Autoconf documentation.

Makefile:	config.status $(srcdir)/Makefile.in
	CONFIG_FILES=$@ CONFIG_HEADERS= $(SHELL) ./config.status

Makefiles makefiles:	config.status $(srcdir)/Makefile.in
	@for mf in $(CREATED_MAKEFILES); do \
		CONFIG_FILES=$$mf CONFIG_HEADERS= $(SHELL) ./config.status ; \
	done

config.h:	stamp-h 

stamp-h:	config.status $(srcdir)/config.h.in $(srcdir)/config.h.top $(srcdir)/config.h.bot
	CONFIG_FILES= CONFIG_HEADERS=config.h $(SHELL) ./config.status

config.status:	$(srcdir)/configure
	$(SHELL) ./config.status --recheck

# comment out for distribution
#$(srcdir)/configure:	$(srcdir)/configure.in $(srcdir)/aclocal.m4
#	cd $(srcdir) && autoconf

mkversion:	$(SUPPORT_SRC)mkversion.c
	$(CC) $(CCFLAGS) -I.. -o $@ $(SUPPORT_SRC)mkversion.c

newversion:	mkversion
	$(RM) .build
	./mkversion -dir $(srcdir) -dist
	mv -f newversion.h version.h
	$(MAKE) -f $(srcdir)/Makefile $(MFLAGS) srcdir=$(srcdir)

doc documentation:  force
	@(cd $(DOCDIR) ; $(MAKE) $(MFLAGS) )

info dvi ps: force
	@(cd $(DOCDIR) ; $(MAKE) $(MFLAGS) CFLAGS='$(CCFLAGS)' $@ )

force:

tags:	$(SOURCES) $(BUILTIN_C_SRC) $(LIBRARY_SOURCE)
	etags $(SOURCES) $(BUILTIN_C_SRC) $(LIBRARY_SOURCE)

TAGS:	$(SOURCES) $(BUILTIN_C_SRC) $(LIBRARY_SOURCE)
	ctags -x $(SOURCES) $(BUILTIN_C_SRC) $(LIBRARY_SOURCE) > $@

# Targets that actually do things not part of the build

installdirs:
	@${SHELL} $(SUPPORT_SRC)mkdirs $(bindir)
	@${SHELL} $(SUPPORT_SRC)mkdirs $(man1dir) $(man3dir)
	@${SHELL} $(SUPPORT_SRC)mkdirs $(infodir)

install:	.made installdirs
	$(INSTALL_PROGRAM) $(Program) $(bindir)/$(Program)
	$(INSTALL_PROGRAM) bashbug $(bindir)/bashbug
	-( cd $(DOCDIR) ; $(MAKE) $(MFLAGS) \
		man1dir=$(man1dir) man1ext=$(man1ext) \
		man3dir=$(man3dir) man3ext=$(man3ext) \
		infodir=$(infodir) $@ )

install-strip:
	$(MAKE) $(MFLAGS) INSTALL_PROGRAM='$(INSTALL_PROGRAM) -s' \
		prefix=${prefix} exec_prefix=${exec_prefix} install

uninstall:	.made
	$(RM) $(bindir)/$(Program) $(bindir)/bashbug
	-( cd $(DOCDIR) ; $(MAKE) $(MFLAGS) \
		man1dir=$(man1dir) man1ext=$(man1ext) \
		man3dir=$(man3dir) man3ext=$(man3ext) \
		infodir=$(infodir) $@ )

.PHONY: basic-clean clean realclean maintainer-clean distclean mostlyclean
basic-clean:
	$(RM) $(OBJECTS) $(Program) bashbug
	$(RM) .build .made .machine version.h

clean:	basic-clean
	( cd $(DOCDIR) && $(MAKE) $(MFLAGS) $@ )
	( cd builtins && $(MAKE) $(MFLAGS) $@ )
	-(cd $(RL_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(HIST_LIBDIR) && test -f Makefile && $(MAKE) $(MFLAGS) $@)
	-(cd $(TERM_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(GLOB_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(TILDE_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(ALLOC_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	$(RM) $(CREATED_SUPPORT)

mostlyclean: basic-clean
	( cd $(DOCDIR) && $(MAKE) $(MFLAGS) $@ )
	( cd builtins && $(MAKE) $(MFLAGS) $@ )
	-(cd $(RL_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(HIST_LIBDIR) && test -f Makefile && $(MAKE) $(MFLAGS) $@)
	-(cd $(TERM_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(GLOB_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(TILDE_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(ALLOC_LIBDIR) && $(MAKE) $(MFLAGS) $@)

distclean:	basic-clean
	( cd $(DOCDIR) && $(MAKE) $(MFLAGS) $@ )
	( cd builtins && $(MAKE) $(MFLAGS) $@ )
	-(cd $(RL_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(HIST_LIBDIR) && test -f Makefile && $(MAKE) $(MFLAGS) $@)
	-(cd $(TERM_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(GLOB_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(TILDE_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(ALLOC_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	$(RM) $(CREATED_CONFIGURE) tags TAGS 
	$(RM) $(CREATED_SUPPORT) Makefile $(CREATED_MAKEFILES)

maintainer-clean:	basic-clean
	@echo This command is intended for maintainers to use.
	@echo It deletes files that may require special tools to rebuild.
	$(RM) y.tab.c y.tab.h parser-built tags TAGS
	( cd $(DOCDIR) && $(MAKE) $(MFLAGS) $@ )
	( cd builtins && $(MAKE) $(MFLAGS) $@ )
	-(cd $(RL_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(HIST_LIBDIR) && test -f Makefile && $(MAKE) $(MFLAGS) $@)
	-(cd $(TERM_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(GLOB_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(TILDE_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	-(cd $(ALLOC_LIBDIR) && $(MAKE) $(MFLAGS) $@)
	$(RM) $(CREATED_CONFIGURE) $(CREATED_MAKEFILES)
	$(RM) $(CREATED_SUPPORT) Makefile

recho:		$(SUPPORT_SRC)recho.c
	@$(CC) -o $@ $(SUPPORT_SRC)recho.c

zecho:		$(SUPPORT_SRC)zecho.c
	@$(CC) -o $@ $(SUPPORT_SRC)zecho.c

tests check:		force $(Program) recho zecho
	@-test -d tests || mkdir tests
	@cp recho zecho $(SUPPORT_SRC)printenv tests
	@( cd $(srcdir)/tests && \
		PATH=$$PATH:$(BUILD_DIR)/tests THIS_SH=$(THIS_SH) sh run-all )

symlinks:
	$(SHELL) $(SUPPORT_SRC)fixlinks -s $(srcdir)

dist:	force
	@echo Bash distributions are created using $(srcdir)/support/mkdist.
	@echo Here is a sample of the necessary commands:
	@echo $(Program) $(srcdir)/support/mkdist -m $(srcdir)/MANIFEST -s $(srcdir) -r ${Program} `cat $(srcdir)/.distribution`
	@echo tar cf $(Program)-`cat $(srcdir)/.distribution`.tar ${Program}-`cat $(srcdir)/.distribution`
	@echo gzip $(Program)-`cat $(srcdir)/.distribution`.tar

############################ DEPENDENCIES ###############################

# Files that depend on the definitions in config.h.top, which are not meant
# to be changed
shell.o: config.h.top
input.o: config.h.top
y.tab.o: config.h.top
jobs.o: config.h.top
nojobs.o: config.h.top
execute_cmd.o: config.h.top
builtins/break.o: config.h.top
builtins/common.o: config.h.top
builtins/echo.o: config.h.top
variables.o: config.h.top
builtins/command.o: config.h.top

copy_cmd.o: shell.h bashjmp.h sig.h command.h stdc.h hashlib.h
copy_cmd.o: general.h variables.h config.h memalloc.h quit.h
copy_cmd.o: dispose_cmd.h make_cmd.h subst.h externs.h
dispose_cmd.o: shell.h bashjmp.h sig.h command.h stdc.h
dispose_cmd.o: general.h variables.h config.h memalloc.h quit.h
dispose_cmd.o: dispose_cmd.h make_cmd.h subst.h externs.h
error.o: error.h
execute_cmd.o: shell.h bashjmp.h sig.h command.h stdc.h y.tab.h posixstat.h
execute_cmd.o: general.h variables.h config.h memalloc.h quit.h hashlib.h jobs.h
execute_cmd.o: unwind_prot.h siglist.h builtins/builtext.h config.h flags.h
execute_cmd.o: dispose_cmd.h make_cmd.h subst.h externs.h bashtypes.h
execute_cmd.o: pathexp.h
expr.o: shell.h bashjmp.h sig.h command.h stdc.h hashlib.h
expr.o: general.h variables.h config.h memalloc.h quit.h
expr.o: dispose_cmd.h make_cmd.h subst.h externs.h
flags.o: flags.h stdc.h config.h memalloc.h general.h quit.h
general.o: shell.h bashjmp.h sig.h command.h stdc.h maxpath.h
general.o: general.h variables.h config.h memalloc.h quit.h unwind_prot.h
general.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
getcwd.o: config.h config.h.bot bashtypes.h maxpath.h posixstat.h
hashlib.o: shell.h bashjmp.h sig.h command.h stdc.h hashlib.h
hashlib.o: general.h variables.h config.h memalloc.h quit.h
hashlib.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
jobs.o: shell.h bashjmp.h sig.h command.h stdc.h hashlib.h trap.h jobs.h 
jobs.o: general.h variables.h config.h memalloc.h quit.h bashtty.h siglist.h
jobs.o: dispose_cmd.h make_cmd.h subst.h externs.h builtins/builtext.h
jobs.o: unwind_prot.h
mailcheck.o: posixstat.h maxpath.h variables.h
mailcheck.o: hashlib.h quit.h mailcheck.h
make_cmd.o: shell.h bashjmp.h sig.h command.h stdc.h flags.h input.h 
make_cmd.o: general.h variables.h config.h memalloc.h quit.h bashtypes.h
make_cmd.o: dispose_cmd.h make_cmd.h subst.h externs.h
y.tab.o: shell.h bashjmp.h sig.h command.h stdc.h flags.h maxpath.h alias.h
y.tab.o: general.h variables.h config.h memalloc.h quit.h mailcheck.h parser.h
y.tab.o: dispose_cmd.h make_cmd.h subst.h externs.h bashtypes.h bashline.h
y.tab.o: builtins/builtext.h
print_cmd.o: shell.h bashjmp.h sig.h command.h stdc.h y.tab.h
print_cmd.o: general.h variables.h config.h memalloc.h quit.h
print_cmd.o: dispose_cmd.h make_cmd.h subst.h externs.h unwind_prot.h
shell.o: shell.h bashjmp.h sig.h command.h stdc.h flags.h stdc.h
shell.o: general.h variables.h config.h memalloc.h quit.h
shell.o: dispose_cmd.h make_cmd.h subst.h externs.h mailcheck.h
shell.o: posixstat.h filecntl.h jobs.h input.h
subst.o: shell.h bashjmp.h sig.h command.h stdc.h flags.h jobs.h siglist.h
subst.o: general.h variables.h config.h memalloc.h quit.h bashtypes.h
subst.o: dispose_cmd.h make_cmd.h subst.h externs.h execute_cmd.h
subst.o: ${DEFSRC}/getopt.h pathexp.h bashline.h
pathexp.o: config.h shell.h bashjmp.h command.h stdc.h general.h
pathexp.o: error.h variables.h quit.h maxpath.h unwind_prot.h dispose_cmd.h
pathexp.o: make_cmd.h subst.h sig.h pathnames.h externs.h
pathexp.o: $(GLOB_LIBSRC)/glob.h $(GLOB_LIBSRC)/fnmatch.h
test.o: posixstat.h
trap.o: trap.h shell.h bashjmp.h sig.h command.h stdc.h hashlib.h unwind_prot.h
trap.o: general.h variables.h config.h memalloc.h quit.h signames.h
trap.o: dispose_cmd.h make_cmd.h subst.h externs.h
unwind_prot.o: config.h memalloc.h general.h unwind_prot.h sig.h
variables.o: shell.h bashjmp.h sig.h command.h stdc.h hashlib.h flags.h
variables.o: config.h memalloc.h general.h variables.h quit.h mailcheck.h
variables.o: execute_cmd.h dispose_cmd.h make_cmd.h subst.h externs.h
sig.o: shell.h bashjmp.h sig.h command.h stdc.h hashlib.h flags.h
sig.o: config.h memalloc.h general.h variables.h quit.h
sig.o: bashtypes.h jobs.h bashline.h unwind_prot.h
version.o: version.h .build
oslib.o: config.h bashtypes.h posixstat.h filecntl.h bashansi.h maxpath.h
oslib.o: shell.h bashjmp.h sig.h command.h stdc.h mailcheck.h
oslib.o: general.h error.h variables.h quit.h unwind_prot.h dispose_cmd.h
oslib.o: make_cmd.h subst.h pathnames.h externs.h
xmalloc.o: config.h ansi_stdlib.h general.h error.h

eval.o: config.h bashansi.h shell.h trap.h flags.h builtins/common.h
eval.o: input.h execute_cmd.h
eval.o: bashjmp.h command.h general.h error.h variables.h quit.h
eval.o: maxpath.h unwind_prot.h dispose_cmd.h make_cmd.h subst.h
eval.o: sig.h pathnames.h externs.h

locale.o: bashintl.h bashansi.h config.h bashtypes.h shell.h
locale.o: bashjmp.h command.h general.h error.h variables.h quit.h
locale.o: maxpath.h unwind_prot.h dispose_cmd.h make_cmd.h subst.h
locale.o: sig.h pathnames.h externs.h


alias.o: ansi_stdlib.h
bashline.o: ansi_stdlib.h
variables.o: ansi_stdlib.h
shell.o: ansi_stdlib.h
error.o: ansi_stdlib.h
hash.o: ansi_stdlib.h
signames.o: ansi_stdlib.h
expr.o: ansi_stdlib.h
general.o: ansi_stdlib.h
input.o: ansi_stdlib.h

jobs.o: jobs.c
nojobs.o: nojobs.c

array.o: general.h shell.h bashjmp.h sig.h variables.h quit.h config.h
array.o: command.h error.h maxpath.h unwind_prot.h dispose_cmd.h memalloc.h
array.o: make_cmd.h subst.h externs.h
array.o: array.h stdc.h $(DEFSRC)/common.h

braces.o: general.h shell.h bashjmp.h sig.h variables.h quit.h config.h
braces.o: dispose_cmd.h make_cmd.h subst.h externs.h memalloc.h
braces.o: maxpath.h unwind_prot.h command.h stdc.h

bracecomp.o: bracecomp.c
bracecomp.o: shell.h bashjmp.h sig.h command.h hashlib.h builtins.h general.h
bracecomp.o: quit.h alias.h config.h  variables.h
bracecomp.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
bracecomp.o: $(RL_LIBSRC)/readline.h

bashline.o: shell.h bashjmp.h sig.h command.h stdc.h hashlib.h builtins.h
bashline.o: general.h variables.h config.h memalloc.h quit.h alias.h
bashline.o: dispose_cmd.h make_cmd.h subst.h externs.h config.h bashline.h
bashline.o: $(GLOB_LIBSRC)/glob.h pathexp.h execute_cmd.h

bashhist.o: config.h bashansi.h posixstat.h filecntl.h parser.h
bashhist.o: shell.h bashjmp.h sig.h command.h stdc.h hashlib.h builtins.h
bashhist.o: general.h variables.h memalloc.h quit.h alias.h execute_cmd.h
bashhist.o: dispose_cmd.h make_cmd.h subst.h externs.h flags.h

bashline.o: $(RL_LIBSRC)/chardefs.h $(RL_LIBSRC)/readline.h
bashline.o: $(RL_LIBSRC)/keymaps.h
y.tab.o: $(RL_LIBSRC)/keymaps.h $(RL_LIBSRC)/chardefs.h
y.tab.o: $(RL_LIBSRC)/readline.h

subst.o: $(HIST_LIBSRC)/history.h
bashline.o: $(HIST_LIBSRC)/history.h
bashhist.o: $(HIST_LIBSRC)/history.h
y.tab.o: $(HIST_LIBSRC)/history.h

subst.o: $(GLOB_LIBSRC)/fnmatch.h
execute_cmd.o: $(GLOB_LIBSRC)/fnmatch.h
bashhist.o: $(GLOB_LIBSRC)/fnmatch.h

execute_cmd.o: $(TILDE_LIBSRC)/tilde.h
general.o: $(TILDE_LIBSRC)/tilde.h
mailcheck.o: $(TILDE_LIBSRC)/tilde.h
shell.o: $(TILDE_LIBSRC)/tilde.h
subst.o: $(TILDE_LIBSRC)/tilde.h
variables.o: $(TILDE_LIBSRC)/tilde.h

builtins/common.o: shell.h bashjmp.h sig.h command.h config.h memalloc.h
builtins/common.o: variables.h input.h $(DEFSRC)/hashcom.h siglist.h
builtins/common.o: quit.h unwind_prot.h maxpath.h jobs.h builtins.h
builtins/common.o: dispose_cmd.h make_cmd.h subst.h externs.h bashhist.h
builtins/common.o: execute_cmd.h stdc.h general.h error.h unwind_prot.h
builtins/alias.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/alias.o: quit.h $(DEFSRC)/common.h
builtins/alias.o: shell.h bashjmp.h sig.h command.h stdc.h unwind_prot.h
builtins/alias.o: dispose_cmd.h make_cmd.h subst.h externs.h variables.h 
builtins/bind.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/bind.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/bind.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h
builtins/bind.o: $(DEFSRC)/bashgetopt.h
builtins/break.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/break.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h
builtins/break.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/builtin.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/builtin.o: quit.h $(DEFSRC)/common.h
builtins/builtin.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/builtin.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/cd.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/cd.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h
builtins/cd.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/cd.o: $(DEFSRC)/common.h quit.h 
builtins/command.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/command.o: quit.h $(DEFSRC)/bashgetopt.h
builtins/command.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/command.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/declare.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/declare.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h
builtins/declare.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/echo.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/echo.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h
builtins/echo.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/enable.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/enable.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h
builtins/enable.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/eval.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/eval.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h 
builtins/eval.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/exec.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/exec.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h
builtins/exec.o: dispose_cmd.h make_cmd.h subst.h externs.h execute_cmd.h
builtins/exec.o: flags.h quit.h $(DEFSRC)/common.h stdc.h
builtins/exit.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/exit.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h
builtins/exit.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/fc.o: builtins.h command.h stdc.h 
builtins/fc.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/fc.o: flags.h unwind_prot.h variables.h shell.h bashjmp.h sig.h 
builtins/fc.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h quit.h 
builtins/fc.o: $(DEFSRC)/bashgetopt.h bashhist.h
builtins/fg_bg.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/fg_bg.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h
builtins/fg_bg.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/getopts.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/getopts.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h 
builtins/getopts.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/hash.o: builtins.h command.h execute_cmd.h stdc.h $(DEFSRC)/common.h
builtins/hash.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/hash.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h 
builtins/help.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/help.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/help.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h
builtins/help.o: $(GLOB_LIBSRC)/glob.h
builtins/history.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/history.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/history.o: filecntl.h shell.h bashjmp.h sig.h unwind_prot.h
builtins/history.o: bashhist.h variables.h 
builtins/inlib.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/inlib.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h quit.h 
builtins/inlib.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/jobs.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/jobs.o: quit.h $(DEFSRC)/bashgetopt.h
builtins/jobs.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/jobs.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/kill.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/kill.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/kill.o: shell.h bashjmp.h sig.h trap.h unwind_prot.h variables.h 
builtins/let.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/let.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/let.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/pushd.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/pushd.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/pushd.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h
builtins/pushd.o: $(DEFSRC)/common.h
builtins/read.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/read.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/read.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/return.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/return.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/return.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/set.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/set.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/set.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h flags.h
builtins/setattr.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/setattr.o: quit.h $(DEFSRC)/common.h $(DEFSRC)/bashgetopt.h
builtins/setattr.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/setattr.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/shift.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/shift.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/shift.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/shift.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/source.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/source.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/source.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/suspend.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/suspend.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/suspend.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/test.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/test.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/test.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/times.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/times.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/times.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/trap.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/trap.o: quit.h $(DEFSRC)/common.h
builtins/trap.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/trap.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/type.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/type.o: quit.h $(DEFSRC)/common.h execute_cmd.h
builtins/type.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h
builtins/type.o: dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/ulimit.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/ulimit.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/ulimit.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/umask.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/umask.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/umask.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h 
builtins/wait.o: command.h config.h memalloc.h error.h general.h maxpath.h
builtins/wait.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h stdc.h
builtins/wait.o: shell.h bashjmp.h sig.h unwind_prot.h variables.h
builtins/shopt.o: command.h config.h memalloc.h error.h general.h
builtins/shopt.o: quit.h dispose_cmd.h make_cmd.h subst.h externs.h
builtins/shopt.o: shell.h bashjmp.h unwind_prot.h variables.h maxpath.h
builtins/shopt.o: $(DEFSRC)/common.h $(DEFSRC)/bashgetopt.h

builtins/bashgetopt.o: bashansi.h ansi_stdlib.h
builtins/mkbuiltins.o: bashansi.h ansi_stdlib.h
builtins/fc.o: bashansi.h ansi_stdlib.h

builtins/bind.o: $(RL_LIBSRC)/chardefs.h $(RL_LIBSRC)/readline.h
builtins/bind.o: $(RL_LIBSRC)/keymaps.h

builtins/bind.o: $(HIST_LIBSRC)/history.h
builtins/fc.o: $(HIST_LIBSRC)/history.h
builtins/history.o: $(HIST_LIBSRC)/history.h

builtins/common.o: $(TILDE_LIBSRC)/tilde.h
builtins/cd.o: $(TILDE_LIBSRC)/tilde.h 

builtins/alias.o: $(DEFSRC)/alias.def
builtins/bind.o: $(DEFSRC)/bind.def
builtins/break.o: $(DEFSRC)/break.def
builtins/builtin.o: $(DEFSRC)/builtin.def
builtins/cd.o: $(DEFSRC)/cd.def
builtins/colon.o: $(DEFSRC)/colon.def
builtins/command.o: $(DEFSRC)/command.def
builtins/declare.o: $(DEFSRC)/declare.def
builtins/echo.o: $(DEFSRC)/echo.def
builtins/enable.o: $(DEFSRC)/enable.def
builtins/eval.o: $(DEFSRC)/eval.def
builtins/exec.o: $(DEFSRC)/exec.def
builtins/exit.o: $(DEFSRC)/exit.def
builtins/fc.o: $(DEFSRC)/fc.def
builtins/fg_bg.o: $(DEFSRC)/fg_bg.def
builtins/getopts.o: $(DEFSRC)/getopts.def
builtins/hash.o: $(DEFSRC)/hash.def
builtins/help.o: $(DEFSRC)/help.def
builtins/history.o: $(DEFSRC)/history.def
builtins/inlib.o: $(DEFSRC)/inlib.def
builtins/jobs.o: $(DEFSRC)/jobs.def
builtins/kill.o: $(DEFSRC)/kill.def
builtins/let.o: $(DEFSRC)/let.def
builtins/pushd.o: $(DEFSRC)/pushd.def
builtins/read.o: $(DEFSRC)/read.def
builtins/reserved.o: $(DEFSRC)/reserved.def
builtins/return.o: $(DEFSRC)/return.def
builtins/set.o: $(DEFSRC)/set.def
builtins/setattr.o: $(DEFSRC)/setattr.def
builtins/shift.o: $(DEFSRC)/shift.def
builtins/shopt.o: $(DEFSRC)/shopt.def
builtins/source.o: $(DEFSRC)/source.def
builtins/suspend.o: $(DEFSRC)/suspend.def
builtins/test.o: $(DEFSRC)/test.def
builtins/times.o: $(DEFSRC)/times.def
builtins/trap.o: $(DEFSRC)/trap.def
builtins/type.o: $(DEFSRC)/type.def
builtins/ulimit.o: $(DEFSRC)/ulimit.def
builtins/umask.o: $(DEFSRC)/umask.def
builtins/wait.o: $(DEFSRC)/wait.def
