# Generated automatically from Makefile.in by configure.
# This Makefile for building libbuiltins.a is in -*- text -*- for Emacs.
#
MKBUILTINS = mkbuiltins
RANLIB = ranlib
CFLAGS = -g -O2
LOCAL_CFLAGS = 
CPPFLAGS = 
SHELL = /bin/sh
CC = gcc
AR = ar
RM = rm -f
CP = cp

LIBS = -ldl 

srcdir = .
VPATH = .:.
topdir = ..
includedir = ${prefix}/include

DEFS = -DHAVE_CONFIG_H

INCLUDES = -I. -I.. -I$(topdir) -I$(topdir)/lib -I$(srcdir)

CCFLAGS = $(DEFS) $(SYSTEM_FLAGS) $(CPPFLAGS) ${INCLUDES} $(LOCAL_CFLAGS) $(CFLAGS)

DIRECTDEFINE = -D $(srcdir)

# xxx this is bad style
RL_LIBSRC = $(topdir)/lib/readline

.SUFFIXES:
.SUFFIXES: .def .c .o
# How to make a .o file from a .def file.
.def.o:
	$(RM) $@
	./$(MKBUILTINS) $(DIRECTDEFINE) $<
	$(CC) -c $(CCFLAGS) $*.c || ( $(RM) $*.c ; exit 1 )
	$(RM) $*.c

# How to make a .c file from a .def file.
.def.c:
	$(RM) $@
	./$(MKBUILTINS) $(DIRECTDEFINE) $<

# default rule for making a .o file from a .c file
.c.o:
	$(RM) $@
	$(CC) -c $(CCFLAGS) $<

DEFSRC =  $(srcdir)/alias.def $(srcdir)/bind.def $(srcdir)/break.def \
	  $(srcdir)/builtin.def $(srcdir)/cd.def $(srcdir)/colon.def \
	  $(srcdir)/command.def $(srcdir)/declare.def $(srcdir)/echo.def \
	  $(srcdir)/enable.def $(srcdir)/eval.def $(srcdir)/getopts.def \
	  $(srcdir)/exec.def $(srcdir)/exit.def $(srcdir)/fc.def \
	  $(srcdir)/fg_bg.def $(srcdir)/hash.def $(srcdir)/help.def \
	  $(srcdir)/history.def $(srcdir)/jobs.def $(srcdir)/kill.def \
	  $(srcdir)/let.def $(srcdir)/read.def $(srcdir)/return.def \
	  $(srcdir)/set.def $(srcdir)/setattr.def $(srcdir)/shift.def \
	  $(srcdir)/source.def $(srcdir)/suspend.def $(srcdir)/test.def \
	  $(srcdir)/times.def $(srcdir)/trap.def $(srcdir)/type.def \
	  $(srcdir)/ulimit.def $(srcdir)/umask.def $(srcdir)/wait.def \
	  $(srcdir)/reserved.def $(srcdir)/pushd.def $(srcdir)/shopt.def

STATIC_SOURCE = common.c evalstring.c evalfile.c getopt.c bashgetopt.c \
		getopt.h 

OFILES = builtins.o \
	alias.o bind.o break.o builtin.o cd.o colon.o command.o \
	common.o declare.o echo.o enable.o eval.o evalfile.o \
	evalstring.o exec.o \
	exit.o fc.o fg_bg.o hash.o help.o history.o jobs.o kill.o let.o \
	pushd.o read.o return.o set.o setattr.o shift.o source.o \
	suspend.o test.o times.o trap.o type.o ulimit.o umask.o \
	wait.o getopts.o shopt.o getopt.o bashgetopt.o 

CREATED_FILES = builtext.h builtins.c psize.aux pipesize.h

all: $(MKBUILTINS) libbuiltins.a

libbuiltins.a: $(MKBUILTINS) $(OFILES)
	$(RM) $@
	$(AR) cr $@ $(OFILES)
	-$(RANLIB) $@

