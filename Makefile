INPUT = research-paper
BUILDDIR = build
all:
	pandoc				\
	  --filter pandoc-citeproc	\
	  --csl=turabian.csl		\
	  --standalone			\
	  --smart                       \
	  -t native                     \
	  --filter smallcaps.py    	\
	  $(INPUT).md		\
	|				\
	pandoc				\
	  -f native                     \
	  --latex-engine=lualatex	\
	  --template=template.tex	\
          --variable fontsize=12pt      \
          --variable linkcolor=black    \
          --variable urlcolor=black     \
          --variable citecolor=black    \
	  --no-tex-ligatures            \
	  --smart                       \
	  -o $(BUILDDIR)/$(INPUT).tex

	rubber --into build --warn all --pdf $(BUILDDIR)/$(INPUT).tex



docx:
	pandoc				\
	  --filter pandoc-citeproc	\
	  --csl=turabian.csl		\
	  --standalone			\
	  --smart                       \
	  --filter smallcaps.py    	\
	  $(INPUT).md			\
          -o $(INPUT).docx
