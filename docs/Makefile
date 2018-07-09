SPHINXOPTS    =
SPHINXBUILD   = python -msphinx
SPHINXPROJ    = webviz
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) --help

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.
%: Makefile
	mkdir -p _static
	@$(SPHINXBUILD) -W -b $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
