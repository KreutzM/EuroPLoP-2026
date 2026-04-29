# latexmk configuration for the EuroPLoP 2026 LNCS paper.
# Keep generated files local; do not commit build artifacts.

$pdf_mode = 1;
$interaction = 'nonstopmode';

# Use pdflatex because the Springer LNCS workflow and current sources are pdflatex-compatible.
$pdflatex = 'pdflatex %O %S';

# Keep the default output directory so Overleaf/local workflows remain familiar.
# The Makefile/.gitignore keep generated files out of version control.

$bibtex_use = 1;

# Continue to show useful diagnostics while still failing on hard errors.
$silent = 0;
