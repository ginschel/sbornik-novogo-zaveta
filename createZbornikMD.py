from transliterator import (
    latin_to_stdCyrillic,
    latin_to_tradCyrillic,
    latin_to_glagolitic
)
def create_book(title, foreword_file, output_file, transform, *content_files):
    with open("compiledMarkdownBooks/"+output_file, "w", encoding="utf-8") as outfile:

        # Transform title (foreword stays untouched)
        transformed_title = transform(title) if transform else title

        metadata = rf"""---
title: {transformed_title}
author:
date:
documentclass: book
mainfont: NotoSerif
mainfontoptions:
  - Path=fonts/
  - Extension=.ttf
  - UprightFont=*-Regular
  - BoldFont=*-Bold
  - ItalicFont=*-Italic
  - BoldItalicFont=*-BoldItalic
fontsize: 12pt
geometry: a4paper, margin=2.5cm
linestretch: 1.3
header-includes:
  - \usepackage{{parskip}}
  - \usepackage{{titlesec}}
  - \newcommand{{\sectionbreak}}{{\clearpage}}

---

"""
        outfile.write(metadata)

        # Foreword (NO transliteration)
        with open(foreword_file, "r", encoding="utf-8") as fore:
            foreword_text = fore.read().strip()

            # Only replace ě with e if transform is latin_to_glagolitic
            if transform == latin_to_glagolitic:
                foreword_text = foreword_text.replace("ě", "e")

            outfile.write(foreword_text)

        outfile.write("\n\n")
        translationsfolder = "translations/"
        # Content files (WITH transliteration)
        for content_file in content_files:
            with open(translationsfolder + content_file, "r", encoding="utf-8") as content:
                text = content.read().strip()

                if transform:
                    text = transform(text)

                outfile.write(text)

            outfile.write("\n\n")
            
if __name__ == "__main__":

    title = "Sbornik tekstov Novogo Zavěta"

    foreword = "foreword.md"
    proglas = "proglas.md"
    ev_mat = "Evangelje_Mateja.md"
    ev_mrk = "Evangelje_Marka.md"
    ev_luk = "Evangelje_Lukasa.md"
    ev_jon = "Evangelje_Joana.md"
    luk_dej = "dějanja_fixed.md"
    apendix = "molitvy.md"

    content_files = (
        proglas,
        ev_mat,
        ev_mrk,
        ev_luk,
        ev_jon,
        luk_dej,
        apendix
    )

    # Latin original
    create_book(
        title,
        foreword,
        "sbornik_novogo_zaveta_latinica.md",
        None,
        *content_files
    )

    # Standard Cyrillic
    create_book(
        title,
        foreword,
        "sbornik_novogo_zaveta_kirilica.md",
        latin_to_stdCyrillic,
        *content_files
    )

    # Traditional Cyrillic
    create_book(
        title,
        foreword,
        "sbornik_novogo_zaveta_trad_kirilica.md",
        latin_to_tradCyrillic,
        *content_files
    )

    # Glagolitic
    create_book(
        title,
        foreword,
        "sbornik_novogo_zaveta_glagolica.md",
        latin_to_glagolitic,
        *content_files
    )

    print("All book versions have been succesfully created.")