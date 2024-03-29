# Generated automatically from Makefile.in by configure.
# This Makefile is for the Bash/documentation directory -*- text -*-.
#
RM	    = rm -f

topdir = ..
srcdir = .
VPATH = .:.

infodir = ${prefix}/info

mandir = ${prefix}/man
manpfx = man

man1ext = 1
man1dir = $(mandir)/$(manpfx)$(man1ext)
man3ext = 3
man3dir = $(mandir)/$(manpfx)$(man3ext) 

INSTALL = /usr/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644
BUILD_DIR = /home/jeff/git-mods/2021.0349/data/bash/src

# bad style
RL_LIBDIR = $(topdir)/lib/readline

# unused
TEXINDEX    = texindex
TEX	    = tex

MAKEINFO    = makeinfo
TEXI2DVI    = ${topdir}/support/texi2dvi
TEXI2HTML   = ${topdir}/support/texi2html
QUIETPS	    = #set this to -q to shut up dvips
DVIPS	    = dvips -D 300 $(QUIETPS) -o $@	# tricky
TEXINPUTDIR = $(RL_LIBDIR)/doc

MKDIRS      = ${topdir}/support/mkdirs

# This should be a program that converts troff to an ascii-readable format
NROFF	    = groff -Tascii

# This should be a program that converts troff to postscript
GROFF	    = groff

HSUSER      = $(RL_LIBDIR)/doc/hsuser.texinfo
RLUSER      = $(RL_LIBDIR)/doc/rluser.texinfo

.SUFFIXES:	.0 .1 .3 .ms .ps .txt .dvi

.1.ps:
	$(RM) $@
	-${GROFF} -man $< > $@

.1.0:
	$(RM) $@
	-${NROFF} -man $< > $@

.ms.ps:
	$(RM) $@
	-${GROFF} -ms $< > $@

.ms.txt:
	$(RM) $@
	-${NROFF} -ms $< > $@

.3.ps:
	$(RM) $@
	-${GROFF} -man $< > $@

.3.0:
	$(RM) $@
	-${NROFF} -man $< > $@

all: ps info dvi text html
nodvi: ps info text html

ps: bash.ps bashbug.ps readline.ps article.ps builtins.ps
dvi: bashref.dvi bashref.ps 
info: bashref.info
text: bash.0 bashbug.0 builtins.0 readline.0
html: bashref.html

bashref.dvi: $(srcdir)/bashref.texi $(HSUSER) $(RLUSER)
	TEXINPUTS=.:$(TEXINPUTDIR):$$TEXINPUTS $(TEXI2DVI) $(srcdir)/bashref.texi

bashref.ps: bashref.dvi
	$(RM) $@
	$(DVIPS) bashref.dvi

bashref.info: $(srcdir)/bashref.texi $(HSUSER) $(RLUSER)
	$(MAKEINFO) --no-split -I$(TEXINPUTDIR) $(srcdir)/bashref.texi

bashref.html: bashref.texi $(HSUSER) $(RLUSER)
	$(TEXI2HTML) -I $(TEXINPUTDIR) $(srcdir)/bashref.texi

bash.dvi: bash.texinfo $(HSUSER) $(RLUSER)
	TEXINPUTS=.:$(TEXINPUTDIR):$$TEXINPUTS $(TEXI2DVI) bash.texinfo

bashman.ps: bash.dvi
	$(RM) $@
	$(DVIPS) bash.dvi

bash.txt: bash.1
bash.ps: bash.1
bashbug.ps: bashbug.1
builtins.ps: builtins.1 bash.1
bash.0: bash.1
bashbug.0: bashbug.1
builtins.0: builtins.1 bash.1
readline.0: readline.3
readline.ps: readline.3
article.ps: article.ms

faq:	faq.news faq.news2 faq.mail faq.version

faq.version:	FAQ.version FAQ
	sh mkfaqvers FAQ.version > $@

faq.news: FAQ FAQ.headers.news faq.version
	$(RM) $@
	cat FAQ.headers.news faq.version FAQ > $@

faq.news2: FAQ FAQ.headers.news2 faq.version
	$(RM) $@
	cat FAQ.headers.news2 faq.version FAQ > $@

faq.mail: FAQ FAQ.headers.mail faq.version
	$(RM) $@
	cat FAQ.headers.mail faq.version FAQ > $@

clean:
	$(RM) *.aux *.cp *.fn *.ky *.log *.pg *.toc *.tp *.vr *.cps \
		*.pgs *.bt *.bts *.rw *.rws *.fns *.kys *.tps *.vrs *.o \
		core rluser.texinfo hsuser.texinfo

distclean mostlyclean: clean
	$(RM) Makefile

maintainer-clean:	clean
	$(RM) *.0 *.ps *.dvi *.info *.txt
	$(RM) Makefile

installdirs:
	-test -d $(man1dir) || $(SHELL) ${MKDIRS} $(man1dir)
	-test -d $(man3dir) || $(SHELL) ${MKDIRS} $(man3dir)
	-test -d $(infodir) || $(SHELL) ${MKDIRS} $(infodir)
	
install: info installdirs
	-$(INSTALL_DATA) $(srcdir)/bash.1 $(man1dir)/bash.${man1ext}
	-$(INSTALL_DATA) $(srcdir)/bashbug.1 $(man1dir)/bashbug.${man1ext}
	-$(INSTALL_DATA) $(srcdir)/readline.3 $(man3dir)/readline.${man3ext}
	-$(INSTALL_DATA) $(srcdir)/bashref.info $(infodir)/bash.info
# uncomment the next line to install the builtins man page
#	$(INSTALL_DATA) builtins.1 $(man1dir)/bash_builtins.${man1ext}

uninstall:
	$(RM) $(man1dir)/bash.${man1ext} $(man1dir)/bashbug.${man1ext}
	$(RM) $(man3dir)/readline.${man3ext} $(infodir)/bash.info

# for use by chet
inst:	bashref.texi
	$(SHELL) ./mkinstall
	cmp -s INSTALL ../INSTALL || mv INSTALL ../INSTALL
	$(RM) INSTALL

posix:	bashref.texi
	$(SHELL) ./mkposix
	cmp -s POSIX.NOTES ../CWRU/POSIX.NOTES || mv POSIX.NOTES ../CWRU/POSIX.NOTES
	$(RM) POSIX.NOTES