builtext.h builtins.c: $(MKBUILTINS) $(DEFSRC)
	$(RM) builtext.h builtins.c
	./$(MKBUILTINS) -externfile builtext.h -structfile builtins.c \
	-noproduction $(DIRECTDEFINE) $(DEFSRC)

mkbuiltins: $(srcdir)/mkbuiltins.c ../config.h
	$(CC) $(CCFLAGS) -o $(MKBUILTINS) $(srcdir)/mkbuiltins.c $(LIBS)

# rules for deficient makes, like SunOS
common.o: common.c
bashgetopt.o: bashgetopt.c
getopt.o: getopt.c

ulimit.o: ulimit.def pipesize.h

pipesize.h:	psize.aux
	$(SHELL) $(srcdir)/psize.sh > pipesize.h

psize.aux:	psize.c
	$(CC) $(CCFLAGS) -o $@ $(srcdir)/psize.c

documentation: builtins.texi

$(OFILES):	$(MKBUILTINS) ../config.h

builtins.texi: $(MKBUILTINS)
	./$(MKBUILTINS) -documentonly $(DEFSRC)

clean:
	$(RM) $(OFILES) $(CREATED_FILES) $(MKBUILTINS) libbuiltins.a

mostlyclean: 
	$(RM) $(OFILES) libbuiltins.a

distclean maintainer-clean: clean
	$(RM) Makefile

alias.o: alias.def
bind.o: bind.def
break.o: break.def
builtin.o: builtin.def
cd.o: cd.def
colon.o: colon.def
command.o: command.def
declare.o: declare.def
echo.o: echo.def
enable.o: enable.def
eval.o: eval.def
exec.o: exec.def
exit.o: exit.def
fc.o: fc.def
fg_bg.o: fg_bg.def
hash.o: hash.def
help.o: help.def
history.o: history.def
jobs.o: jobs.def
kill.o: kill.def
let.o: let.def
pushd.o: pushd.def
read.o: read.def
return.o: return.def
set.o: set.def
setattr.o: setattr.def
shift.o: shift.def
source.o: source.def
suspend.o: suspend.def
test.o: test.def
times.o: times.def
trap.o: trap.def
type.o: type.def
umask.o: umask.def
wait.o: wait.def
getopts.o: getopts.def
reserved.o: reserved.def

