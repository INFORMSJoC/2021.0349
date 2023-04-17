##############################################################################
# SPECtools2000
#   Version 0.1
#   This makefile should NOT be changed other than to customize for a 
#   particular benchmark.  Users may overide variables by placing them
#   in the Makefile.spec file.  Or by using the "runspec" program to 
#   build the Makefile.spec file for them.
###############################################################################
#	BENCHMARK	-- standard definitions for this benchmark

NUMBER    = 176
NAME      = gcc.exe

# Provide a list of the object modules which are required to link the binary
OBJS = c-parse.$(OBJ) c-lang.$(OBJ) c-lex.$(OBJ) c-pragma.$(OBJ) c-decl.$(OBJ) \
	    c-typeck.$(OBJ) c-convert.$(OBJ) c-aux-info.$(OBJ) c-common.$(OBJ) \
	    c-iterate.$(OBJ) toplev.$(OBJ) version.$(OBJ) tree.$(OBJ) print-tree.$(OBJ) \
	    stor-layout.$(OBJ) fold-const.$(OBJ) function.$(OBJ) stmt.$(OBJ) expr.$(OBJ) \
	    calls.$(OBJ) expmed.$(OBJ) explow.$(OBJ) optabs.$(OBJ) varasm.$(OBJ) rtl.$(OBJ) \
	    print-rtl.$(OBJ) rtlanal.$(OBJ) emit-rtl.$(OBJ) real.$(OBJ) dbxout.$(OBJ) \
	    sdbout.$(OBJ) dwarfout.$(OBJ) xcoffout.$(OBJ) integrate.$(OBJ) jump.$(OBJ) cse.$(OBJ) \
	    loop.$(OBJ) unroll.$(OBJ) flow.$(OBJ) stupid.$(OBJ) combine.$(OBJ) regclass.$(OBJ) \
	    local-alloc.$(OBJ) global.$(OBJ) reload.$(OBJ) reload1.$(OBJ) caller-save.$(OBJ) \
	    insn-peep.$(OBJ) reorg.$(OBJ) sched.$(OBJ) final.$(OBJ) recog.$(OBJ) reg-stack.$(OBJ) \
	    insn-opinit.$(OBJ) insn-recog.$(OBJ) insn-extract.$(OBJ) insn-output.$(OBJ) \
	    insn-emit.$(OBJ) insn-attrtab.$(OBJ) m88k.$(OBJ) getpwd.$(OBJ) convert.$(OBJ) \
	    bc-emit.$(OBJ) bc-optab.$(OBJ) obstack.$(OBJ)

# Choose your compilers.  Vendor makefile wrappers may override these.
# Make sure that you specify the correct compiler for linking!!!

CC = $(CC)
LINKER = $(LINKER)
EXEF = out:

OPT =  $(OPT)
LIBS =
OBJOPT = -c
OBJ = obj

STD_CFLAGS =
STD_LDFLAGS =

EXTRA_CFLAGS = -Dalloca=_alloca
EXTRA_LDFLAGS = $(LINKFLAGS) -STACK:10000000
EXTRA_LIBS =

CFLAGS  = $(STD_CFLAGS) $(OPT) $(EXTRA_CFLAGS)
LDFLAGS = $(STD_LDFLAGS) $(EXTRA_LDFLAGS)

$(NAME): $(OBJS)
	$(LINKER) @<<link.rsp
$(LDFLAGS) -$(EXEF)$@ $(OBJS) $(LIBS) $(EXTRA_LIBS)
<<keep


compile: $(NAME)

.c.obj::
    $(CC) @<<cl.rsp
$(CFLAGS) -c $<
<<keep
