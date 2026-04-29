.PHONY: pdf check clean distclean check-bib check-markers

MAIN := main
LATEXMK := latexmk
LATEXMK_FLAGS := -pdf -interaction=nonstopmode -halt-on-error

pdf:
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

check: pdf check-bib check-markers

check-bib:
	python3 scripts/check_bib_keys.py literature.bib

check-markers:
	python3 scripts/check_markers.py

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
