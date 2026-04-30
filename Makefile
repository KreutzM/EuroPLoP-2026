.PHONY: pdf check clean distclean check-bib check-markers check-tools

MAIN := main
LATEXMK := latexmk
LATEXMK_FLAGS := -pdf -interaction=nonstopmode -halt-on-error

# Prefer python3 on Unix-like systems, but fall back to python/py for Windows.
# Override manually if needed, e.g. `make PYTHON=py check`.
PYTHON ?= $(shell command -v python3 2>/dev/null || command -v python 2>/dev/null || command -v py 2>/dev/null || echo python)

pdf:
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

check: check-tools pdf check-bib check-markers

check-tools:
	@command -v $(LATEXMK) >/dev/null 2>&1 || { echo "ERROR: latexmk not found. Install MiKTeX/TeX Live and make sure latexmk is on PATH."; exit 1; }
	@$(PYTHON) --version >/dev/null 2>&1 || { echo "ERROR: Python not found. Install Python 3 or run 'make PYTHON=py check'."; exit 1; }

check-bib:
	$(PYTHON) scripts/check_bib_keys.py literature.bib

check-markers:
	$(PYTHON) scripts/check_markers.py

clean:
	$(LATEXMK) -C $(MAIN).tex
	find . -maxdepth 1 -type f \( \
		-name '*.aux' -o -name '*.bbl' -o -name '*.bcf' -o -name '*.blg' -o \
		-name '*.fdb_latexmk' -o -name '*.fls' -o -name '*.log' -o -name '*.out' -o \
		-name '*.run.xml' -o -name '*.synctex.gz' -o -name '*.toc' -o -name '*.lof' -o \
		-name '*.lot' -o -name '*.acn' -o -name '*.acr' -o -name '*.alg' -o \
		-name '*.glg' -o -name '*.glo' -o -name '*.gls' -o -name '*.ist' -o \
		-name '*.xdy' \
	\) -delete

# Remove generated PDF as well. Use before creating a clean release/build state.
distclean: clean
	rm -f $(MAIN).pdf
