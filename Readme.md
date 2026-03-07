# Sbornik tekstov Novogo Zavěta

## Overview

**Sbornik tekstov Novogo Zavěta** is a collection of translations of the four Gospels and the *Acts of the Apostles* into Interslavic.

The goal of this project is to present the foundational texts of the New Testament in a form understandable to speakers of all Slavic languages, following the original vision of a common Slavic literary tradition.

## Requirements

- **Python 3.10 or newer** – for running the transliteration and book-generation scripts.  
- **Pandoc** – for converting Markdown to PDF.  
  [Install instructions](https://pandoc.org/installing.html)  
- **XeLaTeX** – required by Pandoc to generate PDFs.  

## Available transliterations

The compile script generates PDF versions of the text in multiple orthographies and scripts:

* **Standard Latin orthography of Interslavic**
* **Standard transliteration into Cyrillic**
* **Glagolitic script**
* **Simplified transliteration into Etymological Traditional Cyrillic**, giving the text a pseudo-archaic appearance reminiscent of historical Slavic manuscripts

All transliterations are performed by a **custom Python script** included in the repository, rather than using the official TypeScript transliteration tools. This ensures that PDF compilation has **minimal dependencies**, requiring only Pandoc, XeLaTeX, and the included fonts.


## Translation Sources

### Gospel of Matthew, Gospel of Luke, and Acts of the Apostles

These translations are based primarily on:

* *Biblia Gdańska* (1881)
* German *Allioli Bible*
* sometimes *Biblia Jakuba Wujka* (especially in Luke 1)

Together, these three sources constitute approximately 99% of the textual basis.

In cases of uncertainty regarding interpretation or phrasing, I occasionally consulted the Polish *Biblia Tysiąclecia* for comparison and clarification.

### Gospel of Mark

Main sources:

* *Biblia Jakuba Wujka*
* German *Allioli-Arndt Bible* (1914)

### Gospel of John

Main sources:

* *Biblia Jakuba Wujka*
* *Biblia Gdańska* (1881)

Because these translations are closely based on the Latin *Vulgata* and may at times be more difficult to understand than modern renderings, I occasionally referred to:

* German *Einheitsübersetzung*
* Polish *Biblia Tysiąclecia*

This was done when questions of interpretation or wording arose.

## Appendix

In addition to the biblical texts, the project includes an appendix containing several prayers translated into Interslavic.

All prayers in the appendix were translated by me, except for the Divine Mercy Chaplet (*Korunica božjemu milosrdju*), which is included with permission from Michał Swat.


## Acknowledgments

I would like to express my sincere gratitude to Michał Swat for granting me permission to include his excellent translation of the *Proglas*—the poetic foreword traditionally attributed to St. Cyril and attached to the first Slavic translation of the Gospels. The text included here is based on his Proglas video on the official Medžuslovjansky YouTube channel.

I have made only minimal editorial adjustments, correcting minor spelling inconsistencies—likely stemming from the use of an older version of the Interslavic dictionary—and adapting the names of the Evangelists to correspond with the forms used in my Gospel translations, in order to maintain consistency and avoid confusion.

I also thank him for allowing me to include his translation of the Divine Mercy Chaplet (*Korunica božjemu milosrdju*).

## License

All translations authored by me — including:

* The four Gospels
* The Acts of the Apostles
* All prayers in the appendix (except the Divine Mercy Chaplet)

and all my scripts in this repository are licensed under the **Creative Commons CC BY 4.0** license.

This license allows anyone to:

* Share
* Copy
* Redistribute
* Adapt
* Build upon the material

for any purpose, including commercial use, provided that appropriate credit is given.

The translations by Michał Swat are included with his explicit permission and are not covered by the Creative Commons license applied to the rest of this work.

The Noto fonts in this repository are free fonts that can be used freely, including in commercial projects.

## Project Status

⚠️ **This project is not yet complete.**

While the translations themselves are largely finished, significant work remains.

Contributions are very welcome.


## How You Can Contribute

We are looking for help with:

* Improving the LaTeX layout
* Language corrections to increase clarity and accessibility for all Slavs
* Adding explanatory footnotes with alternative vocabulary
* Providing illustrations for each chapter
* Designing a book cover
* Fixing punctuation, spelling, and grammatical issues
* Theological review and corrections
* Adding more prayers to the appendix
* (Optional) Converting simplified orthography into etymological spelling

If these aspects are improved collaboratively, this project can become a high-quality publication and a meaningful contribution to strengthening the literary presence of the Interslavic language.

## Vision

My greatest motivation in undertaking this work was the hope that it might one day serve many readers and demonstrate the expressive power of Interslavic.

Although I may not have sufficient time to complete all refinements on my own, I firmly believe that community collaboration can accomplish even tasks that initially seem unrealistic.

As a computer scientist, I see parallels in large cooperative projects such as the development of Linux or major reverse-engineering initiatives — examples of how shared vision and collective effort can achieve extraordinary results.

It is my sincere hope that this project will inspire others to continue building upon it.
