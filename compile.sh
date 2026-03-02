#!/bin/bash

python createZbornikMD.py
pandoc compiledMarkdownBooks/sbornik_novogo_zaveta_latinica.md -o Sbornik_novogo_zaveta_latinica.pdf --from markdown+hard_line_breaks  --pdf-engine=xelatex 
pandoc compiledMarkdownBooks/sbornik_novogo_zaveta_kirilica.md -o Sbornik_novogo_zaveta_kirilica.pdf --from markdown+hard_line_breaks --pdf-engine=xelatex 
pandoc compiledMarkdownBooks/sbornik_novogo_zaveta_trad_kirilica.md -o Sbornik_novogo_zaveta_trad_kirilica.pdf --from markdown+hard_line_breaks --pdf-engine=xelatex 
pandoc compiledMarkdownBooks/sbornik_novogo_zaveta_glagolica.md \
  -o Sbornik_novogo_zaveta_glagolica.pdf \
  --from markdown+hard_line_breaks \
  --pdf-engine=xelatex \
  -V header-includes="\usepackage{fontspec}
\newfontfamily\glafont{NotoSansGlagolitic}[Path=fonts/,Extension=.ttf,UprightFont=*-Regular]
\usepackage{ucharclasses}
\setDefaultTransitions{}{}
\setTransitionsFor{Glagolitic}{\glafont}{}"