common.o: $(topdir)/shell.h $(topdir)/command.h ../config.h
common.o: $(topdir)/memalloc.h $(topdir)/general.h
common.o: $(topdir)/variables.h $(topdir)/input.h $(srcdir)/hashcom.h
common.o: $(topdir)/bashhist.h $(topdir)/quit.h  $(topdir)/unwind_prot.h
common.o: $(topdir)/maxpath.h $(topdir)/jobs.h $(topdir)/builtins.h
common.o: $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h $(topdir)/subst.h
common.o: $(topdir)/execute_cmd.h $(topdir)/error.h $(topdir)/externs.h
alias.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
alias.o: $(topdir)/error.h $(topdir)/general.h $(topdir)/maxpath.h
alias.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
alias.o: $(topdir)/subst.h $(topdir)/externs.h $(srcdir)/common.h
alias.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
bind.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h $(topdir)/error.h
bind.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
bind.o: $(topdir)/subst.h $(topdir)/externs.h $(srcdir)/bashgetopt.h
bind.o: $(topdir)/general.h $(topdir)/maxpath.h $(topdir)/bashline.h
bind.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h 
break.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h 
break.o: $(topdir)/error.h $(topdir)/general.h
break.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
break.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
break.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
builtin.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
builtin.o: $(topdir)/error.h $(topdir)/general.h $(topdir)/externs.h
builtin.o: $(topdir)/quit.h $(srcdir)/common.h $(topdir)/maxpath.h
builtin.o: $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h $(topdir)/subst.h
builtin.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h 
cd.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h $(topdir)/error.h
cd.o: $(topdir)/general.h $(topdir)/quit.h $(topdir)/dispose_cmd.h
cd.o: $(topdir)/make_cmd.h $(topdir)/subst.h $(topdir)/externs.h
cd.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
cd.o: $(srcdir)/common.h $(topdir)/maxpath.h
command.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
command.o: $(topdir)/error.h $(topdir)/general.h $(topdir)/externs.h
command.o: $(topdir)/quit.h $(srcdir)/bashgetopt.h $(topdir)/maxpath.h
command.o: $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h $(topdir)/subst.h
command.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h 
declare.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
declare.o: $(topdir)/error.h $(topdir)/general.h
declare.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
declare.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
declare.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
echo.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h $(topdir)/error.h
echo.o: $(topdir)/general.h $(topdir)/subst.h $(topdir)/externs.h
echo.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
echo.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
echo.o: $(topdir)/maxpath.h
enable.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
enable.o: $(topdir)/error.h $(topdir)/general.h
enable.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
enable.o: $(topdir)/subst.h $(topdir)/externs.h
enable.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
enable.o: $(topdir)/maxpath.h
eval.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
eval.o: $(topdir)/error.h $(topdir)/general.h
eval.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
eval.o: $(topdir)/subst.h $(topdir)/externs.h
eval.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
eval.o: $(topdir)/maxpath.h
exec.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
exec.o: $(topdir)/error.h $(topdir)/general.h
exec.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
exec.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/flags.h
exec.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
exec.o: $(srcdir)/common.h $(topdir)/execute_cmd.h $(topdir)/maxpath.h
exit.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
exit.o: $(topdir)/error.h $(topdir)/general.h
exit.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
exit.o: $(topdir)/subst.h $(topdir)/externs.h
exit.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
exit.o: $(topdir)/maxpath.h
fc.o: $(topdir)/builtins.h $(topdir)/command.h $(srcdir)/bashgetopt.h
fc.o: $(topdir)/bashhist.h
fc.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h $(topdir)/error.h
fc.o: $(topdir)/general.h $(topdir)/maxpath.h
fc.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
fc.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/shell.h
fc.o: $(topdir)/flags.h $(topdir)/unwind_prot.h $(topdir)/variables.h
fg_bg.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
fg_bg.o: $(topdir)/error.h $(topdir)/general.h
fg_bg.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
fg_bg.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
fg_bg.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
getopts.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
getopts.o: $(topdir)/error.h $(topdir)/general.h
getopts.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
getopts.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
getopts.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
hash.o: $(topdir)/builtins.h $(topdir)/command.h $(topdir)/quit.h
hash.o: $(topdir)/execute_cmd.h $(topdir)/hashlib.h
hash.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
hash.o: $(topdir)/error.h $(topdir)/general.h
hash.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
hash.o: $(srcdir)/common.h $(topdir)/maxpath.h
help.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
help.o: $(topdir)/error.h $(topdir)/general.h
help.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
help.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
help.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
history.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
history.o: $(topdir)/error.h $(topdir)/general.h
history.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
history.o: $(topdir)/subst.h $(topdir)/externs.h
history.o: $(topdir)/filecntl.h $(topdir)/shell.h $(topdir)/unwind_prot.h
history.o: $(topdir)/variables.h $(topdir)/bashhist.h $(topdir)/maxpath.h
inlib.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
inlib.o: $(topdir)/error.h $(topdir)/general.h
inlib.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
inlib.o: $(topdir)/maxpath.h $(topdir)/subst.h $(topdir)/externs.h
inlib.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
jobs.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h $(topdir)/error.h
jobs.o: $(topdir)/general.h $(topdir)/quit.h $(srcdir)/bashgetopt.h
jobs.o: $(topdir)/maxpath.h $(topdir)/externs.h
jobs.o: $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h $(topdir)/subst.h
jobs.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h 
kill.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h $(topdir)/error.h
kill.o: $(topdir)/general.h $(topdir)/subst.h $(topdir)/externs.h
kill.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
kill.o: $(topdir)/shell.h $(topdir)/trap.h $(topdir)/unwind_prot.h
kill.o: $(topdir)/variables.h $(topdir)/maxpath.h
let.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
let.o: $(topdir)/error.h $(topdir)/general.h
let.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
let.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
let.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
pushd.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
pushd.o: $(topdir)/error.h $(topdir)/general.h
pushd.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
pushd.o: $(topdir)/subst.h $(topdir)/externs.h
pushd.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
pushd.o: $(topdir)/maxpath.h $(srcdir)/common.h
read.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
read.o: $(topdir)/error.h $(topdir)/general.h
read.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
read.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
read.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
return.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
return.o: $(topdir)/error.h $(topdir)/general.h
return.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
return.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
return.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
set.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
set.o: $(topdir)/general.h $(topdir)/subst.h $(topdir)/externs.h
set.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
set.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
set.o: $(topdir)/maxpath.h $(topdir)/error.h
setattr.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
setattr.o: $(topdir)/error.h $(topdir)/general.h $(topdir)/maxpath.h
setattr.o: $(topdir)/quit.h $(srcdir)/common.h $(srcdir)/bashgetopt.h
setattr.o: $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h $(topdir)/subst.h
setattr.o: $(topdir)/externs.h
setattr.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h 
shift.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
shift.o: $(topdir)/error.h $(topdir)/general.h
shift.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
shift.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
shift.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
source.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
source.o: $(topdir)/error.h $(topdir)/general.h
source.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
source.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
source.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
suspend.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
suspend.o: $(topdir)/error.h $(topdir)/general.h
suspend.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
suspend.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
suspend.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
test.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
test.o: $(topdir)/error.h $(topdir)/general.h
test.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
test.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
test.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
times.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
times.o: $(topdir)/error.h $(topdir)/general.h
times.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
times.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
times.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
trap.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
trap.o: $(topdir)/error.h $(topdir)/general.h $(topdir)/externs.h
trap.o: $(topdir)/quit.h $(srcdir)/common.h $(topdir)/maxpath.h
trap.o: $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h $(topdir)/subst.h
trap.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
trap.o: $(topdir)/execute_cmd.h
type.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
type.o: $(topdir)/error.h $(topdir)/general.h
type.o: $(topdir)/quit.h $(srcdir)/common.h $(topdir)/maxpath.h
type.o: $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h $(topdir)/subst.h
type.o: $(topdir)/externs.h
type.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h 
ulimit.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
ulimit.o: $(topdir)/error.h $(topdir)/general.h
ulimit.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
ulimit.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
ulimit.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
umask.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
umask.o: $(topdir)/error.h $(topdir)/general.h
umask.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
umask.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
umask.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
wait.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
wait.o: $(topdir)/error.h $(topdir)/general.h
wait.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
wait.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
wait.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
shopt.o: $(topdir)/command.h ../config.h $(topdir)/memalloc.h
shopt.o: $(topdir)/error.h $(topdir)/general.h 
shopt.o: $(topdir)/quit.h $(topdir)/dispose_cmd.h $(topdir)/make_cmd.h
shopt.o: $(topdir)/subst.h $(topdir)/externs.h $(topdir)/maxpath.h
shopt.o: $(topdir)/shell.h $(topdir)/unwind_prot.h $(topdir)/variables.h
shopt.o: $(srcdir)/common.h $(srcdir)/bashgetopt.h
bashgetopt.o: $(topdir)/bashansi.h $(topdir)/ansi_stdlib.h
mkbuiltins.o: $(topdir)/bashansi.h $(topdir)/ansi_stdlib.h
fc.o: $(topdir)/bashansi.h $(topdir)/ansi_stdlib.h

#bind.o: $(RL_LIBSRC)chardefs.h $(RL_LIBSRC)readline.h $(RL_LIBSRC)keymaps.h
