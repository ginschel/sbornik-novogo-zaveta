---
title: Sbornik tekstov Novogo Zavěta
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
  - \usepackage{parskip}
  - \usepackage{titlesec}
  - \newcommand{\sectionbreak}{\clearpage}

---

# Foreword

## Foreword

This volume, titled Sbornik tekstov Novogo Zavěta, presents my translations of the four Gospels and the Acts of the Apostles into Interslavic. The work aims to offer the foundational texts of the New Testament in a form that is understandable to speakers of all Slavic languages, following the original vision of a common Slavic literary tradition.

The translations of the Gospel of Luke, the Acts of the Apostles, and equally the Gospel of Matthew are based primarily on the Biblia Gdańska and the German Allioli Bible, which together constitute the foundation for approximately 99% of the text. In cases of uncertainty regarding interpretation or phrasing, I occasionally consulted the Polish Biblia Tysiąclecia for comparison and clarification, and sometimes Biblia Jakuba Wujka (especially in Luke 1).

For the Gospel of Mark, I relied mainly on the Biblia Jakuba Wujka and the German Allioli-Arndt Bible (1914).

For the Gospel of John, my principal source texts were the Biblia Jakuba Wujka and the Biblia Gdańska (1881).

Since these translations are closely based on the Latin Vulgata and can at times be more difficult to understand than modern renderings, I occasionally referred to the German Einheitsübersetzung and again to the Polish Biblia Tysiąclecia when questions of interpretation or wording arose.

Given the length and complexity of these biblical texts, it is possible that certain passages may require refinement in future revisions. I intend to review and improve the translations over time in order to ensure greater clarity, linguistic balance, and theological precision.

In addition to the biblical texts, this volume contains an appendix with several prayers translated into Interslavic.

I would like to express my sincere gratitude to Michał Swat for granting me permission to include his excellent translation of the Proglas—the poetic foreword traditionally attributed to St. Cyril and attached to the first Slavic translation of the Gospels. There could hardly be a more fitting introduction to Gospel translations in a Slavic language than the first known Slavic poem itself. The text of the Proglas included in this volume is based on his Proglas video on the official Medžuslovjansky YouTube channel. I have made only minimal editorial adjustments, correcting a few minor spelling inconsistencies—likely stemming from the use of an older version of the Interslavic dictionary—and adapting the names of the Evangelists to correspond with the forms used in my Gospel translations, in order to maintain consistency and avoid confusion. I also thank him for allowing me to include his translation of the Divine Mercy Chaplet (Korunica božjemu milosrdju) in the appendix.

## License and Copyright

All translations authored by me—including the four Gospels, the Acts of the Apostles, and all prayers in the appendix except for the Divine Mercy Chaplet—are licensed under the Creative Commons CC BY 4.0 license.

This license permits anyone to share, copy, redistribute, adapt, and build upon the material for any purpose, including commercial use, provided that appropriate credit is given to the original author.

The translations by Michał Swat are included with his explicit permission and are not covered by the Creative Commons license applied to the rest of this work.

## The State of the Project

This project is not yet complete. While I have invested many hours in producing the translations themselves, much work remains to be done.

Contributors are warmly invited to assist with:

* improving the LaTeX layout,
* correcting and refining the language to increase clarity and accessibility for all Slavs,
* adding footnotes with alternative vocabulary where certain words may not be universally understood,
* providing illustrations for each chapter,
* designing a book cover,
* correcting punctuation, spelling, and grammatical errors that may have occurred due to the length of the text,
* offering theological review and corrections,
* adding more prayers to the appendix,
* optionally adapting the simplified orthography into an etymological spelling system.

If these aspects are improved through collaborative effort, I am convinced that *Sbornik tekstov Novogo Zavěta* can become a high-quality publication and a meaningful contribution to elevating the status of the Interslavic language.

My greatest motivation in undertaking this work was the hope that it might one day serve many readers and demonstrate the expressive power of Interslavic. Although I may not have sufficient time to complete all the necessary refinements on my own, I firmly believe that community collaboration can achieve even tasks that initially seem unrealistic.

As a computer scientist, I see strong parallels in large cooperative projects such as the development of Linux or major reverse-engineering initiatives—endeavors that demonstrate how shared vision and collective effort can accomplish extraordinary things.

It is my sincere hope that this work will inspire others to continue building upon it.

1 March 2026
Aleksander Ginschel

\newpage
\tableofcontents

# Proglas

Ja jesm prědslovje svetomu Evangelju: 
Kako proroki prědpověděli prěde,
Hristos ide sobrati narody,
za to čto on jest světlo vsemu temu světu
To stalo se vo našem sedmom stolětju.
Za to čto oni rěkl: slěpi budut uviděti,
gluhi uslyšati slovo pisemno.
Tako, Boga poznati jest trěba. 


Iz togo povoda slyšite, Slovjani vsi,
za to čto tutoj dar jest od Boga dany,
dar božji, on jest pravoj česti,
dar dušam, ktory nikogda ne gnije,
tym dušam, ktore jego budut prijeti.
Matej, Mark, Lukas, Joan
učet vse narody i govoret:
Ako li svojih duš krasotu viděti hčete
i radovati se, grěšnu tmu izgnati
i světa togo prazdninu odložiti
i rajsky život sobě dobyti
i izběgti od ognjev goreča,
slyšite v toj moment svoj razum.

Slyšite cěly slovjansky narode:
slyšite slovo, ktoro od Boga prišlo,
slovo, ktoro krmi člověčje duše,
slovo, ktoro krěpi i srdce i razum,
slovo, ktoro gotovi daby Boga poznati.
Bez světla ne bude radovati se,
oko ktoro vidi vse božje stvorjenje,
no jemu vse bude ni krasivo ni vidno.
Tako i duša vsekaka bez bukv: ne znaje
zakona božjego, zakona knižnogo i duhovnogo,
zakona, ktory objavjaje raj božji.
A ktory sluh, ktory zvuka groma
ne slyši, može bojati se Boga?
I nozdra, ktore ne njuhajete cvěty,
kako božje čudo možete razuměti?
I usta, ktore ne čujut sladkosti,
tvoret člověka tako kako kamenj.
Vyše od togo duša bezpismenna
javjaje se vo ljudah mrtva.

To vsečto my, brati,
jesmo obdumali, i govorimo
dobru pomoč, ktora vsih ljudij odděliti bude
od žverskogo života i žednosti,
dabyste ne imali razum nerazumny:
za to čto v čudžem jezyku slušajuči slovo
kako měděnogo zvona glas slyšite.
Za to tako svety Pavol učil i rěkl:
Molitvu svoju voznošeči k Bogu,
ja hču samo pet sloves rěkti 
i razumlivo govoriti, daby i vsi brati razuměli,
a ne govoriti mrak rěči nerazumnyh.
Itak, kaky člověk, ktory ne razuměje, 
može prědložiti povědku mudru,
ktora by rěkla nam prave rěči? Za to čto
kako gnilnost ovladyvaje tělo i vse razpadaje,
vyše od gnoja gnije, kogdy [tělo] ne imaje
svojego jedanja, tako i duša vsekaka slaběje [vo] žitju,
ako božjego ne imaje života,
kogdy slova božjego ne slyši.

Rěknijmo ješče drugu veliko mudru
povědku k ljudjam,
ktori ljubet jedin drugogo,
ktori hčut rasti božjim rastom,
ili tomu, kto ne znaje toj pravoj věry,
kako sěmena padajuče na nivě,
tako jest i na srdcah člověčjih,
one potrěbujut dožda božjih bukv,
daby plod božji rastl lěpje.
Kto može rěkti vse opověsti
napominajuče vse bez knig narody,
ktore ne govoret glasom razumlivym?
Ni někto, kto znaje vse jezyky,
ne može opisati jih bezsilnost.
Jednakože, nehaj i ja svoju povědku prědstavjam,
i kažu mnogo mudrosti v nemnogyh rěčah.
Gole sut vse bez knig narody:
bez oružja ne mogut bojevati
so protivnikom duš naših i gotovi
sut daby stali plěnom muk věčnyh.
No, narody ktore vraga ne ljubite,
i boriti se s njim silno myslite,
otvorite ohotno dveri razuma vašego,
prijmite oružje tvrdo v tutoj čas,
ktore kujut knigy Gospodnje, ktore
glavu djavolsku močno raztirajut.

Bukvy te, kto bude prijeti
tomu Hristos bude objaviti svoju mudrost,
i pismenami duše vaše podkrěpi
i apostolami s prorokami vsimi.
A ljudi, ktori jih slova
govoret možni budut
vraga ubiti i pobědu prinositi dobru k Bogu,
i izběgti od gnijučego razpada těla;
těla, ktorogo život - kako vo sně
ne padajuči, no krěpko stoječi,
oni Bogu budut objavjati se kako hrabri,
i stojati po desnici božjego trona,
kogda ognjem [Bog] bude suditi narody.
Oni budut radovati se s angelami navěky,
slaviti věčno Boga milosrdnogo
vsimi knižnymi pěsnjami,
Bogu pěvati, ktory ljubi ljudij.
Ibo Jemu prinaleži vsa slava,
Tobě čest i hvala, Božji Syne,
zajedno so Otcem i Svetym Duhom
na věky věkov od vsego stvora. Amin

# Evangelje Mateja

## Razděl 1

1 Kniga o rodu Jezusa Hristosa, syna Davida, syna Abrahama.
2 Abraham byl otcem Izaaka, a Izaak byl otcem Jakoba, a Jakob byl otcem Judy, i bratov jego.
3 A Juda byl otcem Faresa i Zora, ktoryh mati byla Tamara, a Fares byl otcem Esroma, a Esrom byl otcem Arama.
4 A Aram byl otcem Aminadaba, a Aminadab byl otcem Naasona, a Naason byl otcem Salmona.
5 A Salmon byl otcem Booza, ktorogo mati byla Rahava, a Booz byl otcem Obeda, ktorogo mati byla Rut, a Obed byl otcem Jessogo.
6 A Jesse byl otcem Davida kralja, a David kralj byl otcem Solomona, a mati byla ta, ktora byla ženoju Urijova.
7 A Salomon byl otcem Roboama, a Roboam byl otcem Abiasa, a Abija byl otcem Azy.
8 A Aza byl otcem Jozafata, a Jozafat byl otcem Jorama, a Joram byl otcem Ozije.
9 A Ozija byl otcem Joatama, a Joatam byl otcem Ahaza, a Ahaz byl otcem Ezekije.
10 A Ezekija byl otcem Manasesa, a Manases byl otcem Amona, a Amon byl otcem Jozije.
11 A Jozija byl otcem Jekonije i bratov jego v času prěseljenja do Babilona.
12 A po prěseljenju do Babilona Jekonija byl otcem Salatijela, a Salatijel byl otcem Zorobabela.
13 A Zorobabel byl otcem Abijuda, a Abijud byl otcem Ilijakima, a Ilijakim byl otcem Azora.
14 A Azor byl otcem Sadoka, a Sadok byl otcem Ahima, a Ahim byl otcem Ilijuda.
15 A Ilijud byl otcem Eleazara, a Eleazar byl otcem Mattana, a Mattan byl otcem Jakoba.
16 A Jakob byl otcem Jozefa, muža Marije, iz ktoroj se narodil Jezus, ktorogo zovut Hristos.
17 A tak jest od Abrahama až do Davida četyrinadset pokoljenij, a od Davida až do prěseljenja do Babilona, četyrinadset pokoljenij, a od prěseljenja do Babilona až do Hristosa, četyrinadset pokoljenij.
18 A Rodženje Jezusa Hristosa tako bylo: Ibo kogdy Marija, mati jego, svatbena byla Jozefu, najprvo než se sošli, najdena byla brěmennoju Duhom Svetym.
19 No Jozef, muž jej, suči čestnym i ne hčuči jej izstaviti i činiti neslavnoju, htěl ju tajno ostaviti.
20 A kogdy on o tym myslil, vot jemu se Angel Gospodinsky vo snu ukazal, govoreči: Jozefe, syne Davida! ne boji se prijeti Mariju, ženu tvoju; ibo, čto se v njej počelo, iz Duha Svetogo jest.
21 A urodi syna, i nazoveš imenom jego Jezus; ibo on izbavi ljud svoj od jih grěhov.
22 A to se vse stalo, aby se izpolnilo, čto pověděno od Gospodina črěz proroka:
23 Vot děva bude brěmenna i urodi syna, a nazovut imenom jego Emanuel, čto znači: Bog s nami.
24 Itak Jozef vozbudivši se iz sna, učinil, kako jemu pověděl Angel Gospodinsky, i prijel ženu svoju;
25 No jej ne poznal, až porodila syna svojego prvorodnogo, i nazval imenom jego Jezus.

## Razděl 2

1 A kogdy se Jezus narodil v Betlehemu Judejskom vo dni Heroda kralja, mudrci iz vozhoda prišli do Jeruzalema, govoreči:
2 Kde jest toj kralj židovsky, ktory se narodil? Ibo jesmo viděli zvězdu jego na vozhodu, i jesmo prijehali, abysmo jemu se poklonili.
3 Kogdy togo kralj Herod uslyšal, prěstrašil se, i ves Jeruzalem s njim.
4 Zatom sobravši vsih vysših duhovnikov i učiteljev ljuda, dovědal se od njih, kde by se iměl Hristos roditi.
5 A oni jemu rěkli: V Betlehemu Judejskom: ibo tak jest napisano črěz proroka:
6 I ty Betleheme, zemjo Judejska! nijednoju měroju ne jesi najmenša medžu gradami knezev Judejskymi; ibo iz tebe izojde načelnik, ktory vladati bude nad mojim izraelskym ljudom.
7 Itak Herod pozvavši tajno tyh mudrcov, spěšno se dovědal od njih o času, v ktorom se zvězda pokazala.
8 A poslavši jih do Betlehema, rěkl: Jehavši, spěšno se dovědajte o tom dětetu; a kogdy nahodite, objavite mně, abyh i ja prijehavši, poklonil se jemu.
9 Oni itak, uslyšavši kralja, pošli; a ta zvězda, ktoru viděli na vozhodu, vodila jih, až priševši, stanula nad městom, kde bylo děte;
10 A kogdy ugleděli tu zvězdu, radovali se s velikoju radostju;
11 I vševši v dom, našli děte s Marijeju, materiju jego, a padši, poklonili se jemu, i otvorivši skarby svoje, žrtvovali jemu dary: zlato i kadilo i mirru.
12 No suči napomněni od Boga vo snu, aby se ne vračali do Heroda, inoju stežkoju vratili se do krajiny svojej.
13 A kogdy oni odšli, vot Angel Gospodinsky ukazal se vo snu Jozefu govoreči: Vstavši, prijmi to děte i mati jego, a idi do Egipta, a bud tam, až tobě pověm; ibo Herod bude iskati dětetka, aby je ubil.
14 On vstavši, vzel děte i mati jego v noči, i odšel do Egipta;
15 I byl tam až do smrti Herodq, aby se izpolnilo, čto pověděno od Gospodina črěz proroka: Iz Egipta jesm pozval syna mojego.
16 Itak Herod ugleděvši, že byl razočarovany črěz mudrcov, razgněval se mnogo, a kazal ubiti vse děti, ktore byli v Betlehemu i po vsih granicah, od vozrasta dvoh lět i niže, do časa, o ktorom se spěšno dověděl od mudrcov.
17 Itak se izpolnilo, čto pověděno bylo črěz Jeremije proroka:
18 Glas v Ramě slyšany jest, plač, i veliky ston: Rahel plačuča synov svojih ne dala se utěšiti, zatom, že jih už ne ima.
19 A kogdy umrl Herod, vot Angel Gospodinsky ukazal se vo snu Jozefu v Egiptu,
20 Govoreči: Vstavši, prijmi děte i mati jego, a idi do zemji Izraelskoj; ibo umrli ti, ktori htěli děte ubiti.
21 A on vstavši, vzel do sebe děte i mati jego, i prišel do zemji Izraelskoj.
22 No kogdy uslyšal, že Arhelaj vladal na Judzkoj zemji na městu Heroda, otca svojego, bojal se tam idti; no napomněny suči od Boga vo snu, odstupil v stranu Galilejsku;
23 I priševši žil v gradu, ktory zovut Nazaret, aby se izpolnilo čto pověděno črěz prorokov: Nazarejcem nazvany bude.

## Razděl 3

1 V te dni prišel Joan Krestitelj, kažuči na pustynji na judzkoj zemji,
2 A govoreči: Obračajte se; ibo se približilo kraljevstvo nebesko.
3 Toj ibo jest on, o ktorom bylo pověděno črěz Izaiji proroka: Glas zovučego na pustynji: Pripravite stežku Gospodinsku, premo činite stežky jego.
4 A toj Joan iměl oděž iz srsti velbluda, i pas koženy okolo svojih bedr, a jeda jego byla saranča I lěsny med.
5 Itak prišel do njego ljud iz Jeruzalema i vsa Judejska zemja i vsa krajina okolo Jordana;
6 I byli kreščeni od njego v Jordanu, izpovědajuči grěhy svoje.
7 A kogdy ugleděl mnogo iz Farizejev i Saducejev prihodečih do kresta, rěkl jim: Narode zmiji! kto vam pokazal, abyste izběgli prěd budučim gněvom?
8 Prinosite že itak plody dostojny pokajanja;
9 A ne myslite, že možete govoriti: Otca imamo Abrahama; ibo govorju vam, že Bog i iz tyh kamenjev vozbuditi može děti Abrahamu.
10 A už i sěkyra pri korenjah drěv položena jest; vsako itak drěvo, ktoro ne prinosi ploda dobrogo, bude izrězano, i v ogonj kydnuto.
11 Ja vas krešču vodoju k pokajanju; no toj, ktory ide za mnoju, močnějši jest nad mnoju; Jemu ne jesm dostojny, aby obuvi nositi; toj vas krestiti bude Duhom Svetym i ogonjem.
12 Ima lopatu v rukě jego, a očisti malat svoj, i sbere pšenicu svoju do gumna, no plěvy spali ogonjem neugasimym.
13 Itak Jezus prišel od Galileji nad Jordan do Joana, aby byl kreščeny od njego;
14 No jemu Joan mnogo zabranjal, govoreči: Ja trěbuju, abyh byl kreščeny od tebe, a ty ideš do mene?
15 A odgovarjajuči Jezus, rěkl do njego: Dopusti tutčas; ibo tak dostojno nam, abysmo izpolnili vse, čto spravědlivo; itak go dopustil.
16 A Jezus kreščeny suči, směsta vstupil iz vody, a vot se jemu odkryli nebesa, i viděl Duha Božjego, spuščajučego se kako golubicu, i prihodečego na njego;
17 A vot glas iz nebes govoril: Toj jest moj Syn ljubimy, za ktorogo imam simpatiju.

## Razděl 4

1 Itak Duh vvedl Jezusa na pustynju, aby byl pokušeny od djavla.
2 A postil četyrideseti dni i četyrideseti noči, potom gladnil.
3 I pristupivši do njego pokušitelj, rěkl: Jestli jesi Syn Božji, kaži, aby se te kamenje staly hlěbom.
4 A on odgovarjajuči rěkl: Napisano jest: Ne samym hlěbom člověk žiti bude, no vsakom slovom izhodečim črěz usta Božje.
5 Itak go vzel djavol do grada svetogo, i postavil go na narožnom svetilišča,
6 I rěkl jemu: Jestli jesi Syn Božji, spusti se na dol, ibo jest napisano: Angelam svojim razkaže o tobě, i budut tebe na rukah nosili, abys očevidno ne udaril o kamenj nogy svojej.
7 Rěkl jemu Jezus: No jest napisano: Ne budeš pokušati Gospodina, Boga tvojego.
8 Vzel go snova djavol na goru mnogo vysoku, i pokazal jemu vse kraljevstva světa i slavu jih,
9 I rěkl jemu: To vse dam tobě, jestli padši, pokloniš se mně.
10 Itak jemu rěkl Jezus: Pojdi von, satane! ibo jest napisano: Gospodinu Bogu tvojemu klanjati se budeš, i jemu samomu služiti budeš.
11 Itak go opustil djavol, a vot Angeli pristupili i služili jemu.
12 A kogdy uslyšal Jezus, že Joan byl prědany do vezenja, vratil se do Galileji;
13 A opustivši Nazaret, prišel, i žil v Kafarnaumu, ktoro jest nad morjem v granicah Zabulona i Neftalogo;
14 Aby se izpolnilo, čto pověděno črěz Izaiji proroka:
15 Zemja Zabulona i zemja Neftalogo pri stežkě morskoj za Jordanom, Galileja poganov;
16 Ljud, ktory sěděl v temnosti, viděl světlo veliko, a žiteljam v krajině v těnju smrti vošlo světlo.
17 Od togo časa začel Jezus kazati i govoriti: obračajte se, ibo se približilo kraljevstvo nebesko.
18 A kogdy Jezus hodil nad morjem Galilejskom, ugleděl dvoh bratov: Simona, ktorogo zovut Petrom, i Andreja, brata jego, ktori spuščali sět v morje; ibo byli rybakami.
19 I rěkl jim: Pojdite za mnoju, a učinju vas rybakami ljudij.
20 A oni momentalno opustivši sěti, šli za njim.
21 A postupivši odtud, ugleděl drugyh dvoh bratov, Jakoba, syna Zebedeja, i Joana, brata jego, v lodi s Zebedejem, otcem jih, popravjajučih sěti svoje, i pozval jih.
22 A oni skoro opustivši lod i otca svojego, pošli za njim.
23 I hodil Jezus črěz vsu Galileju, učeči v synagogah jih, i glaseči Evangelje kraljevstva, a lěčil vsaku hvorobu i vsaku nemoč posrěd ljuda.
24 I razošla se věst o njem po cěloj Siriji; i privodženo do njego vsih zlo imějučih se, s raznymi bolěznjami i nedugami, takože i vladenyh črěz běsov, i epileptykov i paralizovanyh; i ozdravjal jih.
25 A šel za njim ljud veliky iz Galileje, iz Dekapola, i iz Jeruzalema, i iz Judeje, i iz Zajordanije.

## Razděl 5

1 A Jezus videči ljuda, vstupil na goru; a kogdy usědl, pristupili do njego učeniki jego.
2 A otvorivši usta svoje, učil jih, govoreči:
3 Blagoslovjeni ubogi v duhu; ibo jih jest kraljevstvo nebesko.
4 Blagoslovjeni, ktori se smutet; ibo utěšeni budut.
5 Blagoslovjeni tihi; ibo oni dostanut zemju.
6 Blagoslovjeni, ktori gladnet i žedajut spravědlivosti; ibo oni syti budut.
7 Blagoslovjeni milosrdni: ibo oni milosrdja dostanut.
8 Blagoslovjeni ti čistogo srdca; ibo oni Boga ogledajut.
9 Blagoslovjeni pokoj čineči; ibo oni synami Božjimi nazvani budut.
10 Blagoslovjeni, ktori trpet gonjenje za spravědlivost; ibo jih jest kraljevstvo nebesko.
11 Blagoslovjeni jeste, kogdy vas nenaviděti budut, i vas prěslědujut, i govoriti vse zlo budut protiv vam, aby iz mojego povoda lgati.
12 Radujte se, i radujte se; ibo zaplata vaša bujna jest v nebesah; tak ibo gnali prorokov, ktori byli prěd vami.
13 Vy jeste soljju zemje; jestli itak solj ne bude imati vkusa, čim soliti budut? Do ničego se už ne bude dostojna, jedino aby byla von izkydana i od ljudij toptana.
14 Vy jeste světlo světa, ne može se grad ukryti na gorě ležeči.
15 Ni zapali se svěče, i ne postavja jej pod korec, no na svěčnik. O světi vsim, ktori sut v domu.
16 Tak nehaj světi světlo vaše prěd ljudami, aby vaše dobre děla viděli, a hvalili otca vašego, ktory jest v nebesah.
17 Ne myslite, abyh prišel razvezyvati zakon ili prorokov; jesm ne prišel  razvezyvati, no izpolniti.
18 Zapravdu ibo govorju vam: Až pominut nebo i zemja, jedna iota ili jedna črtka ne pomine iz zakona, až vse se stalo.
19 Kto by itak razvezal jedno iz tyh zapovědij najmenših, i učil by tak ljudij, najmenšim bude nazvany v kraljevstvu nebeskom; a ktokoli by činil i učil, toj bude velikym nazvany v kraljevstvu nebeskom.
20 Ibo govorju vam: Jestli ne bude obilnějša spravědlivost vaša, než naučenyh v Pismu i Farizejev, ne vojdete do kraljevstva nebeskogo.
21 Jeste slyšali, že rěčeno starym: Ne budeš ubivati; a ktokoli ubil, bude vinny sudu;
22 No ja vam govorju: Že vsaky, kto se gněva na brata svojego bez pričiny, bude vinny sudu; a ktokoli rěče bratu svojemu: Raka; bude vinny radu, a ktokoli rěče: Bezumniče! bude vinny ognju peklnomu.
23 A tak jestli bys žrtvoval dar tvoj na oltaru, a tam bys pomněl, že brat tvoj ima čto protiv tobě,
24 Ostavi tam dar tvoj prěd oltarem, a odidi, najprvo se pomiri iz bratom tvojim; a potom priševši žrtvuj dar tvoj.
25 Pomiri se s tvojim protivnikom skoro, dopoka jesi s njim na stežkě, by tebe očevidno protivnik ne podal sudji, a sudja by tebe podal slugě, i bys byl kydnuty do vezenja.
26 Zapravdu tobě govorju: Ne izojdeš odtud, až bys ne oddal do poslědnjego groša.
27 Jeste slyšali, že rěčeno starym: Ne budeš dělati prěljubstva;
28 No Ja vam govorju: Že vsaky, ktory gleda na ženu, aby ju žedal, už z njeju prěljubstvo v svojem srdcu sdělal.
29 Jestli tobě itak tvoje oko jest povodom grěha, izbavi se go, i kydni od sebe; ibo lěpje jest tobě, aby izgyne jedin iz členov tvojih, a vse tělo tvoje ne bylo kydnuto do ognja peklnogo.
30 A jestli tobě tvoja prava ruka jest povodom do grěha, odrěži ju, i kydni od sebe; ibo lěpje jest tobě, aby izgyne jedin iz členov tvojih, a vse tělo tvoje ne bylo kydnuto do ognja peklnogo.
31 Tož bylo rěčeno: Ktokoli opustil ženu svoju, nehaj jej da pismo razvodno;
32 No Ja vam govorju: Ktokoli opustil ženu svoju, kromě do dělanja prěljubstva, privodi ju v dělanje prěljubstva, a kto by opuščenu vzel, prěljubstvo děla.
33 Jeste tož slyšali, že rěčeno starym: Ne budeš lgati, no budeš se k Gospodinu držati tvojej prisegy;
34 No Ja vam govorju, abyste sovsěm ne prisegali, ni na nebo, ibo jest tronom Božjim;
35 Ni na zemju, ibo jest osnovoju nog jego; ni na Jeruzalem, ibo jest gradom velikogo kralja;
36 Ni na glavu tvoju budeš prisegati, ibo ne možeš jedinogo vlasa bělym ili črnym učiniti.
37 No govor vaš nehaj bude: Tak, tak; ne, ne; a čto vyše jest, to od zlogo jest.
38 Jeste slyšali, že rěčeno: Oko za oko, a zub za zub;
39 No Ja vam govorju: Abyste se ne protivili se zlomu, no kto by tebe udaril v tvoje pravo lice, daj jemu i drugo;
40 I tomu, ktory se s toboju hče sporiti prěd sudom i oděž tvoju vzeti, odpusti jemu i plašč;
41 A kto by tebe prinudžal idti tyseči krokov, idi s njim i dva tyseči;
42 Tomu, ktory tebe prosi, daj, a od togo, ktory hče od tebe pozajeti, ne odvračaj se.
43 Jeste slyšali, že rěčeno: Budeš miloval bližnjego tvojego, a budeš iměl v nenavisti neprijatelja tvojego;
44 No Ja vam govorju: Ljubite neprijateljev vaših; dobro činite tym, ktori vas imajut v nenavisti, i molite se za tymi, ktori vam zlost dělajut i vas gonet;
45 Abyste byli synami Otca vašego, ktory jest v nebesah; ibo on to čini, že solnce jego vozhodi na zlo i na dobro, i dožd spušča na čestny i na nečestnyh,
46 Ibo jestli ljubite tyh, ktori vas ljubet, kaku zaplatu imate? či i mytniki togo ne činet?
47 A jestli byste jedino bratov vaših pozdravjali, čto osobnogo činite? či i mytniki tako ne činet?
48 Budite vy itak doskonali, kako i Otec vaš, ktory jest v nebesah, doskonaly jest.

## Razděl 6

1 Strěžite se, abyste vaših nabožnyh děles ne činili prěd ljudami zato, abyste byli viděni od njih; inače ne budete iměli zaplaty u Otca vašego, ktory jest v nebesah.
2 Zatom, kogdy daš milostynje, ne trubi prěd soboju, kako liceměri činet v synagogah i na ulicah, aby byli hvaljeni od ljudij; zapravdu govorju vam, že už dostali svoju zaplatu.
3 No ty kogdy daš milostynje, nehaj ne zna lěvica tvoja, čto čini pravica tvoja.
4 Aby milostynja tvoja byla v tajnosti, a Otec tvoj, ktory vidi v tajnosti, toj tobě javno odda.
5 A kogdy se moliš, ne bud kako liceměri; ibo oni ljubet v synagogah i na rogah ulic stoječi, moliti se, aby byli viděni od ljudij; zapravdu govorju vam, že už dostali svoju zaplatu.
6 No ty, kogdy se moliš, vojdi do komory svojej, a zaključivši dveri svoje, moli se do Otca tvojego, ktory jest v tajnosti; a Otec tvoj, ktory vidi v tajnosti, odda tobě javno.
7 A moleči se, ne budite mnogoslovni, kako pogani; ibo oni myslet, že za svoju mnogoslovnost uslyšani budut.
8 Ne budite itak jim podobni, ibo zna Otec vaš, čego potrěbujete, najprvo než  vy o to prosite.
9 Vy itak tako nehaj se molite; Otče naš, ktory jesi v nebesah! Sveti se ime tvoje;
10 Prijdi kraljevstvo tvoje; bud volja tvoja kako v nebu, tak i na zemji.
11 Hlěba našego vsakodennogo daj nam tutdenj.
12 I odpusti nam naše grěhy, kako i my odpuščajemo našim dolžnikam;
13 I ne vodi nas na pokušenje, no nas spasi od zlogo; ibo tvoje jest kraljevstvo i moč i hvala na věky. Amen.
14 Ibo jestli odpustite ljudam jih grěhy, odpusti i vam vaš Otec nebesky;
15 A jestli ne odpustite ljudam jih grěhov, i vaš Otec ne odpusti vam vaših grěhov.
16 A kogdy postite, ne imajte smutnogo lica, kako liceměri; razrušajut ibo lica svoje, aby byli viděni od ljudij, že postet; zapravdu govorju vam, že už dostali svoju zaplatu.
17 No ty, kogdy postiš, omasti tvoju glavu, i umyj lice tvoje,
18 Abys ne byl viděny od ljudij, že postiš, no od Otca tvojego, ktory jest v tajnosti; a Otec tvoj, ktory vidi v tajnosti, odda tobě javno.
19 Ne sbirajte sobě skarbov na zemji, kde molj i rdža kaziti, i kde zloději podkopyvajut i kradut;
20 No sbirajte sobě skarby v nebu, kde ni molj ni rdža razžerajut, i kde zloději ne vlamyvajut se, ni kradut.
21 Ibo kde jest skarb vaš, tam jest i srdce vaše.
22 Oko tvoje jest svěčeju těla tvojego; jestli itak oko tvoje bylo čisto, vse tělo tvoje jasno bude;
23 Jestli jednako oko tvoje zlo bylo, vse tělo tvoje temne bude; jestli itak světlo, ktoro jest v tobě, temnotoju jest, sama temnost kaka velika bude?
24 Nikto ne može dvom gospodinam služiti, ibo jedinogo bude iměl v nenavisti, a drugogo bude miloval; ili jedinogo držati se bude, a drugogo prězira; ne možete Bogu služiti i mamonu.
25 Zato govorju vam: Ne bezpokojite se o život vaš, čto byste jeli, ili čto byste pili, ni o tělo vaše i čim byste se oděvali; či život ne jest važnějši než jeda, i tělo než oděž?
26 Pogledajte na ptice nebeske, ne sějut ni žnut, ni sbirajut do gumen, a Otec vaš nebesky je živi; či vy ne jeste mnogo važnějši nad njimi?
27 I kto iz vas zajmajučih se svojimi mysljami i nepokojem, može pridati do rasta svojego jedin lakot?
28 A o oděž začto že se bezpokojite? Prigledajte se lilijam polnym, kako rastut; ne rabotajut, ni snujut.
29 A Ja vam govorju, že ni Salomon vo cěloj slavě svojej ne byl tak oděty, kako jedna iz tyh.
30 Jestli itak travu polnu, ktora tutdenj jest, zautra bude v peč kydnuta, Bog tak oděvaje, či ne mnogo veče vas! o malověrni!
31 Ne bezpokojite se itak, govoreči: Čto budemo jesti? ili čto budemo piti? ili čim se budemo oděvati?
32 Ibo togo vsego pogani iščut; Zna ibo Otec vaš nebesky, že togo vsego potrěbujete.
33 No iščite najprvo kraljevstva Božjego, i spravědlivosti jego, a to vse bude vam dodano.
34 Zatom ne bezpokojite se o zautrišnji denj: ibo zautrišnji denj bezpokojiti se bude o svoje potrěby. Dostatočno ima denj svojej bědy.

## Razděl 7

1 Ne sudite, abyste ne byli sudženi;
2 Ibo kakym sudom sudite, takym sudženi budete, i kakoju měroju měrite, taku vam měrjeno bude.
3 A čemu vidiš steblo v oku brata tvojego, a dosky, ktora jest v oku tvojem, ne vidiš?
4 Ili kako rěčeš bratu tvojemu: Dopusti, že vozmu steblo iz oka tvojego, a vot doska jest v oku tvojem.
5 Liceměre! Vozmi najprvo dosky iz oka tvojego, itak prěglediš, abys izjel steblo iz oka brata tvojego.
6 Ne davajte svetogo psam, ni kydnite vaših perl prěd svinje, by jih očevidno ne toptali nogami svojimi, i obrativši se ne raztrgali vas.
7 Prosite, a bude vam dano, iščite, a nahodite; stukajte, a bude vam otvorjeno.
8 Vsaky ibo, ktory prosi, bere; a kto išče, nahodi; a tomu, ktory stuka, bude otvorjeno.
9 či iz vas jest člověk, ktorogo prosil by syn jego o hlěb, I jemu da kamenj?
10 A kakby prosil o rybu, či jemu da zmiju?
11 Jestli vy itak suči zlymi, znate dobre dary davati dětam vašim, čim veče Otec vaš, ktory jest v nebesah, da dobre věči tym, ktori go proset.
12 Vse itak, čto byste htěli, aby vam ljudi činili, tak i vy činite jim; toj ibo jest zakon i proroki.
13 Vhodite črěz těsne vrata; ibo široke sut vrata i široka jest stežka, ktora vodi na izgubu, a mnogo jih jest, ktori črěz ju vhodet.
14 A těsne sut vrata i těsna jest stežka, ktora vodi do života; a malo jih jest, ktori ju nahodet.
15 A shranite se falšivyh prorokov, ktori prihodet do vas v koži ovce, no vnutri sut volkami i predatorami.
16 Iz plodov jih poznate jih; či sbirajut iz trna plody vina, ili iz osta figy?
17 Tak tobě vsako dobro drěvo dobre plody prinosi; no zlo drěvo zle plody prinosi.
18 Ne može dobro drěvo plodov zlyh prinositi, ni drěvo zlo plodov dobryh prinositi.
19 Vsako drěvo, ktoro ne prinosi ploda dobrogo, byvaje izrězano i v ogonj kydnuto.
20 A tak iz plodov jih poznate jih.
21 Ne vsaky, ktory mně govori: Gospodine, Gospodine! vojde do kraljevstva nebeskogo; no toj, ktory čini volju Otca mojego, ktory jest v nebesah.
22 Mnogo jih rěče mně v tom dnju: Gospodine, Gospodine! Či jesmo v imenu tvojem ne prorokovali, i v imenu tvojem djavlov ne izganjali, i v imenu tvojem mnogo čudes ne činili?
23 A itak jim pověm: Jesm vas nikogdy ne znal; odidite od mene, ktori činite krivdy.
24 Vsakogo itak, ktory slyše tyh slov mojih i čini je, sravnju mužu mudromu, ktory postavil dom svoj na kamenju;
25 I spal silny dožd, i prišel potop, i větry vějali, i udarili na dom, no ne upadl, ibo byl osnovany na kamenju.
26 A vsaky, ktory slyše tyh slov mojih, a ne čini jih, sravnju mužu bezumnomu, ktory postavil dom svoj na pěsku;
27 I spal dožd silny, i prišel potop, i větry vějali, a udarili na dom, i upadl, a byl veliky upad jego.
28 I stalo se, kogdy dokončil Jezus tyh slov, že se udivil ljud nad naukoju jego.
29 Ibo jih učil kak toj, ktory moč imaje, a ne kako naučeni v Pismu.

## Razděl 8

1 A kogdy spuščal se iz gory, šel za njim veliky ljud;
2 A vot leprosny priševši, poklonil se jemu, govoreči: Gospodine! jestli hčeš, možeš mene očistiti.
3 I iztrgnuvši Jezus ruku, dotknul go, govoreči: Hču, bud očiščeny; i momentalno byl očiščeny iz lepry jego.
4 Itak jemu rěkl Jezus: Bud ostražny, abys nikomu o tom ne govoril, no idi, ukaži se duhovniku, i žrtvuj dar, ktory prikazal Mojzes na svědočstvo za njih.
5 A kogdy Jezus všel do Kafarnauma, prišel do njego sotnik, proseči go,
6 I govoreči: Gospodine! sluga moj leži v domu paralizovany, i težko se muči.
7 I rěkl jemu Jezus: Ja prijdu i ozdravju go.
8 A odgovarjajuči sotnik rěkl: Gospodine! ne jesm dostojny, abys všel pod strěhu moju; no jedino rěči slovo, a bude ozdravjany sluga moj.
9 Ibo jesm ja člověk pod močju inogo, no imaju pod soboju vojinov; i govorju tomu: Idi, a ide; a drugomu: Prijdi, a prihodi; a slugě mojemu: Čini to, a čini.
10 A kogdy to uslyšal Jezus, udivil se, i rěkl tym, ktori šli za njim: Zapravdu govorju vam: Ni v Izraelu takoj velikoj věry jesm ne našel.
11 A govorju vam: Že mnogo jih od vozhoda i od zapada prijde, a usědut za stolom s Abrahamom i s Izaakom i s Jakobom v kraljevstvu nebeskom.
12 No syni kraljevstva budut izkydnuti v temnosti vně, tam bude plač i skripěnje zubov.
13 I rěkl Jezus sotniku: Idi, a kako jesi uvěril, nehaj tobě se stane; i ozdravjany jest sluga jego v toj že časině.
14 A kogdy Jezus prišel do doma Petra, ugleděl svekrov jego, ktora ležala na ložu i imala gorečku.
15 I dotknul ruky jej, i opustila ju gorečka; i vstala, a služila jim.
16 A kogdy byl večer, privedli do njego mnogo vladanyh črěz běsov: i izganjal duhov slovom; i vsih, ktori se zlo iměli, ozdravjal;
17 Aby se izpolnilo, čto pověděno črěz Izaiji proroka: On nemoči naše na sebe vzel, a bolěznji naše nosil.
18 A videči Jezus veliky ljud okolo sebe, kazal plyvti na drugu stranju morja.
19 Itak pristupivši něktory iz naučenyh v Pismu, rěkl jemu: Učitelju! pojdu za toboju, kdekoli pojdeš.
20 I rěkl jemu Jezus: Lisi imajut jamy, a ptice nebeske gnězda; no Syn člověčsky ne ima, o čto by glavu oprl.
21 A drugy iz učenikov jego rěkl jemu: Gospodine! dopusti mně najprvo odidti i pogrebti otca mojego;
22 No jemu Jezus rěkl: Pojdi za mnoju, a nehaj umrli pogrebajut mrtvyh svojih.
23 A kogdy on vstupil v lod, vstupili za njim i učeniki jego.
24 A vot se velika burja stala na morju, tak že se lod valami pokryvala; a on spal.
25 A pristupivši učeniki jego, vozbudili go, govoreči: Gospodine! izbavi nas, pogynemo.
26 I rěkl do njih: Začto že jeste bojazlivi? o malověrni! Itak vstavši, zgromil větry i morje, i stalo se utišenje veliko.
27 A ljudi se divili, govoreči: Kaky to jest, že jemu i větry i morje poslušne sut?
28 A kogdy se on prišel na drugu stranju morja do krajiny Gergezenov, priběgli jemu dva vladani črěz běsov iz grobov izhodeči, mnogo diki, tak že ne mogl nikto prěhoditi toju stežkoju.
29 A vot vozkliknuli, govoreči: Čto my s toboju imamo, Jezuse, Syne Božji? Jesi prišel tu prěd časom mučiti nas?
30 I bylo daleko od njih stado veliko svinej, ktore pasli se.
31 Itak go djavli prosili, govoreči: Jestli nas izgoneš, dopusti nam vstupiti v stado tyh svinej.
32 I rěkl jim: Idite. A oni izševši, vošli v to stado svinej, a vot raztrgnuvši se vse stado svinej, s pogonom padlo v morje, i izgynuli v vodah.
33 No pastyri uběgli, a poševši do grada, glasili o vsem i o tom, čto se s tymi vladanyh črěz běsov stalo.
34 A ves grad izšel protiv Jesusu, a ugleděvši go prosili, aby iz jih granic odšel.

## Razděl 9

1 Itak vstupivši v lod, vratil se, i prišel do grada svojego;
2 A prinesli jemu paralizovanogo, na ložu ležečego. A videči Jezus věru jih, rěkl paralizovanomu: Dověrjaj, syne! odpuščene sut tobě grěhy tvoje.
3 A něktori iz naučenyh v Pismu govorili sami v sobě: Toj bogohuli.
4 A videči Jezus myslji jih, rěkl: Začto vy myslite zlo věči v srdcah vaših?
5 Ibo čto prostějše rěkti: Odpuščeno sut tobě grěhy, či rěkti: Vstani, i hodi?
6 No abyste znali, že ima moč Syn člověčsky na zemji odpuščati grěhy, itak rěkl paralizovanomu: Vstavši, vozmi lože tvoje, i idi do doma tvojego.
7 Itak vstavši, pošel do doma svojego.
8 To ugleděvši ljud, divoval se, i hvalil Boga, ktory dal taku moč ljudam.
9 A odhodeči odtud Jezus, ugleděl člověka sědučego v komorě mynicoj, ktorogo zvano Matej, i rěkl jemu: Pojdi za mnoju; itak vstavši, šel za njim.
10 I stalo se, kogdy Jezus sěděl za stolom v domu jego, že mnogo mytnikov i grěšnikov priševši, usědli s Jezusom i s jego učenikami.
11 To videči Farizeji, rěkli učenikam jego: Začto že s mytnikami i grěšnikami je vaš učitelj?
12 A Jezus uslyšavši togo, rěkl jim: Ne potrěbujut zdravi lěkara, no ti, ktori se zlo imajut.
13 Očevidno idite, a naučite se, čto to jest: Milosrdja hču, a ne žrtvy; ibo jesm ne prišel zvati spravědlivyh, no grěšnyh do pokajanja.
14 Itak prišli do njego učeniki Joana, govoreči: Začto my i Farizeji često postimo, a učeniki tvoji ne postet se?
15 I rěkl jim Jezus: Či mogut gosti svatby se smutiti, až s njimi jest mladoženih? No prijdut dni, kogdy od njih bude mladoženih odjety, a itak postiti budut.
16 A nijedin ne prišije platna novogo suknja na staru oděž; ibo to platno odimaje něčto od oděži, i stana se gorše prodrenje;
17 Ni lijut vina mladogo v stare buklaky; ibo inače razsadi buklaky, a vino izteče, i buklaky se izniščet; no mlado vino lijut v nove buklaky, i oboje byvajut hranjene.
18 To kogdy on do njih govoril, něktory načelnik synagogy priševši poklonil se jemu, govoreči: Dočerka moja umrla; no pojdi, a položi na nju ruku tvoju, a ožive.
19 Itak vstavši Jezus, šel za njim, i učeniki jego takože.
20 (A vot žena, ktora izplyvanje krvi stradala od dvanadset lět, pristupivši iz zada, dotknula dol oděži jego;
21 Ibo rěkla sama v sobě: Jestli jedino dotknu oděž jego, budu ozdravjana.
22 No Jezus obrativši se i ugleděvši ju, rěkl: Dověrjaj, dočerko! věra tvoja tebe ozdravila; i ozdravjana byla žena od toj časiny.)
23 A kogdy prišel Jezus v dom načelnika, i ugleděl flejtnistov i glasny ljud,
24 Rěkl jim: Odstupite; ibo děvka ne umrla, no spi. I smějali se iz njego.
25 No kogdy izgnany byl ljud, vševši, vzel ju za ruku, i vstala děvka.
26 I razošla se ta věst po cěloj zemji.
27 A kogdy Jezus odhodil odtud, šli za njim dva slěpi, zovuči i govoreči: Syne Davida! pomiluj se nad nami.
28 A kogdy on všel do doma, prišli do njego slěpi; i rěkl jim Jezus: Věrite, že to mogu učiniti? Rěkli jemu: Očevidno Gospodine!
29 Itak dotknul očij jih, govoreči: Po věrě vašej nehaj se vam stane.
30 I odkryli se oči jih; i kazal jim žestoko Jezus, govoreči: Uvažajte že, aby nikto o tym ne znal.
31 No oni izševši, raznesli to po cěloj toj zemji.
32 A kogdy oni izhodili, privedli jemu člověka němogo, vladeny črěz běsa.
33 A kogdy byl izgnany běs, snova govoril němy; i divoval se ljud, govoreči: Nikogdy se taka věč ne pokazala v Izraelu.
34 No Farizeji govorili: Črěz kneza djavolskogo izganja djavlov.
35 I hodil Jezus črěz vse grady i gradka, učeči v synagogah jih, i kažuči Evangelje kraljevstva, a ozdravjajuči vsaku bolěznj, i vsaku nemoč.
36 A videči ljud, pomiloval jih, ibo ljud byl ogorčany i razprašeny kako ovce ne imajuče pastyra.
37 Itak rěkl učenikam svojim: Urodžaj zapravdu veliky, no rabotnikov malo.
38 Prosite itak Gospodina urodžaja, aby izgnal rabotnikov na svoje sbože.

## Razděl 10

1 A pozvavši dvanadset učenikov svojih, dal jim moč nad duhami nečistymi, aby jih izganjali, i ozdravjali vsaku bolěznj i vsaku nemoč.
2 A dvanadset Apostolam sut imena: Prvy Simon, ktorogo zovut Petr, i Andrej, brat jego; Jakob, syn Zebedeja, i Joan, brat jego;
3 Filip i Bartolomej, Tomas i Matej toj mytnik, Jakob, syn Alfeusa, i Lebej, nazvany Tadej;
4 Simon Hananejac, i Judas Iskariot, ktory go tož prodal.
5 Tyh dvanadset poslal Jezus, jim govoreči: Na stežku poganov ne vhodite, i do grada Samarijanov ne vhodite;
6 No skorěje idite do ovc, ktore pogynuli iz doma Izraelskogo;
7 A iduči glasite: Približilo se kraljevstvo nebesko.
8 Boljnyh ozdravjajte, leprosnyh čistite, mrtvyh vozkresajte, djavlov izganjajte; zadarmo jeste vzeli, zadarmo davajte.
9 Ne berite so soboju zlata, ni srěbra, ni mědí do vaših měškov;
10 Ni torby na stežku, ni dvoh suknej, ni obuvi, ni kyja; ibo dostojny jest rabotnik jela svojej.
11 A do ktorogokoli grada ili gradka vojdete, dovědajte se, kto by v njem byl dostojny, a tam živite, až ne izojdete;
12 A vševši v dom, pozdravite go.
13 A jestli by dom togo byl dostojny, nehaj na njego prijde pokoj vaš; a jestli by ne byl dostojny, pokoj vaš nehaj se vrati do vas.
14 A kto by vas ne prijel, ni slyšal slov vaših, izhodeči iz doma ili iz grada togo, odtrěsajte prah iz nog vaših.
15 Zapravdu vam govorju: prostějše bude zemji Sodomskoj i Gomorskoj v denj sudny, než tomu gradu.
16 Vot Ja vas posylaju kako ovce medžu volki; budite itak mudrymi kako zmiji, a čistymi kako golubi,
17 A shranite se ljudij; ibo vas budut prědavati do sudom, i v synagogah svojih vas bičevati budut.
18 Takože prěd starosty i prěd kralji vodženi budete za mene, na svědočstvo jim i poganam.
19 No kogdy vas prědadut, ne bezpokojite se, kako i čto byste govorili; ibo vam dano bude v toj časině, čto byste iměli govoriti;
20 Ibo vy ne jeste, ktori budut govoriti, no duh Otca vašego, ktory govori za vas.
21 I prěda brat brata na smrt, i otec syna, i vstanut děti protiv roditeljam, i budut jih ubivati.
22 I budete v nenavisti u vsih za moje ime; no kto prětrpi do konca, toj bude izbavjeny.
23 A kogdy vas prěslědovati budut v tym gradu, běžite do drugogo; ibo zapravdu govorju vam, že ne obojdite gradov Izraelskyh, až prijde Syn člověčsky.
24 Ne jest učenik nad učiteljem, ni sluga nad Gospodinom svojim;
25 Dost učeniku, aby byl kako učitelj jego, a sluga kako Gospodin jego; jestli gospodara Beelzebubom nazvali, čim veče domovnikov jego nazyvati budut.
26 Zatom ne bojite se jih; ibo ničto ne jest ukrytogo, čto by ne imělo byti objavjeno, i ničto tajnogo, čego by se dověděti ne ima.
27 Čto vam v temnosti govorju, govorite na světlu; a čto na uho slyšite, proglasite na strěhah;
28 A ne bojite se tyh, ktori ubivajut těla, no duši ubiti ne mogut; no skorěje bojite se togo, ktory može i dušu i tělo izgubiti v peklnom ognju.
29 Či dvoh vrabcev za groš ne prodadut? A nijedin iz njih ne upade na zemju bez voli Otca vašego.
30 Až i vlasy vse na glavě vašej sčisljene sut.
31 Ne bojite se itak; jeste važnějši od vrabcev.
32 Vsaky itak, ktory by mene izpověděl prěd ljudami, izpověm go Ja tož prěd Otcem mojim, ktory jest v nebesah;
33 A kto by se mene odkazal prěd ljudami, odkažu se go i Ja prěd Otcem mojim, ktory jest v nebesah.
34 Ne myslite, jesm prišel davati pokoj na zemju; ne prišel jesm davati pokoja, no meč.
35 Ibo jesm prišel, abyh raztrgnutje učinil medžu synom a otcem jego, i medžu dočerkoju a materiju jej, takože medžu snahoju i svekrovju jej;
36 I neprijateljami budut člověku domovniki jego.
37 Kto ljubi otca ili mati nad mnoju, ne jest mně dostojny; a kto ljubi syna ili dočerku nad mnoju, ne jest mně dostojny;
38 A kto ne bere križa svojego, i ne ide za mnoju, ne jest mně dostojny.
39 Kto by našel dušu svoju, izgubi ju; a kto by izgubil dušu svoju za mene, nahodi ju.
40 Kto vas prijma, mene prijma; a kto mene prijma, prijma togo, ktory mene poslal.
41 Kto prijma proroka v imenu proroka, nagradu proroka prijma; a kto prijma spravědlivogo v imenu spravědlivogo, spravědlivogo nagradu prijma.
42 Kto by tož podal čašu zimnoj vody jednomu iz tyh malyh v imenu učenika, zapravdu govorju vam, ne izgubi nagrady svojej.

## Razděl 11

1 I stalo se, kogdy Jezus prěstal davati zapověd dvanadseti učenikam svojim, pošel odtud, aby učil i kazal v gradah jih.
2 A Joan uslyšavši v vezenju o dělah Hristosa, poslavši dvoh iz učenikov svojih,
3 Rěkl jemu: Ty jesi on, ktory ima prijdti, či inogo čekati imamo?
4 A odgovarjajuči Jezus, rěkl jim: Ševši, objavite Joanu, čto slyšite i vidite.
5 Slěpi videt, a hromi hodet, leprosni berut očiščenje, a gluši slyšet, umrli vozkresajut, i ubogym Evangelje razkazano byvaje;
6 A blagoslavjany jest, ktory se ne sumněva vo mně.
7 A kogdy oni odšli, začel Jezus govoriti do ljuda o Joanu: Čto jeste izšli na pustynji viděti? Či trn hvějuči se od větra?
8 No čto jeste izšli viděti? Či člověka v mekku oděž oblěčenogo? vot ktori mekku oděž noset, v domah kraljevskyh sut.
9 No čto jeste izšli viděti? Či proroka? Zapravdu govorju vam, i veče než proroka.
10 Ibo toj jest, o ktorym jest napisano: Vot ja posylaju Angela mojego prěd obličjem tvojim, ktory prigotovi stežku tvoju prěd toboju.
11 Zapravdu govorju vam: Ne vstal iz tyh, ktori se iz žen rodet, večši nad Joanom Krestiteljem; no ktory jest najmenšim v kraljevstvu nebeskom, večši jest, než on.
12 A od časa Joana Krestitelja až dotud kraljevstvo nebesko nasilje trpi, a nasilniki hvatajut je.
13 Ibo vsi proroki i zakon až do Joana prorokovali.
14 A jestli hčete prijeti, on jest Ilija, ktory iměl prijdti.
15 Kto ima uši k slyšanju, nehaj slyše.
16 No komu sravnju toj narod? podobny jest dětam, ktore sědet na trgah, i zovut do tovarišev svojih,
17 I govoret: Jesmo igrali vam, a jeste ne tancevali; jesmo pěvali pěsnje žalostne, a jeste ne plakali.
18 Ibo prišel Joan ni jeduči ni pijuči, a govoret: Djavla ima.
19 Prišel Syn člověčsky jeduči i pijuči, a govoret: Vot člověk nenasytnik i pijanica vina, prijatelj mytnikov i grěšnikov; i opravdana jest mudrost od synov svojih.
20 Itak začel napominati gradam, v ktoryh se največe jego čudes stalo, ibo ne pokajali se, govoreči:
21 Běda tobě Horazine! běda tobě Betsajdo! ibo kakby se stali v Tirě i v Sidonu te čudesa, ktore se u vas staly, davno by byli v vrěči i v pepelu by se pokajali.
22 Ibo govorju vam: Legše bude Tiru i Sidonu v sudnom dnju, než vam.
23 A ty Kafarnaume! ktoro jesi až do neba vozvyšeno, až do pekla kydnuto budeš; ibo kakby se stali v Sodomu te čudesa, ktore se stali u tebe, stal by až do dnja tutdennogo.
24 Tož govorju vam: Že legše bude zemji Sodomskoj v sudnom dnju, než tobě.
25 V tom času Jezus rěkl: Slavju tobě, Otče, Gospodine neba i zemji! jesi te věči ukryl prěd mudrymi i umnymi, a jesi objavil je dětam.
26 Zapravdu, Otče! tak tobě podobalo.
27 Vse věči dane mně sut od Otca mojego, i nikto ne zna Syna, jedino Otec. Ni Otca nikto zna, jedino Syn i toj, komu by htěl Syn objaviti.
28 Pojdite do mene vsi, ktori jeste otrudnjeni i obreměnjeni, a Ja vam dělam odpočinok ;
29 Prijmite jarmo moje na sebe, a učite se od mene, ibo jesm Ja tihy i pokornogo srdca; a nahodite odpočinok za vaše duše;
30 Ibo jarmo moje sladko jest, a brěme moje legko jest.

## Razděl 12

1 Někogdy šel Jezus v subotu črěz sboža, a učeniki jego byli gladni, i začeli rvati klasy i jesti.
2 A ugleděvši to Farizeji, rěkli jemu: Vot učeniki tvoji činet, čego se ne godi činiti v subotu.
3 A on jim rěkl: či jeste ne čitali, čto učinil David, kogdy byl gladny, i ti, ktori s njim byli?
4 Kako všel do doma Božjego, i hlěby žrtvene jel, ktoryh jemu se ne godilo jesti, ni tym, ktori s njim byli, jedino samym duhovnikam.
5 Ili jeste ne čitali v zakonu, že v subotu i duhovniki v crkvi subotu lamajut, a bez dolga sut?
6 No govorju vam, že tu něčto večše jest než svetilišče.
7 A kakby jeste znali, čto to jest: Milosrdja hču, a ne žrtvy, ne abyste osudili nevinnyh;
8 Ibo Syn člověčsky Gospodinom jest i suboty.
9 A odševši odtud prišel do synagogy jih;
10 A vot byl tam člověk imajuči ruku usohnutu; i pytali go, govoreči: Godi li se v subotu ozdravjati? aby go obvinili.
11 A on jim rěkl: Jest li člověk iz vas, ktory by iměl jednu ovcu, a kakby jemu ta v subotu v dol padla, či jej ne hvata i ne iztegne?
12 A čim važnějši jest člověk než ovca. Zatom godi se v subotu dobro činiti.
13 Itak rěkl člověku tomu: Iztegni ruku tvoju; a on iztegnul, i vozvračena jest do zdravja kako i druga.
14 A izševši Farizeji, učinili radu protiv njemu, kakoby go izgubili.
15 No Jezus poznavši to, odšel odtud, i šel za njim ljud veliky; i ozdravil jih vsih,
16 I zabranil jim, aby go ne izjavili,
17 Aby se izpolnilo, čto pověděno črěz Izaiji proroka:
18 Vot toj sluga moj, ktorogo jesm izbral, toj ljubimy moj, za ktorogo moja duša ima simpatiju; položu duha mojego na njim, a zakon narodam razkaže;
19 Ne bude se sporiti, ni bude zval, i nikto na ulicah ne uslyši glasa jego;
20 Trostiny sgnetenoj ne razlomi, a knota tlějučego ne ugasne, až sud ima pobědu;
21 A v jego imenu narodi budut iměti naděju.
22 Itak privedeno do njego vladanogo črěz běsa, ktory byl slěpy i němy, i ozdravil go, tak že slěpy i němy mogl govoriti i viděti.
23 I udivil se ves ljud, i govorili: či toj ne jest syn Davida?
24 No Farizeji uslyšavši to, rěkli: Toj ne izganja djavlov, jedino črěz Beelzebuba, kneza djavolskogo.
25 No Jezus videči myslji jih, rěkl jim: Vsako kraljevstvo razděljeno samo protiv sobě pustěje, i vsaky grad ili dom, sam protiv sobě razděljeny, ne ostane se.
26 A jestli satan satana izganja, sam protiv sobě razděljeny jest; kako se itak ostane kraljevstvo jego?
27 A jestli že ja črěz Beelzebuba izganjaju djavlov, syni vaši črěz kogo že izganjajut? Zatom oni sudjami vašimi budut;
28 A jestli že ja duhom Božjim izganjaju djavlov, togda do vas prišlo kraljevstvo Božje.
29 Ili kako može kto vstupiti do doma močnogo, i instrumenty jego razgrabiti, jestli by najprvo ne svezal togo močnogo? Potom može dom jego razgrabiti.
30 Kto ne jest so mnoju, protiv mene jest, a kto ne sbiraje so mnoju, razprašaje.
31 Zato govorju vam: Vsaky grěh i bogohuljenje ljudam odpuščene budut; no bogohuljenje protiv Duhu Svetomu ne bude odpuščeno ljudam.
32 I ktokoli rěkl slovo protiv Synu člověčskomu, jemu bude odpuščeno; no kto by govoril protiv Duhu Svetomu, ne bude jemu odpuščeno, ni v tom věku ni v budučim.
33 Činite že ili drěvo dobro, i plod jego dobry; ili činite drěvo zlo, i plod jego zly; ibo iz ploda drěvo poznano bude.
34 Narode zmiji! kako možete govoriti dobre věči, suči zlymi, ibo iz bujnosti srdca usta govoret?
35 Dobry člověk iz dobrogo skarba srdca iznosi dobre věči, a zly člověk iz zlogo skarba iznosi zle věči.
36 No govorju vam, že za vsako slovo prazdno, ktoro by ljudi govorili, budut vo dnju suda karani;
37 Ibo za govory tvoje budeš opravdany, i za govory tvoje budeš sudženy.
38 Itak odgovorili něktori iz naučenyh v Pismu i Farizejev, govoreči: Učitelju, hčemo od tebe znak viděti.
39 A on odgovarjajuči rěkl jim: Rod zly i dějuči prěljubstva znaka išče; no jemu ne bude znak dano, jedino znak Jonasa proroka.
40 Ibo kako Jona byl v brjuhu velikoj ryby tri dni i tri noči, tak bude Syn člověčsky v srdcu zemji tri dni i tri noči.
41 Muži iz Ninivi stanut na sudu s tym rodom, i osudet go, zatom že pokajali se na propověd Jonasa; a vot tu jest veče než Jona.
42 Kraljeva iz poldnja stane na sudu s tym rodom, i osudi go; ibo prišla iz granic zemji, aby slyšala mudrosti Salomona; a vot tu jest veče než Salomon.
43 A kogdy nečisty duh od člověka izhodi, hodi se po městah suhyh, iščuči odpočinka, no ne nahodi.
44 Itak govori: Vraču se do doma mojego, odkud jesm izšel; a priševši nahodi go prazdny i očiščeny i ukrašeny.
45 Itak ide, i bere so soboju sedm inyh gorših duhov, než on sam: a vševši živut tam, i byvajut poslědnje věči člověka togo gorše, než prve. Tak se stane i tomu rodu zlomu.
46 A kogdy on ješče govoril do ljuda, vot mati i brati jego stali prěd domom hčuči s njim govoriti.
47 I rěkl jemu něktory: Vot mati tvoja i brati tvoji stojet prěd domom, hčuči s toboju govoriti.
48 A on odgovarjajuči, rěkl tomu, čto jemu to pověděl: Ktora jest mati moja? i ktori sut brati moji?
49 A iztrgnuvši ruku svoju na učenikov svojih, rěkl: Vot mati moja i brati moji!
50 Ibo ktokoli činil volju Otca mojego, ktory jest v nebesah, toj jest bratom mojim, i sestroju i materiju.

## Razděl 13

1 A dnja togo izševši Jezus iz doma, usědl nad morjem:
2 I sobral se do njego veliky ljud, tak že vstupivši v lod, sěděl, a ves ljud stal na brěgu.
3 I govoril do njih mnogo v parabolah i rěkl: Vot izšel razsějati;
4 A kogdy on razsějal, něktore padlo pri stežkě; i priletěli ptice, a pojeli je.
5 A druge padli na město kamenisto, kde ne bylo mnogo zemji; i směsta otvorilo se, ibo ne imělo glubiny zemji.
6 No kogdy solnce vošlo, obžglo, a ibo ne imělo korenja obsohnulo.
7 A druge padli medžu trny, i kogdy izrastli trny, a udušili je.
8 A druge padli na zemju dobru i dali korist, jedno stokratno, druge šestdesetkratno, a druge tridesetkratno.
9 Kto ima uši k slyšanju, nehaj slyše.
10 Itak pristupivši učeniki, rěkli jemu: Začto jim v parabolah govoriš?
11 A on odgovarjajuči, rěkl jim: Vam dano znati tajnost kraljevstva nebeskogo, no tym ne dano;
12 Ibo kto ima, bude jemu dano, i izbytok imati bude. No kto ne ima, tomu i to, čto ima, bude od njego odjeto.
13 Zato jim v parabolah govorju, ibo videči ne videt, i slyšeči ne slyšet, ni razumějut.
14 I stane se v njih prědskazanje Izaiji, ktory govori: Sluhom slyšati budete, no ne razumějete; i videči viděti budete, no ne uvidite;
15 Ibo otvrdělo se srdce ljuda togo, a ušami težko slyšali, i oči svoje žmurili, aby očami ne viděli i ušami ne slyšali, a srdcem ne razuměli, i ne obratili se, abyh jih ozdravil.
16 No oči vaše blagoslovjene, že videt, i uši vaše, že slyšet;
17 Ibo zapravdu govorju vam, že mnogo prorokov i spravědlivyh žedalo viděti to, čto vy vidite, no ne viděli, i slyšati to, čto slyšite, no ne slyšali.
18 Vy itak slyšite paraboly togo sějatelja.
19 Jestli někto slyše slov o tym kraljevstvu, a ne razuměje, prihodi zly i hvata to, čto sějano v srdcu jego; toj jest, ktory pri stežkě sějany jest.
20 A na kamenistyh městah sějany toj jest, ktory slyši slova i momentalno je s radostju prijme;
21 No ne ima korenja v sobě, no časovy jest; a kogdy prihodi nepokoj, ili gonjenje za slova, směsta odstupajut iz věry.
22 A medžu trny sějany toj jest, ktory slyši slov; no nepokoj světa togo i iluzija bogatstv uduši slovo, i staje se bez koristi.
23 A na dobroj zemji sějany jest toj, ktory slyši slov i razuměje, toj korist prinosi; a prinosi jedin stokratno, drugy šestdesetkratno, a drugy tridsetkratno.
24 Drugu parabolu postavil jim, govoreči: Podobno jest kraljevstvo nebesko člověku, ktory razsějiva dobro sěme na svojem polju.
25 A kogdy ljudi usnuli, prišel neprijatelj jego, i sějal plevla medžu pšeniceju, i odšel.
26 A kogdy izrastlo sbože i korist prineslo, se pokazal i plevel.
27 Itak pristupivši slugi gospodarski, rěkli jemu: Gospodine! či jesi dobrogo sěmena ne sějal na tvojem polju? Odkud itak ima plevel?
28 A on jim rěkl: Zly člověk to učinil. I rěkli slugi do njego: A hčeš, abyhmo pošli i go sobrali?
29 A on rěkl: Ne! Abyste očevidno sbirali plevel, ne izkorenili zajedno s njim i pšenicu.
30 Dopustite obom zajedno rasti až do žetva; a časa žetva rěku rabotnikam: Sberite najprvo plevel, a svežite go v snopy do spaljenje; no pšenicu sberete do gumna mojego.
31 Ino parabolu postavil jim, govoreči: Podobno jest kraljevstvo nebesko zrnu gorčice, ktoro vzevši člověk, razsějal na svojem polju.
32 Najprvo najmenše jest iz vsih sěmen; no kogdy izraste, najvysše jest iz vsih rastlin, i staje se drěvom, tak že ptice nebeske prilětajuči, gnězda sobě činet na větkah jego.
33 Inu parabolu pověděl jim: Podobno jest kraljevstvo nebesko kvasu, ktory vzevši žena, ukryla vo tri měry muky, až vse kyslo bylo.
34 To vse govoril Jezus v parabolah do ljuda, a bez parabol ne govoril do njih;
35 Aby se izpolnilo, čto pověděno črěz proroka: Otvorju v parabolah usta moje, izrěku věči ukryte od osnovanja světa.
36 Itak izslal ljud I prišel Jezus do doma; i pristupili do njego učeniki jego, govoreči: Objasni nam podobnost o plevelah togo polja.
37 A on odgovarjajuči, rěkl jim: Toj, ktory razsěje dobro sěme, jest Syn člověčsky;
38 A polje jest svět, a dobrym sěmenem sut syni kraljevstva; no plevlami sut syni zlogo;
39 Neprijatelj, ktory go razsějal, jest djavol, a sbože jest koncem světa, a rabotniki sut Angelami.
40 Kako itak sbirajut plevel, a spali go v ognju, tak bude pri koncu togo světa.
41 Pošlje Syn člověčsky Angelov svojih, a oni sberut iz kraljevstva jego vse zlo, i tyh, ktori krivdy činet;
42 I kydnut jih v peč razpaljeny, tam bude plač i skripěnje zubov.
43 Itak čestni blěskati se budut kako solnce v kraljevstvu Otca svojego. Kto ima uši k slyšanju, nehaj slyši.
44 Podobno jest kraljevstvo nebesko skarbu ukrytomu v polju, ktory naševši go člověk ukryl, i iz radosti, ktoru iměl iz njego, odhodil. I vse, čto ima, proda, i kupuje tu polje.
45 Podobno jest kraljevstvo nebesko člověku kupcu, iščučemu krasivyh perl;
46 Naševši jednu mnogo dragoju perlu, odšel, i prodal vse, čto iměl, i kupil ju.
47 Podobno jest kraljevstvo nebesko sěti spuščenoj v morje, ktora ryby vsakogo roda hvata.
48 Kogdy byla polna, iztrgnuli rybaki ju na brěg, a usědši, izbirali dobre ryby v posudah, a zle von izkydali.
49 Tak bude pri koncu světa; izojdut Angeli, i vozmut zlo iz posrěd spravědlivyh,
50 I kydnut jih v peč razpaljeny; tam bude plač i skripěnje zubov.
51 Rěkl jim Jezus: Razuměli jeste to vse? Rěkli jemu: Tak, Gospodine!
52 A on jim rěkl: Zatom vsaky naučeny v Pismu, ktory stal se naučeny v kraljevstvu nebeskom, podobny jest otca rodiny, ktory iznosi iz skarba svojego nove i stare věči.
53 I stalo se, kogdy Jezus dokončil te paraboly, že pošel odtud.
54 A priševši do otčiny svojej, učil v synagogě jih, tak že se mnogo divili i govorili: Odkud tomu ta mudrost, i ta moč?
55 či toj ne jest syn stoljara? či mati jego ne zovut Mariju, a brati jego Jakob, i Jozef, i Simon, i Judas?
56 A sestry jego vse u nas ne sut? Odkud itak tomu to vse?
57 I sumněvali se o njem; no Jezus rěkl jim: Ne jest prorok bolje grdženy než v otčině svojej i v domu svojem.
58 I ne učinil tam mnogo čudes za nevěrje jih.

## Razděl 14

1 V tom času uslyšal Heroda Tetrarh, věsti o Jezusu.
2 I rěkl slugam svojim: Toj jest Joan Krestitelj; on vozkresnul, i zato se čudesa črěz njego dějut.
3 Ibo Herod shvatil Joana, svezal go i vložil do vezenja za Herodijadu, ženu Filipa, brata svojego.
4 Ibo jemu Joan govoril: Ne godi tobě se ju imati.
5 No kogdy go on htěl ubiti, bojal se ljuda: ibo go za proroka iměli.
6 Kogdy itak prišel denj urodženja Heroda, tancevala dočerka Herodijady posrěd gostev, i podobala se Herodu.
7 Zatom pod prisegoju oběčal jej dati, čegoby žedala.
8 A ona prědtym suči podgovorjena od materi svojej, rěkla: Daj mně tu na miskě glavu Joana Krestitelja.
9 I smutil se kralj; no za prisegu i za gostev kazal jej dati.
10 A poslavši mučitelja, sěkl Joana v vezenju.
11 I prineseno glavu jego na miskě, i prědano děvkě, i odnesla ju materi svojej.
12 A priševši jego učeniki vzeli tělo i pogrebli go, a pošli i pověděli Jezusu.
13 To uslyšavši Jezus, odstupil odtud v lodi na město prazdno, oddělno; a uslyšavši togo ljud, šli za njim iz města pěše.
14 Izševši itak Jezus ugleděl veliky ljud, i iměl simpatiju do njih i ozdravjal hvoryh jih.
15 A kogdy prihodil večer, pristupili do njego učeniki jego, govoreči: Prazdno jest to město, a čas už prěšel; izsylaj toj ljud, aby odševši do gradkov, kupili sobě jela.
16 A Jezus jim rěkl: Ne potrěba jim odhoditi, dajte vy jim něčto jesti.
17 No jemu oni rěkli: Ne imamo tu ničto. Jedino pet hlěbov i dvě ryby.
18 A on rěkl: Prinesite mně je tu.
19 I kazal ljudu usěsti na travě, vzel tyh pet hlěbov i dvě ryby, a pogledavši v nebo, blagoslavjal, a lamajuči daval učenikam hlěby, a učeniki ljudu.
20 I jeli vsi, a syti byli; i sobrali to, čto bylo iz ostatkov, v dvanadset polnyh košah.
21 A tyh, ktori jeli, bylo okolo peti tyseči mužev bez čisljenja žen i dětej.
22 A skoro prinudil Jezus učenikov svojih, aby vstupili v lod, i prěd njim na drugu stranu plavati, až izšlje ljud.
23 A izslavši ljud, vstupil na goru sam, aby se molil; a kogdy byl večer, sam tam byl.
24 A lod už v posrěd morja suči, metana byla od val; ibo byl větr protivny.
25 No o četvrtoj straži nočnoj šel do njih Jezus, hodeči po morju.
26 A ugleděvši go učeniki po morju hodečego, prěstrašili se, govoreči: Liceměrje to jest! i od straha vozkliknuli.
27 No směsta rěkl do njih Jezus, govoreči: dověrjenja! Ja jesm; ne bojite se.
28 A odgovarjajuči jemu Petr rěkl: Gospodine! Jestli jesi ty, kaži mně prijdti do tebe po vodě.
29 A on rěkl: Pojdi! A Petr, postupivši iz lodi, šel po vodě, aby prišel do Jezusa;
30 No videči silny větr, prěstrašil se; a kogdy začel tonuti, vozkliknul, govoreči: Gospodine, spasi mene!
31 A Jezus momentalno iztrgnuvši ruku, vzel go za ruku i rěkl jemu: O malověrny! Začto jesi sumněval se?
32 A kogdy oni vstupili v lod, utišil se větr.
33 A ti, ktori byli v lodi, pristupivši poklonili se jemu, govoreči: Pravdivo jesi Synom Božjim.
34 I prěpravivši se, prišli do zemji Genezaret.
35 A poznavši go muži togo grada, poslali po cěloj toj okolnoj krajině; i prineseno do njego vsih, ktori se zlo iměli.
36 I prosili go, aby jedino dol oděži jego dotykali; a ktokoli go dotknul, ozdravjeny byl.

## Razděl 15

1 Itak pristupili do Jezusa iz Jeruzalema naučeni v Pismu i Farizeji, govoreči:
2 Čemu učeniki tvoji prěstupajut zakon starših? ibo ne umyvajut ruk svojih, kogdy imajut jesti hlěb.
3 A on odgovarjajuči, rěkl jim: Čemu i vy prěstupajte zapověd Božju za zakony vaše?
4 Ibo Bog prikazal, govoreči: Čti otca tvojego i mati; i kto by klel na otca ili mati, nehaj umre.
5 No vy govorite: Kto by rěkl otcu ili materi: Dar, ktory ja žrtvoju, tobě koristny bude; A jestli toj ne čtilby otca svojego ili materi svojej, bez dolga bude.
6 I jeste tak izbavili se zapovědi Božjej za zakony vaše.
7 Liceměri! dobro o vas govoril Izaija, govoreči:
8 Ljud toj približaje se do mene ustami svojimi, i ustami čti mene; no srdce jih daleko jest od mene.
9 No prazdno mene čtet, učeči zakonov, ktore sut zapovědi ljudske.
10 A pozvavši do sebe ljud, rěkl jim: Slyšite, a razumějte.
11 Ne to, čto vhodi v usta, čini člověka nečistym; no čto izhodi iz ust, to čini člověka nečistym.
12 Itak pristupivši učeniki jego, rěkli jemu: Znaš, že Farizeji, uslyšavši toj govor, gněvali se?
13 A on odgovarjajuči rěkl: Vsaky sad, ktorogo ne nasadil Otec moj nebesky, izkorenjeny bude.
14 Ostavite jih; To sut slěpi načelniki slěpyh, a slěpy jestli by slěpogo vodil, oba v dol padut.
15 A odgovarjajuči Petr, rěkl jemu: Objasni nam tu parabolu.
16 I rěkl Jezus: To i vy ješče bezumni jeste?
17 Ješče ne razumějete, že vse, čto vhodi v usta, v brjuho ide, i do izhoda byvaje izkydnuto?
18 No čto iz ust izhodi, iz srdca izhodi, a to čini člověka nečistym.
19 Ibo iz srdca izhodet zle myslji, ubijstva, prěljubstva, bludy, kradeži, falšive svědočstva, bogohuljenja
20 To jest, čto čini člověka nečistym: no jesti nečistymi rukami, to ne čini člověka nečistym.
21 A izševši Jezus odtud, odstupil v strany Tira i Sidona.
22 A vot žena Hananejska iz tyh granic izševši, zvala, govoreči do njego: Pomiluj se nad mnoju Gospodine, syne Davida! dočerka moja težko byvaje od djavla mučena.
23 A on jej ne odgovoril ni slovom. Itak pristupivši učeniki jego, prosili go, govoreči: Odsylaj ju, ibo zove za nami.
24 A on odgovarjajuči rěkl: Ne jesm poslany, jedino do ovc, ktore pogynuli iz doma Izraelskogo.
25 No ona pristupivši, poklonila se jemu, govoreči: Gospodine, spasi mene!
26 A on odgovarjajuči rěkl: Nezlo jest brati hlěb dětam, a metati psam.
27 A ona rěkla: Tak jest, Gospodine! a ibo male psi jedut krohy, ktore padut iz stola gospodinov jih.
28 Itak odgovarjajuči Jezus rěkl jej: O ženo! velika jest věra tvoja; nehaj tobě se stane, kako hčeš. I ozdravjana jest dočerka jej od toj že časiny.
29 A Jezus poševši odtud, prišel nad morje Galilejsko, a vstupivši na goru, sěděl tam.
30 I prišel do njego veliky ljud, imajuči s soboju hromyh, slěpyh, němyh i inyh mnogo, i kladli jih u nog Jezusa, i ozdravjal jih,
31 Tak že se ljud divoval, videči, že němi govoret, hvori ozdravjeni sut, hromi hodet, a slěpi videt; i slavili Bogu Izraelskomu.
32 No Jezus pozvavši učenikov svojih, rěkl: Žalj mně togo ljuda; ibo už tri dni pri mene ostavajut, a ne imajut, čto by jeli, a ne hču jih izsylati gladnyh, by očevidno ne oslabili na stežkě.
33 Itak jemu rěkli učeniki jego: Odkud bysmo vzeli tak mnogo hlěba na toj pustynji, abysmo tak veliky ljud nasytili?
34 I rěkl jim Jezus: Koliko imate hlěbov? A oni rěkli: Sedm, i malo ryb.
35 Itak kazal ljudu, aby sědli na zemji.
36 A vzevši sedm hlěbov i te ryby, učinivši hvalu, lomil i dal učenikam svojim, a učeniki ljudu.
37 I jeli vsi i syti byli, i sobrali, čto ostalo od jela, sedm polnyh košev.
38 A bylo tyh, ktori jeli, četyri tyseči mužev bez čisljenja žen i dětij.
39 Itak izsylavši ljud, vstupil v lod, i prišel na granice Magdalenske.

## Razděl 16

1 A pristupivši Farizeji i Saduceji, pokušajuči prosili go, aby jim znak iz neba ukazal.
2 A on odgovarjajuči, rěkl jim: Kogdy byvaje večer, govorite: Pogoda bude; ibo se nebo črveni.
3 A rano: Tutdenj bude burja; ibo se nebo mutno črveni. Liceměri! obraz neba razsuditi znate, a znakov tyh časov ne možete.
4 Rod zly, ktory děla prěljubstva, znaka išče; no jemu znak ne bude dano, jedino  znak Jonasa proroka. I opustivši jih, odšel.
5 A kogdy se prěpravili učeniki jego na drugu stranju morja, vozpametali vzeti hlěby.
6 I rěkl jim Jezus: Budte ostražni i shranite se kvasa Farizejev i Saducejev.
7 A oni razgovarjali medžu soboju, govoreči: Ne jesmo vzeli hlěba.
8 To ugleděvši Jezus, rěkl jim: O čim razgovarjate medžu soboju, o malověrni, jeste hlěba ne vzeli?
9 či ne razumějete, ni pametate o tyh peti hlěbov za tyh peti tyseči ljudij i koliko jeste košev sobrali?
10 Ni tyh sedmi hlěbov za četyri tyseči ljudij i koliko jeste košev sobrali?
11 Kako ne razumějete, jesm vam ne o hlěbu pověděl, govoreči: Abyste se shranjali kvasa Farizejev i Saducejev?
12 Itak razuměli, že ne govoril, aby se shranjali kvasa hlěba, no učenja Farizejev i Saducejev.
13 A kogdy prišel Jezus v stranu Cezariji Filipovoj, pytal učenikov svojih, govoreči: Za kogo imajut ljudi Syna člověčskogo?
14 A oni rěkli: Jedni za Joana Krestitelja, a drugi za Iliju, ini tož za Jeremiju, ili jednym iz prorokov.
15 I rěkl jim: A vy za kogo mene imate?
16 A odgovarjajuči Simon Petr rěkl: Ty jesi Hristos, Syn Boga živogo.
17 Itak Jezus odgovarjajuči rěkl jemu: Blagoslavjany jesi Simone, syne Jonasa! ibo togo tělo i krov ne objavili tobě, no Otec moj, ktory jest v nebesah.
18 A Ja tobě tož govorju, jesi Petr; a na tom kamenju postavju moju crkov, a vrata peklne ne pobědet go:
19 I tobě dam ključe kraljevstva nebeskogo; a čtokoli svežeš na zemji, bude svezano i v nebesah; a čtokoli razvežeš na zemji, bude razvezano i v nebesah.
20 Itak prikazal učenikam svojim, aby nikomu ne govorili, že on jest Jezus Hristos.
21 I odtud začel Jezus pokazyvati učenikam svojim, že imaje odidti do Jeruzalema, i mnogo trpěti od starših i od vysših duhovnikov i naučenyh v Pismu. I bude ubity i tretjego dnja vozkresne.
22 A vzevši go Petr na stranju, začel go koriti, govoreči: Pomiluj se sam nad soboju, Gospodine! ne prijde to na tebe.
23 A on obrativši se, rěkl Petru: Idi od mene, satane! jesi mně prěškoda; ibo ne razuměješ togo, čto jest Božjego, no čto jest ljudskogo.
24 Itak rěkl Jezus do učenikov svojih: Jestli kto hče idti za mnoju, nehaj  se samogo sebe odkaže, a prijme križ svoj, i slěduje mene!
25 Ibo kto by htěl dušu svoju hraniti, izgubi ju; a kto by izgubil dušu svoju za mene, nahodi ju.
26 Ibo čto pomože člověku, hot by ves svět dobyl, a na duši svojej poškodženje imal? čto v zaměn da člověk za dušu svoju?
27 Ibo Syn člověčsky prijde v slavě Otca svojego so svojimi Angelami, a itak odda vsakomu za jih děla.
28 Zapravdu govorju vam: Sut něktori iz tyh, ktori tu stojet, ktori ne izkuset smrti, až ugleděli Syna člověčskogo, idučego v svojem kraljevstvu.

## Razděl 17

1 A po šesti dnjah vzel Jezus Petra i Jakoba i Joana, brata jego, i vvedl jih na vysoku goru oddělno.
2 I prěobražany byl prěd njimi, a prosvětilo se obličje jego kako solnce, a oděž jego stala se běla kako světlo.
3 A vot pokazali se jim Mojzes i Ilija, ktori s njim govorili.
4 I Petr rěkl do Jezusa: Gospodine! dobro nam tu byti; jestli hčeš, učinimo tu tri šatory, tobě jedin, i Mojzesu jedin, i Iliji jedin.
5 A kogdy on ješče govoril, vot oblak jasny otěnil jih; a glas iz oblaka govoril: Toj jest Syn moj mily, v ktorom imaju simpatiju, togo slyšite.
6 To uslyšavši učeniki, padli na lice svoje i bojali se mnogo.
7 Itak pristupivši Jezus dotknul jih i rěkl: Vstanite, a ne bojite se.
8 A oni voznesli oči svoje, nikogo ne viděli, jedino Jezusa samogo.
9 A kogdy spuščali se iz gory, prikazal jim Jezus, govoreči: Nikomu ne govorite o tom viděnju, až Syn člověčsky vozkresne.
10 I pytali go učeniki jego, govoreči: Čto itak naučeni v Pismu govoret, že ima Ilija najprvo prijdti?
11 A Jezus odgovarjajuči, rěkl jim: Ilija najprvo prijde i popravi vse;
12 No vam govorju: Že Ilija už prišel, ibo ne poznali go, no učinili jemu, čtokoli htěli; tak i Syn člověčsky ima utrpěti od njih.
13 Itak razuměli učeniki, že o Joanu Krestitelju govoril do njih.
14 A kogdy prišli do ljuda, pristupil do njego člověk, i upadl prěd njim na kolěna,
15 I rěkl: Gospodine! Pomiluj se nad synom mojim: ibo epileptykom jest, i težko se muči; često ibo padaje v ogonj, i često v vodu.
16 I jesm privedl go do učenikov tvojih, no go ne mogli ozdraviti.
17 A odgovarjajuči Jezus, rěkl: O rode nevěrny i prěvratny! Kako dolgo imam byti s vami? Kako dolgo imaju vas trpěti? privedite mně go.
18 I sgromil togo djavla Jezus; i izšel od njego, i ozdravjany jest junak od toj že časiny.
19 Itak pristupivši učeniki do Jezusa oddělno, rěkli jemu: čemu že jesmo go izgnati ne mogli?
20 No Jezus rěkl do njih: Za nevěrje vaše; zapravdu ibo govorju vam: Jestli byste imali věru kako zrno gorčice, byste rěkli toj gorě: Prěnesi se odtud na to město, itak se prěnese, a ničto nemožnogo vam ne bude.
21 No toj rod běsov možno izgnati jedino molitvoju i postom.
22 A kogdy prěbyvali v Galileji, rěkl do njih Jezus: Syn člověčsky bude prědany v ruky ljudske;
23 I ubijut go, no tretjego dnja vozkresne. I smutili se mnogo.
24 A kogdy prišli do Kafarnaum, pristupili ti do Petra, ktori dvudrahmy izbirali, i rěkli: Či učitelj vaš ne da danji dvudrahmy?
25 I rěkl: Tak. A kogdy vhodil v dom, prěduprědil go Jezus, govoreči: Čto ty mysliš, Simone? Kralji zemni od kogo berut myto ili danje? od synov svojih, itak od čudžih?
26 Rěkl jemu Petr: Od čudžih. I rěkl jemu Jezus: Zatom syni sut svobodni.
27 Ibo abysmo jih ne dali povoda do gněva, ševši do morja, kydni vudicu, a tu rybu, ktora kako prva ugryze, vozmi, a otvorivši usta jej, najdeš stater. Toj vzevši, daj jim za mene i za sebe.

## Razděl 18

1 V toj časině pristupili učeniki do Jezusa, govoreči: Kto najvysši jest v kraljevstvu nebeskom?
2 A pozvavši Jezus děti, postavil je v posrěd jih,
3 I rěkl: Zapravdu govorju vam: Jestli se ne obratite i ne stanete se kako děti, nikogdy do kraljevstva nebeskogo ne vojdete.
4 Kto se itak ponizi kako to děte, toj jest najvysšim v kraljevstvu nebeskom.
5 A kto by prijel jedno děte tako v mojem imenu, mene prijme.
6 Kto by jednako stal se povodom grěha jedinogo iz tyh malyh, ktori v mene věret, lěpje by jemu bylo, aby věšeny byl kamenj mlynsky na šiji jego, a utopjeny byl v glubině morskoj.
7 Běda světu za pogoršenja! ibo pogoršenja sut dolžni prijdti; ibo běda člověku tomu, črěz ktorogo prihodet pogoršenja!
8 Zatom jestli ruka tvoja ili noga tvoja gorši tebe, odrěži ju i kydni od sebe; lěpje jest tobě vstupiti do života hromym ili ulomnym, než dvě ruky ili dvě nogy imajuči, kydnutym byti do ognja věčnogo.
9 A jestli tebe oko tvoje gorši, vozmi je i kydni od sebe; lěpje jest tobě jednym okom vstupiti do života, než oba očami imajuči, byti kydnutym do ognja peklnogo.
10 Budte ostražni, abyste ne grdili nikakym iz tyh malyh; ibo vam govorju, že Angeli jih v nebesah vsakčas gledajut na obličje mojego Otca, ktory jest v nebesah.
11 Prišel ibo Syn člověčsky, aby spasl to, čto pogynulo.
12 Čto vy myslite? Kakby něktory člověk iměl sto ovc, a zabludila by se jedna iz njih, či ne ostavja tyh devetdeseti i deveti na gorah, a poševši iz gory, ne išče toj, ktora zabludila?
13 A jestli jemu se stane, že ju najde, zapravdu govorju vam, že se iz njej vyše raduje, než iz tyh devetdeseti i deveti ne, ktore ne zabludili.
14 Tak ne jest volja Otca vašego, ktory jest v nebesah, aby pogynul jedin iz tyh malyh.
15 A jestli by sgrěšil protiv tobě brat tvoj, idi, karaj go medžu toboju i njim: jestli tebe posluša, jesi dobyl brata tvojego.
16 No jestli tebe ne posluša, prijmi do sebe ješče jedinogo ili dvoh, aby dva ili tri svědki stanulo na vsakom slovu děla.
17 A jestli by jih ne poslušal, kaži crkvi; a jestli by crkov ne poslušala, nehaj tobě bude kako poganin i mytnik.
18 Zapravdu govorju vam: Čtokoli byste svezali na zemji, bude svezano i na nebu; a čto byste razvezali na zemji; bude razvezano i na nebu.
19 I govorju vam: Že kakby iz vas dva prosili na zemji o vsaku věč, stane se jim od Otca mojego, ktory jest v nebesah.
20 Ibo kde sut dva ili tri sobrani v imenu mojem, tam jesm v posrěd njih.
21 Itak pristupivši do njego Petr, rěkl: Gospodine! kolikrat imaju, kak sgrěši protiv mene moj brat, jemu odpustiti? či až do sedmkrat?
22 I rěkl jemu Jezus: Ne govorju tobě až do sedmkrat, no až do sedmdeset sedmikrat.
23 Zato podobno jest kraljevstvo nebesko kralju, ktory se htěl sčitati s slugami svojimi.
24 A kogdy se začel sčitati, postavjeno jemu jedinogo, ktory byl vinny deset tyseči talentov.
25 A kogdy ne iměl odkud jemu oddati, kazal go gospodin prodati, i ženu jego, i děti, i vse, čto iměl, i dolg prědati.
26 Padši itak sluga, poklonil se jemu, govoreči: Gospodine! iměj trpělivost nad mnoju, a vse tobě oddam.
27 A pomilovavši se gospodin togo slugi, izbavil go, i dolg jemu odpustil.
28 A izševši sluga, našel jedinogo iz gospodina drugyh slugov, ktory jemu byl vinny sto grošev; a shvativši go, dušil go, govoreči: Oddaj mně, čto ty vinny.
29 Pripadši itak sluga do nog jego, prosil go, govoreči: Iměj trpělivost nad mnoju, a oddam tobě vse.
30 No on ne htěl, no poševši kydnul go do vezenja, až odda, čto byl vinny.
31 Ugleděvši itak ini slugi gospodina, čto se stalo, smutili se mnogo, a poševši objavili gospodinu svojemu vse, čto se stalo.
32 Itak pozvavši go gospodin jego, rěkl jemu: Slugo zly! ves dolg jesm odpustil tobě, jesi mene prosil.
33 či jesi i ty ne iměl pomilovati se nad drugym slugoju tvojego gospodina, kako jesm se i ja pomiloval nad toboju?
34 A razgněvavši se gospodin jego, podal go mučiteljam, až oddal to vse, čto jemu byl vinny.
35 Tak i Otec moj nebesky učini vam, jestli ne vsaky iz vas odpusti bratu svojemu iz svojego srdca.

## Razděl 19

1 I stalo se, kogdy dokončil Jezus te govory, že odšel iz Galileji, a prišel v granice Judejske za Jordanom.
2 I šel za njim veliky ljud, i ozdravjal jih tam.
3 Itak prišli do njego Farizeji, pokušajuči go i govoreči jemu: Godi li se člověku ostaviti ženu svoju za vsaky povod?
4 A on odgovarjajuči rěkl jim: Ne jeste čitali, že toj, ktory stvoril na početku člověka, kako muža i ženu učinil jih?
5 I rěkl: Zato ostavi člověk otca i mati, a objedinja se so svojeju ženoju, i budut dvoje jednom tělom.
6 A tak už ne sut dvoje, no jedno tělo; čto itak Bog objedinil, člověk nehaj ne razlučaje.
7 Rěkli jemu: Začto-že itak Mojzes kazal dati list razvodny i ostaviti ju?
8 Rěkl jim: Mojzes za tvrdost srdca vašego dopustil vam, ostaviti ženy vaše, no od početka ne bylo tak.
9 No ja govorju vam: Že ktokoli opustil ženu svoju, (ako ne iz povoda prěljubstva), a inu by vzel, čini prěljubstvo; a kto by razvodnu vzel, čini prěljubstvo.
10 Rěkli jemu učeniki jego: Jestli tako jest dělo muža so ženoju, ne jest dobro se ženiti.
11 A on jim rěkl: Ne vsi razumějut toj věči, no jedino ti, ktorym to dano.
12 Ibo sut evnuhi, ktori se tak iz života materi rodili; sut tož evnuhi, ktori črěz ljudij stali se evnuhami; sut tož evnuhi, ktori se sami oskopili za kraljevstvo nebesko. Kto može pojeti, nehaj razuměje!
13 Itak jemu prinošeno děti, aby na ne ruky vkladal i molil se; no učeniki zabranjali jim togo.
14 No Jezus rěkl: Ostavite dětij, a ne zabranjajte jim prihoditi do mene; ibo takym jest kraljevstvo nebesko.
15 A vloživši na nje ruky, pošel odtud.
16 A vot jedin pristupivši, rěkl jemu: Učitelju dobry! čto dobrogo imam činiti, abyh iměl život věčny?
17 No jemu on rěkl: Začto mene zoveš dobrym? nikto ne jest dobry, jedino jedin, to jest Bog; a jestli hčeš vstupiti do života, shranjaj zapovědi.
18 I rěkl jemu: Ktore? A Jezus rěkl: Ne budeš ubivati, ne budeš prěljubstva dělati, ne budeš krasti, ne budeš govoriti falšivogo svědočstva;
19 Čti otca tvojego i mati, i ljubi bližnjego svojego, kako sebe samogo.
20 Rěkl jemu junak: To jesm vse shranjal od mladosti svojej; čego mně ješče nedostava?
21 Rěkl jemu Jezus: Jestli hčeš byti sovršenym, idi, prodaj iměnja tvoje, i razdaj ubogym, a budeš iměl skarb v nebu, a prijdi i slěduj mene.
22 A kogdy junak tyh slov uslyšal, odšel smutny; ibo mnogo iměl iměnja.
23 Itak Jezus rěkl učenikam svojim: Zapravdu govorju vam, že s trudnostju bogaty vojde do kraljevstva nebeskogo.
24 I govorju vam: Že prostějše velbludu črěz uho igly prějdti, než bogatomu vstupiti do kraljevstva Božjego.
25 Togo uslyšavši učeniki jego, udivili se mnogo, govoreči: Kto itak može byti spaseny?
26 A Jezus pogledavši na ne, rěkl jim: U ljudi togo ne možno; no u Boga vse jest možno.
27 Itak odgovarjajuči Petr, rěkl jemu: Vot jesmo opustili vse, i jesmo pošli za toboju; čto nam itak za to bude?
28 A Jezus rěkl jim: Zapravdu govorju vam: Že pri, ktori jeste mene slědovali, v vozrodženju, kogdy usěde Syn člověčsky na tronu slavy svojej, usědete i vy na dvanadset tronah, sudeči dvanadset rodov Izraelskyh.
29 A vsaky, ktory by opustil dom, ili bratov, ili sestry, ili otca, ili mati, ili ženu, ili děti, ili polje, za ime moje, stokratno veče prijme, i život věčny naslědi.
30 A mnogo prvyh bude poslědnjimi, a poslědnjih prvymi.

## Razděl 20

1 Ibo podobno jest kraljevstvo nebesko gospodaru, ktory izšel mnogo rano najmati rabotnikov do vinogradnika svojego.
2 A dogovorivši se s rabotnikami o grošu na denj poslal jih do svojego vinogradnika.
3 A izševši o tretjej časině, ugleděl drugyh, ktori stali na trgu bez raboty;
4 I rěkl jim: Idite i vy do vinogradnika, a čto bude spravědlivo, dam vam.
5 A oni pošli. Snova izševši o šestoj i devetoj časině, takože učinil.
6 Potom o jedinnadsetoj časině izševši, našel drugyh, ktori stali bez raboty, i rěkl jim: Začto tu stojite cěly denj bez raboty?
7 Rěkli jemu: Nas nikto ne najel; i rěkl jim: Idite i vy do vinogradnika, a čto bude spravědlivo, prijmete.
8 A kogdy byl večer, rěkl gospodar vinogradnika upravitelju svojemu: Pozovi rabotnikov, a daj jim zaplatu, začevši od poslědnjih až do prvyh.
9 A kogdy prišli oni, ktori o jedinnadsetoj časině byli najeti, dal vsakomu iz njih denara.
10 Priševši tož i prvi, myslili, že veče prijmut; no dostali i oni po jednom denaru.
11 A vzevši go, roptali protiv gospodaru,
12 Govoreči: Ti poslědnji jednu časinu rabotali, a jesi učinil jih nam ravnymi, ktori jesmo trpěli oteženje dnja i žar.
13 A on odgovarjajuči rěkl jednomu iz njih: Prijatelju! ne činju tobě krivdy; či  jesi se ne o jednom denaru dogovoril so mnoju?
14 Prijmi, čto tvoje jest, a idi; hču ibo tomu poslědnjemu dati kako i tobě.
15 či mně se ne godi činiti s mojim, čto hču? Itak oko tvoje žalostno jest, že jesm dobry?
16 Tako budut poslědnji prvymi, a prvi poslědnjimi; ibo mnogo jest zvanyh, no malo izbranyh.
17 A kogdy Jezus vstupil do Jeruzalema, vzel so soboju dvanadset učenikov osobno i na stežkě rěkl jim:
18 Vot vstupajemo do Jeruzalema, Syn člověčsky bude prědany vysšim duhovnikam i naučenym v Pismu, i sudet go na smrt.
19 I prědadut go poganam na izsmějanje i na bičevanje i na razpinanje; no tretjego dnja vozkresne.
20 Itak pristupila do njego mati synov Zebedeja so svojimi synami, klanjajuči se jemu, i prosili něčto od njego.
21 A on jej rěkl; Čego že hčeš? Rěkla jemu: Kaži, aby sěděli ti dva syni moji, jedin po pravoj tvojej a drugy po lěvici v kraljevstvu tvojem.
22 No Jezus odgovarjajuči rěkl: Ne znate, o čto prosite; možete že piti čašu, ktoru ja budu pil? Rěkli jemu: Možemo.
23 Itak jim rěkl: Čašu moju piti budete; no sěděti po pravoj mojej i po lěvici mojej, ne jest moja věč dati vam, no tym, ktorym jest pripravjeno od Otca mojego.
24 A uslyšavši togo deset, razgněvali se na tyh dvoh bratov.
25 No Jezus pozvavši jih, rěkl: Znate, že knezi narodov vladajut nad njimi, a ktori veliky sut, moči dokazyvajut nad njimi.
26 No ne tak bude medžu vami: no ktokoli medžu vami htěl byti velikym, nehaj bude slugoju vašim.
27 A ktokoli medžu vami by htěl byti prvym, nehaj bude slugoju vašim.
28 Kako i Syn člověčsky ne prišel, aby jemu služeno, no aby služil i dal dušu svoju na izkup za mnogo.
29 A kogdy oni izhodili iz Jeriha, šel za njim veliky ljud.
30 A vot dva slěpi, sědeči pri stežkě, uslyšavši, že Jezus prěhodi, pozovali, govoreči: Pomiluj se nad nami, Gospodine, syne Davida!
31 No ljud sgromil jih, aby molčali; no oni tym veče zvali, govoreči: Pomiluj se nad nami, Gospodine, syne Davida!
32 A stanul Jezus, pozval jih i rěkl: Čto hčete, abyh vam učinil?
33 Rěkli jemu: Gospodine! aby byli otvorjene naše oči.
34 A Jezus iměl simpatiju s njimi, dotknul oči jih, a momentalno viděli oči jih; i šli za njim.

## Razděl 21

1 A kogdy se približili do Jeruzalema i prišli do Betfage, do gory olivnoj,  Jezus poslal dvoh učenikov,
2 Govoreči jim: Idite do gradka, ktory jest naprotiv vam, a momentalno nahodite oslicu svezanu i malogo osla s njeju; odvezite je, a privedite do mene.
3 A jestli by vam něčto kto rěkl, govorite, že Gospodin jih potrěbuje; a v tom samom vrěmenu odpusti je.
4 A to se vse stalo, aby se izpolnilo, čto pověděno črěz proroka:
5 Govorite dočerkě Sionskoj: Vot kralj tvoj ide do tebe lagodno, a sědeči na oslici, i na malom oslu, synu oslice.
6 Poševši itak učeniki, a učinivši tak, kako jim prědskazal Jezus,
7 Privedli oslicu i malogo osla, i vložili na nje svoju oděž, i vložili go na nje.
8 A veliky ljud kladl oděži svoje na stežkě, a drugi rězali větvy iz drěv, i kladli na stežkě.
9 A ljud prěd njim i za njim iduči zval, govoreči: Hosanna synu Davida! blagoslavjany, ktory ide v imenu Gospodinskom, Hosanna na vysotah!
10 A kogdy on vjehal do Jeruzalema, pomrdal se ves grad, govoreči: Kto toj jest?
11 A ljud govoril: Toj jest Jezus, prorok iz Nazareta Galilejskogo.
12 Itak všel Jezus do crkvi Božjego, i izgnal vsih prodavcev i kupujučih v crkvi. A stoly tyh, ktori denarami trgovali, i stoly prodavcev golubov provrgnul,
13 I rěkl jim: Napisano jest: Dom moj domom molitvy nazvany bude; no jeste vy učinili iz njego jamu razbojnikov.
14 Itak pristupili do njego slěpi i hromi v crkvi, i ozdravil jih.
15 A ugleděvši vysši duhovniki i naučeni v Pismu čudesa, ktore činil, i děti, ktore v crkvi govorili: Hosanna Synu Davida: razgněvali se.
16 I rěkli jemu: Slyšiš, čto tobě govoret? A Jezus jim rěkl: Tako jest. Nikogdy že jeste ne čitali, že iz ust dětij i dětetok jesi dělal hvalu?
17 A opustivši jih, izšel iz grada do Betanije, i tam ostal;
18 A rano vračajuči se do grada, byl gladny.
19 I ugleděvši jedno figovo drěvo pri stežkě, prišel do njego, i ne našel ničto na njem. Jedino same listy, i rěkl jemu: Nehaj se veče iz tebe plod ne rodi na věky. I usohnulo v tom samom vrěmenu figovo drěvo.
20 A ugleděvši to učeniki, divili se, govoreči: Kako bystro usohnulo to figovo drěvo!
21 Itak odgovarjajuči Jezus, rěkl jim: Zapravdu govorju vam: Jestli byste iměli věru, a byste se ne sumněvali, ne jedino to, čto se stalo s figovym drěvom, byste učinili. No kakbyste toj gorě rěkli: Vozdvigni se, a kydni se v morje, stane se tako.
22 I vse, o čto byste prosili v molitvě s věroju, prijmete.
23 A kogdy prišel do crkvi, pristupili do njego, kogdy učil, vysši duhovniki i starši ljuda, govoreči: Kakoju močju to činiš? a kto tobě dal tu moč?
24 A odgovarjajuči Jezus, rěkl jim: Pytaju i ja vas o jednu věč. Jestli mně odgovorite, ja vam pověm, kakoju močju to činju.
25 Krest Joana odkud byl? iz neba či od ljudij? A oni myslili sami v sobě, govoreči: Jestli pověmo iz neba, rěče nam: Čemu jeste jemu itak ne uvěrili?
26 Jestli jednako pověmo iz ljudij, bojimo se ljuda; ibo Joana vsi imajut za proroka.
27 A odgovarjajuči Jezusu rěkli: Ne znamo. Rěkl jim on: I ja vam ne pověm, kakoju močju to činju.
28 No čto myslite? Člověk něktory iměl dvoh synov; a pristupivši do prvogo, rěkl: Syne! idi, rabotaj tutdenj na mojem vinogradniku.
29 No on odgovarjajuči rěkl: Ne hču. A potom žalil se i pošel.
30 A pristupivši do drugogo, rěkl takože; a on odgovarjajuči rěkl: Ja idu, gospodine! no ne pošel.
31 Ktory iz tyh dvoh učinil volju otca? Rěkli jemu: Prvy. Rěkl jim Jezus: Zapravdu govorju vam, že mytniki i kurvy prěd vami vhodet do kraljevstva Božjego.
32 Ibo prišel do vas Joan stežkoju spravědlivosti, a jeste ne uvěrili jemu, no mytniki i kurvy uvěrili jemu: a vy videči to, a až do konca ne jeste pomyslili, abyste jemu uvěrili.
33 Drugoj paraboly uslyšite: Člověk něktory byl gospodarom, ktory nasadil vinogradnik, i stěnoju go ogradil, i nakopal v njem presu vina, i postavil věžu, i iznajel ju vinaram, i odšel von.
34 A kogdy se približil čas prijmanja plodov, poslal slugov svojih do tyh vinarov, aby odbrali plodov jih.
35 No vinari shvatili slugov jego, jedinogo bili, a drugogo ubili, a drugogo kamenovali.
36 Snova poslal inyh slugov, veče než prvyh; i takože jim tak učinili.
37 No na ostatok poslal syna svojego, govoreči: Budut se styditi syna mojego.
38 No vinari, ugleděvši togo syna, rěkli medžu soboju: Toj jest naslědnik; pojdimo, ubijmo go, a prijmemo naslědstvo jego.
39 Itak shvativši go, izkydali go von iz vinogradnika i ubili.
40 Kogdy itak gospodin vinogradnika prijde, čto učini tym vinaram?
41 Rěkli jemu: Zlyh ubije, a vinogradnik iznajme inym vinaram, ktori jemu prědavati budut plody časov svojih.
42 Rěkl jim Jezus: Jeste ne čitali nikogdy v Pismah: Kamenj, ktory odkydnuli postavjajuči, se stal glavoju vugolja: od Gospodina se to stalo, i čud jest v očah naših?
43 Zatom govorju vam: Od vas odjeto bude kraljevstvo Božje, i bude dano narodu, ktory izda jego plody.
44 A kto by padl na toj kamenj, razbije se, a na kogo on by upadl, sgnete go.
45 A uslyšavši vysši duhovniki i Farizeji paraboly jego, domyslili se, že o njih govoril;
46 A hčuči go shvatiti, bojali se ljuda, zato,že go iměli za proroka.

## Razděl 22

1 A odgovarjajuči Jezus, snova jim rěkl v parabolah, govoreči:
2 Podobno jest kraljevstvo nebesko kralju, ktory sdělal svatbu synu svojemu;
3 I poslal slugi svoje, aby pozvali zvanyh na svatbu; no ne htěli prijdti.
4 Snova poslal ine slugi, govoreči: Kažite zvanym: Vot jesm moj oběd prigotovil, voly i čto bylo tolstyh zvěrev, jest ubito i vse gotovo. Pojdite na svatbu.
5 No oni ne htěli i odšli. Jedin do polja svojego, a drugy do trga svojego;
6 A drugi shvatili slugov jego, ponizili i ubili jih.
7 Kogdy kralj togo uslyšal, razgněval se, a poslavši vojska svoje, ubil tyh ubijcev, i grad jih goril.
8 Itak rěkl slugam svojim: Svatba zapravdu jest gotova; no zvani ne byli dostojni.
9 Zatom idite na konce stežek i kogokoli nahodite, pozovite na svatbu.
10 Itak izševši slugi na stežky, sobrali vsih, ktoryh našli, zlyh i dobryh, i napolnjena jest svatba gostami.
11 A vševši kralj, aby ogledal gosti, viděl tam člověka ne odětogo v oděži svatbenoj;
12 I rěkl jemu: Prijatelju! Kako jesti tu všel, ne imajuči oděži svatbenoj? A on molčal.
13 Itak rěkl kralj slugam: Svezavši nogy i ruky jego, vozmite go, a kydnite do temnosti vně. Tam bude plač i skripěnje zubov.
14 Ibo mnogo jest zvanyh, no malo izbranyh.
15 Togdy odševši Farizeji učinili radu, kako by go shvatili v besědě.
16 I poslali do njego učenikov svojih s Herodijanami, govoreči: Učitelju! znamo, jesi istinny, i stežek Božjih v pravdě učiš, a ne dbaš o nikom; ibo ne gledaš na lice ljudske.
17 Zatom pověd nam, čto mysliš? Godi li se dati platbu cěsaru, či ne?
18 No Jezus poznavši zlost jih, rěkl jim: Čemu mene pokušate, liceměri?
19 Pokažite mně monetu platby; a oni jemu podali groš.
20 I rěkl jim: Čij že to obraz i napis?
21 Rěkli jemu: Cěsara. Itak jim rěkl: Oddavajte že itak, čto jest cěsara, cěsaru, a čto jest Božjego, Bogu.
22 To uslyšavši, udivili se, a opustivši go, odšli.
23 Dnja togo prišli do njego Saduceji, ktori govoret, že ne ima vozkrešenja, i pytali go,
24 Govoreči: Učitelju! Mojzes pověděl: Jestli by kto umrl, ne imajuči děti, aby brat jego vzel ženu jego, i vozbudil sěme bratu svojemu.
25 Bylo itak u nas sedm bratov; a prvy vzevši ženu, umrl, a ne imajuči sěmena, ostavil ženu svoju bratu svojemu.
26 Takože tož vtory i tretji, až do sedmogo.
27 A na koncu umrla i žena.
28 Zatom pri vozkrešenju, ktorogo iz tyh sedmi bude ženoju, ibo ju vsi iměli?
29 A odgovarjajuči Jezus rěkl jim: Bludite, ne znajuči Pisma, ni moči Božjej.
30 Ibo pri vozkrešenju ni se ženiti, ni za muž hoditi ne budut, no budut kako Angeli Božji v nebu.
31 A o vstanju mrtvyh jeste ne čitali, čto vam pověděno od Boga:
32 Jesm Bog Abrahama, i Bog Izaaka, i Bog Jakoba? Bog ne jest Bogom mrtvh, no živyh.
33 A uslyšavši togo ljud, udivil se nad naukoju jego.
34 No kogdy uslyšali Farizeji, že zaključil usta Saducejam, sobrali se zajedno.
35 I pytal go jedin iz njih, učeny v Pravu, pokušajuči go:
36 Učitelju! ktora jest najvysša zapověd v zakonu?
37 A Jezus jemu rěkl: Budeš miloval Gospodina, Boga tvojego, iz vsego srdca tvojego, i iz cěloj duši tvojej i iz cěloj myslji tvojej.
38 To jest prva i najvysša zapověd.
39 A vtora podobna jest tomu: Budeš miloval bližnjego tvojego, kako samogo sebe.
40 Na tyh dvoh zapovědah ves zakon i proroki opirali se.
41 A kogdy se Farizeji sobrali, pytal jih Jezus,
42 Govoreči: Čto myslite o Hristosu? Kogo jest synom? Rěkli jemu: Davida.
43 I rěkl jim: Kako itak David v duhu zove go Gospodinom? govoreči:
44 Rěkl Gospodin Gospodinu mojemu: Sědi po pravoj mojej, až položu neprijateljev tvojih pod nogy tvoje.
45 Zato že go itak David zove Gospodinom, kako jest synom jego?
46 A nijedin jemu ne mogl odgovoriti jednogo slova, i nikto ne byl hrabry go  veče od togo dnja pytati.

## Razděl 23

1 Itak Jezus rěkl do ljuda i do učenikov svojih, govoreči:
2 Na tronu Mojzesa usědli naučeni v Pismu i Farizeji.
3 Zatom, čego li by vam kazali shranjati, shranjajte i činite, no po dělah jih ne činite; ibo oni govoret, no ne činet.
4 Ibo vežut brěmena težke i ne do nošenja, i kladut je na ramena ljudske, no prstom svojim ne hčut jih dvignuti.
5 A vse děly svoje činet, aby byli viděni od ljudij, i razširjajut tefiliny svoje, i razpuščajut dol plaščev svojih.
6 Takože ljubet prve města na večerah, i prve stolky v synagogah.
7 I pozdravjenja na trgah, i aby jih nazvali ljudi: Učitelju, učitelju!
8 No vy ne nazyvajte se učiteljami; ibo jedin jest učitelj vaš, Hristos; no vy jeste vsi bratami.
9 I nikogo ne zovite otcem vašim na zemji; ibo jedin jest Otec vaš, ktory jest v nebesah.
10 A nehaj vas ne zovut učiteljami, ibo jedin jest učitelj vaš, Hristos.
11 No kto iz vas najvysši jest, bude slugoju vašim.
12 A kto by se vozvyšal, bude poniženy; a kto by se ponižal, bude vozvyšeny.
13 No běda vam, naučeni v Pismu i Farizeji liceměri! že zaključate kraljevstvo nebeske prěd ljudami; ibo tam sami ne vhodite, ni tym, ktori by vstupiti htěli, vhoditi ne dopuščate.
14 Běda vam, naučeni v Pismu i Farizeji liceměri! že požirate domy vdov, a to pod govorjenju dolgyh molitv, zato težši sud dostanite.
15 Běda vam, naučeni v Pismu i Farizeji liceměri! že obhodite morje i zemju, abyste učinili jedinogo novogo Žida; a kogdy se njim stane, činite go synom grěha, dvukratno veče neželi jeste sami.
16 Běda vam, načelniki slěpi! ktori govorite: kto by prisegal na svetilišče, to ničto ne znači: no kto by prisegal na zlato svetilišča, vinny jest.
17 Glupi i slěpi! ibo čto jest vysšego, zlato či svetilišče, ktoro sveti zlato?
18 A kto by prisegal na oltar, to ničto ne znači; no kto by prisegal na žrtvu, ktora jest na njim, vinny jest.
19 Glupi i slěpi! ibo čto jest vysšego? žrtva, či oltar, ktory sveti žrtvu?
20 Kto itak prisega na oltar, prisega na njego, i na to vse, čto na njim jest;
21 A kto prisega na svetilišče, prisega na njego, i na togo, ktory v njem žive;
22 I kto prisega na nebo, prisega na tron Božji, i na togo, ktory sědi na njem.
23 Běda vam, naučeni v Pismu i Farizeji liceměri! že date desetinu iz mety i iz kopra i iz kmina, i ne ostrěgate važnějših věčij v zakonu. Sud, milosrdje i věra; te věči jest iměli činiti, a jih ne ostrěgate.
24 Načelniki slěpi! ktori prěcědite komara, i velbluda goltate.
25 Běda vam, naučeni v Pismu i Farizeji liceměri! že čistite čašu i misku iz vněšnjej strany, a vnutri polna jest nečistota.
26 Farizeje slěpy! očisti najprvo to, čto jest vnutri v čaši i v miskě, aby i to, čto jest na vněšnjej, čisto bylo.
27 Běda vam, naučeni v Pismu i Farizeji liceměri! že jeste podobni grobam oběljenym, ktore iz vněšnjej stany sut krasne, no vnutri polne sut kosti mrtvyh i vsakoj nečistoty.
28 Takože i vy iz vněšnjej stany izgledate kak ljudi čestnymi; no vnutri jeste polni liceměrnosti i nepravdy.
29 Běda vam, naučeni v Pismu i Farizeji liceměri! že postavjate groby prorokov, i ukrašate groby spravědlivyh,
30 I govorite: Kakbyhmo byli za dni otcev naših, ne byhmo byli surabotnikami jih v litju krvi prorokov.
31 A tak svědčite sami protiv sobě, že jeste syni tyh, ktori prorokov ubivali.
32 I vy tož dopolnjate měry otcev vaših.
33 Zmiji! Rode zmiji! i kako budete mogli odidti od suda ognja peklnogo?
34 Zatom vot ja pošlju do vas prorokov, i mudrcev, i naučenyh v Pismu, a iz njih něktoryh ubijete i razpnete, a něktoryh iz njih bičujete v synagogah vaših, i budete je prěslědovati od grada do grada;
35 Aby prišla na vas vsa krov čestna, prolita na zemji, od krve Abla spravědlivogo až do krve Zaharija, syna Barahija, ktorogo jeste ubili medžu svetiliščem a oltarem.
36 Zapravdu govorju vam: Prijde to vse na toj narod.
37 Jeruzalem! Jeruzalem! ktory ubivaš prorokov, i ktory kamenuješ tyh, ktori do tebe byli posylani: kolikokat jesm htěl sobrati děti tvoje, tak kako sbiraje kura svoje male kury pod krilom, a jeste ne htěli?
38 Vot vaš dom vam pusty ostane.
39 Ibo govorju vam, že mene ne ugledate od togo časa, až rěčete: Blagoslavjany, ktory ide v imenu Gospodinskom.

## Razděl 24

1 A izševši Jezus iz svetilišča pristupili učeniki jego, aby jemu pokazali ozdoby svetilišča.
2 I rěkl jim Jezus: či ne vidite togo vsego? Zapravdu govorju vam, ne ostane tu kamenj na kamenju, ktory by ne byl razvaljeny.
3 A kogdy sěděl na gorě olivnoj, pristupili do njego učeniki oddělno, govoreči: Pověd nam, kogdy se to stane, i kaky bude znak prijdenja tvojego i dokončenja světa?
4 I odgovarjajuči Jezus, rěkl jim: Gledajte, aby vas kto ne pokusil.
5 Ibo mnogo jih prijde pod imenom mojem, govoreči: Jesm Hristos; i mnogo jih pokuset.
6 I uslyšite vojny i věsti o vojnah; gledajte že, abyste se tym ne strašili; ibo imaje to vse byti, no ješče tu ne jest konec.
7 Ibo povstane narod protiv narodu, i kraljevstvo protiv kraljevstvu, i budut glady, bolěznji i tresenja zemji městami.
8 No to vse jest početkom bolja.
9 Togdy vas prědadut v mučenje, i budut vas ubivati, i budete v nenavisti u vsih narodov za imene moje.
10 A itak mnogo se jih bude gněvati, a jedni drugyh prědadut, i jedni drugyh nenaviděti budut.
11 I mnogo falšivyh prorokov povstane, i pokuset mnogo.
12 A ibo se razmnoži krivda, ohladi se ljubov mnogo.
13 No kto prětrpi až do konca, toj spaseny bude.
14 I bude kazano Evangelje kraljevstva po vsem světu, na svědočstvo vsem narodam. A togda prijde konec.
15 Zatom kogdy ugleděte omrženje opustěnja, razkazano črěz Danijela proroka, kak stane na městu svetom, (kto čita, nehaj razumě),
16 Itak ti, ktori budut v zemji Judzkoj, nehaj běžet v gory;
17 A kto bude na strěhě, nehaj ne spušča se, aby něčto vzel iz doma svojego;
18 A kto na polju, nehaj nazad ne vrati, aby vzel oděži svoje.
19 A běda brěmennym i prsami krmečim v te dni!
20 Zatom molite se, aby ne bylo vaše běgstvo v zimě ili v subotu.
21 Ibo togda bude veliky sgnetenje, kakogo ne bylo od početka světa až dotud i na vsakčas.
22 A kakby ne byli skračene te dni, nijednogo těla by ne bylo spasenogo: no za izbranyh budut skračene te dni.
23 Itak jestli by vam kto rěkl: Vot tu jest Hristos, ili tam, ne věrite.
24 Ibo vstanut falšivi Hristosi, i falšivi proroki, i činiti budut velike znaky i čudesa, tak aby pokusili (jestli možno) i izbranyh.
25 Vot jesm vam prědskazal.
26 Jestli by vam itak rěkli: Vot na pustynji jest, ne izhodite; vot v komorah, ne věrite.
27 Ibo kako blěskavica izhodi od vozhoda i pokaže se až na zapad. Tak bude s prijdenjem Syna člověčskogo.
28 Ibo kdekoli bude mrtvec, tam se sberut i orli.
29 A momentalno po sgnetenju v tyh dnjah solnce se zatmi, a měsec ne da světla svojego, i zvězdy budut padati iz neba, i moči nebeske pomrdajut se.
30 Togda se ukaže znak Syna člověčskogo na nebu, a itak budut roptati vse rody zemji, i uvidet Syna člověčskogo, prihodečego na oblakah nebesnyh, s močju i so slavoju velikoju;
31 I pošlje On Angelov svojih s truboju glasa velikogo, i sberut izbranyh jego od četyrěh větrov, od jednogo konca nebes až do drugogo konca.
32 A od drěva figovogo naučite se toj paraboly: Kogdy se už větva jego obnavja i listy odpuščaje, poznajete, že blizko jest lěto.
33 Takože i vy, kogdy uvidite to vse, poznajte, že blizko jest, vo dverah.
34 Zapravdu govorju vam, že ne skonči se to pokoljenje, až se to vse stalo.
35 Nebo i zemja minut, no slova moje ne minut.
36 A o tom dnju i časině nikto ne zna, ni Angeli nebesni, jedino sam Otec moj.
37 No kako bylo za dni Noego, tak bude i prijdenjem Syna člověčskogo.
38 Ibo kako za te dni prěd potopom jeli, i pili, i ženili se i za muž izdavali, až do togo dnja, ktorogo všel Noe do arky,
39 I ne razuměli, až prišel potop i vzel vse: tak bude i prijdenje Syna člověčskogo.
40 Itak budut dva na polja; jedin bude vzety, a drugy ostavjeny;
41 Dvě budut mlěti vo mlynu; jedna bude vzeta, a druga ostavjena;
42 čuvajte itak, zato že ne znate, v ktoroj časině Gospodin vaš prijde.
43 A to znate, kakby znal gospodar, o ktoroj časině zloděj ima prijdti, by čuval i ne dal by podkopati doma svojego.
44 Zatom i vy budite gotovi; ibo v časině, ktoroj by ne očekyvali, Syn člověčsky prijde.
45 Ktory itak jest sluga věrny i mudry, ktorogo postavil gospodin jego nad čeljadju svojeju, aby jim daval jedu na čas pravy?
46 Blagoslavjany sluga, ktorogo by, priševši gospodin jego, našel tak činečego;
47 Zapravdu govorju vam, že go nad vsimi tovarami svojimi postavi.
48 A jestli zly sluga by rěkl v srdcu svojem: Gospodin moj s prihodom svojim spozdnja se;
49 I začel by biti drugyh slugov, a jesti i piti s pijanicami:
50 Prijde gospodin slugy togo, dnja, ktorogo se ne očekyvaje, v časině, ktoroj ne zna;
51 I prěsěkti go na pol. A čest jego položi s liceměrami; tam bude plač i skripěnje zubov.

## Razděl 25

1 Itak podobno bude kraljevstvo nebeske deseti děvam, ktore vzevši lampy svoje, izšli na strětenje s mladoženihom.
2 A bylo iz njih pet mudryh, a pet bezumnyh.
3 Te bezumne vzevši lampy svoje, ne vzeli masla so soboju.
4 No mudre vzeli maslo v svojih posudah s lampami svojimi.
5 A kogdy mladoženih spozdnil s prihodom, byli vse izmučene i usnuli.
6 A o polnoči stal se krik: Vot mladoženih ide; izojdite do njego!
7 Itak vstali vse děvy i čistili lampy svoje.
8 No bezumne rěkli do mudryh: Dajte nam iz masla vašego, ibo lampy naše gasnut.
9 I odgovorili mudre, govoreči: Ne damo, ibo očevidno nam i vam ne jest dostatočno; idite skorěje do prodavcev, a kupite sobě.
10 A kogdy odšli kupovati, prišel mladoženih; a te, ktore byli gotove, pošli s njim na svatbu; i zaključene sut dveri.
11 No potom prišli i druge děvy, govoreči: Gospodine, gospodine, otvori nam!
12 A on odgovarjajuči, rěkl: Zapravdu govorju vam, ne znaju vas.
13 čuvajte itak; ibo ne znate dnja ni časiny, v ktoroj Syn člověčsky prijde.
14 Ibo kako člověk von odježdžajuči pozval slugov svojih i oddal jim dobra svoje;
15 I dal jednomu pet talentov, a drugomu dva, a drugomu jedin, vsakomu po sposobnosti jego, i momentalno von odšel.
16 A poševši toj, ktory vzel pet talentov, dělal njimi, i dobyl druge pet talentov.
17 Takože i toj ktory vzel dva, dobyl druge dva.
18 No toj, ktory vzel jedin, odševši izkopal dol v zemji, i ukryl monetu gospodina svojego.
19 A po dolgom času prišel Gospodin tyh slugov, i sčital se s njimi.
20 Itak pristupivši on, ktory vzel pet talentov, prinesl druge pet talentov, govoreči: Gospodine! Jesm prědal mně pet talentov, vot jesm druge pet talentov dobyl njimi.
21 I rěkl jemu gospodin jego: To dobro, slugo dobry i věrny! Nad malom jesi byl věrnym, nad mnogo tebe postavju; vojdi do radosti gospodina tvojego.
22 A pristupivši i on, ktory dva talenty vzel, rěkl: Gospodine! Jesi prědal mně dva talenty, vot jesm druge dva talenty dobyl njimi.
23 Rěkl jemu gospodin jego: To dobro, slugo dobry i věrny! Ibo jesi byl věrny nad malom, nad mnogo tebe postavju; vojdi do radosti gospodina tvojego.
24 A pristupivši i toj, ktory vzel jedin talent, rěkl: Gospodine! Jesm znal,  jesi člověk strogy, ktory žneš, kde jesi ne razsějival, i sbiraš, kde jesi ne razsypyval;
25 Boječi se itak, jesm šel i ukryl talent tvoj v zemji; vot imaš, čto tvoje jest.
26 A odgovarjajuči gospodin jego, rěkl jemu: Slugo zly i lěnivy! Jesi znal, že žnu, kde jesm ne razsějival, i sbiraju, kde jesm ne razsypyval;
27 Zato jesi mogl toj talent dati tym, ktori grošami trgujut, a ja priševši, byh vzel, čto jest moje, s procentami.
28 Zatom prijmite od njego toj talent, a dajte tomu, ktory ima deset talentov.
29 (Ibo vsakomu, ktory ima, bude dano, i izbytok jim bude; a od togo, ktory ne ima, i to, čto ima, bude od njego odjeto.)
30 A nekoristnogo slugu kydnite do tyh temnosti vněšnjih, tam bude plač i skripěnje zubov.
31 A kogdy prijde Syn člověčsky v slavě svojej, i vsi Angeli s njim, usěde na tronu slavy svojej,
32 I budut sobrano prěd njim vse narody, i děli jedni od drugyh, kako pastyr děli ovce od kozlov.
33 A postavi ovce po pravoj svojej, a kozli po lěvici.
34 Itak rěče kralj tym, ktori budut po pravoj jego: Pojdite, blagoslavjani Otca mojego! naslědujte kraljevstvo vam pripravjeno od osnovanja světa.
35 Ibo jesm byl gladny, a jeste dali mně jesti; jesm žedal, a jeste dali mně piti; jesm byl gostem, a jeste prijeli mene;
36 Jesm byl nagy, a jeste oděli mene; jesm byl boljny, a jeste prišli do mene; jesm byl vo vezenju, a jeste prihodili do mene.
37 Itak jemu odgovoret spravědlivi: Gospodine! Kogdy jesmo tebe viděli gladnym, a jesmo krmili tebe? ili žedajučim, a jesmo dali piti jesmo tebe?
38 I kogdy jesmo tebe viděli gostem i prijeli tebe? ili nagym, a oděli tebe?
39 Ili kogdy jesmo tebe viděli boljnym, ili v vezenju, a prihodili do tebe?
40 A odgovarjajuči kralj, rěče jim: Zapravdu govorju vam, čto li jeste učinili jednomu iz tyh bratov mojih najmenših, mně jeste učinili.
41 Potom rěče i tym, ktori budut po lěvici: Idite od mene, prokleti! v ogonj věčny, ktory pripravjeny jest djavlu i angelam jego.
42 Ibo jesm byl gladny, a jeste ne dali mně jesti; jesm žedal, a jeste ne dali mně piti;
43 Jesm byl gostem, a jeste ne prijeli mene; nagy, a jeste ne oděli mene; boljny i vo vezenju, a jeste ne prišli do mene.
44 Itak jemu odgovoret oni: Gospodine! kogdy jesmo tebe viděli gladnym, ili žedajučim, ili gostem, ili nagym, ili boljnym, ili vo vezenju, a jesmo ne služili tobě?
45 Itak jim odgovori: Zapravdu govorju vam, čego jeste ne učinili jednomu iz tyh najmenših, i mně jeste ne učinili.
46 I pojdut ti na muky věčne; no spravědlivi do života věčnogo.

## Razděl 26

1 I stalo se, kogdy dokončil Jezus te vse govory, rěkl do učenikov svojih:
2 Znate, že po dvoh dnjah bude Pasha, a Syn člověčsky bude prědany, aby byl razpety na križu.
3 Itak se sobrali vysši duhovniki i naučeni v Pismu i starši ljuda do dvora vrhovnogo duhovnika, ktorogo zvano Kajaf;
4 I sovětovali, kakoby Jezusa hytrostju shvatili i ubili;
5 No govorili: Ne v prazdniku, aby ne byl bunta medžu ljudami.
6 A kogdy Jezus byl v Betaniji, v domu Simona leprosnogo,
7 Pristupila do njego žena, imajuča sodržnik alabastrovy masti mnogo dragoj, i prolila ju na glavu jego, kogdy sěděl u stola.
8 To videči učeniki jego, razgněvali se, govoreči: I na čto to raztračenje?
9 Ibo mogla byti ta mast drago prodana, i moglo se to dati ubogym.
10 Uslyšavši togo Jezus, rěkl jim: Začto odčajivate tu ženu? Zapravdu dobro dělo učinila protiv mene.
11 Ibo uboge vsakčas imate so soboju, no mene ne vsakčas iměti budete.
12 Ibo ona prolivši tu mast na tělo moje, učinila to, pripravjajuči mene k pogrebu.
13 Zapravdu govorju vam: Kdekoli bude kazano to Evangelje po vsem světu, bude govorjeno, čto ona učinila, na pamet jej.
14 Itak odševši jedin iz dvanadseti, ktorogo zvano Judasom Iskariotom, do vysših duhovnikov,
15 Rěkl jim: Čto mně hčete dati, a ja go vam prědam? A oni jemu naznačili trideset srěbrnikov.
16 A odtud iskal možnosti, aby go prědal.
17 A prvogo dnja kyslyh hlěbov pristupili učeniki do Jezusa, govoreči jemu: kde hčeš, abyhmo prigotovili, abys jel baranka Pashy?
18 A on rěkl: Idite do grada, do něktorogo člověka, a rěčite jemu: Kazal tobě učitelj pověděti: Čas moj blizko jest, u tebe jesti budu baranka s učenikami mojimi.
19 I učinili učeniki, kako jim kazal Jezus, i prigotovili baranka.
20 A kogdy byl večer, usědl za stolom so dvanadsetju.
21 A kogdy jeli, rěkl: Zapravdu govorju vam, jedin iz vas prěda mene.
22 I smutivši se mnogo, začeli govoriti do njego vsaky iz njih: či jesm ja njim, Gospodine?
23 A on odgovarjajuči, rěkl: Ktory moči so mnoju ruku v miskě, toj mene prěda.
24 Syn člověčsky ide, kako napisano o njem; no běda člověku tomu, črěz ktorogo Syn člověčsky prědany bude! dobro by jemu bylo, by se ne narodil toj člověk.
25 A odgovarjajuči Judas, ktory go prědal, rěkl: Či jesm ja njim, Učitelju? Govori jemu: Ty jesi pověděl.
26 A kogdy oni jeli, vzevši Jezus hlěb, a blagoslovivši lomil, i dal učenikam i rěkl: Berite, jedite, to jest tělo moje.
27 A vzevši čašu i blagodarivši, dal jim, govoreči: Pijte iz togo vsi;
28 Ibo to jest krov moja novogo zavěta, ktora za mnogo bude izlita na odpuščenje grěhov.
29 No govorju vam, odtud ne budu piti iz togo ploda vinnogo kusta, až do dnja togo, kogdy go budu piti s vami novy v kraljevstvu Otca mojego.
30 I spěvavši himn, izšli na goru olivnu.
31 Itak jim rěkl Jezus: Vy vsi budete sumněvati se v mene toj noči; ibo jest Napisano: Udarju pastyra, i budut razprašene ovce stada.
32 No kogdy ja vozkresnu, budu hoditi prěd vami do Galileji.
33 A odgovarjajuči Petr, rěkl jemu: Hot by vsi sumněvali se v tebe, ja nikogdy ne budu sumněvati se v tebe.
34 Rěkl jemu Jezus: Zapravdu govorju tobě, že toj noči, najprvo než kokot spěva, trikratno se mene odkažeš.
35 Rěkl jemu Petr: Hot byh s toboju iměl i umirati, ne odkažu se tebe. Takože i vsi učeniki govorili.
36 Itak prišel Jezus s njimi na město, ktore zvano Getsemane, i rěkl učenikam: Sědite tu, odidu i budu se tam molil.
37 A vzevši so soboju Petra i dvoh synov Zebedeja, začel se smutiti i byti trevožnym.
38 Itak jim rěkl Jezus: Smutna jest duša moja až do smrti; ostanite že tu, a čuvajte so mnoju.
39 A postupivši malo dalje, padl na lice svoje, moleči se i govoreči: Otče moj, jestli možno, nehaj mene ta čaša obojde; Jednako ne tako kak ja hču, no kak ty.
40 Itak prišel do učenikov, i našel je spečih, i rěkl Petru: Takože jeste ne mogli črěz jednu časinu čuvati so mnoju?
41 čuvajte že, a molite se, abyste ne byli pokušeni; duh ima ohotu, no tělo jest slabo.
42 Snova odševši, molil se, govoreči: Otče moj, jestli mene ne može ta čaša obojdti I jesm dolžen, abyh go pil, nehaj se stane volja tvoja.
43 A priševši, našel jih snova spečih; ibo oči jih byli težke.
44 A ostavivši jih, snova odšel i molil se po tretje, tož slova govoreči.
45 Itak prišel do učenikov svojih i rěkl jim: Spite už i odpočivajte; vot se približila časina, a Syn člověčsky bude prědany v ruky grěšnikov.
46 Vstanite, pojdemo! vot se približil toj, ktory mene prěda.
47 A kogdy on ješče govoril, vot Judas, jedin iz dvanadset, prišel, a s njim velika banda s mečami i s kyjami, od vysših duhovnikov i starših ljuda;
48 No toj, ktory go prodaval, dal jim znak, govoreči: Ktorogokoli cěluju, toj jest On; berite go.
49 A směsta pristupivši do Jezusa, rěkl: Bud blagoslovjeny, Učitelju! i cěloval go.
50 No jemu rěkl Jezus: Prijatelju! Po něčto jesi prišel? Itak pristupivši, kydnuli ruky na Jezusa i shvatili go.
51 A vot jedin iz tyh, ktori byli s Jesusom, iztrgnul ruku, i dobyl svoj meč, a udarivši slugu duhovnika vrhovnogo, urězal jemu uho.
52 Itak jemu rěkl Jezus: Obrati meč svoj na město jego; ibo vsi, ktori meč berut, od meča pogynut.
53 či mysliš, byh ne mogl tutčas prositi Otca mojego, a postavil by mně veče než dvanadset vojsk Angelov?
54 No kakoby se izpolnili Pisma, ktore govoret, že se tak imaje stati?
55 V toj časině govoril Jezus do toj tolpy: Jeste izšli kako na razbojnika s mečami i s kyjami, shvatiti mene; Vo vsaky denj jesm sěděl u vas, učeči v svetilišču, a jeste ne shvatili mene.
56 No se to vse stalo, aby se izpolnili Pisma prorokov. Itak učeniki jego vsi opustivši go, uběgli.
57 A oni shvativši Jezusa, vodili go do Kajafy, vrhovnogo duhovnika, kde se sobrali naučeni v Pismu i starši.
58 No Petr šel za njim iz daleka až do dvora vrhovnogo duhovnika; a vševši tam, sěděl so slugami, aby ugleděl konec.
59 No vysši duhovniki i starši, i vsaka sovět iskali falšivogo svědočstva protiv Jezusa, aby go na smrt prědali.
60 No ne našli; i hot mnogo falšivyh svědkov prihodilo, ničego ne našli. A na koncu postupivši dva falšivi svědki,
61 Rěkli: Toj govoril: Mogu razvaliti svetilišče Božje, a za tri dni postaviti go.
62 A vstavši najvysši duhovnik, rěkl jemu: Ničto ne odgovarjaš na to, čto protiv tobě svědčet?
63 No Jezus molčal. A odgovarjajuči najvysši duhovnik rěkl: Prisegaju tebe črěz Boga živogo, abys nam pověděl, jestli jesi ty Hristos, ov Syn Božji?
64 Rěkl jemu Jezus: Ty jesi pověděl; ibo govorju vam: Odtud uvidete Syna člověčskogo sědečego na pravoj straně Božjej, i prihodečego na oblakah nebesnyh.
65 Itak najvysši duhovnik razdrl oděž svoju, govoreči: Bogohulil! Do čego ješče potrěbujemo svědkov? Vot jeste tutčas slyšali bogohuljenja jego.
66 Čto vy myslite? A oni odgovarjajuči, rěkli: Vinny jest smrti.
67 Itak pljuvali na obličje jego, i grstami go bili, a drugi go bili v lice,
68 Govoreči: Prorokuj nam, Hristose! kto jest toj, ktory tebe udaril?
69 No Petr sěděl prěd domom na dvoru. Itak pristupila do njego jedna děvka, govoreči: I ty jesi byl s tym Jezusom Galilejskym.
70 A on se odkazal prěd vsimi, govoreči: Ne znaju, čto govoriš.
71 A kogdy on izhodil do vrat, ugleděla go ina děvka, i rěkla do tyh, ktory tam byli: Toj byl s tym Jezusom Nazaretskym.
72 Itak povtorno odkazal se s prisegoju, govoreči: Ne znaju togo člověka.
73 A pristupivši po malom času ti, ktori tam stali, rěkli Petru: Pravdivo i ty jesi iz njih; ibo i govor tvoja tebe prědava.
74 Itak začel sebe prokleti i prisegati, govoreči: Ne znaju togo člověka; a v tom samom vrěmenu kokot spěval.
75 I pomněl Petr slova Jezusa, ktory jemu pověděl: Najprvo než kokot spěva, trikratno se mene odkažeš; a izševši von, gorko plakal.

## Razděl 27

1 A kogdy bylo rano, zvali radu vsih vysših duhovnikov i starših ljuda protiv Jezusu, aby go ubili;
2 I svezavši go, vodili i podali Pontskomu Pilatu, vrhnym načelniku Jeruzalema.
3 Itak Judas, ktory go prodal, videči to, že byl sudženy, žalujuči togo, vratil te trideset srěbrnikov, vysšim duhovnikam i staršim ljuda.
4 Govoreči: Jesm sgrěšil, prědavši krov nevinnu! A oni rěkli: Čto nam do togo? ty uvidiš!
5 A ostavivši te srěbrniky v svetilišču, odšel, a odševši pověsil se.
6 No vysši duhovniki vzevši te srěbrniky, govorili: Ne godi se jih klasti do skarba svetilišča, ibo to zaplata za krov jest.
7 I sovětovavši se, kupili za to polje grnčara na pogrebenje občih.
8 Zato to polje nazvano jest poljem krve, až do dnja tutdennogo.
9 Itak se izpolnilo, čto pověděno črěz Jeremije proroka, govorečego: I vzeli trideseti srěbrnikov, zaplatu za togo, ktory byl ocěnjeny od synov Izraelskyh;
10 I dali je za polje grnčara, kako mně kazal Gospodin.
11 A Jezus stal prěd starostoju; i pytal go starosta, govoreči: Ty jesi ov kralj židovsky? A Jezus jemu rěkl: Ty govoriš.
12 A kogdy jego obvinjali vysši duhovniki i starši, ničto ne odgovoril.
13 Itak jemu rěkl Pilat: Ne slyšiš kako mnogo věčij protiv tobě svědčet?
14 No jemu ne odgovoril na nijedno slovo, tak že se starosta mnogo divoval.
15 No byl obyčaj, že v prazdniku starosta izpušča ljudu jedinogo vezenja, ktorogo by htěli.
16 I iměli tutčas vezenja znamenitogo, ktorogo zvano Barabas.
17 A kogdy se sobrali, rěkl do njih Pilat: Ktorogo hčete, abyh vam odpustil? Barabasa, či Jezusa, ktorogo zovut Hristosom?
18 Ibo znal, že go iz nenavisti prědali.
19 A kogdy on sěděl na sudnom tronu, prišla do njego žena jego, govoreči: Ne iměj nijednogo děla s tym spravědlivym; ibo jesm mnogo utrpěla tutdenj vo snu iz jego povoda.
20 No vysši duhovniki i starši podgovorili ljuda, aby prosili o Barabasa, aby Jezusa izgubiti.
21 A odgovarjajuči starosta, rěkl jim: Ktorogo hčete, abyh vam iz tyh dvoh odpustil? a oni odgovorili: Barabasa.
22 Rěkl jim Pilat: Čto itak učinju s Jezusom, ktorogo zovut Hristosom? Rěkli jemu vsi: Nehaj bude razpety na križu.
23 A starosta rěkl: Čto že zlogo učinil? No oni tym vyše zvali, govoreči: Nehaj bude razpety na križu!
24 A videči Pilat, že to ničto ne pomagalo, no očevidno se vysše smetenje vozbudžalo, vzevši vodu, umyl ruky prěd ljudom, govoreči: Ne jesm ja vinny krve togo spravědlivogo; vy uvidite.
25 A odgovarjajuči ves ljud, rěkl: Krov jego na nas i na děti naše.
26 Itak jim izpustil Barabasa; no Jezusa bičevavši, prědal go, aby byl razpety na križu.
27 Itak vojini starosty privedši Jezusa do pretorium, sobrali kolo njego vsu kohortu;
28 A razděli go, oděli go v purpurny plašč;
29 I pletši věnec iz trna, vložili na glavu jego, i dali trstinu v pravu ruku jego, a padajuči prěd njim na kolěna, smějali se iz njego, govoreči: Bud blagoslavjany, kralju židovsky!
30 A pljuvajuči na njego, vzeli tu trstinu, i bili go v glavu jego.
31 A kogdy se iz njego smějali se, sjeli iz njego plašč, i oblěkli go v oděž jego, i vodili go, aby byl razpety na križu.
32 A izhodeči našli člověka iz Kyreny, imenom Simon; togo prinudili, aby nesl križ jego.
33 A priševši na město rěčeno Golgota, ktore zovut městom mrtvyh glav,
34 Dali jemu piti ocet iz žolčju směšany; a vkusivši, ne htěl piti.
35 A razpinali go, razdělili oděži jego, i metali sudby, aby se izpolnilo, čto pověděno črěz proroka: Razdělili sobě oděži moje, a o oděži moje sudby metali.
36 A sědeči, čuvali nad njim.
37 I pribili nad glavoju jego vinu s napisom: Toj jest Jezus, kralj židovsky.
38 Byli tož razpeti s njim dva razbojniki, jedin po pravoj, a drugy po lěvici.
39 A ti, ktori mimo hodili, bogohulili go, hvějuči glavami svojimi,
40 I govoreči: Ty, čto razvaljaš svetilišče, a v trěh dnjah postavjaš go, spasi samogo sebe; jestli jesi Syn Božji, spusti se iz križa.
41 Takože i vysši duhovniki s naučenymi v Pismu, i s staršimi, bogohulili govoreči:
42 Inyh spasal, a samogo sebe spasati ne može; jestli jest kraljem Izraelskym, nehaj tutčas spusti se iz križa, a uvěrimo jemu.
43 Dověrjal v Boga, nehaj go tutčas izbavi, jestli go ljubi; ibo pověděl: Jesm Synom Božjim.
44 Takože tož i razbojniki, ktori byli s njim razpeti, bogohulili jego.
45 A od šestoj časiny stala se temnost po cěloj zemji až do devetoj časiny.
46 A okolo devetoj časiny pozval Jezus glasom velikym, govoreči: Eli, Eli, Lama Sabahtani! to jest, Bože moj! Bože moj! čemu jesi mene opustil?
47 Itak něktori iz tyh, ktori tam stali, uslyšavši togo, govorili: Iliji toj zove.
48 A v tom samom vrěmenu běgal jedin iz njih do, vzel gubku, i napolnil ju octom, a vloživši na trstinu, dal jemu piti.
49 A drugi govorili: Ostavi; Uvidimo, jestli prijde Ilija, aby go izbavil.
50 No Jezus pozvavši povtorno glasom velikym, oddal duha.
51 A vot zavěsa svetilišča raztrgnula se na dvě česty od vrha až do dola, i potresala se zemja, a kamenje se razpadali.
52 I groby se otvarjali, a mnogo těl svetyh, ktori usnuli, vstalo:
53 A izševši iz grobov po vozkrešenju jego, vošli do grada svetogo, i pokazali se mnogym.
54 Itak sotnik i ti, ktori s njim nad Jezusom čuvali, videči tresenje zemji, i to, čto se stalo, prěstrašili se mnogo, govoreči: Zapravdu toj byl Synom Božjim.
55 A bylo tam mnogo žen iz daleka se prigledajučih, ktore prišli s Jezusom od Galileji, služeči jemu;
56 Medžu njimi byla Marija Magdalena, i Marija, mati Jakoba i Jozefa, i mati synov Zebedeja.
57 A kogdy byl večer, prišel člověk bogaty iz Arimatije, imenom Jozef, ktory tož byl učenikom Jezusa.
58 Toj priševši do Pilata, prosil o tělo Jezusa. Itak Pilat kazal, aby jemu bylo Jego tělo prědano;
59 A Jozef vzevši Jego tělo, ovinul je v čisto platno;
60 I položil je v svojem novom grobu, ktory v kamenju kazal izrězati; a sunul prěd dveri groba veliky kamenj i odšel.
61 A byla tam Marija Magdalena, i druga Marija, ktore sěděli naprotiv groba.
62 A drugogo dnja, ktory byl prvy po prigotovjenju, sobrali se vysši duhovniki i Farizeji do Pilata.
63 Govoreči: Gospodine! Jesmo vozpametali, že ov obmannik pověděl, kogdy ješče živy byl: Po trěh dnjah vozkresnu.
64 Kaži itak čuvati nad grobom až do dnja tretjego, aby ne prišlo učeniki jego v noči ukradli go, i ne pověděli ljudu, že vstal iz mrtvyh; i bude poslědnji omam gorši než prvy.
65 Rěkl jim Pilat: Imate stražu, idite i čuvajte, kako znate.
66 A oni poševši, obstupili grob stražeju, aby čuvali nad kamenjem.

## Razděl 28

1 A kogdy se skončila subota, v času razsvěta prvogo dnja togo tydnja prišla Marija Magdalena i druga Marija, aby grob ogledali.
2 A vot stalo se veliko tresenje zemji; ibo Angel Gospodinsky spustivši se iz neba, pristupil i sunul kamenj, i usědl na njem.
3 A byl izgled jego kako blěskavica, a oděž jego běla kak sněg.
4 A ti, ktori shranjali grob, zadržali, boječi se go, i stali se kako mrtvi.
5 No Angel odgovarjajuči, rěkl do žen: Ne bojite se; ibo znaju, že Jezusa, ktory byl razpety na križu, iščete.
6 Ne ima go tu; ibo vozkresnul, kako pověděl; hodite, ogledajte město, kde ležal Gospodin.
7 A bystro idite, glasite učenikam jego, že vozkresnul; a vot bude hoditi prěd vami do Galileji, tam go uvidite; vot jesm vam pověděl.
8 Itak izševši bystro od groba s bojaznju i s velikoju radostju, běgali, aby to glasili učenikam jego.
9 A kogdy šli, aby to glasiti učenikam jego, vot Jezus byl prěd njimi, govoreči: Budite pozdravjeni. A one pristupivši, objeli nog jego i dali jemu poklon.
10 Itak jim rěkl Jezus: Ne bojite se; idite, glasite bratam mojim, aby pošli do Galileji, a tam mene uvidet.
11 A kogdy one pošli, něktori iz straže priševši do grada, donesli vysšim duhovnikam vse, čto se stalo.
12 Oni sobrali se so staršimi, i sovětovavši se, dali nemalo grošev vojinam,
13 Govoreči: Govorite, učeniki jego v noči priševši, ukradli go, kogdy jesmo spali.
14 A jestli by to prišlo do uha starosty, my go podgovorimo, a vas bezopasnymi učinimo.
15 A oni vzevši groši, učinili, kako jih naučeno. I raznesla se ta pověst medžu židami až do dnja tutdennogo.
16 No jedinnadset učenikov pošli do Galileji na goru, dokud jim kazal pojdti Jezus.
17 No ugleděvši go, poklonili se jemu; no něktori sumněvali se.
18 No Jezus pristupivši, govoril do njih, a rěkl: Dana mně jest vsaka moč na nebu i na zemji.
19 Idite itak, učite vsih narodov, kresteči jih v ime Otca, i Syna, i Duha Svetogo;
20 Učite je shranjati vse, čto vam prikazal. A vot Jesm s vami vo vsih dnjah, až do skončenja světa.

# Evangelje Marka

## Razděl 1

1 Početok Evangelij Jezusa Hrista, Syna Božjego.
2 Kako jest napisano u proroka Izaje: Gledajte, ja posylaju angela mojego prěd lice Tvoje, ktory prigotovi put Tvoj.
3 Glas zovučego na pustynji: Gotovite put Gospodnji, učinite Jemu proste stežky.
4 Byl Joan na pustynji, kresteči i dělal krest pokajanja na odpuščenje grěhov.
5 I izhodila k njemu vsa krajina židovska i vsi iz Jeruzalema, i byli od njego kreščeni v rěkě Jordan, izpovědajuči se grěhov svojih,
6 A Joan nosil odědžu iz srsti velbludskoj i pas koženy okrug bedr svojih, krmil se sarančami I medom lěsnym..
7 I prědskazal: Ide za mnoju silnějši od mene, ktorogo ne jesm dostojen, padavši razrěšiti remenj u Jego sandalov.
8 Jesm vas krestil vodoju, ale On vas bude krestiti Duhom Svetym.
9 I stalo se, v ove dni prišel Jezus iz Nazareta v Galileji byl kreščen od Joana v Jordanu.
10 A směsta, izstupivši iz vody, uzrěl odkryvajuče se nebesa i Duha kako golubicu trvajuči na Njim.
11 I izjavil se glas iz neba: Ty jesi Moj mily Syn, v Tobě imam spodobanje.
12 A směsta Duh izgnal jego na pustynju.
13 I byl na pustynji četyrideset dni i četyrideset noči, i byl pokušeny od djabla, i byl s zvěrami, a angeli služili Mu.
14 A potom, kogda Joan byl izdany, prišel Jezus do Galileje, prědskazyvajuči Evangelje carstva Božjego,
15 govoreči: Uže se izpolnil čas i približilo se carstvo Božje. Obračajte se i věrite v Evangelje.
16 I iduči mimo Galilejskogo morja, viděl Simona i Andreja, brata jego, metajuči sěti do morja (bo byli rybakami),
17 i rěkl jim Jezus: Idite za Mnoju, i učinju vas, da budete rybakami ljudij.
18 I tutčasno ostavivše sěti, pošli za Njim.
19 I odstupivši toliko malo, viděl Jakoba Zebedejeva i Joana, brata jego, ktori napravjali sěti v lodi,
20 i iznenada jih pozval do sebe. I ostavivše otca svojego Zebedeja v lodi s najemnikami, pošli za Njim.
21 I došli do Kafarnauma. I iznenada v subotu, všel do synagogy i učil jih.
22 I čudili se učenju Jego: bo on jih učil kak vladec, a ne kako učeni v Pismu.
23 I byl v synagogě čelověk, v ktorom byl duh nečisty. I glasil:
24 Čto nam s toboju, Jezuse Nazaretsky? Jesi prišel izgubiti nas? Znam, kym jesi: Svety Bože!
25 I grozil mu Jezus, govoreči: Molči i izojdi iz člověka!
26 I trgajuči go duh nečisty i s glasnym krikom, izšel iz njego.
27 I divili se vsi, tako, že se medžu soboju pytali, govoreči: Čto to jest? Čto to za novo učenje? Už s vladoju duham nečistym razkazyvaje i sut mu poslušne?
28 I tutčasno se raznesla slava Jego po vsej Galilejskoj krajině.
29 I směsta izševši iz synagogy, došli do domu Simona i Andreja s Jakobom i s Joanom.
30 A svekrov Simona ležala, imajuči gorečku, a uže pověděli Jemu o njej.
31 I pristupivši, držal ruku jej, i skoro ju gorečka ostavila, i služila jim.
32 A kogda byl večer, kogda solnce zašlo, prinosili k Njemu vsih, ktori byli boljni i vladeni črěz demonov,
33 i vse město sobralo se pri dverah.
34 I uzdravil mnogo ljudij, ktori stradali različnymi hvorobami, i izgnal mnogo črtov, i ne dopustil jim govoriti, že Go poznali.
35 Utrom izšel na puste město i tam se molil.
36 I šel za Njim Simon i ti, ktori pri Njim byli.
37 Kogdy našli Go, pověděli Mu: Vsi tebe iščut.
38 I rěkl jim: Pojdemo drugoju dragoju do susědnyh gradov, dabyh i tam mogl učiti, bo na to jesm izšel.
39 I glasil v jih synagogah i po vsej Galileji i izgnal črty.
40 I prišel k Njemu leprovaty člověk, prosil Go, padajuči na kolěna: Jestli hčeš, možeš me očistiti.
41 A Jesus, pomilujuči se nad njim, iztegnul svoju ruku i dotknuvši jego, rěkl mu: Hču, dabys byl očiščen.
42 A kogda rěkl, naglo lepra ostavila go, i byl očiščen.
43 I zagrozil mu, i směsta go pustil.
44 I rěkl mu: Gledaj, dabys nikomu ničto ne povědal. Ale idi, pokaži se najvysšemu kaplanu i složi za svoje očiščenje žrtvu, ktoru prikazal Mojzes na svědočstvo jim.
45 Ale on izšel i začel povědati i razglasiti slovo, tako že Jezus už ne mogl javno vojdti do grada, ale prěbyval na pustyh městah, a odvsud prihodili do Njego.

## Razděl 2

1 I snova prišel do Kapernauma po několiko dnjah,
2 i uslyšano, že On jest v domu, i mnogo ljudij se sobralo, tak, da se poměstiti ne mogli až pri dverah. I govoril k njim slovo.
3 I prišli do Njego, nesuči paralizovanogo, kogo nesli četyri.
4 A kogda jego ne mogli prinesti jego povodom tolpy, odkryli pokryv doma, v ktorom On byl, i učinivši diru v njem, spustili lože, na ktorom paralizovany ležal.
5 A Jezus, uzrěvši věru jih, rěkl paralizovanomu: Synu, odpuščajut se tobě grěhy tvoje.
6 A byli tam něktori iz učenyh v Pismu, sědeči i mysleči v srdcah svojih:
7 Čemu toj tako govori? Bogohuli! Kto grěhy odpustiti može, než jedino sam Bog?
8 Jezus poznavši duhom svojim, že tako v sobě myslili, rěkl jim: Čemu to myslite v srdcah vaših?
9 Čto prostějše jest rěkti paralizovanomu: Odpuščajut se tobě grěhy, ili rěkti: Vstani, vozmi lože tvoje i idi?
10 A dabyste věděli, že syn člověčsky ima moč odpustiti grěhy na zemji (rěkl do paralizovanogo):
11 Tobě govorju: vstani, vozmi lože tvoje, a idi do doma tvojego.
12 A on směsta vstal, a vzevši lože, izšel prěd vsimi, tak, že se vsi udivili i hvalili Boga, govoreči: Jesmo nikogdy tako čuda ne viděli.
13 I izšel snova do morja, a ves ljud prihodil k Njemu, a On go naučil.
14 A kogda mimo hodil, uzrěl Levi Alfejeva sědečego v komorě mytnice i rěkl jemu: Pojdi za Mnoju. A vstavši, šel za Njim.
15 I stalo se, kogda sěděl u stola v domu jego, mnogo mytnikov i grěšnikov zajedno sěděli s Jezusom i so Jego učenikami. Bo jih mnogo bylo, ktori hodili za Njim.
16 I kogdy viděli učeny v Pismo i farizeje, že on jel s mytnikami i grěšnikami, rěkli jego učenikam: "Čemu vaš učitelj je i pije s mytnikami i grěšnikami?"
17 To uslyšavši, Jesus jim rěkl: "Zdravi ne trěbujut lěkara, toliko boljni. Bo ja ne prišel zvati spravědlivyh, toliko grěšnyh."
18 A učeniki Joana i farizeje postili, i prišli, i rěkli Jemu: "Čemu učeniki Joana i farizeje postet, a tvoji učeniki ne postet?"
19 I rěkl Jim Jesus: "Či ljudi mogut na svatbě postiti, dopoka mladoženih jest s njimi? Ne mogut postiti, poka mladoženih jest u njih.
20 Ale prijdut dni, kogda mladoženih bude vzety od njih, i togda budut postiti v ove dni.
21 Nikto ne prišije laty iz surovogo suknja k staroj oděži, bo nova lata obryva ješče čest iz staroj oděži i tvori se gorše razdiranje..
22 I nikto ne lije novogo vina v stare měhy, bo inače vino razrve měhy i vino izlije se, a měhy izniščet. Ale novo vino imaje byti lito v nove měhy."
23 I stalo se, kogda Gospodin hodil v suboty črěz žito, a jego učeniki načeli idti i rvati klasy.
24 A farizeje Mu rěkli: "Gledaj, čto činet v suboty, čto ne dostojno!"
25 I rěkl Jim: "Jeste nikogda li ne čitali, čto učinil David, kogda iměl potrěbu i byl gladny i ti, ktori byli s njim?
26 Kako všel do doma Božjego za Abiatara, najvysšego kaplana, i jedl hlěby žrtvene, ktoryh ne bylo svobodno jesti nikomu, než kaplanam, i dal tym, ktoris byli s Njim?"
27 I rěkl jim: "Subota učinjena jest za člověka, a ne člověk za suboty.
28 I tako Syn Člověčsky jest gospodom i suboty."

## Razděl 3

1 I všel snova do synagogy, a tam byl člověk, imajuči izsušanu ruku.
2 I slědovali Jego, či bude go v sobotu uzdravjati, aby jego obviniti..
3 I rěkl člověku, ktory imal izsušanu ruku: Vstani na srědu.
4 I rěkl jim: Či godi se v subotu dobro dělati, ili zlo? Dušu uzdravjati, ili ubiti? A oni molčali.
5 I pogledal na njih s gněvom, smutivši se za slěpost srdca jih, rěkl člověku: Iztegni ruku svoju. I iztegnul. I zdrava byla jego ruka.
6 A izšli farizeje, tvorili směsta radu s herodijancev protiv njemu, kako by Jego ubili.
7 A Jezus s učenikami svojimi odšel do morja, a veliko množstvo iz Galileje i iz Judejskoj zemje pošlo za Njim.
8 I tož iz Jeruzalema, i iz Idumeje, i iz Zajordanije, i ti, ktori byli iz okolin Tira i Sidona. Mnoga tolpa prišla do Njego, kogdy slyšala, čto On tvoril.
9 I rěkl učenikam svojim, aby iměli čoln povodom tolpy, aby se na Njego ne tiskali.
10 Bo mnogo jih uzdravjal. Tako mnogo, da vsi, ktori imali někake hvoroby, tisknuli se k Njemu, da by Jego dotknuti.
11 A duhy nečiste, kogdy jego viděli, padali prěd Njim i glasili:
12 Ty jesi Syn Božji. I silno jim grozil, aby Jego ne izjavili.
13 I všel na goru, prizval k sobě, ktoryh sam htěl, i prišla do Njego.
14 I učinil dvanadset, aby byli s Njim i aby jih poslal propovědati.
15 I dal jim moč uzdravjati hvoryh i izganjati črtov.
16 I dal Simonu ime Petr;
17 i prizval do sebe Jakoba Zebedejeva, i Joana, brata Jakoba, i dal jim imena Boanerges, to jest syni groma;
18 i takože Andreja, i Filipa, i Bartolomeja, i Mateja, i Tomasa, i Jakoba Alfejeva, i Tadeja, i Simona Kananejskogo,
19 i Judasa Iskariotskogo, ktory Jego izdal.
20 I prišli do domu, i sobrala se snova tolpa, tak že ne mogli až hlěba jesti.
21 A kogdy uslyšali togo svoji, izšli, aby jego pojmali: ibo govorili, že on odšel od smyslov.
22 A učeni v Pismu, ktori prišli iz Jeruzalema, govorili da on ima Belzebuba a črěz moč kneza djabolskogo črty izganja.
23 I pozvavši jih, govoril do njih v parabolah: Kako može djabol djabla izganjati?
24 I kraljevstvo, jestliby protiv sebe bylo razděljene, ne može to kraljevstvo ostati.
25 I dom, jestliby protiv sebe byl razděljeny, ne može toj dom ostati.
26 I djabel, jestliby sam protiv sebe povstal, razděljeny jest i ne bude mogti ostati, ale by imal konec.
27 Nikto ne može vojdti do domu silnogo muža i orudja jemu ukrasti, jestli silnogo muža najprvo ne sveže, i togda dom jego ograbi. 
28 Zapravdu povědam vam, da vse grěhy budut odpuščene synom ljudskym i vsim bogohulstvam, ktorymi by bogohulili.
29 Ale kto by bogohulil protiv Duhu svetomu, ne ima odpuščenja na věky, ale bude vinen grěha věčnogo.
30 I govorili: On ima duha nečistogo.
31 I prišli Jego mati i brati, i stoječi prěd domom, poslali po Njego, aby Go prizvali.
32 I tolpa sěděla okolo Njego. I rěkla jemu: „Gledaj, tvoja mati i tvoji brati iščut te prěd domom.“
33 I odgovoril jim: „Kym sut moja mati i moji brati?“
34 I pogledavši na tyh, ktori sěděli okolo Njego, rěkl: „Tu sut, moja mati i moji brati!
35 Ibo kto bude tvoriti volju Božju, toj jest brat moj, sestru moja i mati moja.“

## Razděl 4

1 I počel snova učiti pri morju: sobralo se pri Njemu velika tolpa, tako že všel do čolna i sěděl na morju, a vsa tolpa byla na pobrěžnom.
2 I učil jih mnogo v parabolah, i govoril jim v naukě svojej:
3 Slušajte: Sějatel izšel sějati.
4 A kogdy sějal, jedno spadlo pri dragě, a ptice nebeske prišli i jeli je.
5 A druge padlo na kamenno město, na ktorom ne bylo mnogo zemje. I směsta vozošlo, ibo ne bylo glubokoj zemje,
6 a kogda solnce vozošlo, obžglo se i ne imajuči korenja, usohnulo.
7 A druge padlo v trny. I izrastli trny, i dušili je, i ne dalo plod.
8 A druge upadlo na zemju dobru. I dalo plod bujny i razmnoživšego se: a jedno prineslo tridesetkratno, jedno šestdesetkratno, jedno stokratno.
9 I govoril: Kto ima uši do slyšanja, nehaj slyši.
10 A kogda sam toliko byl, pytali jego ti dvanadset, ktori pri Njem byli, o parabolu.
11 I govoril jim: Vam dano jest poznati tajenstvo kraljevstva Božjego; ale tym, ktori vně sut, vse jest učeno v parabolah:
12 aby viděli očima, a ne viděli, a slyšali, a ne razuměli: by se ne obratili a byli jim odpuščene grěhy.
13 I rěkl jim: Ne razumějete toj paraboly? To kako že budete razuměti vse paraboly?
14 Toj, ktori sěje, slovo sěje.
15 A ti pri dragě, sut ti, ktori, kak jest razsějivano slovo, ono uslyšet. No směsta prihodi djabol a bere slovo, ktoro jest sějano v srdca jih.
16 Takože i sut ti, ktori na kamennoj zemji sut posějani; kogdy slyšet slovo, směsta jego s radostju prijmut,
17 a ne imajut korenja v sobě, I sut nestali. Potom, kogdy prijde gnet i prěslědovanje za slovo, uže se lamajut.
18 A drugi sut ti, ktori medžu trnami sut posějani; Oni slovo slušajut,
19 a nepokoj světa i iluzija bogatstv, i pohota inyh věčij, vojdut, zadušet slovo i staje se bez ploda.
20 A ti, ktori na dobroj zemji sut posějani, ktori slušajut slovo i je prijmajut, prinoset plod, jedni tridesetkratno, jedni šestdesetkratno, i jedni stokratno.
21 I govoril jim: Či po to svěču vnoset, aby ju stavili pod miskoju abo pod ložem? Či ne po to, aby byla na svěčniku postavjena?
22 Ibo ne ima ničego tajnogo, ktoro by se objaviti ne imělo.
23 Jestli někto uši ima do slušanja, nehaj sluša!
24 I govoril jim: Budte ostražni, čego slušajete. Kakoju měroju měrite, bude vam měreno i ješče vam doložet.
25 Ibo kto ima, tomu bude dano; a kto ne ima, izbavet jego i iz togo, čto ima.
26 I govoril: Tako jest carstvo Božje. S njim jest kakoby člověk sěme izkydal v zemju.
27 A spal by i vstaval v noči i dnje, a sěme by vozhodilo i izrastlo, kogdy on o tym ne vě.
28 Bo zemja sama od sebe plod rodi, najprvo travu, potom klas, a potom polno zrno v klasě.
29 A kogdy kondicija zborja na to pozvoli, skoro priloži srp, bo žetva prišla.
30 I govoril: Komu podobnym učinimy carstvo Božje? Abo k komu podobnosti sravnimo jego?
31 Kako zrno gorčice, ktoro kogda sějut v zemju, jest menše od vsego sěmena, ktoro jest na zemji.
32 A kogda bude posějano, vozrasta i byva največši nad vsimi zeleninami. I čini velike vetvy, tako že pod jego těnjem mogut byvati nebeske ptice.
33 I mnogo takovymi parabolami govoril k njim slovo, kako mogli slyšati.
34 A bez parabol ne govoril jim. A svojim učenikam osobno vse objasnil.
35 I govoril jim v ovom dnju, kogdy večer nastal: Prěplyvajmo na drugu stranu.
36 A ostavivši tolpu, vzeli jego, kako byl, v čolnu, a ini ljudi byli s Njim.
37 I stala se velika burja větra, i valy lili v čolnu, tako že čoln se napolnil.
38 A on byl na zadu čolna, speči na poduškě. I budili jego, i govorili Mu: Učitelju, Tobě jest vsejedno, da pogynamo?
39 A probudivši se, zagrozil větru i rěkl morju: Molči, bud tihy! I prěstal větr, i stala se tišina velika.
40 I rěkl jim: Čemu jeste bojazlivi? Či ješče ne imate věry?
41 I prěstrašili se strahom velikym. I govorili jedin k drugomu: Kym že to jest, že i větr, i morje poslušne jemu?

## Razděl 5

1 I prišli za more do kraja Gerazenskogo.
2 I kogda On izhodil iz čolna, směsta Mu priběgl iz grobov čelověk s nečistym duhom,
3 ktory žil v grobah, i nikto ne mogl jego už lancuhami svezati:
4 ibo često svezali go v lancuhah na nogah i rukah, ktore drobil i raztrgal, i nikto jego ne mogl go pokoriti;
5 i vsegda v dnju i v noči v grobah i v gorah byl, kričal i tolkl sebe kamenem.
6 Uzrěl Jezusa iz daleka, priběgl i poklonil se Jemu,
7 i kričavši glasno, rěkl: Čto mně i tobě, Jezuse, synu Boga Najvysšego? Zaklinam te pri Bogu, da ne mučiš mene!
8 Ibo mu rěkl: Izojdi, duhu nečisty, iz čelověka!
9 I pytal jego: Kako jest tvoje ime? I rěkl Mu: Ime mi Legion, ibo nas jest mnogo.
10 I prosil Jego mnogokratno, daby ne izgnal jih iz kraja.
11 A tam pri gorě bylo veliko stado svinej, ktoro paslo.
12 I prosili jego črty: Pusti nas v svinje, dabyhmo v nje vošli.
13 I směsta jim dopustil Jezus. I izšli duhy nečiste, vošli v svinje; i kydnulo se stado velikym běgom v morje, okolo dvoh tyseč, i utonuli v morju.
14 A ti, ktori jih pasli, utekli i glasili to v gradu i na poljah. I izšli, daby uviděti, čto se stalo.
15 I prišli do Jezusa, i uviděli togo, ktory byl vladany črěz běsa, kak sěděl
oblěčeny s dobrym razumom: i bojali se.
16 Ti, ktori to viděli, povědali jim, kako se stalo s tym, kto iměl běsa, i o svinjah.
17 I načeli jego prositi, da by odšel iz jih granic.
18 A kogda vstupal v čoln, načel jego prositi on, ktori byl vladany črěz běsa, daby byl pri njem.
19 Ale on jemu togo ne dopustil, a rěkl mu: Idi do svojego doma k svojim, i glasi jim, kake velike děla Gospodin učinil tobě i pomiloval se nad toboju.
20 I odšel, i načel slaviti v Dekapolu, kake velike děla učinil mu Jezus: i vsi se divili.
21 A kogda se Jezus snova prěpravil v čolnu za morje, sobrala se pri Njem velika tolpa, i byl nad morjem.
22 I prišel jedin iz načelnikov synagogy, imena Jair, i uzrěl Go, upadl pri nogah Jego,
23 i prosil jego velmi: Moja dočera umre. Pojdi, vloži na nju ruky, daby ozdravěla i živa ostala.
24 I šel s njim, a za Njim šla velika tolpa i tisknuli jego.
25 A žena, ktora iměla tečenje krvi dvanadset let,
26 i mnogo byla vytrpěla od mnogyh lěkarev, I iměnje svoje izdala, a ničto jej ne pomoglo i se ješče gorše iměla,
27 uslyšavši o Jezusu, prišla s tyla medžu tolpoju i dotknula odědžu Jego.
28 Ibo govorila: Ako toliko tknu odědžu jego, budu zdrava.
29 Už ustal jej krvotok i počula v tělu, da byla uzdravjena od hvoroby.
30 A poznavši směsta Jezus v sobě moč, ktora iz Njego izšla, obrativši se k tolpě, govoril: Kto dotknul odědžu moju?
31 A jego učeniki Mu govorili: Vidiš kak tolpa tiskne se, a govoriš: Kto me dotknul?
32 I on se obziral po narodu, da by viděl tu, ktora to učinila.
33 A žena, boječi se i državši, bo věděla, čto se s njeju stalo, prišla i upadla prěd Njim a pověděla mu vsu pravdu.
34 A on jej rěkl: Dočerko, tvoja věra te uzdravila. Idi v mir, i budi zdrava od tvojej hvoroby.
35 A kogdy on ješče govoril, prišli od načelnika synagogy i govoreči: Tvoja dočerka umrla. Čemu ješče trudiš učitelja?
36 A Jezus uslyšavši slova, ktore pověděli, rěkl načelniku synagogy: Ne boj se, toliko věri.
37 I ne dopustil nikomu idti za Njim, jedino Petru i Jakobu, i Joanu, bratu Jakoba.
38 I prišli do domu načelnika synagogy, i viděl golk, i plače i revenje.
39 I vševši, rěkl jim: Čemu golk tvorite i plačete? Děvčina ne umrla, ale spi.
40 I smějali se iz Njego. A on izgnavši vsih, vzel otca i mati děvčiny i tyh, ktori byli s Njim, i všel do komnaty, v ktoroj děvčina ležala.
41 I vzel za ruku děvčinu, rěkl jej: Talita kumi, to jest, prěvodženo: Děvčino, (tobě govorju), vstani!
42 I směsta děvčina vstala i hodila, a iměla dvanadset lět. I začudili se velikym začudženjem.
43 I kazal jim silno, daby togo nikto ne věděl. I rěkl, daby jej dali jesti.

## Razděl 6

1 I izševši odtud, prišel do otčiny svojej, i šli za Njim učeniki jego.
2 I kogdy prišla subota, počel v synagogě učiti. I mnogi, slušajuči Go, čudili se učenju jego, govoreče: Odkud jemu to vse? I čto to za mudrost, ktora jemu jest dana, i take čudesa, ktore se dějut črěz ruky jego?
3 Či toj ne jest remeslnik, syn Marije, brat Jakoba, i Josifa, i Judasa, i Simona? Či i sestry jego tu u nas ne sut? I sumněvali se o Njem..
4 I Jezus jim govoril: Prorok nikde ne jest bez česti, toliko v otčině svojej i v domu svojem a medžu rodinoju svojej.
5 I ne mogl tam učiniti nijednogo čuda, a toliko malo hvoryh, kladuči ruky, uzdravjal.
6 I divoval se povodom nevěrja jih. I obhodil okolne sela i učil.
7 I pozval dvanadset. I počel je po dvoma posylati, i dal jim moč nad duhami nečistymi.
8 I razkazal jim, aby ničto na dragu ne brali, toliko palu: ni torby, ni hlěba, ni monety v měšku;
9 I aby se obuli v sandalah, a ne oblačili dvě suknje.
10 I govoril jim: Kogdy do někakogo domu vojdete, ostanite tam, až odsud izojdete.
11 A kogdy někto by vas ne prijmal ni vas slyšal, odidite odtud, potresite prah iz nog vaših na svědočstvo jim.
12 I izšli glasiti, aby pokajali se.
13 I izgnali mnogo črtov, i mnogo hvoryh olejem mazali, i uzdravjali.
14 I uslyšal car Herod (bo ime jego bylo razglašeno), i govoril: Joan Krestitelj vstal iz mrtvyh i povodom jego v njem se čudesa okazyvajut.
15 A drugi govorili: To jest Ilija. Drugi ale govorili: On jest prorok, kak jedin iz davnyh prorokov.
16 I čuvši to Herod, rěkl: „Joan, ktorogo jesm kazal obezglaviti, vstal iz mrtvyh.“
17 Herod ibo poslal i kazal pojmati Joana i svezal jego v vezenju poradi Herodjady, ženy Filipa, brata jego, ktoru on za svoju ženu vzel.
18 No Joan govoril Herodu: „Ne dozvoljeno tobě iměti ženy brata tvojego.“
19 A Herodjada srdila se na njego i htěla jego ubiti, no ne mogla.
20 Herod bojal se Joana, věděvši, da on jest muž pravedny i svety. I bral jego v ohranu. A slušajuči jego, mnogo činil i rad byl jego slyšati.
21 I kogdy byl denj po tomu, Herod v dnju rodženja svojego strojil pir Gospodinam i najvysšim ljudam Galileje.
22 I kogdy vošla dočera toj Herodjady i tancevala, i spodobala se Herodu i sědečim s njim. Rěkl car děvkě: „Prosi mene, o čem hčeš, i dam to tobě.“
23 I prisegnul jej: „O čto bys prosila, dam ti, daže polovinu carstva mojego.“
24 No ona izševši, rěkla materi svojej: „O čto imam prositi?“ A ona rěkla: „O glavu Joana Krestitelja.“
25 I kogdy vošla skoro s pospěhom do cara, prosila: „Hču, abys mi dal na talirkě glavu Joana Krestitelja.“
26 I smutil se car. Povodom prisegy i povodom sědečih s njim ne htěl jej odkazati,
27 no poslavši kata, žedal prinesti glavu jego na talirkě.
28 I posěkl jego v vezenju i prinesl glavu jego na talirkě i oddal ju děvkě, a děvka oddala ju materi svojej.
29 Učeniki jego to čuvši prišli i vzeli tělo jego i položili go v grobu.
30 I sobrali se apostole pri Jezusu, pověděli jemu vse, čto činili i čto učili.
31 I rěkl jim: Pojdite osobno na pusto město i odpočnite malo. Ibo mnogo bylo tyh, ktori prihodili i odhodili, i ni času iměli da jedenja. 
32 I vstupivše v čoln, odplyvli na pusto město osobno. 
33 I viděli jih odplyvati, i mnogo priměčali to, i sběgali se tam pěše iz vsakyh měst, a prěduprědžali jih. 
34 I izševši Jezus viděl veliku tolpu i byl milosrdny nad njimi, ibo byli kako ovce ne imajuče pastyra. I počel jih učiti mnogo věčij. 
35 A kogdy už byla pozdna časina, pristupili učeniki Jego, govoreči: Pusto to město jest, a časina už minula. 
36 Odpust jih, daby pošli do blizkyh sel i gradov kupiti sobě jedlo.
37 A odgovorivši, rěkl jim: Dajte jim jesti. I rěkli Mu: My povinni pojdti i kupiti za dvěstě groše hlěby, čtoby jih pokrmiti? 
38 I rěkl jim: Koliko hlěba imate? Idite i obzirajte. A kogdy dověděli se nomera hlěba, pověděli: Pet i dvě ryby.
39 I kazal jim sobrati vsih v grupah na zelenoj travě. 
40 I sěděli po sto i po petdeset. 
41 A vzevši pet hlěbov i dvě rybě, gleděl na nebo, blagoslovil i razdrobil hlěb, i daval učenikam svojim, daby kladli je prěd njimi; i dvě ryby razdělili medžu vsimi. 
42 I jeli vsi, i nasytili se. 
43 I sobrali ostatky, ostatky dvanadset košev polnyh, i ostatky od ryb. 
44 A tyh, ktori jedli, bylo pet tyseč mužev. 
45 I skoro poslal učenikov svojih vstupiti v čoln, daby Jego vzeli za morje do Betsaidy, prěd izslanjem ljuda.
46 I odpustivši jih, odšel na goru moliti se.
47 A kogdy byl večer, byl čoln posrěd morja, a on sam na zemji.
48 I viděvši jih trudivših se pri veslah, (ibo jim byl větr protivny), a okolo četvrtoj straže nočnoj prišel k njim, hodivši po morju, i htěl minuti jih.
49 A oni skoro uzrěli jego hodečego po morju, myslili, da to jest duh, i izkriknuli.
50 Ibo vsi jego viděli i prěstrašili se. A směsta govoril s njimi i rěkl: Ne bojite se.
51 I vstupil do njih v čoln, i prěstal větr. I tym věče sami byli začudženi,
52 ibo ne razuměli o hlěbu: bo srdce jih bylo slěpo.
53 I prěplyvši, prišli do zemji Genezaret i pribyli do brěga.
54 I izševši iz čolna, směsta jego poznali.
55 I sběgavši črěz vsu krajinu, počeli nositi na ložah hvoryh, kogdy uslyšali, da On jest.
56 I kde-nebud prišel do gradov ili do sel, ili do velikyh gradov, kladli hvoryh po ulicah i prosili Go, daby dotknuli toliko čestku oděva Jego: a vsi, ktori Jego dotknuli, zdravi se stali.

## Razděl 7

1 I sobrali se pri Njem Farizeje i něktori od učenyh v Pismo, ktori prišli iz Jeruzalema.
2 A viděvši, čto něktori iz jego učenikov jedli hlěb s nečistymi rukami, to jest neumytymi, napominali.
3 Ibo Farizeje i vsi Židi, jestliby često ruk ne umyvali, ne mogliby jesti povodom prava starših.
4 I po trgu, jestliby se ne umyli, ne mogut jesti. I mnogo sut drugyh věčij, ktore jim do hranjenja sut podane: umyvanja kubkov i džbankov, i posud mědnyh, i lož.
5 I pytali jego Farizeje i učeni v Pismu: Čego tvoji učeniki ne hodet po podanju starših, ale jedut hlěb s nečistymi rukami?
6 A on rěkl jim: Dobro Izaja o vas, liceměrah, glasil, kako jest napisano: Ljud toj čti Mene ustami, no jego srdce jest daleko od mene.
7 No naprazdno Mene čti, učeči nauky i zapovědi člověčske.
8 Ibo odstavite zapověd Božju, držite zakony ljudske: umyvanje džbankov i kubkov i mnogo drugyh věčij tomu podobnyh činite.
9 I govoril jim: Čisto niščite zapovědi Božje, abyste ohranili vaš zakon.
10 Ibo Mojzes rěkl: Čti otca tvojego i matku tvoju: kto klne na otca ili mati, nehaj smrtju umre.
11 A vy govorite: Jestliby člověk rěkl otcu ili materi: Korban (to jest dar), kto-nebud bude od mene, tobě pomočny bude.
12 I ne dopuščate jemu više ničto činiti svojemu otcu ili materi,
13 niščeči slovo Božje črěz zakon vaš, ktory jeste utvrdili; I mnogo onyh věčij tym podobnyh činite.
14 A prizvavši do sebe tolpu, govoril jej: Slušajte Mene vsi, i razumějte.
15 Ne jest věč jedna izvně člověka i vhodeča v njego, ktora by jego mogla činiti nečistym: a věči, ktore izhodet iz člověka, one mogut člověka činiti nečistym.
16 Kto ima uši abyh slyšil, nehaj slyši!
17 A kogdy odšel v dom od tolpy, jego učeniki Jego pytali o tu parabolu.
18 I rěkl jim: Čto vy taki nerazumni jeste? Ne razumějete li, da vse, čto iz vně vhodi v člověka, ne može jego učiniti nečistym.
19 Ibo ne vhodi v srdce jego, ale v tělo ide i črěz naturalny izhod izhodi.
20 I povědal, da to, čto izhodi iz člověka, to nečisti člověka.
21 Ibo izvnutra srdca člověčskogo izhodet mysli zle, blud, kradeži, ubijstva,
22 prěljubstvo, lakomstvo, ložnost, zloumyslnost, zavist, obrazy, vozvyšenost, glupost.
23 Vse to zlo izvnutra izhodi i nečisti člověka.
24 A vstavši odtud, odšel na granicu Tyra i Sidona: a voševši v dom, ne htěl, daby někto o tom věděl. No ukryti se ne mogl.
25 Ibo směsta kako uslyšala o Njem žena, ktoroj dočera iměla duha nečistogo, vošla i upadla pri nogah Jego.
26 Ibo byla žena poganska, rodom Syrofenička. I prosila Go, daby črta izgnal iz dočery jej.
27 On rěkl jej: Daj prvo synam najesti se, ibo ne jest dobro brati hlěb synam, a mětati psom.
28 A ona odgovorila i rěkla Mu: Da, Gospodine, ibo i ščeneta jedut pod stolom krohy synov.
29 I rěkl jej: Povodom togo slova idi, izšel črt iz dočery tvojej.
30 A kogdy odšla do doma svojego, našla ležeču dočeru na ložu a črt izšel.
31 I izšel iz granic Tyra, prišel črěz Sidon k Galilejskomu Morju črěz srědu granic dekapolskyh.
32 I privedli do Njego gluhogo i prosili Jego, daby položil na njego ruku.
33 I vzevši jego od naroda, vložil prsty svoje v uši jego, i pljunuvši, dotknul jezyk jego,
34 i podgledavši na nebo, vozdohnul i rěkl mu: Effetah, to jest: otvori se.
35 I směsta se otvorili uši jego, i razvezali se vezy jezyka jego, i govoril dobro.
36 I kazal jim, daby nikomu ne povědali o tom. Ale čim on više zabranil, tym vyše daleko to razglašali.
37 i tym boljše se divili, govoreči: Dobro vse učinil: i gluhym učinil, daby slyšali, i němym, daby govorili.

## Razděl 8

1 I v ove dni, kogdy byla velika tolpa, i ne iměla čego jesti, prizval učenikov svojih i rěkl jim:
2 žalj mi jest ljudam, ktori už tri dni sut pri Mně, i ne imajut čego jesti,
3 a jestli ja odpušču jih gladnyh do domov jih, oni oslabějut na dragě;, ibo něktori iz njih iz daleka prišli.
4 I odgovorili Mu jego učeniki: Odkud, někto može nakrmiti jih hlěbom tut na pustynji?
5 I pytal jih: Koliko hlěba imate? Oni odgovorili: Sedm.
6 I razkazal tolpě sěděti na zemju. A vzevši sedm hlěbov, blagordaril i lamal i daval učenikam svojim, daby položili je prěd njimi: i položili prěd tolpoju.
7 Iměli tož několiko ryb: i one blagoslovil i razkazal položiti prěd njimi.
8 I jedli, i najedli se, i sobrali, čto ostalo iz ostatkov, sedm košev.
9 A bylo tyh, ktori jedli, okolo četyri tyseči. I odpustil jih.
10 I skoro všel v čoln s učenikami svojimi, prišel v stranu Dalmanuty.
11 I izšli farizeje, i počeli s Njim razgovarjati, hočuče od Njego znamenja s neba, pokušajuči Go.
12 I vozdyhavši v duhu, rěkl: Čemu narod toj znamena probuje najdti? Zapravdu povědam vam, jestli bude dano znamenje narodu tomu.
13 I odpustivši jih, všel do čolna i odplyvl za morje.
14 I zabezpametili vzeti hlěba i ne iměli s soboju, jedino jedin hlěb v čolnu.
15 I kazal jim: Gledajte i hranite se kvasa farizejskogo i kvasa herodovogo.
16 I dumali jedin k drugomu, govoreči: Tak jest, ibo ne imajemo hlěba.
17 To poznavši, rěkl jim Jezus: Čto myslite, da hlěba ne imate? Ješče li ne vidite ni razuměte? Ješče li imate srdce vaše slěpo?
18 Oči imajuči, ne vidite i uši imajuči, ne slyšite? Ni pametajete,
19 kogdy pet hlěbov lamal na pet tyseč, koliko jeste odnesli košev polnyh ostatkov? Rěkli mu: Dvanadset.
20 A kogdy sedm hlěbov na četyri tyčuči, koliko jeste košev sobrali ostatkov? I rěkli mu: Sedm.
21 I govoril jim: Kako ješče ne razuměte?
22 I prišli do Betsajdy i privedli Mu slěpogo, i prosili, aby jego dotknul.
23 A vzel slěpogo za ruku, izvedl jego za selo, a pljuvavši na oči jego, položil ruky svoje I pytal jego, jestliby něčto viděl.
24 A on gleděl i govoril: Vidim ljudij, ktori kak drěva hodet.
25 Potom snova položil ruky na oči jego i počel viděti, i byl uzdravljen, tako da viděl vse jasno.
26 I odslal jego do domu jego, govoreči: Idi do domu svojego, a jestli vojdeš do sela, nikomu ne povědaj.
27 I izšel Jezus i učeni Jego do sela Kesarije Filipa; a na dragě pytal učenikov svojih, govoreči jim: Za kogo Mene imajut ljudji?
28 Něktori mu odgovorili, govoreči: Joanom Krstiteljem, drugi Ilijeju, a drugi za jedina iz prorokov.
29 Togdy jim rěkl: A vy, za kogo vy Mene imate? A odgovoril Petr: Ty jesi Hristos!
30 I zabranil jim, aby o Njem nikomu ne povědali.
31 I počel jih učiti, da syn čelověči mnogo trpěti bude i, da i odkydnuty bude od starějših i od glavnyh kaplanov, i od učenyh v Pismo, i ubity. A po treh dnjah vozkresne.
32 I govoril už netajno te slova. I vzevši Jego Petr, počel jego napominati.
33 A on obrativši se, i uzrěvši učenikov svojih, napominal Petra, govoreči: Idi za mnoju, djable, ibo ne razuměš, čto jest božje, a čto jest ljudsko.
34 I prizvavši tolpu i učenikov svojih, rěkl: Jestli kto hče za mnoju idti, nehaj samogo sebe se odrěče i vozme križ svoj i nehaj mene naslěduje.
35 Ibo kto by htěl hraniti dušu svoju, izgubi ju, a kto by izgubil dušu svoju za mene i Evangelje, shrani jego.
36 Ibo čto pomože člověku, kakby ves svět iziskal, jestli škodu by prijel na duši svojej?
37 Ale čto zaplati člověk za dušu svoju?
38 Ibo, kto by se zasramil mene i slov mojih prěd narodom tym prěljubnym i grěšnym, togo budo zasramiti se syn člověčsky, kogda prijde v slavě otca svojego s angelami svetymi.

## Razděl 9

1 I po šest dnjah vzel Jezus Petra i Jakoba, i Joana, i izvedl jih osobno na vysoku goru, i prěměnil se prěd njimi.
2 I Jego odědžy staly se tako světle i velmi běle kako sněg. Tako běle, kako ni jedin na zemji běliti može.
3 I ukazal se Ilija s Mojzesom, i govorili s Jezusom.
4 I Petr rěkl k Jezusu: Rabbi, dobro nam jest tut byti; učinimo tri šatri: Tobě jedno, a Mojzesu jedno, a Iliji jedno.
5 Ne věděl, čto govoril, ibo byli zastrašeni.
6 I javil se oblak, ktory jih zaslonil, i prišel iz oblaka glas, govoreči: To jest Syn moj ljubjeny, slušajte jego.
7 I směsta obzirajuči se, nikogo više ne viděli, jedino Jezusa samogo.
8 I kogdy shodili iz gory, kazal jim, daby nikomu ne povědali, čto viděli, až Syn Člověčsky ne vstane iz mrtvyh.
9 I shranili to slovo u sebe, pytajuči se medžu soboju, čto to jest: vstati iz mrtvyh.
10 I pytali Jego: Čemu farizeje i učeni v Pismu povědajut, da trěba, daby najprvo prišel Ilija?
11 On odgovoril jim: Ilija prijde najprvo i napravi vse; a kako jest napisano o Synu Člověčskom, daby mnogo trpěl i prězirany byl.
12 Ale vam povědam, da Ilija prišel. Učinili jemu, čto htěli, tako, kako jest napisano o njem.
13 I kogdy prišel do svojih učenikov, viděl mnogu tolpu okolo njih, i učenyh v Pismu govorečih s njimi.
14 I směsta vsi ljudi, viděvši Jezusa, divili se i prěstrašili se. Priběgali, aby Go vitati.
15 I pytal jih: O čem govorite medžu soboju?
16 I odgovoril jedin iz tolpy i rěkl: Učitelju, jesm privedl Tobě syna mojego, ktory ima němy duh.
17 I kdekoli jego napadne, trese jego, i sliny tekut, i skripi zubami, i stane se negybky. Jesm govoril tvojim učenikam, daby jego izgnali, no ne mogli.
18 On odgovoril jim: O narode nevěrny, kak dolgo pri vas budu? Kak dolgo vas trpěti budu? Privedite jego do Mně.
19 I privedli jego do Njego. I kak toliko jego uzrěl, duh počel go tresti, i padši na zemju, valjal se i sliny tekli.
20 I spytal otca jego: Kogdy se to jemu stalo? On rěkl: Od dětinstva.
21 I često jego metal v ogonj i vodu, daby jego ubil; no jestli možeš, pomoži nam, pomiluj se nad nami.
22 Jezus rěkl jemu: Jestli možeš věriti. Vse jest možno věrečemu.
23 I směsta kriknul otec děteta, so solzami rěkl: Věrju, Gospodine! Pomoži mojemu nevěrju.
24 Jezus viděvši, da se tolpa sbirala, grozil nečistomu duhu, rěkl jemu: Němy i gluhy duhu, ja tobě kažu, izojdi iz njego i ne vhodi više v njego.
25 I kriknul, silno go potresl, izšel iz njego, i stal se kako mrtvy, tako že mnogi govorili, da umrl.
26 Jezus vzel jego ruku, voznesl jego, i vstal.
27 I kak všel v dom, Jego učeniki spytali Go: Čemu my jego izgnati ne mogli?
28 I rěkl jim: Toj narod inako ne može izojdti. Jedino črěz molitvu i post.
29 Izšli odtud, prěšli črěz Galileju, i ne htěl, daby kto věděl.
30 Ibo učil svojih učenikov i govoril jim: Syn člověčji bude izdan v ljudske ruky i ubijut jego, i ubity vstane tretjego dnja.
31 No oni slova ne razuměli, a bojali se Go pytati.
32 I prišli do Kapernauma. Kogda byli v domu, pytal jih: O čem jeste na dragě govorili?
33 No oni molčali, ibo na dragě medžu soboju se sporili, kto iz njih byl največši.
34 I usědl, prizval dvanadset i rěkl jim: Jestli někto hče byti prvym, nehaj bude poslědnjim iz vsih i slugoju vsih.
35 I vzevši děte, postavil je posrěd njih, i objevši je, rěkl jim:
36 Kto prijme jedno take děte v ime moje, mene prijme, a kto mene prijme, ne mene prijme, ale Ovogo, ktory Mene poslal.
37 Odgovoril Mu Joan: Učitelju, jesmo viděli něktorogo, ktory v ime tvoje črty izkydnul. Ne hodil s nami, to jesmo mu zabranili.
38 A Jezus rěkl: Ne zabranjajte jemu. Ibo nikto ne jest, ktory by tvoril čuda v ime Moje, a moglby skoro zle govoriti o Mně.
39 Ibo, kto ne jest protiv vam, za vami jest.
40 Ibo, kto by vam dal čašku vody do pitja v ime moje, zato že jeste od Hristosa, istinno povědam vam, ne izgubi svojej nagrody.
41 A kto jest povodom grěha jedinogo iz tyh malyh, věrečih v Mene. Jemu lěpje bylo, daby byl privezany mlynsky kamen okolo šije jego i byl kydnuty v morje.
42 A jestli ruka tvoja jest povodom grěha tvojego, odsěkni ju: lěpje jest tobě vojdti do života věčnogo sěkanym, než imajuči obě ruky, idti do pekla v ogonj neugasimy,
43 kde črvjak jih ne umiraje, a ogonj ne gasne.
44 A jestli noga tvoja jest povodom grěha tvojego, odsěkni ju: lěpje jest tobě vojdti hromym do věčnogo života, než imajuči obě nogy, byti kydnutym do pekla ognja neugasimogo,
45 kde črvjak jih ne umiraje, a ogonj ne gasne.
46 I jestli tvoje oko jest povodom grěha tvojego, izbavi se jego: lěpje jest tobě vojdti jednookym do kraljevstva Božjego, než imajuči oba oči, kydnutym byti do ognjenogo pekla,
47 kde črvjak jih ne umiraje, a ogonj ne gasne.
48 Ibo každy ognjem bude posoljeny, i každa žrtva bude solju posoljena.
49 Dobra jest sol, ale jestli sol svoj vkus izgubi, čim že ju popravite? Imajte v sobě sok, i mir imajte medžu soboju.

## Razděl 10

1 I vstajuči odtud, prišel na granice židovskoj zemje za Jordanom, i šli do Njego tolpy, i učil jih snova, kak byl Jego obyčaj.
2 I pristupivše farizeje, pytali jego: Či godi se mužu pustiti ženu? Pokušajuči Go.
3 On odgovoril: Čto vam razkazal Mojzes?
4 Oni rěkli: Mojzes dopustil napisati list razvodny i opustiti.
5 Odgovoril jim Jezus: Radi tvrdosti vašego srdca napisal vam tu zapověd.
6 No od početka stvorjenja kako muža i ženu učinil jih Bog.
7 Zatom ostavi muž otca svojego i mati svoju, i priluči se k ženě svojej,
8 i budut dva v jednom tělu. I tako už ne sut dva, no jedno tělo.
9 Čto Bog sjedinil, čelověk nehaj ne odključi.
10 I v domu snova učeniki Go o tom pytali.
11 I rěkl jim: Kto by pustil ženu svoju, i bral inu, čini prěljubstvo protiv njej.
12 I jestli by žena ostavila muža svojego, i šlaby za drugogo, čini prěljubstvo.
13 I prinosili do Njego děti, daby jih dotknul. A učeniki grozili prinositeljam.
14 Videči to Jezus, iměl za zlo, i rěkl jim: Pustite dětam idti do Mene, i ne zabranjajte jim, ibo takovo jest carstvo božje.
15 Istinno kažu vam: Kto by ne prijel carstvo božje kak děte, ne vojde do njego.
16 I obimajuči jih, i kladuči na nje ruky, blagoslovil je.
17 A kogda on izšel v put, priběgl jedin, upadavši na kolěna prěd Njim, pytal Jego: „Učitelju dobry. čto imam učiniti, dabyh prijel věčny život?“
18 A Jezus jemu rěkl: „Čemu nazyvaješ me dobrym? Nikto ne jest dobry, jedino Bog.
19 Zapovědi znaješ: Ne čini prěljubstva, ne ubijaj, ne kradi, ne lži, ne obmanuj, počitaj otca svojego i mati.“
20 A on odgovoril Mu: „Učitelju, jesm vsego togo držal se od svojej mladosti.“
21 A Jezus, pogledavši na njego s milostju i rěkl jemu: „Idi, čtokoli imaš, prodaj i razdaj ubogym, i budeš iměti se blago na nebesah. Prijdi, naslěduj me.“
22 S žalostju poslušavši slova, odšel smutny, ibo iměl mnogo iměnja.
23 A Jezus obozrěvši se, rěkl svojim učenikam: „Kako težko jest tym, ktori imajut monety, dojdti do kraljevstva Božjego!“
24 A učeniki se začudili Jego slovami. No Jezus rěkl jim: „Děti, kako trudno jest tym, ktori v monety dověrjajut, dojdti do kraljevstva Božjego.
25 Legše jest velbludu projdti črěz uho igly, než bogatomu vojdti do kraljevstva Božjego.“
26 Oni tym věče se divili, govoreči sami k sobě: „I kto može byti spaseny?“
27 A Jezus pogledavši na njih, rěkl: „U Boga vse jest možno.“
28 I počel jemu Petr govoriti: „Gledaj, my vse ostavili i pošli za Toboju.“
29 A Jezus odgovoril: „Istinno, vam povědam: nikto ne jest, ktory by ostavil dom ili brata, ili sestry, ili otca, ili matere, ili dětij, ili polja povodom Mene i povodom Evangelij,
30 daby ne prijel stokratno. Tutčas bude domy i brati, i sestry, i materi, i děti, i polja prijeti podčas prěslědovanja i v idučem věku věčnogo života.“
31 I mnogo prvyh bude poslědnjimi, a poslědnji prvymi.
32 I byli na dragě, vstupajuči do Jeruzalema. A Jezus šel prěd njimi i čudili se, a učeniki bojali se. I sobral se s Dvanadset, počel jim povědati, čto imělo na Njego prijdti.
33 I vstupajemo do Jeruzalema, i Syn člověčski bude izdan glavnym kaplanam i učenym v Pismu i osudet Go na smrt, i izdadut poganam;
34 i budut se iz Njego smějati, i budut na Njego pljuvati, i bičujut Go, i ubijut Go, a tretjego dnja vozkresne.
35 I prišli do Njego Jakob i Joan, syni Zevedeja, govoreči: Učitelju, hčemo, abys učinil nam, o čto prosimo.
36 A On jim rěkl: Čto hčete, abyh vam učinil?
37 I rěkli: Daj nam, abyhmo sěděli jedin po pravici tvojej, a drugi po lěvici tvojej v slavě tvojej.
38 A Jezus jim rěkl: Ne znate, o čto prosite. Možete piti čašu, ktoru ja piju? Ili byti kreščeni krestom, ktorym ja krešču?
39 A oni mu odgovorili: Možemo. A Jezus jim rěkl: Čašu, ktory ja piju, piti budete, i krestom, ktorym se ja krešču, kreščeni budete,
40 ale sěděti po pravici mojej ili po lěvici ne jest mi dano vam dati, ale ktorym jest povinno.
41 A ti deset, počeli se gněvati na Jakoba i Joana.
42 A Jezus, prizvavši jih, pověděl jim: «Znate, že ti, ktori se uvažajut za vladcev narodov, prěslědujut svoji narody, a nad njim naduživajut svoju vladu.
43 Ale ne tako jest medžu vami, ale ktokoli by htěl byti velikym,, budet slugoju vašim,
44 a ktokoli medžu vami htěl byti prvym, budet vsih slugoju.
45 Ibo Syn člověčsky ne prišel, aby Jemu služili, ale aby služil i dal dušu svoju na izkup za mnogo ljudij.
46 I prišli do Jeriha. I kogda on izhodil iz Jeriha s Jego učenikami i s tolpoju velikoju, syn Timej, slěpy Bartolomej, sěděl podle dragy, kako prosak.
47 Čto uslyšavši, da jest Jezus Nazaretsky, počel kriknuti i govoriti: Jezuse, synu Davida, pomiluj se nad mnoju!
48 I mnogo jemu grozili, da by molčal. A on dalje više glasno kriknuti: Synu Davida, pomiluj se nad mnoju!
49 A Jezus stanuvši, kazal jego prizvati. I prizvali slěpogo, govoreči jemu: Bud dobroj mysli, vstani, On zove tebe.
50 Izkydnul suknju svoju, vskočil i prišel do Njego.
51 I Jezus pytal jego: Čto hčeš, dabyh učinil? A slěpy rěkl jemu: Učitelju, dabyh viděl.
52 A Jezus rěkl jemu: Idi, věra tvoja te uzdravila. I směsta viděl i šel za Njim po dragě.

## Razděl 11

1 I kogdy byli blizko Jerusalemu i Betaniji, pri Olivovoj Gorě, poslal dvoh iz svojih učenikov
2 i rěkl jim: Idite do sela, ktoro jest prěd vami, a kogdy vojdete do sela najdete nedaleko osla privezanogo, na ktorom nikto ješče ne sěděl. Odvežite jego i privedite tut!.
3 I jestli by vam kto rěkl: Čto činite? Povědajte, da jego Gospod potrěbuje, a směsta jego tu pusti.
4 I ševši, našli osla privezanogo do dverij na ulici i odvezali go.
5 I někto iz tyh, ktori tam stojali, govoril jim: Čto činite, odvezuči osla?
6 Jim rěkli, kako jim prikazal Jezus, i pustili jih.
7 I privedli osla do Jezusa, i položili na njego svoje suknja, i On usědl na njego.
8 I mnogo jih klalo svoje odědžy na dragu, drugi rězali větky od drěv i klali na dragu.
9 I ti, ktori prěd njimi i za njimi šli, kriknuli: Hosanna! Blagosloven, ktory ide v ime Gospodina.
10 Blagoslovjeno kraljevstvo otca našego Davida, ktoro prihodi. Hosanna na vysokostjah!
11 I všel v Jeruzalem do synagogy, i obgleděl vse, kogdy už večerna časina byla, izšel do Betanije s dvanadsetju.
12 I zautra, kogdy izšli iz Betanije, on byl gladny.
13 I viděl iz daleka figu imajuča listy, prišel, aby se dověděti, či by mogl něčto na njej najdti. I prišel do njej, ničego ne našel než listy, ibo ne byl čas na figy.
14 I odgovarjajuči, rěkl jej: Da nikto nikogdy ne je od tebe plodov. I slyšali učeniki jego.
15 I prišli do Jeruzalema. I všel v synagogu, počel izganjati tyh, ktori prodavali i kupovali v synagogu. I provrgnul stoly izměnjenja pěnezy i lavky tyh, ktori prodavali golubov,
16 i ne dopustil, daby nesl někto něčto črěz synagogu.
17 I učil jih i govoril jim: Či ne jest pisano, da moj dom jest dom molitvy za vsih narodov? A jeste učinili jego jamoju razbojnikov.
18 Uslyšavši to, glavni kaplany i učeni v Pismu iskali, kako by Jego ubiti. Ibo se Go bojali, kako vsa tolpa imponovala Jego učenje.
19 A večerom izhodil iz grada.
20 A rano, iduči mimo, viděli drěvo figovo usyhalo od koreni.
21 I Petr pripomněl sobě, rěkl Jemu: Rabbi, gledaj, drěvo figovo, ktoro jesi  proklel, izsohnulo.
22 A Jezus odgovoril jim: Imějte věru v Boga.
23 Pravdu vam govorju, da kto by rěkl toj gorě: Voznesi se i kydni se v morje, i ne sumněvalby v svojim srdcu, ale věrilby, da se to stane. Tomu by se to stalo.
24 Zato vam povědam: Vse, o čem v molitvě prosite, věrite, že prijmete, i stane se vam.
25 I kogdy stanete moliti se, odpuščajte, jestli imate něčto protiv něktoromu, daby i vaš otec, ktory jest na nebesah, odpuščal vam vaše grěhy.
26 Ale jestli vy ne odpuščajte, ni vaš otec, ktory jest v nebu, ne odpusti vam vaše grěhy.
27 I prišli nazad do Jeruzalema. I kogdy hodili po synagogě, prišli do Njego glavni kaplany i učeni v Pismu, i starši,
28 i rěkli Mu: Kakoju močju to činiš? I kto ti dal tu vlast, dabys to činil?
29 A Jezus odgovoril jim: Spytam i ja vas o jedno slovo, a odgovorite Mi, i pověm vam, kakoju močju to činju.
30 Kreščenje Joana bylo od neba či od ljudij? Odgovorite Mi.
31 I oni razmysljali, govoreči: Jestli pověmo: Od neba. To odgovori: čemu jeste jemu ne uvěrili?
32 Jestli rěčemo: Od ljudij, bojimo se naroda, bo vsi držali se Joana i iměli go istinno za proroka.
33 A odgovorili Jezusu: Ne znajemo. A Jezus odgovoril jim: To Ja vam tož ne pověm, kakoju močju to činju.

## Razděl 12

1 I načel jim govoriti v parabolah: Člověk zasadil vinograd i ogradil valom, i izkopal presu i postavil věžu, i oddal jego oračam, i izjehal.
2 I pozdněje poslal slugu k oračam, daby od oračev vzel od ploda vinograda.
3 Oni shvatili jego i ubili, i odslali prazdnym.
4 I snova poslal drugogo slugu k njim; i ovogo ranili v glavu i obezčestili.
5 I snova poslal drugogo, i ovogo ubili, i mnogyh drugyh, jednyh bili, a drugyh ubili.
6 Ješče jednogo syna iměl, ljubimogo; i poslal jego poslědnjego k njim, rěkl: Považet syna mojego.
7 Orači rěkli jedin k drugomu: To jest naslědnik: Idite, ubijmo jego, i naše bude naslědstvo.
8 I shvativše jego, ubili i izkydnuli iz vinograda.
9 Čto učini gospodin vinograda? Ide I ubije oračev, i da vinograd inym.
10 Ale jeste ne čitali Pisma: Kamen, ktory odkydnuli budovniki, stal se narožnym kamenem.
11 Od Gospodina stal se to, i jest divnym v očah naših?
12 I iskali Jego shvatiti, i bojali se naroda, ibo poznali, čto o njih tu parabolu pověděl; i ostavivše Jego, pošli.
13 I poslali k Njemu něktoryh iz Farisejev i Herodijanov, daby jego shvatili v slovesi.
14 Oni prišli i rěkli Jemu: Učitelju, věmo, da jesi istinny, i ne dbaš o něktorom, ibo ne glediš na osobu, no istino puti Božjej učiš. Či možno li davati danok Cezaru ili ne?
15 On znal hytrost jih, rěkl jim: Čemu mene pokušajete? Prinesite mi groš, dabyh viděl.
16 I donesli Jemu. I rěkl jim: Čij jest obraz i napis? Rěkli Mu: Cesara.
17 I odgovorivši Jezus, rěkl jim: Oddajte cesaru, čto cesara, a čto božje dajte Bogu. I začudili se.
18 I prišli do Njego Saduceje, ktori povědajut, da ne jest vozkrešenja. I pytali Go, govoreče:
19 Učitelju, Mojzes nam napisal, da jestli brat umre i ostavi ženu, a děti by ne ostavil, daby vzel brat jego ženu i dělal děte bratu svojemu.
20 Bylo togdy sedm bratov. I prvy iměl ženu i umrl, ne ostavivši děta.
21 I vzel ju vtory, i umrl, i ni toj ostavil děta, i tretji takože.
22 I vzeli ju takože sedm, a ne ostavili děta. Poslědnje po vsih umrla i žena.
23 V vozkrešenju togdy, kogdy vstanut, čija iz tyh bude žena? Ibo sedm jih iměli ju za ženu.
24 A Jezus odgovorivši, rěkl jim: Či ne za togo bludite, da ne razumějete Pisma ni moči Božjej?
25 Ibo kogda vozkresnut, ni se ženiti budut, ni za muž hoditi, ale sut kako angeli v nebesah.
26 A o mrtvyh, da vozkresnuti imajut, jeste ne čitali v knigah Mojzesa, kako u kusta govoril Bog jemu: Ja jesm Bog Abrahama, Bog Isaaka i Bog Jakoba.
27 Ne jest On Bog mrtvyh, a živyh. Vy velmi bludite.
28 I pristupil jedin iz učenyh v Pismu, ktory slyšal, kako diskutovali medžu soboju, a videči, da jim dobro odgovoril, pytal Jego, ktoro jest važnějša iz vsih zapovědij?
29 A Jezus mu odgovoril: Slušaj, Izraelju, Gospodin Bog tvoj, Bog jest jedin:
30 a budeš ljubiti Gospodina Boga tvojego iz vsego srdca tvojego i iz vsej duše tvojej, i iz vsego umysla tvojego, i iz vsej sily tvojej. To jest prva zapověd.
31 Druga jest tomu podobna: Ljubi bližnjego svojego kako samogo sebe. Nad to ne imaješ inoj večšej zapovědi.
32 I rěkl Jemu učeny v Pismo: Dobro, Učitelju, v pravdě jesi pověděl, da jedin jest Bog, i ne imaješ inogo kromě Jego.
33 I čtoby byl ljubljeny iz vsego srdca i iz vsego uma, i iz vsej duše, i iz vsej sily, i ljubiti bližnjego kako samogo sebe jest věče nad vsimi paljenjami těl I žrtvami.
34 A viděvši Jezus, da razumno odgovoril, rěkl jemu: Nedaleko jesi od kraljevstva Božjego. I ne směl Jego už nikto pytati.
35 A Jezus odgovorivši govoril, naučeči v synagogě: Kako govoret učeni v Pismu, da Hristos jest syn Davida?
36 Ibo sam David govori v Duhu Svetom: Rěkl Gospod Gospodu mojemu, sědi po pravici mojej, až položu neprijateljev tvojih pod nogy tvoje.
37 Sam David zove jego Gospodinom: a odkud jest syn jego? A velika tolpa byla rada jego slušati.
38 I govoril jim v naukě svojej: Strěžite se učenyh v Pismu, ktori hčut hoditi v dolgyh odježdžah i byti pozdravljeni na trgovišču,
39 i sěděti na prvyh krěslah v synagogah i čestnyh městah v gostiljnji;
40 Objedajut domy vdov i za pozor opravjajut dolge molitvy. Do njih prijde veliky sud.
41 A sěděl Jezus protiv skarbony, prěgleděl se, kako tolpa kydnula pěnezy do skarbony: a mnogo bogatyh mnogo kydnulo.
42 A priševši jedina vdova uboga, vložila dva drobne pěnezy.
43 A prizval učenikov svojih, rěkl jim: Zapravdu povědam vam, da ta uboga vdova věče vložila než vsi ini, ktori kladli do skarbony.
44 Ibo vsi iz togo, čto jim bylo dostatočno, metali, a ta iz nedostatka svojego vse, čto iměla, kydnula, cělu iměnje svoje.

## Razděl 13

1 I kogda on izhodil iz synagogy, rěkl Jemu jedin iz Jego učenikov: „Učitelju, gledaj, kake kamene i kake budovanje!“
2 I Jezus odgovarjajuči rěkl jemu: „Či vidiš vse to veliko budovanje? Ne ostane kamen na kamenju, ktory by ne byl razvaljeny.“
3 I kogda sěděl na Olivnoj Gorě naprotiv synagogy, pytali Go Petr i Jakob, i Joan, i Andrej:
4 „Povědaj nam, kogda se to stane? I kaky znak bude, kogda se to vse počne?“
5 I Jezus, odgovorivši, počel jim govoriti: „Strěžite se, da by vas nikto ne obmanul.
6 Ino mnogo jih prijde v mojem imenu, povědajuči: ‚Ja jesm,‘ i mnogo jih obmanut.
7 I kogda uslyšite vojny i věsti o vojnah, ne bojite se. Ibo to se stati musi, ale to ješče ne konec.
8 Ibo povstane narod protiv narodu i kraljevstvo protiv kraljevstvu. I budut  tresenja zemje i glady. To jest početok hvoroby.
9 A vy imějte se sami na pozornosti. Ibo vas izdadut do sudov i v synagogah vas biti budut a prěd naměstnikami i prěd kraljami za Mene stati budete, jim na svědočstvo.
10 A trěba, aby prvo u vsih narodov byla glaseno Evangelje.
11 I kogdy vas voditi budut, izdavajuči, ne myslite prědtym, čto byste govoriti iměli, ale čto vam bude dano ovoj časině, to govorite. Ibo ne vy jeste, kto govori, a Svety Duh.
12 I izda brat brata na smrt, a otec syna: i povstanut syni protiv roditeljam, i budut jih ubivati.
13 I budete u vih v nenavisti za moje ime. No kto potrva do konca, toj bude izbavjeny.
14 A kogdy uzrite mrzkost opustošenja, izstupajuča tam, kde ne povinna byti. Kto to čita, nehaj razuměje, togdy ti, ktori sut v Judejskoj zemji, nehaj utěkajut na gory;
15 a kto bude na strěhě, nehaj ne shodi do domu ni vhodi, aby iměl něčto vzeti iz svojego domu;"
16 i kto bude na polju, nehaj ne vrati se nazad vzeti odědžu svoju.
17 Gorje brěmennym i krmečim v ove dni.
18 Molite se, da ne bude zimy.
19 Bo ove dni budut take katastrofy, kako ne byli od početka tvorjenja, ktore stvoril Bog, ni snova budut.
20 I jestliby ne skratil Gospodin dnev, nikake by tělo ne bylo shranjeno, ale radi izbranyh, ktore izbral, skratil dni.
21 I togda jestliby vam kto rěkl: „Gledaj, tut jest Hristos, gledaj, tam“: ne věrite.
22 Ibo vstanut falšivi Hristosy i falšivi proroky i budut tvoriti znamena i čudesa do izvedenja v blud. Jestli možno ješče izbranyh.
23 Vy zatom uvažajte, jesm vam vse prědpověděl.
24 No v ove dni po katastrofě ovoj, zatemni se solnce i měsec ne da jasnosti svojej.
25 I zvězdy nebeske padati budut, a sily, ktore sut na nebesah, porušet se.
26 I togda uzret Syna člověčskogo prihodečego v oblakah s velikoju siloju i slavoju.
27 I togda pošlje On Angelov svojih i sbere izbranyh svojih iz četyrěh větrov, od kraja zemje až do vrha neba.
28 Od drěva figova učite se črěz parabolu. Kogdy se uže větka jej nabiraje sokov i izpusti listje, poznajete, da blizko jest lěto:
29 takože i vy, kogdy uzrite, da to se děti bude, vědte, da uže blizko jest, v dverah.
30 Zapravdu vam govorju, da ne propade rod toj, až se to vse stane.
31 Nebo i zemja propadut, ale slova moje ne propadut.
32 O dnju ovom abo o časině nikto ne zna, ni angele nebeski, ni Syn, jedino Otec.
33 Uvažajte, čuvajte i molite se, ibo ne znate, kogdy čas bude.
34 Kako člověk, ktory odšel, ostavil dom svoj i dal slugam svojim vladu nad každoju rabotoju svojeju i vratniku prikazal, daby čuval.
35 čuvajte (ibo ne znate, kogdy gospodin do doma prijde: večerom abo v polnoči, abo kogda kokoty pěvajut, abo rano),
36 daby jestli směsta prijde, ne našel vas spavših.
37 A čto vam govorju, vsim govorju: čuvajte.

## Razděl 14

1 I byli Pasha i Sveto Mac po dvoh dnjah. I iskali vysši kaplani i učeni v Pismu, kako by Jego hytro pojmali i ubili.
2 Ibo govorili: Ne v sveto, daby ne bylo razdora v ljudu.
3 A kogdy byl v Betaniji v domu Simona Leprovatogo i sěděl u stola, prišla žena, imajuči alabastrovy flakonči masla pravdivogo dragogo, a razbivši flakončik, izlila go na glavu Jego.
4 I byli něktori, ktori se gněvali sami v sobě a govorili: čemu se stala ta utrata masla?
5 Ibo moglo se to maslo prodati dražeje než za trista monet i razdati ubogym. I gněvali se na nju.
6 A Jezus rěkl: Dajte jej mir. Čemu jej smutok činite? Dobro dělo za Mene učinila.
7 Ibo vsegda ubogyh imate so soboju: i kogdy budete htěti, možete jim dobro činiti, no Mene ne vsegda imate.
8 Ona, čto mogla, učinila: prěd časom namazala tělo Moje na pogreb.
9 Pravdu povědam vam: kdekoli glaseno bude Evangelije po vsem světu, to, čto ona učinila, povědati budut na pamet jej.
10 A Judas Iskariotsky, jedin iz dvanadseti, odšel do vysših kaplanov, daby Jego jim izdal.
11 To uslyšavši, razradovali se i oběčali mu dati pěnez. I iskal, kako by Jego v ugodny čas izdal.
12 I v prvy denj Sveta Mac, kogdy Pashu požrtvovali, rěkli mu učeniki: Kde hčeš, abyhmo pošli prigotoviti, dabys mogl jesti Pashu?
13 I poslal dvoh iz svojih učenikov, i rěkl jim: Idite do grada, i strětete se s vami člověk, nesuči džban vody. Idite za njim,
14 a kdekoli vojde, povědte gospodaru, da Učitelj pyta: kde jest Moja izba, v ktoroj byh mogl jesti Pashu s učenikami mojimi?
15 A on vam pokaže veliku salu, udobnu i gotovu, i tam prigotovite nam.
16 I odšli Jego učeniki i prišli do grada i našli salu, kak jim pověděl, i prigotovili Pashu.
17 A kogdy byl večer, prišel s dvanadsetoma.
18 I kogda sěděli i jedli, rěkl Jezus: Istinno povědam vam, da jedin iz vas, ktory je s Mnoju, Mene izda.
19 A oni počeli se smutiti i jedin drugogo pytati: Či li ja?
20 Jim rěkl: Jedin iz dvanadset, ktory s Mnoju pogruzi ruku v miskě.
21 Syn Člověčsky ide, kako o Njem jest napisano, a běda tomu člověku bude, črěz kogo syn člověčsky bude izdan; lěpše by Mu bylo, by se toj člověk ne narodil.
22 A kogdy oni jedli, vzel Jezus hlěb i blagoslovivši, lamal i dal jim, i rěkl: Imějte, to jest tělo Moje.
23 A vzevši čašu, kažuči blagodarjenje, dal jim i pili iz njego vsi.
24 I rěkl jim: To jest krov moja novogo testamenta, ktora za mnogyh bude izlita.
25 Istinno povědam vam, da už ne budu piti iz ploda vinovogo kusta do ovogo dnja, kogdy go piti budu novy v kraljevstvu Božjem.
26 A himn pěval, izšli na Olivnu Goru.
27 I rěkl jim Jezus: Udarju pastyra, a odvračajut se ovce.
28 Ale kogdy vozkresnu, pojdu prěd vami do Galileje.
29 A Petr Mu rěkl: Nehaj vsi sumněvali, ale ja ne.
30 I rěkl jemu Jezus: Istinno povědam ti, da ty tutdenj, v toj noči, dopoka kokot ne dvukratno zapěje, trikratno se Mene odrěčeš.
31 No on ješče govoril: Hotby bylo trěba i umrti mi s Toboju, ne odrěku se Tebe. Tak tož i vsi govorili.
32 I prišli do sela, ktoromu jest ime Getsemani, i rěkl učenikam svojim: Sědite tu, až se pomolju.
33 I vzel so soboju Petra i Jakoba, i Joana, i počel strah iměti i tresti se.
34 I rěkl jim: Smutna jest duša moja až do smrti, ostanite tu, i čuvajte.
35 I odševši nedaleko, padl na zemju. I molil se, by, jestli možno bylo, Go obšla ta časina.
36 I govoril: Abba, Otče, vse Tobě jest možno, zaberi od mně toj čaši! Ale nehaj ne to, čto Ja hču, ale čto Ty hčeš se stane.
37 I prišel, i našel jih, kak spali, i rěkl Petru: Simone, spiš? Jeste ne mogli čuvati jedinu časinu?
38 čuvajte i molite se, dabyste ne poddali se pokušenju. Duh v pravdě gotovy, ale tělo slabo.
39 I snova odševši, molil se, povtarjajuči te same slova.
40 A vrativši se, našel jih snova spavših (ibo oči jih byly snom umirjene), a ne věděli, čto Mu odgovoriti.
41 I prišel tretji raz i rěkl jim: Spite li i odpočivajte. Dostatočno. Prišel čas: Bude izdan Syn člověčsky v ruky grěšnikov.
42 Vstanite, idemo: toj, ktory Mene izda, blizko jest.
43 A kogdy ješče govoril, prišel Judas Iskariotsky, jedin iz dvanadset, a s njim velika tolpa s mečami i s kyjami, od najvysših kaplanov i učenyh v Pismu i starših.
44 A dal jim znak toj, ktory Go izda, govoreči: Kogokoli pocěluju, to jest On, hvatajte Go, a provodite ostražno.
45 A priševši, směsta pristupivši k Njemu, rěkl: Bud pozdravjeny, Učitelju. I pocěloval Go.
46 I oni shvatili Go rukami i pojmali Go.
47 I jedin něktory iz tyh, ktori tam stali, iztegnul meč, udaril slugu najvysšego kaplana i odsěkl mu uho.
48 A Jezus, rěkl jim: Kako na razbojnika jeste izšli s mečami i s kyjami pojmati Mene?
49 V každom dnju jesm byl u vas v synagogah, učil, a jeste ne pojmali Mene. Ale imajut se izpolniti Pisma.
50 Togdy učeniki vsi utekli.
51 A něktory mladenec šel za Njim oblěčeny prostrinoju na golom tělu, i pojmali jego.
52 A on ostavivši prostrinu, nago utekl od njih.
53 I privedli Jezusa do najvysšego kaplana. Sobrali se vsi kaplany i učeni v Pismu, i starši.
54 A Petr za Njim šel iz daleka až vnutri do dvora najvysšego kaplana i sěděl so slugami u ognja i grěl se.
55 Najvysši kaplany i cěla rada iskali protiv Jezusu svědočstva, daby jego na smrt sudili, a ne našli.
56 Ibo mnogo jih protiv Njego falšivo svědčili, a svědočstva soglasne ne byli.
57 A něktori, povstavše, falšivo svědčili protiv Njego, govoreči:
58 Jesmo slušali Go govorečego: Ja razrušu synagogu dělana rukoju, a za tri dnji inu, ne rukoju dělana, postavju.
59 I ne bylo soglasno jih svědočstvo.
60 A povstavši v srědinu najvysši kaplan, spytal Jezusa, govoreči: Ničto ne odgovoriš na to, čto svědčet protiv Tebe?
61 No on molčal i ničego ne odgovoril. Snova pytal Jego najvysši kaplan i rěkl  Jemu: „Ty jesi Hristos, Syn Boga Blagoslovjenogo?“
62 A Jezus mu rěkl: „Ja jesm; i vidite syna člověčskogo sedečego na pravici moči Božjej i prihodečego s oblakami nebesnymi.“
63 A najvysši kalan, raztrgal svoje šaty, rěkl: „Do čego nam ješče trěba svědočstv?
64 Jeste slyšali bogohulstvo: Čto vy myslite?“, vsi izdali Mu osud, byti vinnym smrti.
65 I počeli něktori na Njego pljuvati i zakryvati lice Jego i biti Go grstami i govoriti Mu: „Prorokuj!“, a služebniki bili Go takože grstami po licu.
66 A kogda Petr byl na dolu na dvoru, prišla jedna iz slugov najvysšego kaplana
67 i, videči Petra kak grěl se, gleděla na Njego i rěkla: „I jesi byl s Jezusom Nazarejskym.“
68 A on tomu odrěkl: „Ni znaju, ni razuměju, čto govoriš.“ I izšel vně do atrium, i kokot spěval.
69 A sluga, snova videči jego, počela govoriti tym, ktori okolo stali: „On jest jedin iz njih.“
70 A on povtorno tomu odrěkl. A po minutě ti, ktori tam stojali, rěkli Petru: „Istinno jesi jedin iz njih, ibo ty jesi Galilejec.“
71 A on počel se zaklinati i prisegati: „Ne znam člověka, o ktorom povědate.“
72 I v toj minutě povtorno kokot spěval. I spomněl Petr slovo, ktoro mu Jezus rěkl: „Dopoka ne kokot dvukratno spěva, ty trikratno se Mene odrěčeš“, i on počel plakati.

## Razděl 15

1 I utrom rano učinivši radu najvysši kaplany s staršimi i s učenymi v Pismu, i s reštoju rady, svezali Jezusa, izvedli i podali Pilatu.
2 I pytal Go Pilat: Ty jesi kralj židovky? A on pověděl jemu: Ty povědaš.
3 I obvinili Go najvysši kaplany o mnogyh věčah.
4 A Pilat Go pytal: Ničego ne odgovoriš? Vidiš, za kake velike věči te obvinjajut.
5 A Jezus ničego više ne odgovoril, tako da se Pilat čudoval.
6 A na sveto byval obyčaj aby izpuščati jednogo iz vezenja, kogokoli prosili.
7 I byl taky, kogo nazyvali Barabas, ktory s buntovnikami byl v vezenju i v smetenju ubil někogo.
8 A kogdy vstupila tolpa, počela prositi o to, čto jim vsegda činil.
9 A Pilat jim odgovoril i rěkl: Hčete li, byh pustil vam kralja židovskogo?
10 Ibo věděl, da jego iz zavisti najvysši kaplany izdali.
11 No vozbudžali kaplany, aby jim Barabasa pustil.
12 A odpověděvši snova Pilat: Čto hčete, dabyh učinil kralju židovskomu?
13 A oni snova kričali: Ukrižovati Go!
14 A Pilat jim govoril: Čto zlogo učinil? A oni tym više kričali: Ukrižuj Go!
15 A Pilat hčuči zadovoliti gromadu, pustil jim Barabasa, a Jezusa podal bičevati, abyh byl ukrižovan.
16 A vojaki provedli Jego do vnutrnogo dvora i zvali vsu kohortu.
17 I oděli Go v purpur, i položili na Njego korunu iz trna, ktoru spletli.
18 I počeli jego pozdravjati: Vitaj, kralju židovsky!
19 I bili Jego glavu trstinoju, i pljuvali na Njego, a padajuči na kolěna, klanjali se Jemu.
20 A kogdy se iz Njego smějali, sjeli s Njego purpur i oděli Go v Jego odědžu. I izvedli Jego, daby Ho ukrižovati.
21 I prinudili někakogo mimo idučego, Simona iz Kireny, idučego iz sela, otca Aleksandra i Rufa, daby nesl jego križ.
22 I privedli Go na město Golgota, čto znači město mrtvoj glavy.
23 I davali Mu piti vino s mirroju. I ne vzel.
24 A ukrižovavši Jego, razdělili odědžu Jego, metajuči o nju los, kto iměl ju vzeti.
25 A byla tretja časina, kogdy ukrižovali Go.
26 I byl napis viny Jego napisany: Kralj židovsky.
27 A s Njim ukrižovali dvoh zločincev, jednogo po pravici, a drugogo po lěvici Jego.
28 I izpolnilo se Pismo, ktoro govori: A iz zločincami jest klasifikovany.
29 A ti, ktori mimo prěhodili, prokleli Go, kyvajuči glavami svojimi i govoreči: Ah! Toj, ktory razvaljaješ synagogu i v trěh dnjah nanovo buduješ:
30 izbav se samogo iz križa!
31 Tož najvysši kaplany izsmějali Go, jedin k drugomu s učenymi v Pismu govorili: Inyh izbavjal, a samogo sebe izbaviti ne može.
32 Nehaj směsta Hristos, kralj izraelski, stupi iz križa, daby my uviděli i uvěrili. I ti, ktori s Njim byli ukrižovani, sramotili Go.
33 A kogdy nastupila časina šesta, objel mrak vsu zemju do devetoj časiny.
34 O devetoj časině kriknul Jezus ogromnym glasom: Eloi, Eloi, lamma sabakhtani? To jest: Bože moj, Bože moj, čemu jesi Me ostavil?
35 A slyšavši to něktori iz okolo stoječih, govorili: Uvidite, Iliji zove.
36 A priběgl jedin i napolnivši gubku octom, i vloživši ju na trstinu, dal Mu piti, govoreči: čekajte, uvidimo, či prijde Ilija, daby Go od križa sjeti.
37 A Jezus, izpustivši glas ogromny, oddal duha.
38 I razdělila se na dvoje zaslona svetlišča od vrha až do dola.
39 A videči to sotnik, ktory stal protiv, že takym sposobom oddal duha, rěkl: Pravdivo člověk toj byl Synom Božjem.
40 Byli tož i ženy, ktore prigledali iz daleka. Medžu njimi byla Marija Magdalena i Marija, Jakoba Menšego i Jozefa mati, i Salome;
41 i kogda byl v Galileji, hodili za Njim i služili Mu; i mnogo inyh, ktore byli razom s Njim, vstupili do Jeruzalema.
42 A kogdy juže byl večer (ibo byl denj prigotovjenja, ktory jest prěd subotoju),
43 prišel Jozef iz Arimateje, čestny senator, ktory tož očekyval kraljevstva Božjego, i smělo všel do Pilata, i prosil o tělo Jezusa.
44 A Pilat se začudil, da už umrl. A pozvavši sotnika, pytal Go, či už umrl.
45 I dovědavši se togo od sotnika, daroval tělo Jozefu.
46 A Jozef, kupivši platno, i sjevši Go iz križa, ovinul v platno i položil Go v grob, ktory byl izkovany iz skaly. Prěd vhodom do groba suval kamenj.
47 A Marija Magdalena i Marija, mati Jozefa viděli, kde Jego kladli.

## Razděl 16

1 I po prěhodu suboty, Marija Magdalena i Marija, mati Jakoba i Saloma kupili zapahne oleje, daby pošli namazati Jezusa.
2 I utrom rano prvogo dnja po sabotě prišli do groba, kogdy už vošlo solnce.
3 I govorili medžu soboju: Kto nam odsune kamenj od vhoda do groba?
4 I pogledavši, primětili odsunuty kamen: ibo byl velmi veliki.
5 I vševši v grob, uzrěli mladenca sěděčego po pravoj straně, odětogo v šatu bělu, i prěstrašili se.
6 No jim rěkl: Ne bojite se: Jezusa iščete Nazaretskogo, ukrižovanogo. Vstal, ne ima Go tu! Vot město, v ktorom ostal položeny.
7 Ale idite, povědajte učenikom Jego i Petru, da ide prěd vami do Galileje: tam jego uzrite, kako vam pověděl.
8 I one izševši, utekli iz groba, ibo iměli tresenje i strah, a nikomu ničto ne pověděli, ibo se bojali.
9 I vstavši utrom prvogo dnja suboty, ukazal se naprěd Marijei Magdaleně, iz ktoroj izgnal sedm zlyh črtov.
10 Ona pošla, pověděla tym, ktori s Njim byvali, podnurjanym v smutku i plaču..
11 I oni uslyšavši, da žive i da ona Go viděla, ne věrili.
12 Potom tož dvoma iz Njih okazal se v inom obrazu, kogda šli do vsi.
13 I oni ševši, pověděli drugym. A oni jim ne uvěrili.
14 V koncu se ukazal samym Jedinnadset, kogdy sěděli u stola, i obvinil jih za nedostatok věry i neustupnost, da ne věrili tym, ktori viděli Go vozkresanogo.
15 I govoril jim: Idite na cěly svět, glasite Evangelje vsakomu stvorjenju.
16 Kto uvěri i pokresti se, spaseny bude, a kto ne uvěri, sudženy bude.
17 A znamenja tym, ktori uvěret, se pokazyvati budut: V mojem imenu črty budut izganjati, novymi jezykami budut govoriti,
18 zmije budut brati do ruk, i jestli něčto otravno pijut, ne uškodi jim, na hvoryh ruky budut klasti, i dobro jim bude.
19 A Gospodin Jezus, potom kako s njimi govoril, vzety byl do neba i usědl po pravici Božjej.
20 A oni izševši, glasili vesde Evangelje, a Gospodin pomagal i potvrdil slovo črěz znamenja, iduče potom.

# Evangelje Lukasa

## Razděl 1

1 Ibo mnogo ljudij probovalo urediti historiju o tyh věčah, o ktoryh my uvěrjene věsti imamo;
2 Tak kak nam podali, ktori od početka sami viděli, i slugami togo slova byli;
3 Zato hču ja, ktoromu cěla informacija iz početka usrdno došlo, tobě to čestigodno zapisati, čestny Teofile!
4 Abys poznal uvěrjenost tyh věčij, o ktoryh tobě naučeno.
5 Byl za dni Heroda, kralja Judzkogo, duhovnik něktory, imenom Zaharij, iz grupy Abiasa, a žena jego byla iz dočerok Aarona, ktoroj ime bylo Elizabeta.
6 A byli oboje spravědlivymi prěd obličjem Božjim, byli v jedinstvu s vsimi zapovědami i opravdanjami Gospodinskyh bez napomněnja.
7 I ne iměli potomstva, ibo Elizabeta byla neplodna, a byli oboje starcami v lětah svojih.
8 Stalo se itak, kogdy sdělal ured duhovniči v poredku prěměny svojej prěd Bogom.
9 Že po obyčaju ureda kaplanskogo pripadl na njego sudba, aby kadil, I všel do crkvi Gospodina.
10 A vsa tolpa byla na dvoru, moleči se v časině kadženja.
11 Itak jemu se pokazal Angel Gospodinsky, stoječi po pravoj straně oltara, na ktorym kadeno.
12 I prěstrašil se Zaharij ugleděvši go, a strah napadl na njego.
13 I rěkl do njego Angel: Ne boji se, Zahariju! ibo jest izslušana molitva tvoja, a Elizabeta, žena tvoja, urodi tobě syna, i nazoveš jego Joan,
14 Iz njego budeš imati radost i veselost, i mnogo jih budut se radovati iz urodženja jego.
15 Ibo bude velikym prěd obličjem Gospodinskym; vina i napitka močnogo ne bude pil, a Duhom Svetym bude momentalno napolnjeny iz života materi svojej.
16 A mnogo iz synov Izraelskyh on obrati k Gospodinu, Bogu jih.
17 Ibo on pojde premo prěd obličjem jego v duhu i v moči Ilijaša, aby obratil srdca otcev k dětam, i nevěrnyh k mudrosti spravědlivyh, aby uredil Gospodinu ljud gotovy.
18 I rěkl Zaharij do Angela: Po čim to poznaju? ibo jesm stary, a žena moja podšla daleko v dnjah svojih.
19 A odgovarjajuči Angel, rěkl jemu: Jesm Gabrijel, ktory stoju prěd obličjem Božjim, a poslanym, abyh govoril do tebe, žebyh tobě to veselo izvěstje privesti.
20 A vot oněměješ, i ne budeš mogl govoriti až do togo dnja, v ktorom se to stane, zato, že jesi ne uvěril slovam mojim, ktore se izpolnet v času svojem.
21 A ljud očekyval Zaharija; i divili se, že tak dolgo byl v crkvi.
22 A izševši ne mogl do njih govoriti; i poznali, že viděnje viděl v crkvi; ibo jim črěz znaky ukazyval, i ostal němym.
23 I stalo se, kogdy se končili dni posluživanja jego, že odšel do doma svojego.
24 A po tyh dnjah byla brěmenna Elizabeta, žena jego, i kryla se črěz pet měsecev, govoreči:
25 Že mně tak Gospodin učinil vo dni, v ktore na mene pogledal, aby odjel bezčestje moju medžu ljudami.
26 A v měsecu šestym poslany jest Angel Gabrijel od Boga do grada Galilejskogo, ktoro zvano Nazaret,
27 Do Děvy svatbenoj mužu, ktoromu ime bylo Jozef, iz doma Davida, a ime Děvy Marija.
28 A vševši Angel do njej, rěkl: Bud pozdravjena, lasky polna, Gospodin s toboju; blagoslavjana jesi ty medžu ženami.
29 No ona ugleděvši go, prěstrašila se na slova jego, i myslila, kako by to bylo pozdravjenje.
30 I rěkl jej Angel: Ne boji se, Marijo! ibo jesi našla lasku u Boga.
31 A vot budeš brěmenna v životu i porodiš syna, i nazoveš jego Jezus.
32 Toj bude veliky, a Synom Vrhovnogo bude nazvany, i da jemu Gospodin Bog tron Davida, otca jego;
33 I bude vladati nad domom Jakoba na věky, a kraljevstvu jego ne bude konca.
34 Zatom Marija rěkla do Angela: Kako to bude, kak ja muža ne znaju?
35 A odgovarjajuči Angel, rěkl jej: Duh Svety spusti se na tebe, a moč Vrhovnogo otěni tebe; zatom i to, čto sveto se iz tebe porodi, nazvano bude Synom Božjim.
36 A vot Elizabeta, pokrovna tvoja, tož i ona iměla syna v starosti svojej, a toj měsec jest šesty jej, ktoru nazyvano neplodnoju.
37 Ibo ne bude nemožno u Boga nijedno slovo.
38 I rěkla Marija: Vot služebnica Gospodinska; nehaj mně se stane po slovu tvojego. I odšel od njej Angel.
39 Itak vstavši Marija v tyh dnjah, pošla v vrhnu krajinu iz pospěhom do grada Judzkogo.
40 A vševši v dom Zaharija, pozdravila Elizabetu.
41 I stalo se, směsta uslyšala Elizabeta pozdravjenje Mariji, skočilo dětetko v životu jej, i napolnjena byla Elizabeta Duhom Svetym.
42 I zvala glasom velikym, i rěkla: Blagoslavjana jesi ty medžu ženami, i blagoslavjany plod života tvojego!
43 A odkud mně to, že prišla mati Gospodina mojego do mene?
44 Ibo kak došel glas tvojego pozdravjenja do mojih ušij, vskočilo od radosti dětetko v životu mojim.
45 A blagoslavjana, ktora uvěrila: Ibo se izpolnet te věči, ktore jej sut razkazano od Gospodina.
46 Itak rěkla Marija: Oboža duša moja Gospodina;
47 I razradoval se duh moj v Bogu, spasitelju mojim,
48 Že pogledal na nizkost služebnice svojej; ibo odtud blagoslavjanoju mene zvati budut vse narody.
49 Ibo mně učinil velike věči toj, ktory močny jest, i sveto ime jego;
50 I ktorogo milosrdje ostavaje od naroda do naroda nad tymi, ktori se go bojet.
51 Učinil moči ramenem svojim, i razprašil gordo v mysljah jih srdca.
52 Iztegnul avtoritety iz tronov jih, a vozvysil uniženo.
53 Gladnyh napolnil dobrymi věčami, a bogačih razpustil prazdne.
54 Prijel Izrael, slugu svojego, pametajuči milosrdje svoje.
55 Tak, kak govoril do otcev naših, do Abrahama i sěmena jego na věky.
56 I ostala s njeju Marija tri měsece; potom se vratila do doma svojego.
57 A Elizabetě izpolnil se čas, aby porodila, i porodila syna.
58 A uslyšavši susědi i pokrovni jej, že Gospodin s njeju učinil veliko milosrdje svoje, radovali se zajedno s njeju.
59 I stalo se, že v osmom dnju prišli, aby obrězali děte; i nazvali je imenom otca jego, Zaharijem.
60 No odgovarjajuči mati jego rěkla: Ne tak; no nazvany bude Joan.
61 I rěkli do njej: Nijednogo ne imaš v rodině tvojej, ktoru byl zvany tym imenom.
62 I kyvnuli na otca jego, kakby go htěl nazvati.
63 A on kazavši sobě podati tabličku, napisal govoreči: Joan jest ime jego. I divili se vsi.
64 A v tom samom momentu odkryli se usta jego, i jezyk jego, i govoril, obožajuči Boga.
65 I prišel strah na vsih susědov jih, i po cěloj vrhnoj krajině Judzkoj razglašene byli vse te slova.
66 Itak vsi, ktori o tym slyšali, brali to do srdca svojego, govoreči: Čto to že za děte bude? I byla s njim ruka Gospodinska.
67 A Zaharij, otec jego, napolnjeny suči Duhom Svetym, prědviděl govoreči:
68 Blagoslavjany nehaj bude Gospodin, Bog Izraelsky, že prišel do nas i sdělal odkupjenje ljudu svojemu;
69 I izstavil nam rog spasenja v domu Davida, slugi svojego,
70 Tak kak govoril črěz usta svetyh prorokov svojih, ktori byli od věka:
71 Že jim iměl dati izbavjenje od neprijateljev naših i iz ruky vsih, ktori nas nenaviděli;
72 Aby učinil milosrdje s otcami našimi, i pomněl o svojem svetom zavětu,
73 I o prisegu, ktoru prisegal Abrahamu, otcu našemu, že nam to dati iměl,
74 Žebysmo jemu bez bojaznji, iz ruky neprijatelj naših suči izbavjeni, služili;
75 V svetoblivosti i v spravědlivosti prěd obličjem jego, po vse dni života našego.
76 A ty děte! Prorokom Vrhovnogo nazvano budeš; ibo pojdeš premo prěd obličjem Gospodinskym, abys pripravjal stežky jego,
77 A žebys dal vědu spasenja ljudu jego črěz odpuščenje grěhov jih.
78 Črěz vnutrnosti milosrdja Boga našego, v ktoryh prišel do nas Vozhod iz vysoty.
79 Aby se ukazal sědečim v temnosti i v těnju smrti k odgnutju nog naših na stežku pokoja.
80 A ovo děte rastlo, i ukrěpilo se v duhu, i bylo na pustynjah až do togo dnja, v ktorom se okazalo prěd Izraelom.

## Razděl 2

1 I stalo se v te dni, že izšel dekret od cěsara Avgusta, aby zapisano ves svět.
2 A toj prvy spis stal se, kogdy Kyrinej byl starostoju Sirijskym.
3 I šli vsi, aby zapisani byli, vsaky do grada svojego.
4 Vstupil tož i Jozef iz Galilei iz grada Nazareta do zemji Judzkoj, do grada Davida, ktory zovut Betlehem, (ibo že on byl iz doma i iz rodiny Davida;)
5 Aby byl zapisany s Marijeju, svatbenoju sobě suprugoju, ktora byla brěmennoju.
6 I stalo se, kogdy tam byli, že prišel čas, aby porodila.
7 I porodila syna svojego prvoroždjenogo; a ovinula go v peleny, I položila go v jasla-sadku, zato že města ne iměli v gostincu.
8 A byli pastyri v tej krajině v polju nočujuči i iměli straža nočnu nad stadom svojim.
9 A vot Angel Gospodinsky stanul pri njimi, a hvala Gospodinska odvsud osvětlila jih, i velmi se prěstrašili.
10 I rěkl do njih Angel: Ne bojite se; ibo vot blagověstvuju vam radost veliku, ktora bude vsemu ljudu:
11 Že se vam tutdenj narodil spasitelj, ktory jest Hristos Gospodin, v gradu Davida.
12 A to vam bude znak: nahodite dětetko povijeno v peleny, ležeče v jasla-sadku.
13 A momentalno s tym Angelom prišlo množstvo vojsk nebesnyh, hvalečih Boga I govorečih:
14 Hvala na vysotah Bogu, a na zemji pokoj, ludjam dobroj volje.
15 I stalo se, kogdy odšli Angeli od njih do neba, že pastyri rěkli jedni do drugyh: Pojdimo až do Betlehema, a ogledajmo tu věč, ktora se stala, ktoru nam Gospodin objavil.
16 A tak pospěšajuči se, prišli I našli Mariju I Jozefa, i dětetko ležeče v jasla-sadku.
17 I ugleděvši je kazali to, čto jim bylo pověděno o tym dětetu.
18 A vsi, ktori slyšali, divili se tomu, čto jim pastyri govorili.
19 No Marija zadržala vse te slova, myslila o njih v srdcu svojim.
20 I vratili se pastyri, obožajuči I hvaleči Boga za vse, čto slyšali i viděli, tak kako jim bylo pověděno.
21 A po osm dnjah, obrězano bylo děte, ktoro jest nazvano Jezus. Bylo tak nazvano od Angela, prvo než se v životu počelo.
22 Po dnjah očiščenja jej po zakoně Mojzesa, prinesli go do Jeruzalema, aby go po
prěstavili Gospodinu,
23 (Tak kako jest napisano v zakonu Gospodinskym: že vsaky muž, otvarjajuči život, svetym Gospodinu nazvany bude.)
24 Aby oddali žrtvu po tym, čto pověděno v zakonu Gospodinskym, paru gorlic, ili dvoje  golubov.
25 A vot byl člověk v Jeruzalemu, ktoromu ime bylo Simeon; a toj člověk byl spravědlivy i Bogobojny, očekyvajuči utěšy Izraelskoj, a Duh Svety byl nad njim.
26 I objavjeny byl od Boga črěz Duha Svetogo, že ne iměl ogledati smrti, až najprvo ogledal Hristosa Gospodinskogo.
27 Toj prišel iz nadohnenja Duha Svetogo do crkvi; a kogdy roditelji vnosili děte, Jezusa, aby učinili po obyčaju zakonnom pri njim.
28 Itak on vzevši go na ruky svoje, hvalil Boga i govoril:
29 Tutčas dopusti slugu tvojego, Gospodine! Aby pošel po slovu tvojem v pokoju:
30 Ibo oči moje ogledali spasenje tvoje,
31 Ktoro jesi prigotovil prěd obličjem vsih ljudij;
32 Světlo k objavjenju poganam, a hvalu ljudu tvojego Izraelskogo.
33 A otec i mati jego divili se tomu, čto govoreno o njim.
34 I blagoslavjal jim Simeon, I rěkl do Marije, materi jego: Vot toj položeny jest na upad I na voskresenje mnogo jih v Izraelu, i na znak, protiv ktoromu govoriti budut.
35 (I tvoju sobstvennu dušu meč probije,) aby myslji iz mnogo srdc objavjene byli.
36 A byla Anna prorokina, dočerka Fanuela, iz roda Aser, ktora byla velmi stara, i žila sedm lět s mužem od děvstva svojego.
37 A byla vdovoju, okolo osmdeset i četyri lět; ktora ne izhodila iz crkvi, v postah i v molitvah služuči Bogu v noči i vo dnje.
38 Ta tož toj-że časiny nastupivši, izpověděla Gospodina, i govorila o njim vsem, ktori očekyvali odkupjenja v Jeruzalemu.
39 A tak sveršivši vse po zakonu Gospodinskogo, vratili se do Galilei, do svojego grada Nazareta.
40 A děte rastlo, i ukrěpilo se v Duhu, polno mudrosti, a laska Božja byla nad njim.
41 A roditelji jego hodili na vsako lěto do Jeruzalema na prazdnik pashalny.
42 A kogdy už byl v dvanadsetym lětu, oni vstupali do Jeruzalema po obyčaju togo prazdnika;
43 I kogdy skončili se te dni, i už vračali se nazad, ostalo děte Jezus v Jeruzalemu, no togo ne věděli ni Jozef ni jego mati.
44 No mysleči, že jest v družině putujučej, odšli denj stežky, i iščali go medžu srodnikami i medžu znajomymi.
45 A kogdy go ne našli, vratili se do Jeruzalema, iščuči go,
46 I stalo se po trěh dnjah, že go našli sědučogo v crkvi posrěd doktorov, slušajučego i pytajučego jih.
47 I divili se vsi, ktori go slyšali, nad razumom i nad odgovorami jego.
48 A ugleděvši go roditelji, udivili se. I rěkla do njego mati jego: Syne! začto že jesi nam to učinil? Vot otec tvoj i ja s boljem jesmo iskali tebe.
49 I rěkl do njih: Čto jest, že jeste mene iskali? Či jeste ne věděli, že v tyh věčah, ktore sut Otca mojego, ja imaju byti?
50 No oni ne razuměli togo slova, ktoro jim govoril.
51 I spustil se s njimi, i prišel do Nazareta, a byl jim poddany. A mati jego zadržala vse te slova v srdcu svojim.
52 A Jezus razmnožil se v mudrosti, i v rastu i v laskě u Boga i u ljudij.

## Razděl 3

1 V lětu petnadsetom vladanja Tiberija Cěsara, Pontsky Pilat byl starostoju Judejskym, a Herod Tetrarhoju Galilejskym, a Filip, brat jego, Tetrarhoju Iturejskym i krajiny Trachonitskoj, a Lizanijas Tetrarhoju Abilenskim,
2 Za najvysših duhovnikov Annasa i Kajafy, stalo se slovo Božje do Joana, Zaharijeva syna, na pustynji.
3 I prišel do cěloj krajiny ležačej okolo Jordana, kažuci krest pokajanja na odpuščenje grěhov.
4 Kako napisano v knigah proročestv Izaiji proroka, ktori govoril: Glas zovučego na pustynji; pripravite stežku Gospodinsku, premo činite stežky jego.
5 Vsaka dolina bude izpolnjena, a vsaka gora i gorka budut ponižene, i města krive odgnut se, a ostre stežky budut gladkymi;
6 I ogledaje vsako tělo spasenje Bože.
7 Govoril itak ljudu, ktory izhodil, aby byl kreščeny od njego: Roda jaščera! ktory vam pokazal, abyste běgali prěd budučim gněvom?
8 Prinosite itak plody dostojne pokajanja, a ne začinajte govoriti sami v sobě: Otca imamo Abrahama; ibo govorju vam, že Bog može i iz tyh kamenev vozbuditi děti Abrahamu.
9 A už sěkyra do korenja drěv položena jest; zatom každo drěvo, ktoro ne prinosi ploda dobrogo, byvaje izrězano i v ogonj kydnuto.
10 I pytal go ljud: Čto itak činiti budemo?
11 A on odgovarjajuči rěkl jim: Kto ima dvě oděžij, nehaj uděli tomu, čto ne ima; a kto ima jedu nehaj tož-že učini.
12 Prišli tož i mytnici, aby byli kreščeni, i rěkli do njego: Učitelju! a my čto činiti budemo?
13 A on rěkl do njih: Ničto veče ne iztrgnute než to, čto vam postavjeno.
14 Pytali go tož i vojini, govoreči: A my čto činiti budemo? I rěkl do njih: Nikomu nasilja ne činite, i nikogo ne klevetajte, a budite radi za vašu zaplatu.
15 A kogdy ljud očekyval, i myslili vsi v srdcah svojih o Joanu, jestliby očevidno on ne byl Hristosom,
16 Odgovoril Joan vsim, govoreči: Ja vas krešču vodoju; no ide močnějši nad mene, ktoromu ne jesm dostojny razvezati remenja u obuvy jego; toj vas krestiti bude Duhom Svetym i ognjem.
17 Ktorogo lopata jest v rukě jego, a očisti bojno polje svoje, i sbere pšenicu do gumna svojego, no plěvy spali ognjem neugasimym.
18 A tak mnogo i inyh věčij napominajuči, odgovarjal ljudu.
19 A Herod Tetrarh, byl napominany od njego za Herodijadu, ženu Filipa, brata jego, i za vsih zlyh děl, ktore činil Herod.
20 Dodal nad to vse, že vložil Joana do vezenja.
21 I stalo se, kogdy byl kreščeny ves ljud, i kogdy Jezus byl kreščeny, i molil se, že nebo se otvorilo;
22 I spustil se na njego Duh Svety v obrazu tělesnym kako golubica, i stal se glas iz neba, govoreči: Ty jesi moj Syn mily; tebe jesm poljubil.
23 A Jezus začel svoje děla kak iměl trideset lět, suči (kako mněvano,) synom Jozefa, syna Hela,
24 Syna Matata, syna Levi, syna Melhija, syna Joana, syna Jozefa,
25 Syna Mattatijasa, syna Amosa, syna Nauma, syna Esla, syna Naggija,
26 Syna Maata, syna Mattatijasa, syna Semeija, syna Jozefa, syna Juda,
27 Syna Joana, syna Resa, syna Zorobabela, syna Salatijela, syna Nerija,
28 Syna Melhija, syna Addyja, syna Kosama, syna Elmodama, syna Ira,
29 Syna Joza, syna Eliyezera, syna Jorima, syna Mattatego, syna Levia,
30 Syna Simeona, syna Juda, syna Jozefa, syna Jonana, syna Eliyakima,
31 Syna Melea, syna Mainana, syna Mattatana, syna Natana, syna Davida,
32 Syna Jessa, syna Obeda, syna Booza, syna Salmona, syna Nasona,
33 Syna Aminadaba, syna Arama, syna Esroma, syna Faresa, syna Juda,
34 Syna Jakoba, syna Izaaka, syna Abrahama, syna Tarego, syna Nahora,
35 Syna Seruga, syna Ragava, syna Faleka, syna Hebera, syna Sala,
36 Syna Kaina, syna Arfaksada, syna Sema, syna Noeva, syna Lameha,
37 Syna Matusalema, syna Enocha, syna Jareda, syna Malaleela, syna Kainana,
38 Syna Enosa, syna Seta, syna Adama, syna Božjego.

## Razděl 4

1 A Jezus polny suči Duha Svetogo, vratil se iz Jordana, i gnany jest od Duha na pustynju.
2 I byl črěz četyrideseti dni pokušeny od djavla, a ne jel ničto črěz te dni; no kogdy se skončili, potom gladnul.
3 I rěkl jemu djavol: Jestli jesi Synom Božjim, kaži kamenju tomu, aby se stal hlěbom.
4 No Jezus odgovoril jemu: Napisano, že ne samym hlěbom žiti bude člověk, no vsakom slovom Božjim.
5 I vvezl go djavol na goru vysotu, i pokazal jemu vse kraljevstva světa v momentu oka.
6 I rěkl jemu djavol: Dam tobě tu vsu moč i slavu jih; ibo mně jest dana, a komu hču, davaju ju.
7 A jestli se pokloniš prěd mnoju, bude vse tvoje.
8 A odgovarjajuči Jezus rěkl jemu: Pojdi von od mene, satane! ibo Napisano: Gospodinu, Bogu tvojemu, klanjati se budeš, i jemu samomu služiti budeš.
9 Potom vodil go do Jeruzalema, i postavil go na stěně crkovnym, i rěkl jemu: Jestli jesi Synom Božjim, spusti se odtud na dol;
10 Ibo napisano: Že Angelam svojim prikazal o tobě, aby tebe hranil,
11 žeby tebe na rukah nosili, bys očevidno ne poranil se o kamenj nogami tvojimi.
12 A odgovarjajuči Jezus rěkl jemu: Pověděno: Ne budeš pokušal Gospodina, Boga tvojego.
13 A kogdy djavol dokončil vsi pokušenja, odstupil od njego až do časa.
14 I vratil se Jezus v moči togo Duha do Galilei. i razošla se o njim věst po cěloj toj okolnoj krajině.
15 A on naučal v synagogah jih, i byl slavjeny od vsih.
16 I prišel do Nazareta, kde byl vozpitany, i všel po obyčaju svojem v subotu do synagogy, i vstal, aby čital.
17 I podano jemu knigy Izaiji proroka; a otvorivši knigy, našel město, kde bylo napisano:
18 Duh Gospodinsky nad mnoju; zatom mene pomazal, abyh razkazyval Evangeliju ubogym; poslal mene, abyh ozdravjal pokajanyh na srdcu, abyh blagověstvoval pojmanym izbavjenje, i slěpym prěgledanje, i abyh odpustil ugneteno na svobodu;
19 Abyh razkazyval lěto Gospodinsko prijatno.
20 A zaključivši knigu i oddavši ju slugě, usědl; a oči vsih v synagogě spěšno na njego gledali.
21 I začel do njih govoriti: Tutdenj se izpolnilo to pismo v ušah vaših.
22 I vsi jemu davali svědočstvo, i divili se blagodarnosti tyh slov, ktore izhodili iz ust jego, i govorili: či toj ne jest syn Jozefa?
23 I rěkl do njih: Uvěrjeno mně rěčete tu parabolu: Lěkaru! ozdravi samogo sebe! Čto jesmo slyšali, jesi učinil v Kafarnaum, učini i tu v otčině svojej.
24 I rěkl do njih: Zapravdu vam govorju: Nijedin prorok ne jest prijatnym v otčině svojej.
25 No vam v pravdě govorju, že mnogo vdov bylo za dni Ilijaša v ljudu Izraelskym, kogdy bylo zaključeno nebo črěz tri lěta i šest měsecev, takože byl veliky glad po cěloj zemji;
26 Ibo do nijednoj iz njih ne byl poslany Ilijaš, jedino do Sarepty, grada Sidonskogo, do jednoj vdovy.
27 I mnogo bylo leprosnyh za časov Ilizeusa proroka, v ljudu Izraelskym, ibo nijedin iz njih ne byl očiščeny, jedino Naaman, Stryjec.
28 Itak vsi v synagogě, kogdy to slyšali, napolnjeni byli gněvom;
29 A vstavši, izgnali go von iz grada, i izvedli go na vrh gory, na ktoroj grad jih postavjeny byl, aby go iz njej na dol kydnuli.
30 No on prěševši črěz posrěd njih, odšel.
31 I spustil se do Kafarnauma, grada Galilejskogo, a tam naučal v suboty.
32 I divili se nad naukoju jego; ibo byla močny govor jego.
33 A v synagogě byl člověk, ktory iměl duha djavla nečistogo, i pozval glasom velikym,
34 Govoreči: Ah! Čto my s toboju imamo, Jesuse Nazaretky? Jesi prišel, abys nas pogubil; znaju tebe, kym jesi. Jesi Svety Božji.
35 I sgromil go Jezus, govoreči: Molči, a izojdi iz njego. Itak djavol ostavivši go v posrěd, izšel iz njego, ničto jemu ne škodivši.
36 I prišel strah na vsih, i razgovarjali medžu soboju, govoreči: Čto to za slovo, že s vlastju i s močju govori duham nečistym, a izhodet?
37 I razošla se o njim věst na vse města okolnoj krajiny.
38 A Jezus vstavši, iz synagogy všel v dom Simona, a svekra Simona iměla gorečku veliku; i prosili go za njeju.
39 Itak on stanuvši nad njeju, sgromil gorěčku, i opustila ju; a v tom samom vrěmenu vstavši, služila jim.
40 A kogdy solnce zapadalo, vsi, ktori iměli razne hvoroby, privodili je do njego, a on na vsakogo iz njih ruky vloživši, ozdravjal jih.
41 K tomu izhodili i djavli iz mnogo jih, zovuči i govoreči: Ty jesi Hristos, Syn Božji; no on sgromivši jih, ne dopuščal jim govoriti; ibo věděli, že on jest Hristos.
42 A kogdy byl denj, izševši, pošel na město prazdno. A ljud go iskal, i prišli až do njego, i sodržali go, aby ne odhodil od njih.
43 A on rěkl do njih: I inym gradam imaju razkazyvati kraljevstvo Božje; ibo jesm na to poslany.
44 I kazal v synagogah Galilejskyh.

## Razděl 5

1 I stalo se, kogdy na njego ljud nastojal, aby slyšal slova Božje, ibo on stal pri jezeru Genezaretskym.
2 I ugleděl dvě lodi stoječe pri jezeru; no rybaki izševši iz njih, myli sěti.
3 A vstupivši v jednu iz tyh lodji, ktora byla Simona, prosil go, aby malo odšel od brěgu; a usědši, učil ljuda iz toj lodi.
4 A kogdy prěstal govoriti, rěkl do Simona: Prijedi na glubinu, a spustite sěti vaše do lovljenja.
5 A odgovarjajuči Simon, rěkl jemu: Učitelju! črěz cělu noč dělajuči, ničto-že jesmo ne ulovili, ibo na slovo tvoje spustju sět.
6 A kogdy to učinili, lovili mnogo ryb velikyh, tak že se rvala sět jih.
7 I kyvnuli na tovarišev, ktori byli v drugoj lodi, aby prišli i spasali jih; i prišli i napolnili obě lodi, až se smočili.
8 To viduči, pripadl Simon Petr do kolěn Jezusa, govoreči: Izojdi od mene; ibo jesm člověk grěšny, Gospodine!.
9 Ibo go strah obsegnul, i vsi, ktori s njim byli, črěz toj ulov ryb, byli obsegnuti.
10 Takože i Jakob i Joan, syni Zebedeova, ktori byli tovarišami Simona. I rěkl Jezus do Simona: Ne boji se; od togo časa ljudij loviti budeš.
11 A oni iztrgnuvši lod na brěg, vse opustivši, pošli za njim.
12 I stalo se, kogdy byl v něktorom gradu, že vot byl tam muž polny lepry, ktory ugleděvši Jezusa, padl na lice, i prosil go, govoreči: Gospodine! jestli hčeš, možeš mene očistiti.
13 Itak iztrgnuvši Jezus ruku, dotknul go, govoreči: Hču, bud očiščeny; i momentalno odšel lepra od njego.
14 I prikazal jemu, aby togo nikomu ne govoril: no rěkl: Idi, a ukaži se duhovniku, i žrtvuj za očiščenje tvoje, tak kako kazal Mojzes, na svědočstvo protiv njim.
15 I razhodila se tym veče pověst o njim; i shodili se tolpy velike, aby go slyšali i ozdravjeni byli od njego od nemoči svojih.
16 No on odhodil na pustynju, i molil se.
17 I stalo se dnja něktorogo, že on naučal, a sěděli tož tam i Farizeji i učitelji Zakona, ktori sobrali se iz vsih gradov Galilejskyh i Judejskyh, i iz Jeruzalema; a moč Gospodinska prisutna byla ozdravjanju jih.
18 A vot muži nesli na ložu člověka sparalizovango, i iskali, kakoby go vnesti i postaviti prěd njim.
19 A kogdy ne našli, kudy by go vnesli, vstupivši na strěhu, črěz diru spustili go ložem v posrěd prěd Jezusom.
20 Toj ugleděvši věru jih, rěkl jemu: Člověče! odpuščeno sut tobě grěhy tvoje.
21 Itak začeli mysliti naučeni v Pismu i Farizeji, govoreči: Kto to jest, ktory govori bogohuljenja? Kto može odpuščati grěhy než jedino sam Bog.
22 No Jezus poznavši myslji jih, odgovarjajuči rěkl do njih: Čto myslite v srdcah vaših?
23 Čto jest prostějše rěkti: Odpuščeno sut tobě grěhy tvoje, ili rěkti: Vstani i hodi?
24 No abysmo věděli, že Syn člověčsky ima moč na zemji odpuščati grěhy, (rěkl sparalizovanomu:) Tobě govorju: Vstani, a vzevši na sebe lože svoje, idi do doma tvojego.
25 A on v tom samom vrěmenu vstavši prěd njimi, vzevši na sebe to, na čim ležal, šel do doma svojego, obožajuči Boga.
26 I udivili se vsi, i hvalili Boga, i napolnjeni byli strahom, govoreči: Jesmo viděli tutdenj divne věči.
27 A potom izšel i ugleděl mytnika, imenom Levi, sědučego v komnatě mytnoj, i rěkl jemu: Pojdi za mnoju.
28 I opustil vse, a vstavši, pošel za njim.
29 I sdělal jemu Levi pir veliky v domu svojem; a bylo veliko sobranje mytnikov i inyh, ktori s njim za stolom sěděli.
30 Itak roptali naučeni v Pismu i Farizeji, govoreči do učenikov jego: Začto s mytnikami i s grěšnikami jete i pijete?
31 A Jezus odgovarjajuči, rěkl do njih: Ne potrěbujut zdravi lěkara, no ti, ktori se zlo imajut;
32 Ne jesm prišel, zvati spravědlivyh, no grěšnyh do pokajanja.
33 A oni jemu rěkli: Začto učeniki Joanu često postet se i molet se, takože i Farizeji, a tvoji jedut i pijut?
34 A on jim rěkl: Či možete učiniti, aby gosti svatby postili, až s njimi jest mladoženih?
35 No prijdut dni, kogdy mladoženih odjety bude od njih; itak v te dni postiti budut.
36 Pověděl jim tož parabolu: Nijedin latku iz oděži novoj ne prišije do oděži staroj; ibo inače to, čto jest novogo, drži staro, a do starogo ne godi se latka iz novogo.
37 I nikto ne lije vina novogo v stare buklaky; ibo inače vino mlade razsadi buklaky, i samo izteče, i buklaky se izniščet.
38 No mlade vino ima byti nalivano v buklaky nove; a tak oboje byvajut hranjene.
39 A nikto, ktori napil se starogo, ne momentalno hče mladogo; no govori: Lěpše jest staro.

## Razděl 6

1 I stalo se v drugu subotu, že šel Jezus črěz sboža; i rvali učeniki jego klasy, a rukami otirajuči jeli.
2 No něktori iz Farizejov rěkli do njih: Začto že činite to, čego se ne godi činiti v subotu?
3 A odgovarjajuči Jezus, rěkl do njih: A jeste togo ne čitali, čto učinil David, kogdy gladněl sam, i ti, ktori s njim byli?
4 Kako všel do doma Božjego, a vzel hlěby žrtvene, i jel, a dal i tym, ktori s njim byli; ktoryh se ne godilo jesti, jedino samym duhovnikam?
5 I rěkl jim: Syn člověčsky jest Gospodinom i suboty.
6 Stalo se takože i v inu subotu, že Jezus všel do synagogy, i naučal; i byl tam člověk, ktorogo ruka zakony byla usohla.
7 I slědili go naučeni v Pismu i Farizeji, jestliby v subotu ozdravjal, aby našli, za čto jego mogli obvinjati.
8 No on věděl myslji jih, i rěkl člověku, ktory iměl ruku usohlu: Vstani a stani posrěd. A on vstavši, stanul.
9 Rěkl itak do njih Jezus: Pytaju vas o jednu věč: Godi se v suboty dobro činiti, či zlo činiti? Člověka hraniti, či pogubiti?
10 A pogledavši v kolo po vsih, rěkl tomu člověku: Iztrgni ruku tvoju! a on tak učinil i vozvračena jest do zdravja ruka jego, kako i druga.
11 No oni napolnjeni bezumnostju, razgovarjali medžu soboju, čto by učiniti iměli Jesusu.
12 I stalo se v te dni, že odšel na goru, aby se molil; i byl tam črěz noč na molitvě Božjej.
13 A kogdy byl denj, pozval učenikov svojih i izbral iz njih dvanadset, ktoryh tož nazval Apostolami:
14 Simona, ktorogo tož nazval Petrom, i Andreja brata jego, Jakoba, i Joana, Filipa, i Bartlomeja;
15 Mateuša, i Tomasa, Jakoba, syna Alfeusa, i Simona, ktorogo zovut Zelot;
16 Judasa, brata Jakobovogo, i Judasa Iskariota, ktory potom byl izdajnikom.
17 A spustivši se s njimi, stanul na městu polja ravnogo, i gromada učenikov jego, i tolpa ljuda iz cěloj Judzkoj zemji, i iz Jeruzalema, i iz kraja morskogo, ktory byl pri Tirě i Sidoně. Ti prišli, aby go slyšali, i byli ozdravjeni od hvorob svojih;
18 I ti, ktori byli mučeni od duhov nečistyh, byli ozdravjeni.
19 A ves ljud iskal, kakoby go dotknuti; ibo moč izhodila iz njego, i ozdravjala vsih.
20 A on voznevši oči svoje na učenikov, govoril: Blagosloveni jeste, ubogi! ibo vaše jest kraljevstvo Bože.
21 Blagosloveni jeste, ktori tutčas gladněte; ibo budete sytni. Blagosloveni jeste, ktori tutčas plačete; ibo se smějati budete.
22 Blagosloveni budete, kogdy vas ljudi nenaviděti budut, i kogdy izključet posrěd sebe, i budut vas bezčestiti, i ime vaše izkydnut kako zlo, za Syna člověčskogo.
23 Radujte se dnja togo i radujte se; ibo vot zaplata vaša jest bujna v nebesah; ibo tak imenno prorokam činili otci jih.
24 No běda vam bogačam! ibo už imate utěhu vašu.
25 Běda vam, ktori jeste sytni! ibo gladněti budete. Běda vam, ktori tutčas smějete se! ibo smutiti se i plakati budete.
26 Běda vam, kakby dobro o vas govorili vsi ljudi; ibo tak činili falšivym prorokam otci jih.
27 No vam govorju, ktori slyšite: Ljubite neprijateljev vaših, činite dobro tym, ktori vas imajut v nenavisti.
28 Blagoslovite tym, ktori vas klnut; molite se za tymi, ktori vam zlost dělajut.
29 Tomu, ktory by tebe udaril v lice, nastavi jemu i drugo stranu: a tomu, ktory by bral plašč, i oděž ne zabranjaj;
30 I vsakomu, ktory by tebe prosil, daj, a tomu, ktori tvoje bere, ne napominaj se.
31 I čto byste htěli, aby vam ljudi činili, tak i vy jim činite.
32 Ibo jestli ljubite tyh, ktori vas ljubet, kaku lasku imate? ibo tož i grěšniki imenno činet.
33 A jestli dobro činite tym, ktori vam dobro činet, kaku lasku imate? ibo tož i grěšnici imenno činet.
34 A jestli date zajem tym, od ktoryh se nadějete se odbrati, kaku lasku imate? ibo i grěšniki grěšnikam dadut zajem, aby tako mnogo odbrali.
35 Očevidno ljubite neprijateljev vaših, i činite jim dobro, i dajte zajem, ničto se odtud ne očekyvajuči se, a bude velika zaplata vaša, i budete synami Vrhovnogo; ibo on milostivy jest protiv neblagodarnym i zlym.
36 Zatom budite milosrdni, kako i Otec vaš milosrdny jest.
37 Ne sudite, a ne budete sudženi; ne osudite, a ne budete osudženi, a bude vam odpuščeno.
38 Davajte, a bude vam dano; měru dobru, natlačennu, i tressennu, i oplyvajuču dadut na lono vaša; ibo toju měroju, ktoroju měrite, bude vam jednako měrjeno.
39 I pověděl jim parabolu: Či može slěpy slěpogo voditi? I ne oba v dol padut?
40 Ne jest učenik nad učiteljem svojim; no doskonaly bude vsaky, bude kako učitelj jego.
41 A čemu vidiš steblo v oku brata tvojego, a dosky, ktora jest v oku tvojim, ne vidiš?
42 Ili kako možeš rěkti bratu tvojemu: Brate! dopusti, že vozmu steblo, ktoro jest v oku tvojem. A sam dosky, ktora jest v oku tvojem, ne vidiš? Liceměre! Vozmi najprvo dosky iz oka tvojego, a itak prěglediš, abys izjel steblo, ktoro jest v oku brata tvojego.
43 Ne jest ibo drěvo dobro, ktoro prinosi plod zly; ni jest drěvo zlo, ktoro prinosi plod dobry;
44 Ibo vsako drěvo iz ploda vlastnogo poznano byvaje; ibo ne sbirajut iz trna fig, ni iz gloga sbirajut ploda vina.
45 Člověk dobry iz dobrogo skarba srdca svojego iznosi věči dobro, a zly člověk iz zlogo skarba srdca svojego iznosi věči zle; ibo iz bujnosti srdca govoret usta jego.
46 Kako že mene itak zovete Gospodine, Gospodine! a ne činite togo, čto govorju?
47 Vsaky, ktory prihodi do mene, a slyše slov mojih, i čini je, ukažu vam, komu jest podobnym.
48 Podobny jest člověku dom postavjajučemu, ktory kopal i izkopal gluboko, a osnoval zemju na kamenju, a kogdy prišel potop, voznesla se rěka i udarila o dom, no ne mogla go porušiti; ibo byl osnovany na kamenju.
49 No ktory slyše, a ne čini, podobny jest člověku, ktory postavil dom svoj na zemji na zloj osnově; I kogdy rěka se voznesla, v tom samom vrěmenu dom upadl, a byl upad doma togo veliky.

## Razděl 7

1 A kogdy dokončil vsi govory svoje prěd tym ljudom, všel do Kafarnauma;
2 A byl něktory sluga sotnika, ktorogo sotnik mnogo čestil, imal se zlo, i už blizko byl smrti.
3 Toj uslyšavši o Jezusu, poslal do njego starših iz Židov, proseči go, aby priševši ozdraviti slugu jego.
4 A oni priševši do Jezusa, prosili go iz spěšnostju, govoreči: Dostojny jest, abys jemu to učinil;
5 Ibo ljubi narod naš, i on nam synagogu postavil.
6 A tak Jezus šel s njimi. No kogdy nedaleko byl od doma, poslal do njego sotnik prijateljev, govoreči jemu: Gospodine! ne zadavaj sobě raboty; ibo jesm tobě ne jesm dostojny, abys všel pod strěhu moju.
7 Zatom i samogo sebe ne jesm iměl za dostojnogo, abyh iměl prijdti do tebe; no rěči slovo, a bude ozdravjany sluga moj.
8 Ibo jesm tobě i ja člověk pod močju postavjeny, imajučih pod soboju vojinov, i govorju tomu: Idi, a ide, a drugomu: Prijdi, a prihodi, a slugě mojemu: Čini to, a čini.
9 Itak uslyšavši to Jezus, udivil jemu se, i obrativši se, rěkl do ljuda, ktory za njim šel: Govorju vam, jesm že navet v Izraelu tak velikoj věry ne našel.
10 A vrativši se do doma ti, ktori byli poslani, našli slugu, ktory se zlo iměl, zdravogo.
11 I stalo se zautra, že šel do grada, ktore zovut Naim, a šlo s njim mnogo jego učenikov i ljud veliky.
12 A kogdy se približil do vrata grada, itak vot iznošeno mrtvogo, syna jedinogo svojej materi, a ta byla vdovoju, a s njeju šel velika tolpa togo grada.
13 Kogdy ju ugleděl Gospodin iměl simpatiju, i rěkl jej: Ne plači!
14 I pristupivši dotknul grob, (a ti, ktori nesli, stanuli) i rěkl: Mladenče! tobě govorju, vstani.
15 I usědl on, ktory umrl, i začel govoriti; i oddal go materi jego.
16 Itak vsih strah pojel, a slavili Boga, govoreči: Prorok veliky vstal medžu nami, a Bog prišel do ljuda svojego.
17 I razošla se o njim ta věst po cěloj Judzkoj zemji, i po cěloj okolnoj krajině.
18 I objavili Joanu učeniki jego o tym vsem. A Joan pozvavši dvoh iz učenikov svojih,
19 Poslal jih do Jezusa, govoreči: Ty jesi toj, ktory ima prijdti, či drugogo čekati imamo?
20 A kogdy prišli do njego ti muži, rěkli: Joan Krestitelj poslal nas do tebe, govoreči: Ty jesi toj, ktory ima prijdti, či drugogo čekati imamo?
21 A v toj časině mnogo ljudij ozdravil od hvorob, od nemoči, i od duhov zlyh, i mnogo slěpyh vid daroval.
22 A odgovarjajuči Jezus, rěkl jim: Idite i objavite Joanu, čto jeste viděli i slyšali. že slěpi videt, hromi hodet, leprosni berut očiščenje, gluši slyšet, umrli vozkresnut, a ubogym razkazano Evangelja.
23 A blagoslavjany jest, ktory by se ne sumněval v mene.
24 A kogdy odšli poslanniki Joanu, začel govoriti do ljudu o Joanu: Čto jeste izšli na pustynji viděti? Či trn hvějuči se od větra?
25 No čto jeste izšli viděti? Či člověka v mekku oděžju oblěčenogo? Vot ti, ktori v oděžah dragyh i v radosti živut, sut v domah kraljevskyh.
26 No čto jeste izšli viděti? Či proroka? Zapravdu govorju vam, že veče než proroka.
27 Toj ibo jest, o ktorym napisano: Vot Ja posylaju Angela mojego prěd obličjem tvojim, ktory prigotovi stežku tvoju prěd toboju.
28 Ibo govorju vam: večšego proroka iz tyh, ktori se iz žen rodet, ne imaš nad Joanom Krestiteljem nijednogo; no kto najmenši jest v kraljevstvu Božjim, večši jest, neželi on.
29 Itak ves ljud slyšeči to, i mytnici, slavili Boga, suči kreščeni krestom Joana.
30 No Farizeji i učeni v Pismu nenaviděli naměr Božji sami protiv sobě, ne suči kreščeni od njego.
31 I rěkl Gospodin: S kym itak imam sravniti ljudij roda togo, a komu sut podobni?
32 Podobni sut dětam, ktore sědet na trgu, a jedni na drugyh zovut, govoreči: Jesmo igrali vam, a jeste ne tancevali; jesmo pěvali žalostne pěsnje, a jeste ne plakali.
33 Ibo prišel Joan Krestitelj, i hlěba ne jeduči i vina ne pijuči, govorite: Djavla ima.
34 Prišel Syn člověčsky jeduči i pijuči, a govorite: Vot člověk je i pije vina, prijatelj mytnikov i grěšnikov.
35 No opravdana jest mudrost od vsih synov svojih.
36 I prosil go něktory iz Farizejev, aby s njim jel. A tak vševši v dom Farizejev, usědl.
37 A vot žena, ktora byla v gradu grěšna, dověděvši se, že sědi v domu Farizejskym, prinesla alabastrovu banku masti;
38 A stanuvši iz zada u nog jego, plačuči začela solzami polivati jego nogy, a vlasami glavy svojej je iztirala, i cělovala nogy jego, i mastju mazala.
39 A videči to Farizej, ktory go pozval, rěkl sam v sobě, govoreči: Jestli on jest prorokom, věděl by, ktora i kaka jest ta žena, čto go dotyče; ibo jest grěšniceju.
40 A odgovarjajuči Jezus, rěkl do njego: Simone! imam tobě něčto pověděti, a on rěkl: Pověd, Učitelju!
41 Iměl něktory lihvar dvoh dolžnikov; jedin dolžen byl petsot grošej, a drugy petdeset.
42 A kogdy oni ne iměli čim zaplatiti, odpustil obom. Pověd itak, ktory iz njih vyše go ljubiti bude?
43 A odgovarjajuči Simon, rěkl: Myslim, že toj, ktoromu veče odpustil. A on jemu rěkl: Dobro jesi razsudil.
44 I obrativši se do ženy, rěkl Simonu: Vidiš tu ženu? Jesm všel do doma tvojego, jesi ne dal vody na nogy moje; no ona solzami prolila nogy moje, i vlasami glavy svojej iztirala.
45 Ne jesi cěloval mene, no ona kako vošla, ne prěstala cělovati nog mojih.
46 Ne jesi pomazal maslom glavy mojej, no ona mastju pomazala nogy moje.
47 Začto, govorju tobě, odpuščeno jej mnogo grěhov, ibo mnogo ljubila; a komu malo odpuščeno, malo ljubi.
48 A on jej rěkl: Odpuščeno sut tobě grěhy.
49 I začeli sědeči pri njimi govoriti medžu soboju: Kym jest toj, ktory navet grěhy odpuščaje?
50 I rěkl do ženy: Věra tvoja tebe izbavila. Idi v pokoju.

## Razděl 8

1 I stalo se potom, že on hodil po gradah i po gradkah kažuči i razkazyvajuči kraljevstvo Božje, a dvanadset byli s njim,
2 I něktore ženy, ktore ozdravil od duhov zlyh i od nemoči jih, kak Mariju, ktoru zvano Magdalenoju, iz ktoroj sedm djavlov izšlo;
3 I Joana, žena Huzogo, urednika Herodova, i Suzana, i inyh mnogo, ktore jemu služili iz iměnja svojih.
4 A kogdy se shodil veliky ljud iz raznyh měst pri njim, rěkl črěz parabolu;
5 Izšel razsevatelj, aby razsějival sěmena svoje; a kogdy on razsějival, jedno padlo pri stežkě i toptano jest, a ptice nebeske pojeli je.
6 A druge padlo na kamen, a kogdy vozošlo, ushlo, ibo že ne imělo mokrosti.
7 A druge padlo medžu trny; no trny zajedno s njim izrastli, i dušili je.
8 A druge padlo na zemju dobru, a kogdy vozošlo, prineslo korist stokratnu. To govoreči zval: Kto ima uši k slyšanju, nehaj slyše!
9 I pytali go jego učeniki, govoreči: Čto by to byla za parabola?
10 A on jim rěkl: Vam dano věděti tajnost kraljevstva Božjego; no inym v parabolah, aby videči ne viděli, a slyšeči ne razuměli.
11 A ta parabola znači: sěme jest slovo Božje.
12 A pri stežkě sut ti, ktori slyšet, zatom prihodi djavol i izbiraje slovo iz srdca jih, aby uvěrivši, ne byli spaseni.
13 A ti, ktori na kamenju sut, kogdy slyšet, s radostju slovo prijmut, no korenja ne imajut. Ti do časa věret, a po pokušenju uže odstupajut iz věry.
14 A ktore padlo medžu trny, sut ti, ktori slyšet slova: no odševši, od nepokoja i bogatstv, i radosti žitja byvajut dušeni, i ne prinoset koristi.
15 No ktore padlo na zemju dobru, sut ti, ktori v srdcu galantnom i dobrom slyšano slovo hranet, i plod prinoset v trpělivosti.
16 A nijedin zapalivši svěču, ne pokryvaje jej sudom, ni jej klade pod lože, no ju postavet na svěčniku, aby ti, ktori vhodet, viděli světlo.
17 Ibo ne imaš ničto tajnogo, čto by ne imělo byti objavjeno; i ne imaš ničto ukrytogo, čego by ne dověděno, i čto by na javu ne izšlo.
18 Zatom gledajte, kako slyšite: ibo kto ima, tomu bude dano, a kto ne ima, i to, čto mysli, že ima, bude odjeto od njego.
19 Itak prišli do njego mati i brati jego; no do njego pristupiti ne mogli iz povoda ljuda.
20 I dano jemu znati, govoreči: Mati tvoja i brati tvoji stojet prěd domom, hčuči tebe viděti.
21 A on odgovarjajuči, rěkl do njih: Mati moja i brati moji sut ti, ktori slova Božjego slyšet i činet jih.
22 I stalo se dnja jedinogo, že on vstupil v lod s učenikami jego, i rěkl do njih: Prěpravimo se na drugu stranu jezera. I pustili se.
23 A kogdy plavali, usnul. I napadla burja s velikym větrom na jezero, i lod se potopila, tak že byli v bezpečnosti.
24 A pristupivši, vozbudili go, govoreči: Učitelju, učitelju! pogynemo. A on vozbudivši se, zgromil větr i valy vodne, i byli spokojne, i stalo se utišenje.
25 Itak jim rěkl: Kde jest věra vaša?. A boječi se, divili se, govoreči jedni do drugyh: Kym že jest toj, ktori větram kaže i vodam, a sut jemu poslušne?
26 I priplyvali do krajiny Gadarenčikov, ktora jest protiv Galilei.
27 A kogdy vstupil na zemju, poběgl jemu muž něktory iz togo grada, ktori iměl djavli od nemalogo časa, a ne oblačal se v oděž, i ne žil v domu, jedino v grobah.
28 Toj ugleděvši Jezusa, vozkliknul, i upadl prěd njim, a glasom velikym rěkl: Čto ja imam s toboju, Jezuse, Syne Boga vrhovnogo? prošu tebe, ne muči mene.
29 Ibo kazal tomu duhu nečistomu, aby izšel iz togo člověka: ibo od mnogo časov vladal jim; a hoti go vezano lancuhami i v okovah go shranjano, jednako on raztrgnuvši okovy, byval od djavla na pustynju gnany.
30 I pytal go Jezus, govoreči: Čto imaš za ime? A on rěkl: Legion; ibo mnogo djavlov vstupilo v njego.
31 Itak go prosili, aby jim ne kazal odtud odidti v propast.
32 A bylo tam stado veliko svinej, ktoro se paslo na gorě, i prosili go, aby jim dopustil vstupiti v nje. I dopustil jim.
33 A izševši djavli iz togo člověka, vošli v svinje; i raztrgnulo se to stado běgom iz propasti do jezera, i utonula.
34 A videči pastyri, čto se stalo, uběgli; a poševši, objavili to v gradu i v selah.
35 I izšli, aby ogledali to, čto se stalo; a priševši do Jezusa, našli člověka togo, iz ktorogo izšli djavli, oblěčenogo, v dobrom stanju, sědučego u nog Jezusa, i bojali se.
36 Razkazali jim zato ti, ktori viděli, kako ozdravjano togo, ktory byl vladeny črěz běsov.
37 I prosilo go velika tolpa toj okolnoj krajiny Gadarenčikov, aby odšel od njih; ibo jih veliky strah obsegnul. A on vstupivši v lod, vratil se.
38 I prosil go on muž, iz ktorogo izšli djavli, aby byl pri njim; no go Jezus izslal, govoreči:
39 Vrati se se do doma tvojego, a glasi, kako velike věči Bog učinil. I odšel, po vsem gradu glasujuči, kako jemu velike věči Jezus učinil.
40 I stalo se, kogdy se vratil Jezus, že go prijel ljud; ibo na njego vsi očekyvali.
41 A vot prišel muž imenom Jair, a toj byl načelnikom synagogy; a pripadši do nog Jezusa, prosil go, aby všel v dom jego.
42 Ibo iměl dočerku jedinu okolo dvanadset lět, ktora už umirala. (A kogdy on šel, tiskal go ljud.)
43 A žena, ktora na izplyvanje krvi stradala od dvanadset lět, i iztratila na lěkarev vse svoje iměnje, i ne mogla byti od nikogo ozdravjena,
44 Pristupivši iz zada, dotknula dol oděži jego, a v tom samom vrěmenu se skončilo izplyvanje krvi jej.
45 I rěkl Jezus: Kto jest, ktory mene dotknul? a kogdy se vsi odkazali, rěkl Petr i ti, ktori s njim byli: Učitelju! ljud tebe tiska i ne ima města, a ty govoriš: Kto mene dotknul?
46 I rěkl Jezus: Dotknul mene někto, ibo jesm poznal, že moč od mene izšla.
47 A videči žena, že se ne ukryla, s drganjem pristupila i upadla prěd njim, i začto go dotknula, pověděla jemu prěd vsim ljudom, i kako momentalno ozdravjana byla.
48 A on jej rěkl: Dověrjaj, dočerko! věra tvoja tebe ozdravila; idi že v pokoju.
49 A kogdy on to ješče govoril, prišel něktory od načelnika synagogy, govoreči jemu: Umrla dočerka tvoja, ne trudi Učitelja.
50 No Jezus uslyšavši to, odgovoril jemu, govoreči: Ne boji se, jedino dověrjaj, a bude ozdravjana.
51 A vševši v dom, ne dopustil s soboju vstupiti nikomu, jedino Petru, i Jakobu, i Joanu, i otcu i materi toj děvky.
52 A plakali vsi, i narěkali nad njeju. No on rěkl: Ne plačite že! Ne umrla, no spi.
53 I smějali se iz njego, věduči, že umrla.
54 A on izgnavši von vsih, i vzel ju za ruku, pozval, govoreči: Děvko, vstani!
55 I vratil se duh jej; i vstala momentalno; i kazal, aby jej jesti dano.
56 I udivili se roditelji jej. A on jim kazal, aby nikomu ne govorili togo, čto se stalo.

## Razděl 9

1 A pozvavši Jezus dvanadset učenikov svojih, dal jim moč i vlast nad vsimi djavlami, aby ozdravjali hvoryh.
2 I razslal jih, aby kazali kraljevstvo Božje, i ozdravjali nemočnyh.
3 Itak rěkl do njih: Ne berite ničto na stežku, ni kyja, ni torby, ni hlěba, ni pěnezov, ni dvoh suknej imějte.
4 A do ktorogokoli doma vojdete, tam ostanite, i odtud izojdite.
5 A ktorikoli by vas ne prijeli, izhodeči iz grada togo, i prah iz nog vaših otresajte na svědočstvo protiv njim.
6 Izševši itak, hodili vse gradka, glasujuči Evangelje, a vesde hvoryh ozdravjajuči.
7 I uslyšal Herod, Tetrarh, o vsem, čto se dělo, i byl sumnlivy za to, že něktori govorili, že Joan vozkresnul.
8 A něktori zato glasili: Ilijaš se ukazal; a drugi, že jedin prorok iz tyh staryh vozkresnul.
9 Itak rěkl Herod: Joana jesm sěkl; kto že toj jest, o ktorym ja takyh věčij slyšu? i žedal go viděti.
10 A vrativši se Apostoli, govorili jemu, čtokoli činili. A on vzevši je s soboju, odstupil oddělno na město prazdno pri gradu, ktoro zovut Betsajda.
11 Kogdy se ljud o tym dověděl, šel za njim; a prijevši jih, govoril jim o kraljevstvu Božjem; a tyh, ktori ozdravjenja potrěbovali, ozdravjal.
12 A kogdy se denj začel kloniti k večeru, pristupivši ti dvanadset, rěkli jemu: Razpusti toj ljud, aby odševši do gradkov okolnyh, i do sela, i do gostincev, našli jelo; ibo jesmo tu na městu pustom.
13 No on rěkl do njih: Dajte že vy jim jesti. A oni pověděli: Ne imamo veče, jedino pet hlěbov i dvě ryby. Moglibysmo idti, i kupiti, aby toj ves ljud iměl jedu.
14 Ibo bylo mužev okolo peti tyseč. I rěkl do učenikov svojih: Kažite jim usěsti v vsakym redu po petdeset.
15 I učinili tak, i usědli vsi.
16 A on vzevši tyh pet hlěbov i te dvě ryby, pogledavši v nebo, blagoslavjal jim, i lomil i daval učenikam, aby kladli go prěd ljudom.
17 I jeli, i syti sut vsi; i sobrano, čto jim ostalo iz ostatkov, dvanadset košev.
18 I stalo se, kogdy on sam se oddělno molil, že s njim byli učeniki; i pytal jih govoreči: Za kogo mene imějut ljudi?
19 A oni odgovarjajuči rěkli: Joanom Krestiteljem, a drugi Ilijašem, a drugi govoret, že prorok něktory iz tyh staryh vozkresnul.
20 I rěkl jim: A vy za kogo imějte? A odgovarjajuči Petr rěkl: Hristosom, tym Božjim.
21 No on grozivši jim, kazal, aby togo nikomu ne govorili,
22 Govoreči: Syn člověčsky imaje mnogo trpěti, a byti odkydnutym od starših ljuda i od prědnějših duhovnikov i od naučenyh v Pismu, i byti ubity, a tretjego dnja vozkresnuti.
23 I govoril do vsih: Kto hče za mnoju idti, nehaj odkaže se samogo sebe, a nehaj bere križ svoj na vsaky denj, i slěduje mene.
24 Ibo ktokoli by htěl hraniti dušu svoju, izgubi ju; a ktokoli by izgubil dušu svoju za mene, toj ju hrani.
25 Ibo čto pomože člověku, hotby ves svět iziskal, kakby samogo sebe izgubil, ili sobě poškodil.
26 Ibo ktokoli by se stydil za mene i za slova moje, za togo se Syn člověčsky styditi bude, kogdy prijde v slavě svojej i v otcevskoj i svetyh Angelov.
27 No vam govorju pravdivo: Sut něktori iz tyh, ktori tu stojet, ktori ne čuti smrti, až ogledajut kraljevstvo Božje.
28 I stalo se po tyh besědah po osm dnjah vzevši s soboju Petra i Joana i Jakoba, vstupil na goru, aby se molil.
29 A kogdy se molil, stal se ina forma obličja jego, i oděž jego stala se běla i světla.
30 A vot dva muži razgovarjali s njim, a oni byli Mojzes i Ilijaš;
31 Pokazavši se v slavě, govorili o jego smrti, ktoru iměl pristupiti v Jeruzalemu.
32 A Petr i ti, ktori byli s njim, obrěmenjeni byli snom, a vozbudivši se, ugleděli hvalu jego i tyh dvoh mužev, ktori s njim stali.
33 I stalo se, kogdy oni odšli od njego, že rěkl Petr do Jezusa: Učitelju! dobro nam tu byti; zatom učinimo tri šatory, tobě jedin i Mojzesu jedin i Ilijašu jedin; ne věduči, čto govoril.
34 A kogdy on to govoril, stal se oblak, i otěnil jih; i bojali se, kogdy oni vhodili v oblak.
35 I stal se glas iz oblaka govoreči: Toj jest Syn moj mily, togo slyšite.
36 A kogdy se stal toj glas, najdeny jest sam Jezus. A oni molčali, i ne govorili v te dni nikomu ničto iz togo, čto viděli.
37 I stalo se zautra, kogdy oni spustili se iz gory, že jemu ljud veliky priběgl.
38 A vot muž iz togo ljuda pozval, govoreči: Učitelju! prošu tebe, gledi na syna mojego; ibo jedinogo imam.
39 A vot duh zly obhvača go, a momentalno kriči. On raztrga go, slina teče se iz njego, a ledva odhodi od njego, kogda bije go.
40 I jesm prosil učenikov tvojih, aby go izgnali; no ne mogli.
41 Itak Jezus odgovarjajuči rěkl: O rodu nevěrny i prěvratny! dokud s vam budu, i dokud vas trpěti budu? Privedi tu syna tvojego.
42 A naglo, kogdy on prihodil, raztrgnul go djavol i raztrgnul; no Jezus zgromil duha nečistogo i ozdravil mladenca, i oddal go otcu jego.
43 I udivili se vsi nad velmožnostju Božju. A kogdy se vsi divili vsem věčam, ktore činil Jezus, rěkl do učenikov svojih:
44 Skladajte vy do uši vaših slova te: ibo Syn člověčsky ima byti prědany v ruky ljudske.
45 No oni ne razuměli togo slova, i bylo ukryto od njih, že slova pojeti ne mogli, i ne směli go pytati o to slovo.
46 I vozbudila se ogovarjanje medžu njimi, kto by iz njih byl najvelikym.
47 A Jezus videči myslji srdca jih, vzevši děte, postavil je pri sobě,
48 I rěkl jim: Ktokoli prijel to děte v imeni mojem, mene prijma; a ktokoli mene prijel, prijma togo, ktory mene poslal: ibo kto jest najmenši medžu vsimi vam, toj bude velikym.
49 A Joan odgovarjajuči, rěkl: Učitelju! Jesmo viděli něktorogo v imenu tvojim djavli izganjajučego, i jesmo zabranjali jemu, zatom že za toboju s nami ne hodi.
50 I rěkl do njego Jezus: Ne zabranjajte jemu; ibo kto ne jest protiv nam, za nami jest.
51 I stalo se, kogdy se izpolnili dni, aby byl vzety v goru, šel do Jeruzalema.
52 Itak poslal poslov prěd soboju; ktori vošli do gradka Samarijanikogo, aby jemu prigotovili gostinec.
53 No oni go ne prijeli, zatom že obličje jego obračeno bylo do Jeruzalema.
54 A videči to učeniki jego, Jakob i Joan, rěkli: Gospodine! hčeš, že rěčemo, aby ogonj spustil se iz neba i spalil jih, kako i Ilijaš učinil?
55 No Jezus obrativši se, zgromil jih, i rěkl: Ne znate vy, kakogo jeste duha.
56 Ibo Syn člověčsky ne prišel, gubiti duš ljudskyh, no hraniti. I šli do inogo gradka.
57 I stalo se, kogdy oni šli, že na stežkě rěkl něktory do njego: Pojdu za toboju, kdekoli pojdeš, Gospodine!
58 A Jezus jemu rěkl: Lisi imajut jamy, a ptice nebeske gnězda; no Syn člověčsky ne ima, o čto by glavu oprl.
59 I rěkl do drugogo: Pojdi za mnoju! No on rěkl: Gospodine! dopusti mně najprvo odidti i pogrebti otca mojego.
60 No jemu Jezus rěkl: Nehaj umrli pogrebajut mrtvyh svojih; a ty idi, glasi kraljevstvo Božje.
61 Rěkl tož i drugy: Pojdu za toboju, Gospodine! no mně najprvo dopusti proščati se se s tymi, ktori sut v domu mojem.
62 Rěkl do njego Jezus: Nijedin, ktory by položil ruku svoju do pluga, a ogledal by se nazad, ne jest dostojny do kraljevstva Božjego.

## Razděl 10

1 A potom naznačil Gospodin i drugyh sedmdeset, i razslal jih po dvoh prěd obličjem svojim do vsakogo grada i města, do ktorogo prijdti iměl.
2 I govoril jim: Žetva zaisto velika, no rabotnikov malo; prosite itak Gospodina žetva, aby izgnal rabotnikov na žetvu svoju.
3 Idite: Vot ja vas posylaju kako baranky posrěd volkov.
4 Ne nosite měška, ni torby, ni obuvi, i nikogo na stežkě ne pozdravjajte;
5 A do ktorogokoli doma vojdete, naprěd govorite: Pokoj tomu domu.
6 A jestli by tam byl ktory syn pokoja, odpočne nad njim pokoj vaš; a jestli ne, vrati se do vas.
7 A v tom domu ostanite, jeduči i pijuči to, čto imajut; ibo dostojny jest rabotnik zaplaty svojej; ne prěhodite iz doma do doma.
8 A do ktorogokoli grada byste vošli, i jeste byli prijeti, jedite, čto prěd vas položet;
9 I ozdravjajte hvoryh, ktori by v njem byli, a govorite jim: Približilo se do vas kraljevstvo Božje.
10 A do ktorogokoli byste grada vošli, a vas by ne prijeli, izševši na ulice jego, govorite:
11 I prah, ktory priložil se do nas iz grada vašego, otresajemo na vas; ibo to nehaj imate věděti, že se do vas približilo kraljevstvo Božje.
12 A govorju vam: V Sodomu v tom dnju vyše milo bude, než tomu gradu.
13 Běda tobě, Horazině! běda tobě, Betsajdo! ibo kakby se v Tiru i v Sidonu te čudesa staly, ktore se staly u vas, davno by byli oblěčeni do pokajanja i v pepelu sědeči pokajali se.
14 Zato Tiru i Sidonu bude vyše milo na sudu, než vam.
15 A ty, Kafarnaum! ktoro jesi až do neba vozvyšeno, až do pekla budeš byti kydnuto.
16 Kto vas slyše, mene slyše: a kto vam grdi, mnoju grdi; a kto mnoju grdi, grdi tomu, ktory mene poslal.
17 A tak vratili se ti sedmdeset s radostju, govoreči: Gospodine! i djavli se nam poddadut v imenu tvojem.
18 Itak jim rěkl: Jesm viděl satana, kako blěskavicu iz neba padajučego.
19 Vot vam davaju moč, abyste toptali po zmijah i po skorpionah i po cěloj moči neprijateljskoj, a ničto vam ne poškodi.
20 Ibo ne radujte se iz togo, že se vam duhi poddadut; no skorěje radujte se, že imena vaše napisane sut v nebesah.
21 V toj časině razradoval se Jezus v duhu, i rěkl: Slavju tebe, Otče, Gospodine neba i zemji! jesi te věči ukryl prěd mudrymi i tymi, ktori mnogo prěžili. A jesi objavil je dětetkam; zapravdu, Otče! Se tak podobalo tobě.
22 Vse věči dane mně sut od Otca mojego, a nikto ne zna, kym jest Syn, jedino Otec. I kym jest Otec, jedino Syn zna i toj, komu by Syn htěl to objaviti.
23 Itak obrativši se do učenikov, rěkl jim: Blagoslavjane sut oči, ktore videt, čto vy vidite.
24 Ibo govorju vam, že mnogo prorokov i kraljev žedali viděti, čto vy vidite, no ne viděli; i slyšati, čto vy slyšite, no ne slyšali.
25 A vot něktory mnih vstal, pokušajuči go i govoreči: Učitelju! čto imam činiti, abyh naslědil život věčny?
26 A on rěkl do njego: V zakonu čto napisano, kako to čitaš?
27 A on odgovarjajuči rěkl: Budeš miloval Gospodina, Boga tvojego, iz vsego srdca tvojego, i iz cěloj duši tvojej, i iz cěloj sily tvojej, i iz cěloj myslij tvojej; a bližnjego tvojego, kako samogo sebe.
28 I rěkl jemu: Dobro jesi odgovoril; to čini, a budeš žil.
29 A on hčuči samogo sebe opravdati, rěkl do Jezusa: I kto jest mně bližnji?
30 No Jezus odgovarjajuči rěkl: Člověk něktory spuščal se iz Jeruzalema do Jeriha, i upadl medžu razbojnikami, ktori razgrabivši go i rany jemu zadavši, odšli. Ostavivši go pol mrtvogo.
31 I pridalo se, že něktory duhovnik šel toju stežkoju, a ugleděvši go, prěšel.
32 Takože i Levit, dostavši se na to město, a priševši i ugleděvši go, prěšel.
33 No něktory Samaritan jeduči, prijehal do njego, ugleděvši, iměl simpatiju za njego.
34 A pristupivši svezal rany jego, a nalivši olej i vino, i vloživši go na skotu svojem, vodil go do gostinca, i dogledal go, aby snova stal se zdravy.
35 A zautra odježdžajuči, izjel dva groše, i dal gospodaru, govoreči: Dogledaj go, a jestli čtokoli vyše položiš, ja, kogdy vraču se, oddam tobě.
36 Ktory itak iz tyh trěh jest po tvojem mněnju bližnjim tomu, ktory upadl medžu razbojnikami?
37 A on rěkl: Toj, ktory učinil milosrdje nad njim. Rěkl jemu itak Jezus: Idi že, i učini takože.
38 I stalo se, kogdy oni šli, že on všel do něktorogo gradka, a žena něktora, imenom Marta, prijela go do doma svojego.
39 A ta iměla sestru, ktoru zvano Marijeju, ktora usědši u nog Jezusa, slyšala slov jego.
40 No Marta razsějana byla okolo raznoj služby; I pristupivši, rěkla: Gospodine! i ne dbaš, že sestra moja mene samoju ostavila, abyh služila? Rěči jej, aby mně pomogla.
41 A odgovarjajuči Jezus rěkl jej: Marto, Marto! Dbaš i bezpokojiš se o mnogo věčah;
42 No toliko jedinogo potrěba. No Marija dobru čest izbrala, ktora od njej odjeta ne bude.

## Razděl 11

1 I stalo se, kogdy on byl na něktorom městu, moleči se, že kogdy prěstal, rěkl do njego jedin iz učenikov jego, Gospodine! Nauči nas moliti se, tak kako i Joan naučil učenikov svojih.
2 I rěkl jim: Kogdy molite se, govorite: Otče naš, něktory jest v nebesah! Sveti se ime tvoje; prijdi kraljevstvo tvoje; bud volja tvoja, kako v nebu tak i na zemji.
3 Hlěba našego každodenny daj nam tutdenj.
4 I odpusti nam grěhy naše, kako i my odpuščamo našim vinnikam. A ne vedi nas v pokušenje, no nas izbavi od zlogo.
5 Zatom rěkl do njih: Kto iz vas iměti bude prijatelja, i pojde do njego o polnoči i rěče jemu: Prijatelju! Daj zajem mně tri hlěby;
6 Ibo prijatelj moj prišel iz stežky do mene, a ne imam, čto prěd njego položiti.
7 A on suči v domu, odgovoril by govoreči: Ne bezpokoji mně; už sut dveri zaključene, a děti moje sut so mnoju v pokoju; ne mogu vstati, abyh tobě dal.
8 Hot by jemu dalje i dalje bil v dveri, govorju vam: Hot by jemu ne vstal i dal. Zatom že jest prijateljem jego, ibo za bezstydno nastojanje jego by vstal, dal jemu, koliko potrěbuje.
9 I vam govorju: Prosite, a bude vam dano; iščite, a nahodite; stukajte, a bude vam otvorjeno.
10 Vsaky ibo, kto prosi, bere, a kto išče, nahodi, a tomu, ktory stuka, bude otvorjeno.
11 A ktory iz vas prosi kako syn otca o hlěb i dostane od njego kamenj? Ili kakby prosil o rybu, by dostal od njego vměsto ryby zmiju?
12 Ili kakby prosil o jajce, či jemu da skorpiona?
13 Zato vy, suči zlymi, možete dobre dary davati dětam vašim: koliko veče Otec vaš nebesky da Duha Svetogo tym, ktori go o njego proset?
14 Itak izganjal djavla, ktory byl němy. I stalo se, kogdy izšel toj djavol, prěgovoril němy; i divoval se ljud.
15 No něktori iz njih govorili: Črěz Beelzebuba, kneza djavolskogo, izganja běsov.
16 Drugi snova pokuseči go, žedali znaka od njego iz neba.
17 No on videči myslji jih, rěkl jim: Vsakogo kraljevstvo razděljeno samo protiv sobě pustěje, a dom na dom padaje.
18 A jestli i satan razděljeny jest protiv sobě, kako se ostane kraljevstvo jego? ibo govorite, že ja črěz Beelzebuba izganjaju běsov.
19 A jestli ja črěz Beelzebuba izganjaju běsov, syni vaši črěz kogo jih izganjajut? Zatom oni budut sudjami vašimi.
20 No jestli ja prstom Božjim izganjaju běsov, zapravdu prišlo do vas kraljevstvo Božje.
21 Kogdy monarh oružny shranja dvor svoj, v pokoja sut iměnja jego;
22 No kogdy močnějši nad njem nastupivši, pobědi go, odimaje vse oružje jego, v ktore dověril, a plěny jego razda.
23 Kto ne jest so mnoju, protiv mene jest; a kto ne sbiraje so mnoju, razprašaje.
24 Kogdy duh nečisty izhodi od člověka, hodi se po městah suhyh, iščuči odpočivanja, a ne naševši, govori: Vraču se do doma mojego, odkud jesm izšel.
25 A priševši nahodi očiščeny i dekorovany.
26 Itak ide i bere s soboju sedm inyh duhov gorših než on sam, a vševši živut tam, i byvajut věči poslědnje člověka togo gorše, než prve.
27 I stalo se, kogdy on to govoril, že voznesši glas něktora žena iz ljuda, rěkla jemu: Blagoslavjany život, ktory tebe nosil, i prsi, ktore jesi sosal!
28 No on rěkl: Očevidno blagoslavjani sut, ktori slyšet slov Božjego i shranjajut go.
29 A kogdy se ljud sobral, začel govoriti: Toj rod zlym rodom jest; znaka išče, no jemu znak ne bude dano, jedino toj znak proroka Jony.
30 Ibo kako Jona byl znak Ninivitam, tak bude i Syn člověčsky tomu rodu.
31 Kraljeva iz juga stane na sudu s mužami roda togo, i osudi jih; ibo prijehala od koncev zemji, aby slyšala mudrosti Salomona; a vot tu veče, než Salomon.
32 Muži Niniviti stanut na sudu s tym rodom i osudet go, zatom že pokajali se na propověd Jony; a vot tu veče, než Jona.
33 A nikto svěču zapalivši, ne postavja jej v tajnosti, ni pod korec, no na svěčnik, aby ti, ktori vhodet, světlo viděli.
34 Svěčeju těla jest oko; jestli by oko tvoje bylo čiste, vse tělo tvoje bude jasno; a jestli by zlo bylo, tělo tvoje temno bude.
35 Gledaj itak, aby světlo, ktoro jest v tobě, ne bylo temnotoju.
36 Jestli itak vse tělo tvoje jasno bude, ne imajuči kakoj čestky zatmjenoj, bude vse tak jasno, že tebe kako svěča blěskom osvěti.
37 A kogdy to govoril, prosil go něktory Farizej, aby jel oběd u njego; vševši itak, usědl za stolom.
38 A videči to Farizej, divoval se, že se umyl prěd obědom.
39 I rěkl Gospodin do njego: Tutčas vy, Farizeji! To, čto jest vně čašky i misky, čistite, no to, čto jest vnutri vo vas, polno jest graběži i zlosti.
40 Bezumni! či toj, ktory učinil to, čto jest vně, ne učinil tož togo, čto jest vnutri?
41 Ibo i iz togo, čto jest vnutri, davajte milostynju, a  vse věči budut vam čiste.
42 No běda vam, Farizeji! že davajete desětinu iz mety, i iz ruty, i iz vsakoj zeleniny, no opuščajete sud i ljubov Božju: te věči trěba činiti, a tyh ne opuščati.
43 Běda vam Farizeji! že ljubite prve města v synagogah i pozdravjenja na trgah.
44 Běda vam, naučeni v Pismu i Farizeji liceměri! ibo jeste kako groby, ktoryh ne viděti, a ljudi, ktori hodet po njih, ne znajut o njih.
45 A odgovarjajuči něktory iz zakonnikov, rěkl jemu: Učitelju! To govoreči i nas sramiš.
46 A on rěkl: I vam zakonnikam běda! ibo obrěmenjate ljudij brěmenami nesnosnymi, a sami navet ne jedinym prstom svojim tyh brěmen ne dotyčete.
47 Běda vam! že postavjate groby prorokov, a otci vaši ubili jih.
48 Zapravdu svědčite, že se ljubite v dělah otcev vaših; ibo oni jih ubili, a vy postavjate groby jih.
49 Zato tož mudrost Božja rěkla: Poslju do njih prorokov i Apostolov, a iz njih něktoryh ubivati i prěslědovati budut;
50 Aby iskano od togo roda krve vsih prorokov, ktora prolita jest od osnovanja světa,
51 Od krve Abla až do krve Zaharije, ktory izgynul medžu oltarom i crkovju; zapravdu govorju vam, budut iskati od roda togo.
52 Běda vam zakonnikam! ibo jeste vzeli ključ uměnja; sami jeste ne vošli, a tym, ktori vstupiti htěli, jeste zabranjali.
53 A kogdy jim to govoril, začeli na njego naučeni v Pismu i Farizeji mnogo natirati, i pričinu jemu davati do govorjenja o mnogo věčah;
54 čekajuči na njego i iščuči, aby nečto hvatili iz ust jego, aby go obvinili.

## Razděl 12

1 Medžu tym, kogdy se sobralo mnogo tyseči ljuda, tak že jedni po drugyh toptali, začel govoriti do učenikov svojih. Naprěd shranite se kvasa Farizejskogo, ktory jest liceměrje.
2 Ibo ne jest ničto ukrytogo, čto by objavjeno byti ne imělo, ni tajnogo čego by se dověděti ne imalo.
3 Zatom, čto jeste govorili v temnosti, na světlu slyšano bude, a čto jeste v uho šeptali v komorah, razglašeno bude na strěhah.
4 A govorju vam prijateljam mojim: Ne bojite se tyh, ktori tělo ubivajut, a potom ne imajut čto by veče učinili.
5 No vam ukažu, kogo se bojati imate: Bojite se togo, ktory, kogdy ubije, ima moč kydnuti do peklnogo ognja; zapravdu govorju vam, togo se bojite.
6 Či peti vrabcev ne prědadut za dva groši? Ibo nijedin iz njih ne jest v nepameti prěd obličjem Božjim.
7 Očevidno i vlasy glavy vašej vse sut sčisljene. Zatom se ne bojite, nad mnogo vrabcami vy jeste čestnějši.
8 A govorju vam: Vsaky, ktory by mene izpověděl prěd ljudami, i Syn člověčsky izpově go prěd Angelami Božjimi.
9 No kto by se mene odkazal prěd ljudami, odkažu se jego prěd Angelami Božjimi.
10 I vsakomu, kto by govoril slovo protiv Synu člověčskomu, bude jemu odpuščeno: no tomu, kto by protiv Duhu Svetomu bogohulil, ne bude odpuščeno.
11 A kogdy vas budut voditi do synagog, i do načelnikov, i do vlasti, ne bezpokojite se, kako i čto byste k obraně odgovoriti, ili čto byste govoriti iměli.
12 Ibo Duh Svety nauči vas toj že časině, čto byste govoriti iměli.
13 I rěkl jemu něktory iz ljuda: Učitelju! Rěči bratu mojemu, aby se so mnoju razdělil naslědstvom.
14 No jemu on rěkl: Člověče! Kto mene postavil sudjeju ili dělitjeljem medžu vami?
15 I rěkl do njih: Gledajte, a shranite se lakomstva: ibo ne od bujnogo iměnja život jego jest zaležny.
16 I pověděl jim parabolu, govoreči: Polje něktorogo člověka bogatogo bujny urodžaj prinesl.
17 I razmysljal sam v sobě, govoreči: Čto učinju, ibo ne imam, kde byh sobral plody moje?
18 I rěkl: To učinju: Razvalju gumna moje, a veče postavju i sberu tam vse plody moje i dobra moje;
19 I rěku do duši mojej: Dušo! imaš mnogo dobr složenyh na mnogo lět; odpočni že, jedi, pij, bud dobroj myslji.
20 No jemu rěkl Bog: O glupy, toj noči žedaje se duši tvojej od tebe. A to, čto jesi sdělal, čije bude?
21 Tak jest tomu, ktory sobě skarby sbere, a ne jest v Bogu bogaty.
22 I rěkl do učenikov svojih: Zato govorju vam, ne bezpokojite se o život vaš, čto byste jeli, ni o tělo, čim byste se oděvali.
23 Čestnějši jest život, než jeda, a tělo, než odědža.
24 Prigledajte se vranam, ibo ne sějut ni žnut, i ne imajut pivnice, ni gumna, a  je Bog živi; čim jeste vy čestnějši než ptice?
25 I kto iz vas neprěstanno mysleči, može pridati do rasta svojego jedin lakot?
26 Zato itak i najmenšej věči ne prěmožete, čemu se o ine bezpokojite?
27 Prigledajte se lilijam: kako rastut, ne rabotajut, ni predut; a govorju vam, že ni Salomon vo cěloj slavě svojej ne byl tak oděty, kako jedna iz tyh.
28 A travu, ktora tutdenj jest na polju, a zautra bude v peč kydnuta, Bog tak oděvaje. Kako veče vas, o malověrni!
29 Vy itak ne pytajte se, čto byste jedli, ili čto byste piti iměli, ni vysoko letite mysljami vašimi.
30 Ibo togo vsego narody světa iščut; no Otec vaš zna, že togo potrěbujete.
31 Očevidno iščite kraljevstva Božjego, a to vse bude vam pridano.
32 Ne boji se, o malo stado! ibo se podobalo Otcu vašemu, dati vam kraljevstvo.
33 Prodavajte iměnja vaše, a davajte milostynju; pripravite sobě měšky, ktore se ne niščet, skarb, ktory ne hudne v nebesah, kde zloděj pristupa ne ima, ni molj kazi.
34 Ibo kde jest skarb vaš, tam bude i srdce vaše.
35 Nehaj budut prěpasane bedra vaše, i svěči zapaljene.
36 A vy budite podobni ljudam očekyvajučim Gospodina svojego, daby se vratil iz svatby, aby kakby prišel, a stukal, směsta jemu otvorili.
37 Blagoslavjani ti slugi, ktoryh kogdy prijde Gospodin, čuvajučih nahodi; zapravdu govorju vam, že se prěpase, a posadi jih za stol, a hodeči se, bude jim služil.
38 A jestli by prišel o vtoroj straži, i o tretjej straži prišli by, a tak by jih našel, blagoslavjani sut ti slugi.
39 A to vědite, žeby kakby věděl gospodar, o ktoroj časině zloděj ima prijdti, žeby čuval, ne dopustil by podkopati doma svojego.
40 Zatom i vy budite gotovi; ibo o toj časině, o ktoroj ne očekyvajete se, Syn člověčsky prijde.
41 I rěkl jemu Petr: Gospodine! do nas govoriš tu parabolu, itak do vsih?
42 A Gospodin rěkl: Ktory itak jest věrny upravitelj i mudry, ktorogo Gospodin postavi nad čeljadju svoju, aby jim na čas prodaval krmu naznačenu?
43 Blagoslavjany jest toj sluga, ktorogo kakby prišel Gospodin jego, nahodi, kak tak čini;
44 Zapravdu vam govorju, že go nad vsimi tovarami svojimi postavi.
45 No jestli by rěkl toj sluga v srdcu svojim: Gospodin moj dolgo ne vrati se, i začel by biti slugov i služebnic, a jesti, piti i upivati se;
46 Prijde Gospodin slugi togo dnja, ktorogo ne očekyva, i časiny, ktoroj ne zna, i osamoti go, a město jemu da s nevěrnymi.
47 No toj sluga, ktory by znal volju Gospodina svojego, a ne byl gotovym, ni činil po volji jego, mnogo bude karany;
48 No kto by ne věděl, a činil věči dostojne karanja, menje udarov odnese; a od vsakogo, komu mnogo dano, mnogo se od njego napominati budut: a komu mnogo pověrjeno, veče budut htěti od njego.
49 Prišel jesm, abyh ogonj pustil na zemju, i čto hču, jestli už gori?
50 No imam byti krestom kreščeny; a kako jesm jest tisknuty, až se to ne izpolni.
51 Myslite, abyh prišel, pokoj davati na zemju? V nijednom slučaju, govorju vam, no raztrgnutje.
52 Ibo od togo časa bude jih pet v doma jedinym raztrgnutyh, tri protiv dvom, a dva protiv tri.
53 Povstane otec protiv synu, a syn protiv otcu, mati protiv dočerkě, a dočerka protiv materi, svekrov protiv snahě svojej, a snaha protiv svekrvi svojej.
54 Govoril tož i do ljuda: Kogdy vidite oblak vozhodeči od zapada, momentalno govorite: Prihodi silny dožd; i tak byvaje.
55 A kogdy větr věje od juga, govorite: Goreče bude; i byvaje tak.
56 Liceměri! Obraz neba i zemji razpoznati možete, a togo časa kako ne poznajete?
57 Začto i sami črěz sebe ne sudite, čto jest spravědlivo?
58 Kogdy itak ideš s protivnikom svojim prěd ured, staraj se se na stežkě, abys byl svobodny, by tebe očevidno ne trgal prěd sudju, a sudja by tebe podal stražu, a straž by tebe kydnul do vezenja.
59 Govorju tobě: Ne izojdeš odtud, až bys ne oddal poslědnjego groša.

## Razděl 13

1 A bliz tutčas byli prisutni něktori, oglašajuči jemu o Galilejčikah, ktoryh krov Pilat poměšal s jih žrtvami.
2 A Jezus odgovarjajuči, rěkl jim: Myslite, že tobě Galilejčiki nad vsimi inymi Galilejčikamiu grěšnějšimi byli, že take věči utrpěli?
3 V nijednom slučaju, govorju vam: i očevidno, jestli ne budete pokajati se, vsi takože pogynete.
4 Ili osmnadset tyh, na ktore upadla věža v Siloe i ubila jih. Myslite aby oni vinnějšimi byli nad vsimi ljudami živučih v Jeruzalemu?
5 V nijednom slučaju, govorju vam: i očevidno, jestli pokajati se ne budete, vsi takože pogynete.
6 I pověděl jim tu parabolu: Člověk něktory iměl figovo drěvo na svojim vinogradniku, a priševši, iskal na njim ploda, no ne našel.
7 Itak rěkl do sadovinka: Po trěh lětah, iščuči ploda na tym drěvu figovom, nijednogo ploda ne najdu. Izrěži je; ibo začto tu zemju ima obezsiliti?
8 No on odgovarjajuči rěkl jemu: Gospodine! ostavi go ješče i na to lěto, až je okopaju i obložu gnojivom;
9 Može prinese plod, a jestli ne, potom je izrěžeš.
10 I učil v jednoj synagogě v subotu.
11 A byla tam žena, ktora iměla duha nemoči osmnadset lět, a byla klonjena, tak že se ne mogla odgybati.
12 Kogdy ugleděl ju Jezus, pozval ju do sebe i rěkl: Ženo! jesi izbavjena od nemoči tvojej.
13 I vložil na nju ruky, a v tom samom vrěmenu odgnula se i hvalila Boga.
14 Itak odgovarjajuči načelnik nad synagogoju, ktory se mnogo gněval se, že Jezus v subotu ozdravjal, rěkl do ljuda: Šest dni jest, v ktore trěba rabotati; v te dni prihodite, ozdravjajte se, a ne v dnju suboty.
15 No jemu odgovoril Gospodin i rěkl: Liceměre, či vsaky iz vas v subotu ne odveže vola svojego, ili osla svojego od jasla-sadka, a ne vodi, aby go napojil?
16 A ta dočerka Abrahama, ktora byla svezana črěz satana už osmnadset lět, ne iměla byti razvezana od njego v dnju suboty?
17 A kogdy on to govoril, stydili se vsi protivniki jego: no ves ljud radoval se iz tyh vsih slavnyh děl, ktore byli dělani od njego.
18 Zatom rěkl Jezus: Komu podobno jest kraljevstvo Božje, a do čego je sravnju?
19 Podobno jest zrnu gorčice, ktore vzel člověk, kydnul do sada svojego; i rastlo i stalo se drěvom velikym, a ptice nebeske činili sobě gnězda na lozah jego.
20 I rěkl snova: Do čego sravnju kraljevstvo Božje?
21 Podobno jest kvasu, ktory vzela žena, ukryla go vo trěh měrah muky, až vse skvasilo se.
22 I hodil po gradah i gradkah, tak učeči a šel na stežkě do Jeruzalema.
23 I rěkl jemu něktory: Gospodine! itak malo tyh jest, ktori imajut byti spaseni? A on rěkl do njih:
24 Starajte se, abyste prějdti črěz těsne vrata; ibo govorju vam: Mnogo jih budut htěli vstupiti, no ne budut mogli.
25 Kogdy vstane gospodin i zaključi dveri, a začnete stati prěd dverami, i stukati vo dveri, govoreči: Gospodine, Gospodine! otvori nam, itak on odgovarjajuči rěče vam: Ne znaju, odkud jeste.
26 Itak začnete govoriti: Jesmo jedali prěd toboju i pili. Jesi učil na ulicah naših.
27 A on rěče: Govorju vam, ne znaju, odkud jeste; odidite od mene vsi, ktori činite krivdy.
28 Tam bude plač i skripěnje zubov, kogdy uvidite Abrahama, Izaaka, i Jakoba, i vsih prorokov v kraljevstvu Božjim, a samyh sebe von izkydnutyh.
29 I prijdut drugi od vozhoda i od zapada, i od sěvera, i od juga, a usědut za stolom v kraljevstvu Božjim.
30 A sut poslědnji, ktori budut prvymi, a sut prvi, ktori budut poslědnjimi.
31 V tom dnju pristupili něktori iz Farizejev, govoreči jemu: Izojdi, a idi odtud; ibo tebe Herod hče ubiti.
32 I rěkl jim: Idite, a kažite tomu lisu: Izganjaju běsov, i ozdravjaju tutdenj i zautra, a tretjego dnja dokonču moje dělo.
33 Ibo imaju tutdenj i zautra i pozautra hoditi na stežkě: ibo ne može byti, aby iměl prorok izgynuti, v městu poza Jeruzalemom.
34 Jeruzalem! Jeruzalem! ktoro ubivaš prorokov, a kamenuješ tyh, ktori do tebe byvajut poslani; kolikrat jesm htěl sobrati děti tvoje, tak kako ptak sbere ptičky svoje pod krilami, a jeste ne htěli.
35 Vot ostane vam dom vaš pusty. A zapravdu vam govorju, že mene ne uvidite, až prijde čas, kogdy rěčete: Blagoslavjany, ktory ide v imenu Gospodinskom.

## Razděl 14

1 I kogdy všel Jezus v dom něktorogo vyšnogo Farizeja v subotu, aby jel hlěb. Oni go podglědali.
2 A byl něktory opuhnuty člověk prěd njim.
3 A odgovarjajuči Jezus, rěkl do zakonnikov, i do Farizejev: Či jest dozvoljeno v subotu ozdravjati?
4 A oni molčali. Itak on dotknul go, ozdravil i odslal.
5 A odgovarjajuči rěkl do njih: Kakby vaš syn ili vol pade v studnju, ne směsta go iztegnete v dnju suboty?
6 I ne mogli jemu na to odgovoriti.
7 Pověděl tož jim parabolu, (videči, kako lěpše města izbirali,) govoreči jim:
8 Kakby jesi někto prizval na svatbu, ne usědi na lěpšim městu, by časom ne čestnějšy nad toboju byl prizvany od;
9 A priševši toj, ktory tebe i togo prizval, rěkl by tobě: Daj tomu město: a itak bys so stydom začel sěděti na poslědnjim městu.
10 No kakby jesi byl prizvany, usědi na poslědnjim městu; a kakby prišel toj, ktory tebe prizval, rěkl by tobě: Prijatelju! usědi se vyše; itak budeš iměl čest prěd sosedečimi s toboju.
11 Ibo vsaky, ktory se vozvyša, poniženy bude, a kto se ponižaje, vozvyšeny bude.
12 Govoril tož i tomu, ktory go prizval: Kogdy dělaješ oběd ili večerju, ne prizovi prijateljev tvojih, ni bratov tvojih, ni srodnikov tvojih, ni susědov bogatyh, aby tebe časom i oni snova ne prizvali, a stala by tobě se nagrada.
13 No kogdy dělaješ pir, prizovi ubogyh, hromyh I slěpyh,
14 A budeš blagoslovjenym; ibo ne imajut tobě čim nagraditi, no tobě bude nagradženo pri vozkresenju spravědlivyh.
15 A uslyšavši to něktory iz sosedečih, rěkl jemu: Blagoslavjany, ktory je hlěb v kraljevstvu Božjim.
16 A on jemu rěkl: Člověk něktory dělal věčeru veliku i prizval mnogo;
17 I poslal slugu svojego v časině věčery, aby rěkl prizvanym: Pojdite! ibo už vse gotovo.
18 I začeli se vsi izviniti. Prvy jemu rěkl: Jesm kupil polje, i imaju idti, a ogledati je, prošu tebe, iměj mene za opravdanogo.
19 A drugy rěkl: Jesm kupil pet par volov, I idu, abyh jih uviděl: prošu tebe, iměj mene za opravdanogo.
20 A drugy rěkl: Jesm se oženil, a zato prijdti ne mogu.
21 A vrativši se sluga, objavil to Gospodinu svojemu. Itak gospodar razgněvavši se, rěkl slugě svojemu: Idi bystro na ulice i na stežky grada, a ubogyh i hromyh i slěpyh vodi tu.
22 I rěkl sluga: Gospodine! Stalo se, kako jesi zapověděl, a ješče město jest.
23 I rěkl Gospodin do slugy: Idi na stežky i medžu plotami, a prinudi vstupjenje, aby byl napolnjeny moj dom.
24 Ibo govorju vam, že nijedin iz tyh mužev, ktori byli prizvani, ne vkusi věčery mojej.
25 I pošel s njim veliky ljud; a obrativši se, rěkl do njih:
26 Jestli někto ide do mene, a ne ima v nenavisti otca svojego, i materi, i ženy, i dětij, I bratov, I sester, navet i duši svojej, ne može byti učenikom mojim.
27 A ktokoli ne nese križa svojego, i ide za mnoju, ne može byti učenikom mojim.
28 Ibo kto iz vas, hočuči postaviti věžu,  najprvo usěvši, ne izkalkuluje, či ima dostatočno materiala?
29 Aby časom, kakby osnoval fundament, a dokončiti ne mogl, vsi ktori by to viděli, ne začeli se smějati iz njego,
30 Govoreči: Toj člověk začel postavjati, a ne mogl dokončiti.
31 Ili ktory kralj jeduči na vojnu, vojevati se s drugym kraljem, najprvo usěvši, ne mysli, mogliby deset tyseč pobědžati s tym, ktory vls dvadeset tysečami jede protiv njemu?
32 A jestli ne, kogdy on ješče jest daleko od njego, poslov izšlje do njego, i prosi o to, čto naleži, aby imali pokoj medžu soboju.
33 Tož i vsaky iz vas, ktory by se ne izrěkl vsyh iměnij svojih, ne može byti učenikom mojim.
34 Dobra jest solj; no jestli solj už vkusa ne ima, čim ju popraviti?
35 Ne dobra uže ni do zemji ni do gnoja, no ju von izkydet. Kto ima uši do slyšanja, nehaj slyše.

## Razděl 15

1 I približali se do njego vsi mytniki i grěšniki, aby go slyšali.
2 I roptali Farizeji i naučeni v Pismu, govoreči: Toj grěšnikov prijma i je s njimi.
3 I pověděl jim tu parabolu, govoreči:
4 Ktory iz vas člověk, kakby iměl sto ovec, a izgubil by jednu iz njih, ne ostavlja tyh devětdesěti i devěti na pustynji, a ne ide za toju, ktoru izgubil, až by ju našel?
5 A naševši ju, kladne ju na ramena svoje, radujuči se.
6 A priševši do doma, pozove prijateljev, i susědov, govoreči jim: Radujte se so mnoju; ibo jesm našel ovcu, ktora byla izgubjena.
7 Govorju vam, že taka bude radost v nebu nad jedinym grěšnikom obračajučim se, veče než nad devetdeseti i devěti spravědlivyh, ktori ne potrěbujut razkajanja.
8 Ili žena imajuči deset grošej, by izgubila jedin groš , či ne zapaljaje svěče, i ne izměta doma, i ne išče s spešnostju, až bz go našla?
9 A naševši, pozove prijateljek i susědov, govoreči: Radujte se so mnoju; ibo jesm našla groš, ktory jesm izgubila.
10 Tak, govorju vam, bude radost prěd Angelami Božjimi nad jedinym grěšnikom obračajučim se.
11 Tož rěkl: Člověk něktory iměl dvoh synov,
12 I rěkl mladějši iz njih otcu: Otče! Daj mně děl iměnja, ktory na mene pade. I razdělil jim iměnje.
13 A po nemnogo dnjah, mladějši syn zabravši vse, odšel v daleku krajinu, I razprašil tam iměnje svoje, živuči razpuščeno.
14 A kogdy vse izgubil, stal se glad veliky v toj krajině, a on začel nedostatok trpěti.
15 Prišel do jedinogo měščana toj krajiny, ktory go poslal do svojego dvora, aby pasl svinje.
16 I žedal napolniti želudok svoj jedoju, ktoru jedaly svinje; no jemu nikto jej ne daval.
17 Potom pomyslil, rěkl: O kako mnogo najemnikov otca mojego imajut dost hlěba, a ja od glada izgynu!
18 Vstavši itak, pojdu do otca mojego I rěku jemu: Otče! Jesm sgrěšil protiv nebu i prěd toboju.
19 I ne jesm dostojny veče byti zvany synom tvojim, učini mene jedinogo iz najemnikov tvojih.
20 Itak vstavši, pošel do otca svojego. A kogdy on ješče byl blizko, uviděl go otec jego, i iměl žalost do njego, priběgl, kydnul se na šiju jego, cěloval go.
21 I rěkl jemu syn: Otče! Jesm sgrěšil protiv nebu I prěd toboju, i už ne jesm dostojny, abyh byl zvany synom tvojim.
22 Rěkti itak otec do slug svojih: Prineste tu najlěpšu oděž, oblěčite go, i dajte prstenj na ruku jego, i obuv na jego nogy.
23 A privedite tolsto tele, ubijte go, a jěduči budemo radi.
24 Ibo toj syn moj mrtvz byl, a snova ožil; propadl, i najdeny jest; I začeli se radovati.
25 No starši syn jego byl na polju; a kogdy prihodeči približil se k domu, uslyšal muziky i tancev;
26 A pozvavši jedinogo iz slug, pytal, čto by to bylo.
27 A on jemu odgoviril: Brat tvoj prišel, tvoj otec ubil tolsto tele, ibo go zdravogo dostal.
28 I razgněval se, i ne htěl vstupiti; no otec jego izševši prosil go.
29 A on odgovarjajuči, rěkl otcu: črěz tak mnogo lět služu tobě, a nikogdy jesm ne prěstupil tvojej zapovědi; no jesi mně nikogdy ne dal teleta, abyh se s prijateljami mojimi radoval se.
30 No kogdy tvoj syn, ktory požrěl iměnje tvoje s kurvami, prišel, jesi ubil jemu to tolsto tele.
31 A on jemu rěkl; Syne! ty jesi vsakčas so mnoju, a vse dobra moje sut tvoje.
32 No trěba bylo radovati i obradovati se, že tvoj brat umrl, a snova ožil. Propadl a najdeny jest.

## Razděl 16

1 Govoril tož i do učenikov svojih: Člověk něktory byl bogaty, ktory iměl upravitelja. A bylo člověku kazano, že razprašal dobra jego.
2 A pozvavši go, rěkl jemu: Čto slyšu o tobě? Oddaj čislo iz upravy tvojej; ibo už veče ne budeš mogl upravjati.
3 I rěkl upravitelj sam do sebe: Čto učinju, ibo Gospodin moj odbral od mene upravu? Kopati ne mogu, izprašanja stydju se.
4 Znaju, čto učinju, že kogdy budu složeny iz upravy, prijmut mene do domov svojih.
5 Pozvavši itak do sebe vsakogo iz dolžnikov Gospodina svojego rěkl prvomu: Mnogo jesi vinny Gospodinu mojemu?
6 A on rěkl: Sto barel masla. I rěkl jemu: Vozmi zapis tvoj, a sedši bystro, napiši petdeset.
7 Potom drugomu rěkl: A ty jesi mnogo vinny? A on jemu rěkl: Sto korcev pšenice. I rěkl jemu: Vozmi zapis tvoj, a napiši osmdeset.
8 I pohvalil Gospodin upravitelja nespravědlivogo, že mudro učinil; ibo syni togo světa mudrějši sut nad synami světla s rodom svojim.
9 I vam govorju: Činite sobě prijateljev iz nespravědlivosti mamona, aby kogdy vse se dovrša, prijeli vas do věčnyh kvartir.
10 Kto věrny jest v malom, i v mnogo věrnym jest; a kto v malom nespravědlivy, i v mnogo nespravědlivym jest.
11 Zato jeste itak v upravě mamona nespravědlivogo věrnymi ne byli, pravdivy kto vam pověri?
12 A jestli jeste v čudžim věrnymi ne byli, kto vam da, čto vašego jest?
13 Nijedin sluga ne može dvom gospodinam služiti, ibo jedinogo bude iměl v nenavisti, a drugogo bude miloval; ili se jedinogo držati bude, a drugym prězri; ne možete Bogu služiti i mamonu.
14 A slyšali togo vsego i Farizeji, ktori byli htivi, i smějali se se iz njego.
15 I rěkl jim: Vy jeste, ktori sami sebe opravdyvajete prěd ljudami, no Bog zna srdca vaše; ibo čto jest u ljudij vysoko, gnusno jest prěd Bogom.
16 Zakon i proroki segajut až do Joana; a od togo časa kraljevstvo Bože razkazano byvaje, a vsaky se do njego siloju tiska.
17 I prostějše jest nebu i zemji minuti, než jednoj črtkě zakona upasti.
18 Vsaky, ktory opuščaje ženu svoju, a inu vozme, čini prěljubstvo; a kto od muža opuščenu vozme, čini prěljubstvo.
19 A byl něktory člověk bogaty, ktory se oblačal v šarlat i v biser, i upotrěbjal na vsaky denj ščedro.
20 Byl tož něktory prosak, imenom Lazar, ktory ležal u vrat jego pelny vrědov.
21 Žedajuči byti sytny iz ostatkov, ktore padali iz stola bogatyh; no i psi prihodeči lizali vrědy jego.
22 I stalo se, že umrl prosak, i odneseny byl od Angelov na lono Abrahama; umrl tož i bogač, i pogrebeny jest.
23 A suči v peklu, voznesši oči svoje, kogdy byl v mukah, ugleděl Abrahama iz daleka, i Lazara na lonu jego.
24 Itak bogač pozvavši, rěkl: Otče Abrahamě! pomiluj se nad mnoju, a pošlji Lazara, aby močil konec prsta svojego v vodě, a ohladil jezyk moj, ibo muky stradaju v tym plamenju.
25 I rěkl Abraham: Syne! pomni, jesi ty odbral dobro věči tvoje za života tvojego, a Lazar takože zlo; a tutčas on ima razkoš, a ty muky stradaješ.
26 A čto vyše, medžu nami i vam propast velika jest utvrdžena, aby ti, ktori hčut odtud prijdti do vas, ne mogli, ni oni odtud prijdti do nas.
27 A on rěkl: Prošu tebe itak, otče! abys poslal do doma otca mojego:
28 Ibo imam pet bratov. Aby jim svědočstvo prodal, aby tož i oni ne prišli na to město muky.
29 I rěkl jemu Abraham: Imajut Mojzesa i prorokov, nehaj jih slyšet.
30 A on rěkl: Ne, otče Abrahamě! no kakby kto iz mrtvyh pošel do njih, budut pokajati se.
31 I rěkl jemu: Zato že Mojzesa i prorokov ne slyšet, itak, hot by tož někto vozkresnul, ne uvěret.

## Razděl 17

1 I rěkl do učenikov: Ne možno, aby zle věči ne prijdut; no běda tomu, črěz ktorogo prihodet!
2 Lěpje by jemu bylo, aby mlynsky kamenj věšeny byl na šiji jego, i kydnuty byl v morje, než by jednomu iz tyh malyh zlo činil.
3 čuvajte! A jestli by sgrěšil protiv tobě brat tvoj, karaj go, a jestli by iměl žalj, odpusti jemu.
4 A hot by sedmkratno v dnju sgrěšil protiv tobě, i sedmkratno črěz denj se do tebe obratil, govoreči: Žalj mně togo; odpusti jemu.
5 I rěkli Apostoli Gospodinu: Razmnoži nam věry.
6 A Gospodin rěkl: Jestli byste iměli věru kako zrno gorčice, rěkli byste tomu drěvu lěsnoj figy: Izrvi se iz korenja, a vloži se v morju, slyšalo by vas.
7 I kto iz vas imajuči slugu, ktory by dělal oranje ili pasenje, kakby se vratil, momentalno by jemu rěkl: Pojdi, i usedi za stolom?
8 I očevidno, či jemu ne rěče: Kuhaj mně věčerok, prěpasaj se, služi mně, až se najem i napiju, a potom ty jedi i pij?
9 Či blagodari slugě tomu, že učinil to, čto jemu bylo kazano? 
10 Ne myslju tak. Takože i vy, kogdy učinite vse, čto vam kazano, govorite: Slugi nepotrěbni jesmo, ibo čto jesmo byli dolžni učiniti, jesmo učinili.
11 I stalo se, kogdy šel do Jeruzalema, že šel pograničje Samariji i Galileji.
12 A kogdy vhodil do něktorogo gradka, priběgalo do njego deset mužev hvoryh na lepru, ktori stanuli iz daleka.
13 A ti voznesši svoj glas, rěkli: Jezuse, Učitelju! Pomiluj se nad nami.
14 Jih ugleděvši, rěkl jim: Idite, okažite se duhovnikam. I stalo se, kogdy šli, že očiščeni byli.
15 No jedin iz njih uviděl, že jest ozdravjany, vratil se, velikym glasom hvaleči Boga;
16 I padl na lice svoje u nog jego, blagodaril jemu; a toj byl Samaritanin.
17 A Jezus odgovarjajuči, rěkl: či ne deset jest očiščenyh, a kde sut ti devet?
18 Ne pomyslili, aby se vratili, i dali hvalu Bogu. Jedino toj inozemec?
19 I rěkl jemu: Vstani, idi, věra tvoja tebe ozdravila.
20 A suči pytany od Farizejev, kogdy prijde kraljevstvo Božje, odgovoril jim i rěkl: Ne prijde kraljevstvo Božje s priměčanjem;
21 Ni rěkut: Vot tu, ili vot tam jest: ibo vot kraljevstvo Božje vnutri vas jest.
22 I rěkl do učenikov: Prijdut dni, že budete žedati, abyste viděli jedin denj iz dni Syna člověčskogo, no ne ogledajete.
23 I rěkut vam: Vot tu, ili vot tam jest; no ne hodite, ni běgajte za njimi.
24 Ibo kako blěskavica, blěstěje od jednoj strany, ktora jest pod nebom, až do drugoj. Tak bude so Synom člověčskym v dnju svojem.
25 No najprvo imaje mnogo stradati, i byti odkydnutym od naroda togo.
26 A kako bylo za dni Noego, tak bude i za dni Syna člověčskogo.
27 Jeli, pili, ženili se i za muž izhodili až do togo dnja, v ktorom všel Noe do arky, i prišel potop, i vsi umrli.
28 Takože tož kako se stalo za dni Lota, jeli, pili, kupovali, prodavali, sadili, postavjali.
29 No dnja togo, kogdy izšel Lot iz Sodomy, padal ogonj kako dožd s sěroju iz neba, i ubil vsih.
30 Tak tož bude v tom dnju, v ktorom se Syn člověčsky objavi.
31 Togo dnja, kto bude na strěhě, a věči jego v domu, nehaj ne spušča se, aby je vzel; a kto na polju, nehaj takože ne vračaje do togo, čto jest za njim.
32 Pripominajte ženu Lota.
33 Ktokoli by htěl hraniti dušu svoju, izgubi ju; a kto by ju izgubil, oživi ju.
34 Govorju vam: Toj noči bude dvoh na jednom ložu; jedin vzety bude, a drugy ostavjeny.
35 Dvě budut mlěti s soboju; jedna vzeta bude, a druga ostavjena.
36 Dvoh bude na polju; jedin bude vzety, a drugy ostavjeny.
37 A odgovarjajuči rěkli jemu: Kde Gospodine? A on jim rěkl: Kde bude mrtvec, tam se sberut i orli.

## Razděl 18

1 I pověděl jim ješče parabolu o tym, že se vsakčas potrěba moliti, a ne ustavati,
2 Govoreči: Byl něktory sudja v jednom gradu, ktory Boga ne bojal se, i člověka se ne stydil.
3 Byla tož vdova v tym gradu, ktora prihodila do njego, govoreči: Obrani mene prěd protivnikom mojim.
4 No on dolgo ne htěl. No potom rěkl sam do sebe: Hoti se Boga ne boju i člověka se ne stydju se,
5 Ibo že mně muči ta vdova, vozmu v obranu ju, aby na ostatok priševši, ne byla mně težka.
6 Rěkl itak Gospodin: Slyšite, čto govori nespravědlivy sudja.
7 A Bog ne obrani izbranyh svojih, ktori zovut do njego vo dnju i v noči, I bude trpělivy iz jih strany?
8 Govorju vam, že obrani jih skoro. No kogdy prijde Syn člověčsky, on nahodi věru na zemji?
9 Rěkl tož do něktoryh, ktori dověrili sami v sobě, že byli spravědlivymi, a inyh za ničto ne iměli, tu parabolu:
10 Dvoje ljudij vstupilo do crkvi, aby molili se, jedin Farizej a drugy mytnik.
11 Farizej stanuvši, tak sam se molil: Blagodarju tobě, Bože, že ne jesm kako ini ljudi, ktori sut predatori, nespravědlivi, dělajut prěljubstvo, kak i toj mytnik.
12 Postuju dvukratno v tydenj; davaju desetinu iz vsego, čto imam.
13 A mytnik stoječi iz daleka, ne htěl voznesti očij svojih v nebo, no se bil v prsi svoje, govoreči: Bože! bud milosrdny mně grěšnomu.
14 Govorju vam, že toj odšel opravdanym do doma svojego, veče neželi on: ibo kto se vozvyša, bude poniženy, a kto se ponižaje, bude vozvyšeny.
15 Prinošeno tož jemu děti, aby jih dotykal; no kogdy viděli to učeniki, zgromili jih.
16 No Jezus pozvavši jih, rěkl: Dopustite dětam prihoditi do mene, a ne zabranjajte jim; ibo takovym jest kraljevstvo Božje.
17 Zapravdu govorju vam: Ktokoli ne prijel kraljevstva Božjego kako děte, ne vojde do njego.
18 I pytal go něktory knez, govoreči: Učitelju dobry! čto imaju dělati, abhy naslědil život věčny?
19 I rěkl jemu Jezus: Začto mene zoveš dobrym? Nikto ne jest dobry, jedino jedin, to jest Bog.
20 Znaš zapovědi? Ne dělaj prěljubstva, ne ubivaj, ne kradi, ne svědči falšivo, čti otca tvojego i mati tvoju.
21 A on rěkl: To jesm vse dělal od mojej mladosti.
22 Čto uslyšavši Jezus, rěkl jemu: Jedinogo tobě ješče ne imaš; vse, čto imaš, prodaj, a razdaj ubogym, a budeš iměl skarb v nebu; potom prijdi i slěduj mene.
23 A on uslyšavši to, mnogo se smutil; ibo byl mnogo bogaty.
24 A kogdy go Jezus ugleděl mnogo smučenogo, rěkl: Kako težko bogatym, vojdti do kraljevstva Božjego!
25 Ibo prostějše jest velbludu prějdti črěz uho igly, než bogatomu vstupiti do kraljevstva Božjego.
26 Itak rěkli ti, ktori to slyšali: I kto može byti spaseny?
27 No on rěkl: Čto jest nemožno u ljudij, možno jest u Boga.
28 I rěkl Petr: Vot jesmo opustili vse, a jesmo pošli za toboju.
29 Itak jim rěkl: Zapravdu govorju vam, že ne imaš nikogo, ktory by opustil dom, ili roditeljev, ili bratov, ili ženu, ili děti za kraljevstvo Božje,
30 Aby ne dostal daleko veče v tym času, a v budučim věku život věčny.
31 A vzevši so soboju tyh dvanadset, rěkl jim: Vot vstupajemo do Jeruzalema, a izpolni se vse, čto napisano črěz prorokov o Synu člověčskom.
32 Ibo bude prědany poganam, i bude izsmějany, i poniženy, i go pljunut:
33 A bičevavši ubijut go; no dnja tretjego bude vozkrešenje.
34 No oni iz togo ničto ne razuměli, i bylo to slovo ukryto prěd njimi, i ne věděli, čto govorjeno.
35 I stalo se, kogdy se on približal do Jeriha, že něktory slěpy sěděl pri stežkě, proseči.
36 A uslyšavši ljud prěhodeči, pytal, čto by to bylo?
37 I pověděno jemu, že Jezus iz Nazareta tudy ide.
38 I pozval, govoreči: Jezuse, Syne Davida! pomiluj se nad mnoju.
39 No ti, ktori šli premo, zgromili go, aby molčal. No on tym veče zval: Syne Davida! pomiluj se nad mnoju.
40 Stanuvši itak Jezus, kazal go privesti do sebe; a kogdy se približil, pytal go, govoreči:
41 Čto hčeš, abyh tobě učinil? A on rěkl: Gospodine! abyh viděl.
42 A Jezus jemu rěkl: Vidi, věra tvoja tebe ozdravila.
43 I v tom samom vrěmenu viděl, i šel za njim, obožajuči Boga. Takože ves ljud to videči, dal hvalu Bogu.

## Razděl 19

1 A Jezus vševši, šel črěz Jeriho.
2 A byl tam muž, ktorogo zvano imenom Zahej, ktory byl načelnikom nad mytnikami i byl bogaty.
3 I žedal viděti Jezusa, kym on by byl; no ne mogl iz povoda ljuda, ibo byl malogo rasta.
4 A běgavši naprěd, vstupil na drěvo lěsnoj figy, aby go ugleděl; ibo tudy idti iměl.
5 A kogdy prišel na to město, pogledavši Jezus v goru, ugleděl go, i rěkl do njego: Zaheju! spusti se bystro na dol, ibo tutdenj imaju ostati v domu tvojem.
6 I spustil se bystro i prijel go s radostju.
7 A videči to vsi, roptali, govoreči: Do člověka grěšnogo prišel kako gost.
8 A stanuvši Zahej, rěkl do Gospodina: Polovinu iměnja mojego dam ubogym, Gospodine! a jestli jesm kogo v čim obmanul, oddam četyrikratno.
9 I rěkl jemu Jezus: Tutdenj se stalo spasenje tomu domu, zato že i on jest synom Abrahama.
10 Ibo prišel Syn člověčsky, aby iskal i hranil, čto propadlo.
11 Itak kogdy oni slyšali, govoreči dalje pověděl jim parabolu, zato že byl blizko Jeruzalema, a oni myslili, že se směsta kraljevstvo Božje objaviti imělo.
12 Rěkl itak: Něktory člověk roda čestnogo jehal v daleku krajinu, aby sobě vzel kraljevstvo, i snova vratil.
13 A pozvavši deset slug svojih, dal jim deset grošev i rěkl do njih: Trgujte, až prijedu.
14 No měščane jego iměli go v nenavisti, i poslali za njim izvěstje, govoreči: Ne hčemo, aby toj vladal nad nami.
15 I stalo se, že kogdy vratil, ibo dostal to kraljevstvo, že kazal do sebe pozvati slug tyh, ktorym dal groše, aby se dověděl, čto vsaky trgujuči iziskal.
16 Itak prišel prvy, govoreči: Gospodine! Groš tvoj deset grošev sdělal.
17 I rěkl jemu: Dobro, slugo dobry! Jesi byl nad malom věrnym, iměj že vlast nad desetymi gradami.
18 Prišel i drugy, govoreči: Gospodine! Groš tvoj pet grošev sdělal.
19 Rěkl i tomu: I ty bud nad petymi gradami.
20 A iny prišel, govoreči: Gospodine! vot groš tvoj, ktory jesm iměl ukryty v platnu;
21 Ibo jesm se tebe bojal, jesi člověk strogy; bereš, čego jesi ne položil, a žneš, čego jesi ne sějal.
22 Itak jemu rěkl: Iz ust tvojih sudju tebe, zly slugo! Jesi věděl, jesm člověk strogy, ktory beru, čego jesm ne položil, a žnu, čego jesm ne sějal.
23 Začto jesi itak ne dal srěbra mojego do banka? a ja priševši, byh vzel je iz banka.
24 I rěkl tym, ktori tu stali: Prijmite od njego toj groš, a dajte tomu, ktory ima deset grošev.
25 I rěkli jemu: Gospodine! On ima deset grošev.
26 Zapravdu govorju vam, že vsakomu, ktory ima, bude dano, a od togo, ktory ne ima, i to, čto ima, bude od njego odjeto.
27 No i neprijatelji moji, ktori ne htěli, abyh vladal nad njimi, privedite tu, a ubijte prěd mnoju.
28 A to pověděvši, šel premo, iduči do Jeruzalema.
29 I stalo se, kogdy se približil do Betfage i Betaniji, k goram, ktoru zovut olivnoju, poslal dvoh iz učenikov svojih,
30 Govoreči: Idite do gradka, ktory jest naprotiv vam, do ktorogo vševši, nahodite osla svezanogo, na ktorom nijedin člověk nikogdy ne sěděl; odvezavši go, privedite:
31 A jestli by vas kto pytal, začto go odvežete? tak jemu govorite: Zatom, že go Gospodin potrěbuje.
32 Odševši itak ti, ktori byli poslani, našli, kako jim pověděl.
33 A kogdy oni odvezyvali togo osla, rěkli gospodini jego do njih: Začto odvezyvajete osla?
34 A oni pověděli: Gospodin go potrěbuje.
35 I privedli go do Jezusa, a vloživši oděž svoju na togo osla, vsadili Jezusa na njego.
36 A kogdy on jehal, kladli oděž svoju na stežkě.
37 A kogdy se už približal naklon gory olivnoj, počelo vse množstvo učenikov radujuči se hvaliti Boga glasom velikym za vse čudesa, ktore viděli,
38 Govoreči: Blagoslavjany kralj, ktory ide v imenu Gospodinskom; pokoj na nebu, a hvala na vysotah.
39 No něktori iz Farizejev iz togo ljudu rěkli do njego: Učitelju! Zabranjaj togo tvojim učenikam.
40 A on odgovarjajuči, rěkl jim: Govorju vam, jestli by ti molčali, směsta kamene zvati budut.
41 A kogdy se približil, ugleděvši grad, plakal nad njim, govoreči:
42 O kakby jesi poznalo tom dnju to, čto služi pokoju tvojemu! no to tutčas ukryto od očij tvojih.
43 Ibo prijdut na tebe dni, kogdy tebe okružet neprijatelji tvoji valom, i oblěkut tebe, i tisknut tebe odvsud;
44 I poravnet tebe s zemjeju, i děti tvoje s toboju, a ne ostavet v tobě kamenja na kamenju, zato jesi ne poznalo časa posěčenja tvojego.
45 A vševši do crkvi, začel izganjati tyh, ktori v njim prodavali i kupovali.
46 Govoreči jim: Napisano: Dom moj domom molitvy jest, a vy jeste go učinili jamoju razbojnikov.
47 I učil na vsaky denj v crkvi; no vysši duhovniki i naučeni v Pismu, i vysši iz ljuda iskali go ubiti;
48 No ne našli, čto by jemu učinili; ibo ves ljud hodil za njim, slyšeči go.

## Razděl 20

1 I stalo se v jednom iz tyh dni, že kogdy učil ljuda v crkvi i kazal Evangelje, prišli vysši duhovniki i naučeni v Pismu s staršimi,
2 I rěkli do njego, govoreči: Pověd nam, ktoroju močju to činiš, ili kym jest toj, ktory dal tu moč?
3 A on odgovarjajuči, rěkl do njih: Pytaju i ja vas o jednu věč, a povědte mně:
4 Krest Joana byl li iz neba, či tož iz ljuda?
5 A oni myslili sami v sobě, govoreči: Jestli pověmo, iz neba, rěče: Čemu itak jeste jemu ne věrili?
6 Jestli že jednako rěčemo, iz ljuda, ves ljud kamenuje nas, zato že věret, že Joan jest prorokom.
7 I odgovorili, že ne znajut, odkud by byl.
8 A Jezus jim rěkl: I ja vam ne pověm, ktoroju močju to činju.
9 I začel do ljuda govoriti tu parabolu: Člověk něktory nasadil vinogradnik, i najel ju sadovnikam, i odšel von na čas nemaly.
10 A v času svojem poslal slugu do tyh sadovnikov, aby jemu dali čest iz ploda togo vinogradnika; no sadovniki ubivši go, poslali go prazdnogo.
11 I poslal snova drugogo slugu; no oni i togo ubivši i obezčestivši, poslali prazdnogo.
12 I poslal snova tretjego; no oni i togo ranivši, izkydali von.
13 A tak rěkl gospodin vinogradnika: Čto učinju? Pošlju mojego ljubimogo syna, očevidno kogdy togo uvidet, budut se styditi.
14 No sadovniki ugleděvši go, rěkli medžu soboju, govoreči: Toj jest naslědnik; pojdimo i ubijmo go, aby naše bylo naslědstvo.
15 I izgnavši go von iz vinogradnika, ubili. Čto jim itak učini gospodin vinogradnika?
16 Prijde, a ubije sadovnika, a vinogradnik odda inym. Togo oni uslyšavši, rěkli: Ne daj Bože!
17 No on pogledavši na njih, rěkl: Čto itak znači to slovo Pisma: Kamenj, ktory odkydnuli postavjajuči, se stal glavoju vugoljnoju?
18 Vsaky, ktory upade na toj kamenj, razbije se, a na kogo by upadl, raztrěskne go.
19 I starali se vysši duhovniki i naučeni v Pismu, kakoby na njego ruky kydnuli v toj že časině, no se ljuda bojali; ibo poznali, že protiv njim izrěkl tu parabolu.
20 A tak podgledajuči go, poslali špionov, ktori pritvarjali se, kakoby byli spravědlivymi, aby go hvatali v besědě jego, a potom aby go podali vlasti i v moč staršego.
21 I pytali go, govoreči: Učitelju! Znamo, že dobro govoriš i učiš, bez obzira na člověka; no stežky Božjej v pravdě učiš.
22 Dostojno li jest nam dati danok cěsaru, či ne?
23 No on ugleděvši hytrost jih, rěkl do njih: Čemu mene pokušate?
24 Ukažite mně groš; čij ima obraz i napis? A odgovarjajuči rěkli: Cěsara.
25 Zatom on jim rěkl: Oddavajte že itak, čto jest cěsara, cěsaru, a čto jest Božjego, Bogu.
26 I ne mogli go hvatati v besědě jego prěd ljudom, a udivivši se odgovoru jego, molčali.
27 A priševši něktori iz Saducejev, (ktori myslet, že ne ima vozkrešenja), pytali go,
28 Govoreči: Učitelju! Mojzes nam napisal: Jestli by komu brat umrl, imajuči ženu, a umrl by bez dětij, aby brat jego vzel jego ženu, a vozbudil potomstvo bratu svojemu.
29 Bylo itak sedm bratov, iz ktoryh prvy vzevši ženu, umrl bez dětij.
30 I vzel vtory tu ženu, a umrl i toj bez dětij.
31 Potom ju vzel i tretji, takože i vsi sedm, a ne ostavivši dětij, umrli.
32 Po vsih tož umrla i ta žena.
33 Zatom pri vozkrešenju, ktorogo že iz njih bude žena, zato že sedm jih imělo za ženu?
34 Itak odgovarjajuči, rěkl jim Jezus: Syni togo věka ženet se i omužet.
35 No ti, ktori dostojni sut, aby dostali toj život, i vstali iz mrtvyh, ni se ženiti, ni omužet se.
36 Ibo umirati veče ne budut mogli; ibo budut ravni Angelam, suči synami Božjimi, ibo sut synami vozkrešenja.
37 A že umrli vozkresnut, i Mojzes pokazal pri tom kustu, kogdy zove Gospodina Boga Bogom Abrahama i Bogom Izaaka i Bogom Jakoba.
38 A Bog ne jest Bogom mrtvyh, no živyh; ibo jemu vsi živut.
39 Itak odgovarjajuči něktori iz naučenyh v Pismu, rěkli: Učitelju! dobro jesi pověděl.
40 I ne směli go veče o ničto pytati.
41 I rěkl do njih: Kako govoret, že Hristos jest synom Davida?
42 A sam David govori v knigah Psalmov: Rěkl Gospodin Gospodinu mojemu: Sědi po mojej pravoj straně
43 Až položu neprijateljev tvojih kako osnova nog tvojih.
44 Zato že go itak David zove Gospodinom, to kako jest synom jego?
45 A kogdy togo slyšal ves ljud, rěkl učenikam svojim:
46 Shranite se naučenyh v Pismu, ktori hčut hoditi v oděžah dolgyh, i ljubet pozdravjenja na trgah i prve stolky v synagogah, i prve města na večerjah;
47 Ktori požirajut domy vdov, a za pritvorstvo činet dolge molitvy: Tym težši bude jih sud.

## Razděl 21

1 A pogledavši ugleděl bogačev kydajučih dary svoje do skarbnice.
2 Ugleděl tož i něktoru vdovu bědnu, kydajuču tam dva drobne groše.
3 I rěkl: Zapravdu vam govorju, že ta uboga vdova veče než ti vsi kydnula.
4 Vsi iz togo, čto jim bylo izbytočno, kydnuli na žrtvu Božju, no ta iz nedostatka svojego vse, čto iměla na život, kydnula.
5 A kogdy něktori govorili o svetilišču, že bylo krasivym kamenjem i darami ukrašeno, rěkl:
6 Prijdut dni, že iz togo, čto vidite, ne ostane kamenj na kamenju, ktory by ne byl razvaljeny.
7 I pytali go, govoreči: Učitelju! Kogdy že to bude? a kaky znak bude, kogdy se to bude imělo byvati?
8 A on rěkl: Strěžite se, abyste ne byli obmanuti; ibo mnogo jih prijde v imenu mojem, govoreči: Jesm Hristos, a čas se približil; ne hodite itak za njimi.
9 A kogdy uslyšite o vojnah i prěvratah, ne bojite se; ibo ima to byti najprvo, no ješče ne jest konec.
10 Itak jim govoril: Povstane narod protiv narodu, i kraljevstvo protiv kraljevstvu;
11 I budut v mnogo městah velike tresenja zemji, i glady i hvoroby, takože strahy i znaky velike iz neba budut.
12 No prěd tym vsem kydnut na vas ruky svoje, i budut vas prěslědovati, davajuči vas do synagog i do vezenja, vodeči vas prěd kraljev i prěd starost za ime moje.
13 A to vam bude možnost na svědočstvo.
14 Zatom prijmite to do srdc vaših, abyste nikogdy ne myslili, kako byste odgovarjati iměli.
15 Ibo ja vam dam usta i mudrost, ktoroj vaši protiviniki ne budut mogli se odrěkti, ni se protiviti.
16 A budete tož prědani od roditeljev i od bratov i od srodnikov i od prijateljev, i ubijut něktoryh iz vas;
17 Budete v nenavisti u vsih za ime moje.
18 No ni vlas iz glavy vašej ne izgyne.
19 črěz vašu neustuplivost izbavite vaše duše.
20 A kogdy uvidite Jeruzalem od vojsk okruženy, znajte itak, že se približilo opustošenje jego.
21 Itak ti, ktori sut v Judzkoj zemji, nehaj běžet na gory, a ti, ktori sut v gradu, nehaj izhodet, a ti, ktori sut v selah, nehaj ne vhodet do njego.
22 Ibo budut dni pomsty, aby se izpolnilo vse, čto jest napisano.
23 No běda brěmennym i prsami krmečim v te dni! ibo bude tisknutje veliko v toj zemji i gněv Božji nad tym ljudom.
24 I padut od meča, i gnani budut v rabstvo medžu vse narody, i bude Jeruzalem toptano od poganov, až se izpolnet časy poganov.
25 Itak budut znaky na solncu i na měsecu i na zvězdah, a na zemji tisknutje narodov s velikym strahom, kogdy zašumet morje i potoky;
26 Tak, že ljudi omlěvati budut prěd strahom i očekyvanjem tyh věčij, ktore prijdut na ves svět; ibo moči nebeske pomrdajut se.
27 A itak uvidet Syna člověčskogo, prihodečego v oblaku s močju i velikoju slavoju.
28 A kogdy se to začne byvati, pogledajte že, a voznosite glavy vaše, zatom že se približaje odkupjenje vaše.
29 I pověděl jim parabolu: Pogledajte na figovo drěvo i na vse drěva;
30 Kogdy vidite, že izpuščajut pupy, to sami priznajete, že už blizko jest lěto.
31 Takože i vy, kogdy uvidite, že se to děje, znate, že blizko jest kraljevstvo Božje.
32 Zapravdu govorju vam, že ne mine to pokoljenje, až se to vse stalo.
33 Nebo i zemja minut, no slova moje ne minut.
34 A čuvajte, aby očevidno ne byli obtežane vaše srdca obžerstvom i pijanstvom i nepokojem o tom životu, aby naglo ne prišel do vas toj denj.
35 Ibo naglo pripade na vsih, ktori živut na cěloj zemji.
36 Zatom čuvajte, moleči se na vsaky čas, abyste byli dostojni izběgati togo vsego, čto se byvati ima, i stanuti prěd Synom člověčskym.
37 I učil v te dni v svetilišču; no v noči izhodil, prěbyval na gorě, ktoru zovut olivnoju.
38 A ves ljud rano se shodil do njego, aby go slyšal v svetilišču.

## Razděl 22

1 A približalo se prazdnik nekyslenyh hlěbov, ktore zovut Pashoju.
2 I iskali vysši duhovniki i naučeni v Pismu, kakoby go ubili; no se bojali ljuda.
3 I vstupil satan v Judasa, ktorogo zvano Iskariot, ktory byl iz dvanadseti.
4 Toj itak odševši, dogovoril se s vysšimi duhovnikami, i s načelnikami crkvi, kakoby go jim prodal.
5 I radovali se, i dogovorili se s njim, že jemu hčut dati groše.
6 I oběčal, i iskal dobrogo momenta aby go jim prodal bez vědnosti tolpy.
7 Itak prišel denj nekyslenyh hlěbov, v ktorom iměl baranok byti ubity.
8 I poslal Petra i Joana, govoreči: Pojdite, kuhajte nam baranka, abysmo jeli.
9 No oni jemu rěkli: Kde hčeš, abysmo go kuhali?
10 A on rěkl do njih: Vot kogdy do grada vhoditi budete, strěte se s vami člověk, nesuči džban vody; idite-že za njim do doma, do ktorogo vojde,
11 A rěčite gospodaru doma togo: Kazal tobě pověděti učitelj: Kde jest gostinec, v ktorom byh mogl jesti baranka s učenikami mojimi?
12 A on vam ukaže salu veliku, tam kuhajte.
13 Itak odševši našli, kako jim pověděl, i kuhali baranka.
14 A kogdy prišla časina, usědl za stolom, i dvanadset apostolov s njim.
15 I rěkl do njih: Jesm žedal togo baranka jesti s vami, najprvo než budu stradati.
16 Ibo vam govorju, že go veče jesti ne budu, až se izpolni v kraljevstvu Božjim.
17 A vzevši čašu i blagodarivši, rěkl: Prijmite to, a razdělite medžu soboju.
18 Ibo govorju vam, že ne budu pil iz ploda vinnogo kusta, až prijde kraljevstvo Božje.
19 A vzevši hlěb i blagodarivši, lomil i dal jim, govoreči: To jest tělo moje, ktore za vas bude izdano; to činite na pamet moju.
20 Takože i čašu, kogdy bylo po večerji, govoreči: Ta čaša jest novy zavět vo krvi mojej, ktora za vas bude izlita.
21 No vot ruka togo, ktory mene proda, so mnoju jest za stolom.
22 Zapravdu Syn člověčsky ide, tak kako jest postavjeno; no běda člověku tomu, ktory go proda!
23 Itak se začeli medžu soboju pytati o tom, ktory by iz njih to učiniti iměl.
24 A vozbudil se tož spor medžu njimi o tom, ktory by iz njih byl največši.
25 No on jim rěkl: Kralji narodov vladajut nad njimi, a ktori nad njimi moč imajut, dobrodějami zvani byvajut.
26 No vy ne tak imate dělati: očevidno kto najvysši jest medžu vami, nehaj bude kako najmenši, a kto jest načelnikom, bude kako toj, ktory služi.
27 Ibo ktory-že vysši jest? Toj, ktory sědi, či toj, ktory služi? Či ne toj, ktory sědi? No jesm posrěd vas kako toj, ktory služi.
28 A vy jeste, ktori byli neustuplivi pri mně v pokušenjah mojih.
29 I vam doruču, kako mně doručil Otec moj, kraljevstvo,
30 Abyste jeli i pili za stolom mojim v kraljevstvu mojem, i sěděli na tronah, sudeči dvanadset rodov Izraelskyh.
31 I rěkl Gospodin: Simone, Simone! vot satan izprosil vas, aby vas razprašil kako pšenicu,
32 No jesm ja prosil za toboju, aby ne prěstala věra tvoja; a ty iz tvojej strany, utvrdžaj bratov tvojih.
33 A on jemu rěkl: Gospodine! gotovy jesm s toboju idti i do vezenja i na smrt.
34 A on rěkl: Govorju tobě, Petre! ne spěva tutdenj kokot, až se najprvo trikratno odkažeš, že mene ne znaš.
35 I rěkl jim: Kogdy jesm vas poslal bez měška, i bez torby, i bez obuvij, či vam čego nedostavalo? A oni rěkli: Ničego.
36 Itak jim rěkl: No tutčas kto ima měšok, nehaj go prijme, takože i torbu; a kto ne ima meča, nehaj proda oděž svoju, a kupi meč.
37 Ibo govorju vam, že ješče ima to, čto jest napisano, izpolniti na mene, imenno: I s zlodějami čislěny jest; ibo te věči, ktore svědčet o mene, konec imajut.
38 No oni rěkli: Gospodine! vot tu dva meče. A on jim rěkl: Dost jest.
39 I izševši šel po obyčaju na goru Olivnu, a šli za njim učeniki jego.
40 A kogdy prišel na město, rěkl jim: Molite se, abyste se ne poddavali  pokušenju.
41 A sam oddalil se od njih, kakoby na met kamenjem, a kleknuvši na kolěna, molil se,
42 Govoreči: Otče! jestli hčeš, vozmi toj čaši od mene; jednako ne moja volja, no tvoja nehaj se stane.
43 I ukazal jemu se Angel iz neba, ukrěpjajuči go.
44 No suči v boju, gorlivěje se molil, a byl pot jego kak kapje krvi tekuče na zemju.
45 A vstavši od molitvy, prišel do učenikov, i našel jih spečih od smutka.
46 I rěkl jim: Čto spite? vstanite, a molite se, byste se ne poddavali pokušenju.
47 A kogdy on ješče govoril, izjavila se tolpa. I toj, ktorogo zvano Judasom, jedin iz dvanadset, šel prěd njimi, i približil se do Jezusa, aby go cěloval.
48 A Jezus jemu rěkl: Judase! cělovanjem prodaš Syna člověčskogo?
49 A to videči ti, ktori pri njim byli, čto se byvati imělo, rěkli jemu: Gospodine! imamo udariti mečem?
50 I udaril jedin iz njih slugu vrhovnogo duhovnika, i urězal jemu pravo uho.
51 No Jezus odgovarjajuči, rěkl: Prěstanite! A dotknuvši uha jego, ozdravil go.
52 I rěkl Jezus do tyh, ktori prišli protiv njemu, i do vysših duhovnikov i načelnikov crkvi, i do starših: Jeste izšli kako na razbojnika s mečami i s kyjami.
53 Kogdy jesm črěz vsaky denj byval s vami v crkvi, jeste ne vložili ruk na mene; no jest to časina vaša i moč temnosti.
54 Hvatali go itak, vodili go i privodili go v dom vrhovnogo duhovnika, a Petr šel za njim iz daleka.
55 A kogdy oni zapalili ogonj v posrěd dvora i zajedno usědli, usědl i Petr medžu njimi.
56 A ugleděvši go sědečego něktora děvka pri ognju, i spěšno jemu se prigledavši, rěkla: I toj s njim byl.
57 A on se go odkazal, govoreči: Ženo! Ne znaju go.
58 A po malom času ugleděvši go drugy, rěkl: I ty jesi iz njih; no Petr rěkl: Člověče! ne jesm.
59 A kogdy izšla jedna časina, někto iny utvrdžal, govoreči: Pravdivo i toj ¨s njim byl; ibo tož jest Galilejec.
60 A Petr rěkl: Člověče! ne znaju, čto govoriš; a zatom momentalno, kogdy on ješče govoril, kokot spěval.
61 A Gospodin obrativši se, pogledal na Petra. I pomněl Petr na slovo Gospodinsko, kako jemu by pověděl: Že najprvo než kokot spěva, trikratno se mene odkažeš.
62 A Petr izševši von, gorko plakal.
63 No muži, ktori zajedno držali Jezusa, smějali se iz njego, bijuči go;
64 A ukryvši jemu oči, bili lice jego i pytali go, govoreči: Prorokuj, kym jest, ktory tebe udaril.
65 I mnogo inyh věčij bogohulnyh govorili protiv njemu.
66 A kogdy byl denj, sošli se starši iz ljuda i najvysši duhovniki i naučeni v Pismu, a privedli go do rady svojej.
67 Govoreči: Jestli jesi ty Hristos, pověd nam? I rěkl jim: Hot byh vam pověděl, ne uvěrite.
68 A jestli byh tož o to pytal, ne odgovorite mně, ni mene odpustite.
69 Od togo časa bude Syn člověčsky sěděti po pravoj straně Božjej.
70 I rěkli vsi: Ty jesi itak synom Božjim? A on rěkl do njih: Vy govorite to, ibo ja njim jesm.
71 A oni rěkli: Za čto ješče potrěbujemo svědočstva? Ibo jesmo sami slyšali iz ust jego.

## Razděl 23

1 Itak vstavši vse množstvo jih, vodili go do Pilata.
2 I začeli jego obvinjati, govoreči: Togo jesmo našli, že obrati ljud i zabranja dany davati cesaru, govoreči: Že on jest Hristosom, kraljem.
3 I pytal go Pilat, govoreči: Ty jesi kralj židovsky? A on jemu odgovarjajuči rěkl: Ty govoriš.
4 I rěkl Pilat do vysših duhovnikov i do ljuda: Nijednoj viny ne najdu v tom člověku.
5 No se oni vyše trudili, govoreči: Podstrěče ljud, učeči po cěloj Judzkoj zemji, začevši od Galilei až tu.
6 Itak Pilat uslyšavši o Galilei, pytal, jestli by byl člověkom Galilejskym?
7 A kogdy se dověděl, že byl iz carstva Heroda, poslal go do Heroda, ktory tož v Jeruzalemu byl v te dni.
8 A Herod ugleděvši Jezusa, radoval se mnogo; ibo go iz davna žedal viděti, zato, že mnogo o njem slyšal, i očekyval se, že iměl ugleděti kaky znak črěz njego byl učinjeny.
9 I pytal go mnogo; no jemu on ničto ne odgovarjal.
10 A vysši duhovniki i naučeni v Pismu stali, močno obvinjajuči na njego.
11 No prěziravši njim Herod s vojskom svojim i smějavši se iz njego, oblěkl go v oděž bělu i poslal go jednako do Pilata.
12 I Pilat s Herodom stali se prijateljami togo dnja; ibo sobě byli naprěd neprijateljami.
13 A Pilat pozvavši vysših duhovnikov i načelnikov, i ljuda,
14 Rěkl do njih: Jeste mně privedli togo člověka, kakoby ljud obratil se: a vot ja prěd vam pytajuči go, nijednoj viny jesm ne našel v tom člověku v tom, o čto jego obvinjajte;
15 No ni Herod, ibo jesm vas poslal do njego, a vot ničto dostojnogo smrti se ne stalo;
16 Zatom nakazavši odpustu go.
17 A iměl jim Pilat izpuščati jedinogo na prazdnik.
18 Itak pozvalo zajedno vse množstvo, govoreči: Izgubi togo a odpusti nam Barabasa!
19 Ktory byl za někaky bunt v gradu, i za ubijstvo vloženy do vezenja.
20 Itak Pilat snova govoril, hčuči izpustiti Jezusa.
21 No oni zato zvali, govoreči: Na križ s njim, na križ!
22 A on tretji raz rěkl do njih: I čto že toj zlogo učinil? Nijednoj viny dostojnoj smrti ne našel jesm v njim; zatom kažu, odpustiti go.
23 A oni snova glasom velikym žedalo, aby byl razpety; i krěpili se glasy jih.
24 A tak Pilat kazal, aby se stalo žedanje jih.
25 I odpustil jim togo, ktory byl za bunt i ubijstvo vloženy do vezenja, o ktorogo prosili; no Jezusa podal na volju jih.
26 Kogdy go itak vodili, zadržali Simona něktorogo Kirinejca, idučego iz polja, vložili na njego križ, aby go nesl za Jesusom.
27 I pošlo za njim velike množstvo ljuda i žen, ktore go plakali i se jego žalili.
28 No Jezus obrativši se do njih, rěkl: Dočerky Jeruzalemske! ne plačite nad mnoju, no skorěje same nad soboju plačite i nad dětami vašimi.
29 Ibo prijdut dni, v ktoryh budut govoriti: Blagoslovjeno neplodne životy, ktore ne rodili, i prsi, ktore ne krmili.
30 Itak počnut govoriti goram: Padite na nas! a gorkam: Pokryjte nas!
31 Ibo jestli to zelenym drěvom dělajut, čto bude s suhym?
32 Privedeni tož byli ini dva zloději, aby zajedno s njim ubiti byli.
33 A kogdy prišli na město, ktoro zovut Golgota, tam go razpeli, i tyh zlodějev, jedinogo po pravoj, a drugogo po lěvici.
34 Itak Jezus rěkl: Otče! odpusti jim: ibo ne znajut, čto činet. A razdělivši oděž jego, sudbu o nje metali.
35 I stal ljud, prigledajuči se, smějali se iz njego i načelniki s njimi, govoreči: Inyh spasal, nehaj spasa samogo sebe, jestli že on jest Hristos, izbrany Božji.
36 Smějali se tož iz njego i vojini, podhodili, a ocet jemu davajuči,
37 I govoreči: Jestli jesi ty kralj židovsky, izbavi samogo sebe.
38 A byl tož i napis napisany nad njim bukvami Grečskymi i Latinskymi i Židovskymi: Toj jest kralj židovsky.
39 A jedin iz tyh zlodějev, ktori s njim visěli, bogohulil jemu, govoreči: Jestli jesi ty Hristos, izbavi že sebe i nas.
40 A odgovarjajuči drugy, zgromil go govoreči: I ty se Boga ne bojiš, hot imaš samu karu?
41 A my zato spravědlivo dostanemo zaplatu za děly naše; no toj ničto zlogo ne učinil.
42 I rěkl do Jezusa: Gospodine! pomni na mene, kogdy prijdeš do kraljevstva tvojego.
43 A Jezus jemu rěkl: Zapravdu govorju tobě, tutdenj so mnoju budeš v raju.
44 A bylo okolo šestoj časině, i stala se temnost po cěloj zemji až do časiny devetoj.
45 I zatmilo se solnce, a zavěsa crkovna raztrgnula se v pol.
46 A Jezus pozvavši glasom velikym, rěkl: Otče! v ruky tvoje poručaju duha mojego; a to rěkši, umrl.
47 A videči sotnik, čto se stalo, hvalil Boga, govoreči: Zapravdu člověk to byl spravědlivy.
48 Takože i ves ljud, ktory se sošel na to zrělišče, videči, čto se dělo, bili se v prsi svoje, vračal se.
49 A znajemi jego vsi iz daleka stali, i ženy, ktore za njim byli iz Galilei, prigledajuči se tomu.
50 A vot muž, imenom Jozef, ktory byl senatorom, muž dobry i spravědlivy,
51 Ktory ne dozvolil na radu i na dělo jih, iz Arimatiji, grada Judzkogo, ktory tož očekyval kraljevstva Božjego;
52 Toj priševši do Pilata, prosil o tělo Jezusa.
53 I sjel go, ovinul go platnom a položil go v grob v kamenju rězanom, v ktorym ješče nikto nikogdy ne byl položeny.
54 A byl denj prigotovjenja, i subota se počela.
55 Poševši tož za njim i ženy, ktore byli s njim iz Galilei, ogledali grob, i kako bylo položeno tělo jego.
56 A vrativši se, prigotovali aromatnične vony i masti; no v subotu oddohnuli po zakonu.

## Razděl 24

1 A prvogo dnja po subotě mnogo rano hodeči do groba, nesli věči aromatne, ktore prigotovili;
2 I našli kamenj odsunuty od groba.
3 A vševši v grob, ne našli těla Gospodina Jezusa.
4 I stalo se, kogdy se velmi prěstrašili, že vot dva muži stanuli pri njimi v oděžah světlyh.
5 A kogdy se one bojali i sklonili lice svoje k zemji, rěkli do njih: Čto iščete živučego medžu mrtvymi?
6 Ne ima go tu, no vstal: pomnite, kako vam govoril, kogdy ješče byl v Galileji,
7 Govoreči: Syn člověčsky imaje byti prědany v ruky ljudij grěšnyh, i byti razpety, a tretjego dnja vozkresnuti.
8 I vozpametali slova jego.
9 A vrativši se od groba, objavili to vse tym jedinnadsetom i vsim inym.
10 A byla Marija Magdalena i Joana, i Marija, mati Jakoba, i ine s njimi, ktore to govorili Apostolam.
11 No myslili, že jih slova sut bajkoju, i ne uvěrili jim.
12 Itak Petr vstavši, běgal do groba, a sklanjavši se, ugleděl same jedino platny ležeče, i odšel, diveči se tomu, čto se stalo.
13 A vot dva iz njih togo-že dnja šli do gradka, ktori bylo na šestdeset etapov od Jeruzalema, ktoro zvano Emaus.
14 A razgovarjali so soboju o tom vsem, čto se stalo.
15 I stalo se, kogdy oni razgovarjali i zajedno se pytali, že Jezus približivši se, šel s njimi.
16 No oči jih byli sodržane, aby go ne poznali.
17 I rěkl do njih: Čto to za razgovory, ktore imate medžu soboju iduči, a jeste smutni?
18 A odgovarjajuči jemu jedin, ktoromu bylo ime Kleofas, rěkl jemu: Ty jesi věrojetno gostem v Jeruzalemu, a ne znaš, čto se v njem v tyh dnjah stalo?
19 I rěkl jim: Čto? A oni jemu rěkli: To čto, stalo se Jezusom iz Nazareta, ktory byl prorokom, močny v dělu i v slovu prěd Bogom i vsim ljudom;
20 A kako go prodali vysši duhovniki i načelniki naši, aby byl osudženy na smrt; razpinali go.
21 A jesmo myslili, že on iměl odkupiti Izrael; no tutčas po tom vsem tutdenj jest tretji denj, od dnja v ktorom se stalo.
22 No i ženy něktore iz naših prěstrašili nas, ktore rano byli u groba;
23 A ne naševši těla jego govorili, že viděnje od Angelov viděli, ktori govoret, že on žive.
24 I hodili něktori iz naših do groba, i tak vse našli, kak i ženy govorili; no jego ne viděli.
25 Itak on rěkl do njih: O glupi, kak lěnive sut vaše srdca do věry tomu vsemu, čto pověděli proroki!
26 či ne iměl Hristos togo stradati i vstupiti do slavy svojej?
27 A začevši od Mojzesa i od vsih prorokov, učil jim o vsem v Pismah, čto o njem bylo napisano.
28 I približil se k gradku, do ktorogo šli, a on pokazyval, kakoby iměl dalje idti.
29 No go oni prinudili, govoreči: Ostani s nami, ibo už jest večer, i už denj se dovršal. I všel, aby ostal s njimi.
30 I stalo se, kogdy on sěděl s njimi za stolom, vzevši hlěb, blagoslavjal, a lamajuči daval jim.
31 I odkryli se oči jih, i poznali go; no on izčeznul iz očij jih.
32 I govorili medžu soboju: Či srdce naše ne gorělo v nas, kogdy s nami na stežkě govoril, i kogdy nam Pisma objasnjal?
33 A vstavši v toj že časině, vratili se do Jeruzalema, i našli sobranyh jedinnadset, i tyh, ktori s njimi byli,
34 Govorili: Vstal Gospodin pravdivo, i ukazal se Simonu.
35 A oni tož pověděli, čto se stalo na stežkě, i kako go poznali v lamanju hlěba.
36 A kogdy oni to govorili, stanul sam Jezus v posrěd njih, i rěkl jim: Pokoj vam!
37 A oni prěstrašivši se i bojali se, ibo myslili, že duha viděli.
38 I rěkl jim: Čemu jeste se prěstrašili, i čemu sumněvajuče myslji prihodet do srdc vaših?
39 Ogledajte ruky moje i nogy moje, jesm on; dotknite mene, a vidite; ibo duh ne ima těla ni kosti, kako vidite, no ja je imam.
40 A to rěkši, pokazal jim ruky i nogy.
41 No kogdy oni ješče ne dověrjali iz radosti, no se divili, rěkl jim: Imate tu čto jesti?
42 A oni jemu podali čest ryby pečenoj i kus meda.
43 A on vzevši, jel prěd njimi.
44 I rěkl do njih: To sut slova, ktore jesm govoril do vas, suči ješče s vami, že se imaje izpolniti vse, čto napisano v zakonu Mojzesa, u prorokov, i u psalmov o mně.
45 Itak jim otvoril razum, aby razuměli Pisma.
46 I rěkl jim: Tak napisano, i tak iměl Hristos stradati, i tretjego dnja vozkresnuti;
47 I aby byla kazana v imeni jego obračenje i odpuščenje grěhov medžu vsimi narodami, začevši od Jeruzalema.
48 A vy jeste svědkami togo.
49 A vot ja pošlju na vas oběčanje Otca mojego, a vy ostanite v gradu Jeruzalem, až budete oblěčeni močju iz vysoty.
50 I izvedl jih von až do Betaniji, a voznesši ruky svoje blagoslavjal jih.
51 I stalo se, že kogdy jih blagoslavjal, razstal se s njimi, i byl vozneseny v goru do neba.
52 A oni poklonivši se jemu, vratili do Jeruzalema s velikoju radostju.
53 I byli vsakčas v crkvi, hvaleči i blagoslavjajuči Boga.

# Evangelje Joana

## Razděl 1

1 Na početku bylo Slovo, i to Slovo bylo u Boga, i Bogom bylo Slovo. 
2 To bylo na početku u Boga.
3 Vse čto stalo se, stalo se črěz Slovo, i bez njego ničto ne stalo se, čto stalo se.
4 V njem byl život, i život byl to světlo ljudsko.
5 I to světlo světi v mraku, ale mrak jego ne objel.
6 Byl člověk poslany od Boga, ktoromu ime bylo Joan.
7 On prišel na svědočstvo, da by svědčil o tom světlu, da by črěz njego vsi uvěrili.
8 Ne byl on to světlo, ale prišel, da by svědčil o tom světlu.
9 On jest to istinno světlo, ktoro osvěča každogo člověka, ktory prihodi na svět.
10 Na světu byl, i svět črěz njego učinjeny jest; ale jego svět ne poznal.
11 K svojej vlastnosti prišel, ale jego vlastni jego ne prijeli.
12 Vsim, ktori jego prijeli, dal tu moč, da by se stali synami Božjimi, to jest tym, ktori věret v jego ime.
13 Ktori ne od krvi, ni od voli těla, ni od volji muža, ale od Boga narodženi sut.
14 I to Slovo tělom se stalo, i žilo medžu nami, i jesmo viděli jego slavu, slavu jednorodnogo od Otca, polno milosti i pravdy.
15 Joan svědčil o njem, i rěkl glasno: On jest tym, o ktorom pověděl: Ktory poslě mně prijde, stal se prěd mnoju; bo byl prvy. 
16 I od njego polnosti vsi jesmo prijali i lasku za lasku.
17 Ibo zakon črěz Mojzesa jest dany, a laska i pravda črěz Jezusa Hristosa stala se.
18 Boga nikto nikogda ne viděl: jednorodny syn, ktory jest v lonu Otcevskom, nam pověděl.
19 A to jest svědočstvo Joana: poslali Židi iz Jeruzalema svečenniki i Levity, da by jego se spytali: Kto ty jesi?
20 I vyznaval, a ne odrěkl, a vyznaval, že ja ne jesm Hristos.
21 I spytali jego: Čto že ty? Ty jesi Ilija? A on rěkl: Ne jesm. A oni: Prorok ty? i odgovoril: Ne jesm.
22 Rěkli jemu tako: Kto že ty jesi, da byhmo odgovor dali tym, ktori nas poslali? Čto povědaš o sobě?
23 Rěkl: Ja jesm glasom, ktory kriči na pustynji: gotovite put Gospodina, kako pověděl prorok Izaijaš.
24 A ti, ktori byli poslani, byli od Farizejev.
25 I spytali jego i rěkli jemu: Čemu že ty krestiš, jestli ty ne jest Hristos, ni Ilija, ni prorok?
26 Odgovoril jim Joan, govorivši: Ja krešču vodoju; ale posrěd vas stoji toj, ktorogo vy ne znajete.
27 Toj jest, ktory poslě mně prijde, ktory prěd mnoju byl, ktoromu ja ne jesm godny, da byh razvezal obuvi jego.
28 To se stalo v Betaniji za Jordanom, kde Joan krestil.
29 A zautra uzrěl Joan Jezusa idučego k sobě, i rěkl: Vot Baranok Božje, ktory gladi grěh světa.
30 Toj jest, o ktorom ja pověděl, že ide za mnoju muž, ktory stal se prěd mnoju; bo byl prvy.
31 Jesm jego ne znal, no on byl objavjeny Izraelju, tomu ja prišel krestiti vodoju.
32 I svědčil Joan: Jesm viděl Duha shodivšego kako golub s neba, i ostal se na njem.
33 Jesm jego ne znal. No ktory poslal mene krestiti vodoju, rěkl mi: Na kogo bys viděl Duha shodivšego i ostavšego se na njem, on jest tym, ktory kresti Duhom Svetym.
34 I jesm viděl i svědčil, že on jest Synom Božjem.
35 Zautra snova stal Joan tam i dva jego učenikov.
36 I viděvši Jezusa idučego, rěkl: Vot Baranok Božji.
37 I slyšali jego oba učenikov, i šli za Jezusom.
38 I obrativši se Jezus i uviděvši jih za soboju iduči, rěkl jim: Čego iščete? A oni mu rěkli: Rabi! (to jest: Učitelj), kde byvaješ?
39 Rěkl jim: Pojdite i ogledajte. Prišli i viděli, kde žil, i ostali pri njem ovogo dnja; bylo okolo desetoj časiny.
40 A byl Andrej, brat Simona Petra, jedin iz dvoh, ktori to slyšali od Joana, i šli za njim.
41 On najprvo strětl Simona, brata svojego, i rěkl mu: Jesmo našli Mesijasa, (to jest Hristosa).
42 I privedl go do Jezusa. A pogledavši na njego Jezus, rěkl: Ty jesi Simon, syn Joana; ty budeš nazyvany Kefas, to jest Petr.
43 A zautra htěl Jezus pojdti do Galileji, i našel Filipa i rěkl mu: Pojdi za mnoju.
44 A Filip byl iz Betsajdy, iz města Andrejovogo i Petrovogo.
45 Filip našel Natanaela i rěkl mu: Jesmo našli ovogo, o ktorom pisal Mojzes v zakonu i proroki, Jezusa, syna Jozefa, iz Nazareta.
46 I rěkl mu Natanael: Či može iz Nazareta byti něčto dobro? Rěkl mu Filip: Pojdi, i ogledaj!
47 Viděvši Jezus Natanaela prihodivšego k sobě, rěkl o njem: Vot istinno Izraelec, v ktorom ne jest prědavstva.
48 Rěkl mu Natanael: Odkud me znaš? Odgovoril Jezus i rěkl mu: Skorěje než tebe Filip prizval, kogda jesi byl pod smokvoju, jesm viděl te.
49 Odgovoril Natanael i rěkl mu: Učitelju! Ty jesi Synom Božjem, ty jesi kraljem izraelskym.
50 Odgovoril Jezus i rěkl mu: Jesm ti že rěkl: Jesm viděl te pod smokvoju. Večše věči nad tym uzriš.
51 I rěkl mu: Istinno, istinno povědam vam: Od togo času uzrite nebo otvorjeno i angeli Božje vstupajuče i shodivše na Syna člověčskogo.

## Razděl 2

1 A tretjego dnja byla svatba v Kaně Galilejskoj, i tam byla mati Jezusa.
2 Byli pozvani Jezus i jego učeniki na ovu svatbu.
3 A kogdy ne bylo vina, rěkla mati Jezusa jemu: "Vina ne imajut."
4 Rěkl jej Jezus: "Čto ja imam s toboju, ženo? Ješče ne došla moja časina."
5 Rěkla mati jego slugam: "Čto vam rěkl, učinite."
6 Tam bylo šest kamennyh džbanov, postavjenyh po židovskom obyčaju očiščenja, v ktoryh každy imal dva ili tri vědra.
7 Rěkl jim Jezus: "Napolnite džbany vodoju"; i napolnili je do vrha.
8 Togda jim rěkl: "Načrpajte nyně i donesite staršemu svatby." I donesli.
9 A kogdy starši svatby degustoval vodu, ktora stala se vinom (a ne věděl, odkud jest; ale slugi věděli, ktori črpali vodu), kazal do sebe starši mladoženiha;
10 I rěkl jemu: "Každy člověk najprvo vozme dobro vino, a kogdy se napijut, togda gorše; a ty dobro vino shranil do sego vrěmene."
11 Toj početok čudes učinil Jezus v Kaně Galilejskoj, i objavil svoju slavu; i uvěrili v njego jego učeniki.
12 Potom stupil do Kafarnauma, on i mati jego i brati jego i učeniki jego, i žili tam několiko dni.
13 A blizko byla židovska Paša; i vstupil Jezus do Jeruzalema.
14 I našel v svetilišču tyh, ktori prodavali voli i ovce i golubi, i tyh, ktori trgovali s pěnezami.
15 A učinil bič iz vezala, vsih izgnal iz svetilišča, i ovce i voli: a tym, ktori trgovali s pěnezami, pěnezy razsypal i stoly povratil;
16 A tym, ktori golubi prodavali, rěkl: Iznesite to odtud, a ne činite doma Otca mojego domom kupca.
17 I vozpametali sobě učeniki jego, že jest pisano: Usrdnost doma tvojego sje mene.
18 Togda odgovorili Židi i rěkli jemu: Kaky znak nam pokažeš, že to činiš?
19 Odgovoril Jezus i rěkl jim: Razvalite to svetilišče, a vo treh dnjah postavju ju.
20 Rěkli togdy Židi: Četyrideset i šest let se budovala to svetilišče, a ty ju vo treh dnjah postaviš?
21 Ale on govoril o svetilišču těla svojego.
22 Kogda vozkresnul, spomněli učeniki jego, že jim to pověděl; i uvěrili Pismu i slovu, ktoro rěkl Jezus.
23 A kogdy byl v Jeruzalemu v Pašě v den svety, mnogo jih uvěrilo v ime jego, videči čuda jego, ktore činil.
24 Ale Jezus ne pověril jim samogo sebe, bo on znal vsih,
25 A že ne potrěboval, aby jemu kto svědočstvo daval o člověku; zato že on věděl, čto bylo v člověku.

## Razděl 3

1 Byl někaky čelověk iz Farizejev, imenom Nikodem, židovsky knez.
2 On prišel k Jezusu v noči i rěkl jemu: „Rabi! Znajemo, že ty jesi prišel od Boga kako učitelj; bo nikto ne može činiti tyh čudes, ktore ty činiš, jestli že Bog ne byl by s toboju.“
3 Odgovoril Jezus i rěkl jemu: „Istinno, istinno povědam ti: Jestli se kto ne narodi snova, ne može viděti kraljevstvo Božje.“
4 Rěkl jemu Nikodem: „Kako može se čelověk naroditi, kogda jest stary? Či može vtoro vstupiti vo život svojej materi i naroditi se?“
5 Odgovoril Jezus: „Istinno, istinno povědam ti: Jestli že se někto ne narodi iz vody i Duha, ne može vstupiti do kraljevstva Božjego.
6 To, čto se rodilo iz těla, tělom jest, a to, čto se rodilo iz Duha, duhom jest.
7 Ne divi se, že jesm rěkl ti: Vy musite se snova naroditi.
8 Větr, kde hče, věje, i glas jego slyšiš, ale ne znaš, odkud prihodi i kudy ide; tako jest s každym, ktory se narodil iz Duha.“
9 Odgovoril Nikodem i rěkl jemu: „Kako to može byti?“
10 Odgovoril Jezus i rěkl jemu: „Ty jesi učiteljem v Izraelju, a togo ne znaš?
11 Istinno, istinno povědam ti, že to, čto znajemo, govorimo, a to, čto jesmo viděli, svědčimo: ale svědočstva našego ne prijmate.
12 Kogda jesm vam zemne věči povědal, a ne věrite, kako, jestli budu vam nebeske povědati, uvěrite?
13 A nikto ne vstupil do neba, toliko toj, ktori shodil s neba, Syn člověčsky, ktory jest v nebu.
14 A kako Mojzes zmiju na pralěsu vozvysil, tako ima byti vozvyšeny Syn člověčsky,
15 aby každy, kto v njego věri, ne pogynul, ale iměl věčny život.
16 Bo tak Bog ljubil svět, že dal Syna svojego jedinstvenogo, aby každy, ktory v njego věri, ne pogynul, ale iměl věčny život.
17 Bo ne poslal Bog Syna svojego na svět, aby sudil svět, ale aby svět byl spaseny črěz njego.
18 Kto věri v njego, ne bude sudženy; ale kto ne věri, už jest sudženy, že ne pověril v ime jedinstvenogo Syna Božjego.
19 A to jest sud, že světlo prišlo na svět, ale ljudi boljše ljubili temnost než světlo; bo byli zle dělesa jih.
20 Každy bo, kto zle čini, nenavidi světla i ne ide na světlo, aby ne byli izstavjene dělesa jego.
21 No kto čini pravdu, prihodi k světlu, aby byli javne dělesa jego, kak v Bogu sut učinjene.
22 Potom prišel Jezus i učeniki jego do Judejskoj zemji, i tam prěbyval s njimi i krestil.
23 Krestil tož i Joan v Enonu, blizko Salima; bo tam bylo mnogo vod, a ljudi prihodili i krestili se.
24 Bo ješče Joan ne byl podany do vezenja.
25 Vozbudila se besěda medžu učenikami Joana i medžu Židami o očiščenju.
26 I prišli do Joana i rěkli jemu: Učitelju! toj, ktory byl s toboju za Jordanom, komu jesi dal svědočstvo, toj kresti, a vsi idut do njego.
27 Odpovědal Joan i rěkl: Ne može ničto vzeti člověk, jestli by mu ne bylo dano s neba.
28 Vy sami jeste mi svědkami, že jesm rěkl: Ne jesm ja Hristos, ale jesm poslany prěd njim.
29 Kto ima ženu, toj jest mladoženih, a prijatelj mladoženiha, ktory stoji, a sluha jego, veseli se dlja glasu mladoženiha; Ta radost jest moja i stala se istinoju.
30 On povinen rasti, a ja povinen smenšati se.
31 Kto od gory prišel, nad vsim jest; kto iz zemji jest, zemny jest i zemne věči govori; toj, ktory prišel od neba, nad vsim jest.
32 A čto viděl i slyšal, to svědči, ale svědočstva jego nikto ne prijmaje.
33 Kto prijmaje svědočstvo jego, toj posvědčal, že Bog jest istinny.
34 Bo toj, ktorogo Bog poslal, slovo Božje govori; bo ne pod měroju da jemu Bog Duha.
35 Otec ljubi Syna, i vse dal v ruky jego.
36 Kto věri v Syna, ima život věčny; ale kto ne věri Synu, ne ogledaje života, no gněv Božji ostane nad njim.

## Razděl 4

1 A kogda Jezus poznal, že slyšali farizeji, že Jezus veče učenikov činil i krestil, neželi Joan,
2 (hot sam Jezus ne krestil, toliko jego učeniki),
3 ostavil židovsku zemju i odšel nazad do Galileji.
4 A imal prějdti črěz Samariju.
5 I prišel do města v Samariji, ktoro nazyvajut Syhar, blizko zemjedělišča, ktoro dal Jakob Jozefu, synu svojemu.
6 I byla tam studnja Jakoba; Jezus byl na stežkě izmučeny, sěděl na studnji; a bylo okolo šestoj časiny.
7 I prišla žena iz Samariji črpati vodu. I rěkl Jezus do njej: Daj mi piti!
8 (Bo jego učeniki odšli do města, aby kupili jedu.)
9 Rěkla jemu togdy ona, žena samaritska: Kako že ty byvši Židom, prosiš mene napoja, od ženy samaritankoj? (bo Židi ne besědujut s samaritanami.)
10 Odgovoril Jezus i rěkl jej: Bys znala toj dar božji, i kym jest toj, ktori ti govori: Daj mi piti. Ty bys jego prosila, a dal by ti vodu živu.
11 I rěkla jemu žena: Gospodi! Ne imaš i čim načrpati, a studnja jest gluboka, odkud že togda imaš tu vodu živu?
12 Či ty ješče večši, neželi otec naš Jakob, ktory nam dal tu studnju, i sam iz njej pil, i syni jego, i iměnje jego?
13 Odvětoval Jezus i rěkl jej: Každy, kto pije tu vodu, snova bude bolje žedati;
14 ale kto by pil onu vodu, ktoru ja jemu dam, ne bude žedati na věky; ale ta voda, ktoru ja jemu dam, stane se v njem iztočnikom vody izplyvšej k věčnomu životu.
15 Rěkla jemu žena: Gospodi! Daj mi tu vodu, aby ja ne žedala i ne tu črpati hodila.
16 Rěkl jej Jezus: Idi, kaži do sebe svojego muža i vrati tu.
17 Odgovorila žena i rěkla: Ne imam muža. Odgovoril jej Jezus: Dobre jesi rěkla: Ne imam muža.
18 Bo pet mužev jesi iměla, a nyně toj, kogo imaš, ne jest muž tvoj; to jesi pravdu rěkla.
19 Rěkla jemu žena: Gospodi! Vidžu, že ty jesi prorokoms.
20 Otci naši na toj gorě hvalili Boga, a vy povědate, že v Jeruzalemu jest město, v ktorom Boga trěba hvaliti.
21 Odgovoril jej Jezus: Ženo! Věri mi, že ide čas, kogda ni na toj gorě, ni v Jeruzalemu ne budete hvaliti Otca.
22 Vy hvalite, čego ne znate; a my hvalimo, čto znamo; bo izbavjenje jest iz Židov.
23 Ale prijde čas, i nyně jest, kogda istinni hvalitelji budut hvaliti Otca v duhu i v pravdě.
24 Duh jest Bogom. A ti, ktori by jego hvalili, trěba, by go hvalili v duhu i v pravdě. 
25 Rěkla jemu žena: Znam, že prijde Mesijas, kogo nazyvajut Hristosom. Toj, kogda prijde, oglasi nam vse.
26 Rěkl jej Jezus: Ja jesm toj, ktory s toboju govori.
27 A v tom prišli učeniki jego, i divili se, že so ženoju govori; No nikto ne rěkl: O čego se pytaš, abo čego s njeju razgovarjaš?
28 I ostavila ona žena vědro svoje, a pošla do města i rěkla ovym ljudam:
29 Pojdite, ogledajte člověka, ktory mi pověděl vse, čego jesm činila. Či li on jest Hristos?
30 I vyšli iz města i prišli do njego.
31 A medžu tym prosili jego učeniki, govoreči: Učitelju! Jedaj.
32 A on jim rěkl: Imam ja krmu iz bljuda, o ktorom vy ne znate.
33 Govorili togdy učeniki medžu soboju: Či mu někto prinosil jedu?
34 Rěkl jim Jezus: Moje jest jedivo, da byh činil volju ovogo, kto mene poslal, a dokončil děl jego.
35 Či vy ne govorite, že ješče četyri měsece, a sbože prijde? O to vam povědam: Voznesite oči vaše, a uzrite na polja, že sut už běle od sboža.
36 A kto žne, bere zaplatu, i sbiraje plod do věčnogo života, da by i toj, ktory sěje, radoval se zajedno s tym, ktory žne.
37 Bo v tom istinno jest ovo prislovje: Že jedin sěje, a drugi žne.
38 Jesm poslal vas žeti to, čego jeste ne dělali; drugi dělali, a jeste vstupili do roboty jih.
39 Togdy iz města ovogo mnogo Samarijanov uvěrilo mu črěz pověst ovoj ženy, ktora svědčila: On mi vse pověděl, čto jesm činila.
40 A kogda prišli k njemu Samarijani, prosili jego, da by u njih ostal; i ostal tam črěz dva dni.
41 I bolje jih uvěrilo črěz slova jego.
42 A ovoj ženě govorili: I už ne črěz tvoju pověst věrimo; Nyně my sami slyšali i znajemo, že on jest pravym spasiteljem světa, Hristos.
43 A po dvoma dnjah vyšel odtud i pošel do Galileji.
44 Bo sam Jezus svědočstvo izdal, že prorok v otčině svojej ne jest ččeny.
45 A kogda prišel do Galileji, prijali jego Galilejci. Viděli vse, čto činil v Jeruzalemu na prazdnik; bo i oni prišli na prazdnik.
46 I tako prišel Jezus nazad do Kany Galilejskoj, kde učinil iz vody vino. I byl někaky carski služebnik v Kafarnaumu, čijego syn bolěl.
47 On slyšal, že Jezus prišel iz Judejskoj zemji do Galileji, i šel k Njemu, prosil go, da by prišel i uzdravil jego syna, bo on umiral.
48 Jezus rěkl jemu: Jestli ne vidite znakov i čudes, ne věrite.
49 Carski služebnik odgovoril mu: Gospodi, prijdi, prědže než umre moje děte.
50 Jezus mu rěkl: Idi, tvoj syn jest živy. I uvěril člověk slovu, ktoro mu rěkl Jezus, i pošel.
51 I kako on šel, prišli jego slugi i javili, rěkli: Tvoje děte živo.
52 I pytal jih o časinu, v ktoru mu bylo lěpše; i odpověděli jemu, že včera o sedmoj časině ostavila jego gorečka.
53 I poznal otec, že to byla ona časina, o ktoroj mu rěkl Jezus: Tvoj syn živy. I uvěril on sam i ves jego dom.
54 To jest vtory znak, učinil Jezus, priševši iz Judejskoj zemji do Galileji.

## Razděl 5

1 Potom bylo židovsko sveto, i vstupil Jezus do Jeruzalema.
2 A v Jeruzalemu byla pri kaluži ovc jezero, ktoro nazyvajut po židovsku Betsaidu, imajuča pet kolumnad.
3 V tyh ležalo mnogo veliko nemočnyh, slěpyh, hromyh, izsohnutyh, ktori čekali dviženja vody.
4 A angel Gospodina v něktore vrěme stupal v jezero i voznesla se voda; i kto prvy stupil do toj vody, stal se zdravym, ravnodušno kaku hvorobu iměl.
5 A tam byl něktory člověk trideset i osm let s hvoroboju.
6 Kogda go Jezus uzrěl ležečego, i poznavši, že už dolgo vrěme hvoroval, rěkl jemu: Hčeš byti zdravym?
7 Odvětoval jemu on hory: Gospodine! Ne jest člověka, kto by mene, kogda byvaje dviženja vody, dal do jezera; ale kogda ja idu, ini prěd mnoju vstupajut.
8 Rěkl jemu Jezus: Vstani, vozmi lože tvoje, i idi.
9 I zaraz stal se zdravym on člověk, i vzel lože svoje, i pošel. A byla subota.
10 Togdy rěkli Židi ovu uzdravjenomu: Subota jest, ne godi se tobě lože nositi.
11 Odgovoril jim: Toj, kory mene uzdravil, on mi rěkl: Vozmi lože tvoje, i idi.
12 I pytali jego: Kto jest toj člověk, čto ti pověděl: Vozmi lože tvoje, i idi?
13 A on uzdravjeny ne věděl, kto by byl; bo Jezus pošel, bo mnogo ljudij bylo na ovom městu.
14 Potom jego Jezus našel v svetilišču i rěkl jemu: Jesi stal zdravym, ne grěši bolje, aby ničego goršego na tebe ne prišlo.
15 A odšel člověk, pověděl Židam, že to byl Jezus, ktory jego uzdravil.
16 I potom Židi prěslědovali Jezusa i iskali, kako by jego ubili, že to učinil v subotu.
17 A Jezus jim odgovoril: Otec moj do togo dnja rabota, i ja rabotaju.
18 Zato togdy bolje iskali Židi, kako by jego ubili, ne toliko, že lamal subotu, ale že i Otca svojego povědal byti Bogom, čto činilo go ravnym Bogu.
19 Odgovoril togdy Jezus i rěkl jim: Istinno, istinno povědam vam, ne može Syn sam od sebe ničto činiti, jedino čto vidi, že Otec čini; ibo čtokoli on čini, to takože i syn čini.
20 Bo Otec ljubi Syna i ukazyvaje jemu vse, čto sam čini, i boljše jemu nad te děla pokaže, byste se vy divili.
21 Ibo kako Otec budi mrtvo i oživjaje, tako i Syn, ktoro hče, oživjaje.
22 Bo Otec nikogo ne sudi, no vsaky sud dal Synu,
23 Aby vsi čestili Syna, tako kako čestet Otca; kto ne česti Syna, ne česti i Otca, ktory jego poslal.
24 Istinno, istinno povědam vam: Kto slovo moje sluša i věri mu, ktory mene poslal, imaje život věčny i ne prijde na sud, ale prěšel od smrti do života.
25 Istinno, istinno povědam vam: Ide čas i tutčas jest, kogdy mrtvi uslyšet glas Syna Božjego, a ktori uslyšet, živut budut.
26 Ibo kako Otec imaje život sam v sobě, tako dal i Synu, aby iměl život v samom sebe.
27 I dal jemu moč i sud činiti; bo jest Synom člověčjim.
28 Ne divite se tomu; bo prijde čas, v ktorom vsi, ktori sut v grobah, uslyšet glas jego;
29 I pojdut ti, ktori dobro činili, na vozkrešenje života; ale ti, ktori zlo činili, na vozkrešenje suda.
30 Ne mogu ja sam od sebe ničto činiti; kako slyšu, tako sudu, a sud moj jest spravědlivy; bo ne išču volje mojej, ale volju togo, ktory mene poslal, Otca.
31 Ako ja sam o sobě posvědčaju, moje svědočstvo ne jest istinne.
32 Iny jest, ktory o mene svědči, i věm, že istinno jest svědočstvo, ktoro on izda o mně.
33 Vy jeste posylali poslannikov k Joanu, a on dal svědočstvo istině.
34 Ale ja ne od čelověka svědočstva beru, no to govorju, aby vy byli spaseni.
35 On byl svěčeju gorečeju, a vy jeste htěli kratko radovati se v světlu jego.
36 Ale ja imam svědočstvo boljše než Joana; Sut děla, ktore mi dal Otec, byh je izpolnil. Te same děla, ktore ja činju, svědčet o mně, že mene Otec poslal.
37 A Otec, ktory mene poslal, on sam svědčil o mně. Jego jeste glasa nikogda ne slyšali, i jeste osoby jego ne viděli;
38 I slova jego ne imate v sobě; bo, kogo on poslal, tomu ne věrite.
39 Razbirajte Pisma; bo vy myslite, že v njih život věčny imate, a one svědočstvo davajut o mně.
40 A k mně prijdti ne hčete, aby vy život iměli.
41 Hvaly od ljudij ne beru.
42 Ale jesm vas poznal. Milosti Božjej ne imate v sobě.
43 Jesm prišel v imenu Otca mojego, a ne prijmete mene: ako by prišel iny v imenu svojem, ovogo prijmete.
44 Kako vy možete věriti. Vy, ktori hvalu jedin od drugogo prijmate, hvaly, ktora jest od samogo Boga, ne iščete?
45 Ne myslite, byh ja vas iměl obviniti prěd Otcem; jest, ktory obvini vas, Mojzes, v ktorom vy naděju imate.
46 Bo jestli byste věrili Mojzesu, věrili byste i mně; bo on o mně pisal.
47 Ale jestli jego Pismam ne věrite, mojim slovam věriti budete?

## Razděl 6

1 Potom odšel Jezus za Galilejsko morě, ktoro jest Tyberijadsko;
2 I šel za njim veliki narod, bo viděli jego čuda, ktore činil nad boljnymi.
3 I izšel Jezus na goru, i sěděl tam s svojimi učenikami;
4 A byla blizko Paša, židovsko sveto.
5 Togda voznesl Jezus oči i viděl, že veliky narod ide k njemu, rěkl Filipu: Odkud kupimo hlěba, da by se najeli?
6 (Ale to govoril, pokušajuči jego; bo on věděl, čto iměl činiti.)
7 Odgovoril mu Filip: Za dvěstě grošev hlěba ne jim ne bude dostatočno, hot by každy iz njih malo sobě vzel.
8 Rěkl mu jedin iz jego učenikov, Andrej, brat Simona Petra:
9 Jest tu jedno hlapec, ktory imaje pet hlěbov ječmennyh i dvě ryby; ale čto to jest na toliko mnogyh?
10 Togda rěkl Jezus: Kažite narodu posědati. A bylo travy dostatočno na tom městu, i sědělo mužev v čislu okolo pet tyseč.
11 Vzel togdy Jezus ti hlěby, a podekujuči razdal učenikam, a učeniki sědečim; takože i iz tyh ryb, koliko kto htěl.
12 A kogda byli nasyčeni, rěkl svojim učenikam: Sberite te ostatky, da by ničto ne izgynulo.
13 I sbirali i napolnili dvanadset košev ostatkov iz pet hlěbov ječmennyh, ktore ostali.
14 A ti ljudi, viděvši čudo, ktore učinil Jezus, govorili: To jest istinny prorok, ktory iměl prijdti na svět.
15 Togda Jezus poznavši, že iměli prijdti i shvatiti jego, da by jego učinili kraljem, utekl nazad sam jednin na goru.
16 A kogda byl večer, stupili jego učeniki do morja.
17 I vstupili do čolna, jehali za morje do Kafarnauma, i už bylo temno, a Jezus ne prišel do njih.
18 A morje, kogda povstal veliky větr, počelo se buriti.
19 Kogda pluli črěz približno dvadeset pet ili trideset stadijov, uzrěli Jezusa, idučego po morju, približajučego se k čolnu, i prěstrašili se.
20 A on jim rěkl: To ja jesm, ne bojite se.
21 I vzeli go ohotno do čolna, i v tom momentu čoln priplul do zemji, do ktoroj jehali.
22 Na zautra ljud, ktory byl za morjem, viděl, že tam ne bylo drugogo čolna, toliko jednogo, do ktorogo vstupili jego učeniki, i že Jezus ne všel do čolna s svojimi učenikami, a toliko sami jego učeniki ujehali;
23 (I prišli druge čolny iz Tiberijady, blizko do ovogo města, kde jeli hlěb, čto by Gospoda hvaliti.)
24 Kogda ljud viděl, že tam ne bylo Jezusa, ni jego učenikov, vstupili i oni do čolna i prěpluli do Kafarnauma, iščuči Jezusa;
25 I našli go za morjem, rěkli mu: Učitelj! kogda jesi tu pribyl?
26 Odvětoval jim Jezus i rěkl: Istinno, istinno vam povědam: Iščete mene ne za to, že jeste viděli čuda, ale že jeste jeli hlěb, i jeste najedli se.
27 Starajte se ne o jedu, ktora pogyna, ale o jedu, ktora trvaje k věčnomu životu, ktory vam da Syn člověčsky; bo jego zapečatal Bog Otec.
28 Rěkli togdy jemu: Čto budemo činiti, byhmo činili děla Božje?
29 Odgovoril Jezus i rěkl jim: To jest dělo Božje, byste věrili v togo, kogo on poslal.
30 Rěkli jemu togdy: Kaky znak ty činiš, byhmo viděli i věrili tobě? Čto činiš?
31 Otci naši jedli mannu na pustynji, kako jest pisano: Hlěb s neba dal jim do jedanja.
32 Rěkl jim togdy Jezus: Istinno, istinno povědam vam: Ne Mojzes vam dal hlěb s neba, ale Otec moj da vam hlěb istinny s neba.
33 Bo hlěb Božji to jest, ktory stupaje s neba i život da světu.
34 Togdy mu rěkli: Gospodine! daj nam vsegda togo hlěba.
35 I rěkl jim Jezus: Ja jesm hlěb života; kto do mene prihodi, ne bude gladovati, a kto věri v mene, nikogda žedati ne bude.
36 Ale jem vam pověděl: jeste viděli mene, a ne věrite.
37 Vse, čto mi davaje Otec, do mene prijde, a togo, kto do mene prijde, ne izkydnu proč.
38 Bo jesm stupil s neba, ne že byh činil volju svoju, ale volju onogo, ktory mene poslal.
39 A ta jest volja ovogo, ktory mene poslal, Otca, da byh iz vsego togo, čto mi dal, ničto ne tratil, ale da byh to vozkresil v poslědnjem dnju.
40 A ta jest volja onogo, ktory mene poslal, da by každy, ktory vidi Syna, a věri v njego, iměl život věčny; a ja jego vozkresil v ovom poslědnjem dnju.
41 I roptali Židi o njem, že rěkl: Ja jesm hlěb, ktory s neba stupil.
42 I govorili: Či ne jest to Jezus, syn Jozefa, kogo my otca i mati znajemo; kako togda on pověda: Jesm s neba stupil?
43 Togda odgovoril Jezus i rěkl jim: Ne roptajte medžu soboju.
44 Nikto do mene prijdti ne može, jestli Otec moj, ktory mene poslal, jego ne provodi; a ja jego vozkrešu v poslědnjem dnju.
45 Pisano v prorokah: I budut vsi poučeni od Boga; Každy, ktory slyšal od Otca, a naučil se, prihodi do mene.
46 Ne kako by kto viděl Otca, kromě togo, kto jest od Boga; on viděl Otca.
47 Istinno, istinno povědam vam: Kto věri v mene, ima věčny život.
48 Ja jesm hlěbom života.
49 Oči vaši jedli mannu na pustynju, a umrli.
50 To jest hlěb, ktory s neba shodi; jestli by jego kto jel, ne umre.
51 Ja jesm hlěbom živym, ktory shodil s neba: jesti by kto jel od togo hlěba, živy bude na věky; a hlěb, ktory ja dam, jest tělo moje, ktore ja dam za život sveta.
52 Sporili se togdy Židi medžu soboju I kazali: Kako že toj može nam dati tělo svoje do jedenja?
53 I rěkl jim Jezus: Istinno, istinno povědam vam: Jestli ne budete jeli těla Syna člověčskogo, i pili krvi jego, ne imate života v sobě.
54 Kto je tělo moje, a pije krov moju, ima život věčny, a ja jego vozbudžu v ovom poslědnjem dnju.
55 Ibo tělo moje istinno jest jedoju, a krov moja istinno jest napojem.
56 Kto je tělo moje i pije krov moju, vo mně žive, a ja v njem.
57 Kako mene poslal živy Otec, i ja živu črěz Otca; tak kto mně je, živy bude črěz mene.
58 To jest hlěb, ktory shodil s neba, ne kako oči vaši jedli mannu, a umrli; kto je toj hlěb, živy bude na věky.
59 To govoril v bóżnicu, kak učil v Kafarnaumu.
60 Mnogi togdy iz učenikov jego slyšeče to, govorili: Tvrda to jest besěda, kto že jej slušati može?
61 No znajuči Jezus sam v sobě, že o tom roptajut jego učeniki, rěkl jim: To vas uraža?
62 Čto, jestli byste viděli Syna Člověčskogo vstupajučego, tudy, kde byl najprvo?
63 Duh jest, ktory oživjaje, tělo ničto ne pomaga; slova, ktore ja vam govorju, sut duhom i životom.
64 No sut něktori iz vas, ktori ne věret; od početka věděl Jezus, ktori byli ti, ktori ne věrili, i kym jest, ktory jego iměl izdati;
65 I govoril: nikto ne može prijdti do mene, jestli by jemu ne bylo dano od Otca mojego.
66 Od togo vrěmena mnogo učenikov jego odšlo nazad, a už s njim ne hodili.
67 Togda rěkl Jezus ovym dvanadsetom: Tož vy hčete li odidti?
68 I odgovoril jemu Simon Petr: Gospodine! Do kogo pojdemo? Ty imaš slova života věčnogo;
69 A my věrimo i jesmo poznali, že ty jesi Hristos, Syn Boga živogo.
70 Odgovoril jim Jezus: Či jesm ja ne dvanadset iz vas izbral? a jedin iz vas jest běsom.
71 A to govoril o Judasu, synu Simona, Iskarjotskomu; bo jego toj izdati iměl, byvši jednym iz ovyh dvanadseti.

## Razděl 7

1 Potom hodil Jezus po Galileji; bo ne htěl byvati v zemji Judejskoj, bo Židi iskali jego ubiti.
2 I bylo blizko židovskogo sveta hat.
3 Togda rěkl jemu brati jego: odidi odsud, i idi do Judejskoj zemji, da by učeniki tvoji viděli děla tvoje, ktore činiš.
4 Ibo nikto ne čini ničego v tajnosti, kto hoče byti viděny; jestli ty take věči činiš, javi se svetu.
5 Bo i brati jego ne věrili v njego.
6 I rěkl jim Jezus: Čas moj ješče ne došel; ale čas vaš vsegda jest gotovy.
7 Ne može vas svět nenaviděti, ale mene nenavidi; bo ja svědču o njem, že děla jego zle sut.
8 Idite že vy na to sveto, ja že ješče ne idu na toj denj svety; bo moj čas ješče ne izpolnil se.
9 A to jim povědavši, ostal v Galileji.
10 A kogdy pošli brati jego, togda i on pošel na sveto, ne javno, ale kakoby tajemno.
11 A Židi iskali jego v sveto i govorili: Kde že on jest?
12 I bylo o njem veliko roptanje medžu ljudami; bo jedni govorili: Že jest dobry; a drugi govorili: Ne, ale obmanyva ljudij.
13 O njem nikto javno ne govoril, dlja bojazni židovskoj.
14 A kogdy už bylo v pol sveta, vstupil Jezus do svetilišča i učil.
15 I divili se Židi, I govorili: Kako že on zna Pismo, kak ne učil se?
16 Odpověděl jim Jezus i rěkl: Nauka moja ne jest moja, ale togo, ktory poslal mene.
17 Jestli by kto htěl tvoriti volju jego, toj bude mogl poznati, jestli ta nauka jest od Boga, ili ja sam od sebe govorju.
18 Kto od samogo sebe govori, hvaly vlastnoj išče; ale kto išče hvaly togo, ktory poslal jego, toj jest pravdivy, a ne jest v njem nespravědlivosti.
19 Či vam Mojzes ne dal zakona? A ni jedin iz vas ne čini zakona. Čemu iščete mene ubiti?
20 Odpověděl narod i rěkl: Djabolstvo imaš; kto tebe išče ubiti?
21 Odpověděl Jezus i rěkl jim: Jedno dělo jesm tvoril, a vsi se tomu divite!
22 Zato Mojzes dal vam obrězanje (ne že by bylo od Mojzesa, ale od otcev), a v subotu obrěžete člověka.
23 Jestli člověk prijma obrězanje v subotu, aby ne byl narušeny zakon Mojzesa. Čemu se na mene gněvate, že jesm cělogo člověka uzdravil v subotu?
24 Ne sudite po viděnju, ale sudite spravědlivy sudom.
25 Govorili togdy něktori iz Jeruzalema: Či to ne jest toj, ktorogo iščut ubiti?
26 A ovo javno govori, a ničto jemu ne govoret. Či pravdivo poznali starši, že on jest pravdivo Hristos?
27 Ale o tom věmo, odkud jest; ale kogda Hristos prijde, nikto ne bude věděl, odkud byl.
28 Kazal do sebe togdy Jezus v svetilišču, učil i govoril: I mene znate, i odkud jesm, věte; a jesm ne prišel sam v mojim imenu, ale toj jest pravdivy, ktory poslal mene i vy ne znate.
29 A jego ja znam; bo jesm od njego, a on poslal mene.
30 I iskali, kako by jego pojmati; ale ni jedin ne dvignul na njego ruky; bo ješče ne prišla časina jego.
31 I mnogo jih iz naroda uvěrili v Jezusa i govorili: „Hristos, kogda prijde, li više čudesa učini, než to, čto on učinil?“
32 A slyšali Farizeji, že to narod o njem roptal; i poslali Farizeji i starši svečenniki slugy, da by jego pojmali.
33 Rěkl jim Jezus: „Ješče na malo vrěme jesm s vami; potom pojdu do togo, ktory mene poslal.
34 Iskati mene budete, ale ne najdete; a kde ja budu, vy prijdti ne možete.“
35 Govorili Židi medžu soboju: „Kudy toj pojde, že my jego ne najdemo? Či do Grkov pojde i bude učiti jih?
36 Čto to za slovo, ktoro izrěkl: Iskati mene budete, ale ne najdete, i kde ja budu, vy prijdti ne možete?“
37 A v poslědnjem dnju velikogo ovogo prazdnika stal Jezus i kazal glasno: „Jestli li kto žadne, nehaj do mene prijde, i pije.
38 Kto věri v mene, kako govori Pismo, rěky vody živoj iztekut iz života jego.
39 (A to govoril o Duhu, kogo vzeti iměli věreči v Jezusa; ibo ješče ne byl dany Duh Svety, zatože ješče Jezus ne byl slavjeny.)
40 Mnogo jih togdy iz ovogo naroda, slyšeči te slova, govorili: „Toj jest zapravdu jest prorokom.“
41 A drugi govorili: „Toj jest Hristos“; ale něktori govorili: „Či iz Galileji prijde Hristos?“
42 Či ne govori Pismo, že iz sěmena Davida i iz Betlehema městečka, kde byl David, prijde Hristos?
43 A tako razdělil se dlja njego narod.
44 I hotěli jego něktori iz njih pojmati; ale ni jedin ne směl se dotknuti jego rukoju svojeju.
45 Prišli togdy slugy k staršim svečennikam i k farizejam; ktori jim rěkli: „Čego jeste jego ne privedli?“
46 Odgovorili slugi: Nikogda tak ne govoril čelověk, kak toj čelověk.
47 I odgovorili jim farizeji: Či i vy jeste obmanuti?
48 Či kto uvěril v njego iz starših ili iz farizejev?
49 Toliko ti ljudi, ktori ne znajut zakona, prokleti sut.
50 I rěkl jim Nikodem, ktory prišel nočju k njemu, ktory byl jedin iz njih:
51 Či zakon naš sudi čelověka, jestli by prěd razpyta jego i ne poznanja, čto čini?
52 I oni mu odgovorili i rěkli: Či i ty jesi iz Galileji? Razbiraj Pismo i uvidiš, že prorok iz Galileji ne voznese se.
53 I pošel každy do svojego domu.

## Razděl 8

1 A Jezus pošel na Goru Maslinovu.
2 Potom rano prišel do svetilišča, i cěly narod sobral se k njemu; usědl i učil jih.
3 I privedli k njemu naučniki i farizeji ženu, ktoro zastano pri prěljubstvu, i postavivši ju posrěd,
4 rěkl mu: Učitelju! Tu ženu zastali pri samom činu prěljubstva;
5 A v zakonu nam Mojzes pověděl take kamenovati; a ty čto govoriš?
6 A to govorili, izkušajuči jego, da by mogli jego obviniti. A Jezus sklonivši se dolu, pisal prstom na zemji.
7 A kogda ne ustali pytati jego, on voznesl se, rěkl jim: Kto jest bez grěha iz vas, nehaj na nju prvy kamen kydne.
8 A sklonivši se dolu, pisal na zemji.
9 A kogda oni uslyšali, jedin za drugym izhodil, počevši od starših do poslědnyh, že toliko sam Jezus ostal, a žena posrěd stojala.
10 A voznesši se Jezus rěkl jej: Ženo! Kde sut oni, ktori na te skaržili se? Nikto te ne osudil?
11 A ova žena rěkla: Nikto, Gospodine! A Jezus jej rěkl: A tož ja tebe ne osudžu; idi že, a uže veče ne grěši.
12 Že jim rěkl Jezus: Ja jesm světlo světa; kto mně slěduje, ne bude hodil v temnosti, ale bude iměti světlo života.
13 I rěkli mu togdy farizeji: Ty sam o sobě svědčiš, a svědočstvo tvoje ne jest istinno.
14 Odgovoril Jezus jim: Hot ja svědču sam o sobě, jednako istinno jest svědočstvo moje; bo věm, odkud prišel i komu idu; no vy ne věte, odkud jesm prišel i kudy idu.
15 Vy po tělu sudite; ale ja nikogo ne sudžu.
16 A jestli ja sudžu, moj sud jest pravdivy, bo ja ne jesm sam, ale jesm s Otcem, ktory mene poslal.
17 V vašem zakonu jest napisano, že svědočstvo dvoh ljudij jest pravdivo.
18 Ja jesm, ktory sam o sobě davaju svědočstvo, i moj Otec, ktory poslal me, svědočstvo davaje o mně.
19 Potom govorili mu: Kde jest tvoj Otec? Jezus odgovoril: Ne znajete ni mene, ni mojego Otca. Byste znali mene, znali byste i mojego Otca.
20 Te slova govoril Jezus v skarbnici, učil v svetilišču, i nikto jego ne pojmal, bo jego čas ješče ne prišel.
21 On jim povědal: Ja odhodžu, i budete mene iskati, a umrete v vašem grěhu. Kudy ja idu, vy ne možete prijdti.
22 Židi govorili: Či on ubije sebe, že kaže: Kudy ja idu, vy ne možete prijdti?
23 Jezus jim povědal: Vy jeste iz nizkosti, a ja iz vyšiny. Vy jeste iz togo světa, a ja ne jesm iz togo světa.
24 Slědovateljno ja vam povědal, že umrete v grěhah vaših. Jestli ne věrite, že ja jesm, umrete v vaših grěhah.
25 Oni jego pytali: Kto ty jesi? Jezus jim odgovoril: To, čto vam pravim od početka.
26 Mnogo imam o vas govoriti i suditi. Ale toj, ktory poslal me, jest pravdivy, i ja govorju svetu to, čto slyšal od njego.
27 Oni ne razuměli, že jim govoril o Otcu.
28 Jim Jezus povědal: Kogdy povysite Syna člověčskogo, poznate, že ja Jim jesm, i ne činim ničego sam od sebe, ale govorju tako, kako me naučil moj Otec.
29 A toj, ktory poslal me, jest so mnoju. Otec me ne ostavil samogo, bo ja vsegda činim to, čto mu se podoba.
30 Kogdy on to govoril, mnogo jih uvěrilo v njego.
31 Togdy rěkl Jezus Židam, čto jemu uvěrili: Jestli vy ostanete v mojem slovu, istinno učenicami mojimi budete;
32 Poznajete pravdu, i pravda vas osvobodi.
33 I odgovorili jemu: My jesmo sěme Abrahama, a nikogda jesmo ne služili nikomu; kako že ty govoriš: Svobodnymi budete?
34 Odgovoril jim Jezus: Istinno, istinno, povědam vam, iže každy, kto čini grěh, slugoju jest grěha.
35 A sluga ne žive v domu na věky, ale Syn žive na věky.
36 Ibo jestli vas Syn osvobodi, istinno svobodnymi budete.
37 Věm, že jeste sěmenom Abrahama; ale iščete mně ubiti, že mně slovo moje ne imaje u vas města.
38 Ja, čto jesm viděl u Otca mojego, povědam, a vy činite tož to, čto jeste viděli u otca vašego.
39 Odgovorili jemu i rěkli: Otec naš jest Abraham. Rěkl jim Jezus: Byste byli synami Abrahama, činili byste učinky Abrahama.
40 Ale nyně iščete, byste mně ubili, člověka togo, ktory vam pravdu govoril, ktoru jesm slyšal od Boga; togo Abraham ne činil.
41 Vy činite učinky otca vašego. Rěkli jemu togdy: My iz prěljubstva ne jesmo splodženi, jedinogo že Otca imamo, Boga.
42 Togdy jim rěkl Jezus: By Bog byl Otcem vašim, togdy byste mně ljubili, ibo jesm od Boga izšel i prišel, a ne sam od sebe prišel. On mně poslal.
43 Čemu te pověsti moje ne pojmate? Až ne možete slušati rěči mojej.
44 Vy jeste iz otca črta i želanja otca vašego činiti hčete; on byl ubijceju od početka i v pravdě ne ostal, bo v njem pravdy ne imaš: kogda govori lže, iz svojego vlastnogo govori. Ibo jest lžecem i otcem lži.
45 A jestli pravdu govorju, ne věrite mi.
46 Kto iz vas obvini mene iz grěha? Jestli pravdu govorju, čemu vy mně ne věrite?
47 Kto jest od Boga, slov Božjih sluša; po tomu vy ne slušate, že vy ne jeste od Boga.
48 Odgovorili togdy Židi i rěkli jemu: Či my ne dobro govorimo, že ty jesi Samaritaninom i črta imaš?
49 Odrěkl Jezus: Ja ne imam črta, ale čču Otca mojego; a vy jeste mene ne čtili.
50 Ja ne išču slavy mojej; jest on, kto išče i sudi.
51 Istinno, istinno povědam vam: Jestli kto slova moje zadržati bude, smrti ne uzri na věky.
52 Togdy mu rěkli Židi: Tutčas jesmo poznali, že črta imaš. Abraham umrl i proroki; a ty povědaš: Jestli kto slova moje zadržati bude, smrti ne obgleda na věky.
53 Či ty jesi boljši od otca našego Abrahama, ktory umrl? I proroki umrli. Za kogo ty se činiš?
54 Odgovoril Jezus: Jestli ja sam sebe hvalu, slava moja ničto ne jest. Jest Otec moj, ktory mene hvali, o kom vy povědate, že on jest vaš Bog.
55 Ale jego ne znajete. A ja jego znam; i jestli byh rěkl, že jego ne znam, byl byh podobny vam, lžecem; ale jego znam i slova jego strěgu.
56 Abraham, vaš otec, s radostju želal, aby viděl moj den; i viděl i radoval se.
57 Togdy rěkli Židi jemu: Petdeset lět ty ješče ne imaš, a Abrahama jesi viděl?
58 Rěkl jim Jezus: Istinno, istinno povědam vam: Skorěje než Abraham byl, JA JESM.
59 Vozdvignuli togdy kamene, aby na njego metnuti; ale Jezus skryl se i vyšel iz svetilišča.

## Razděl 9

1 I mimo iduči, uzrěl člověka slěpogo od rodženja.
2 I pytali jego učeniki jego: Učitelju! Kto sgrěšil, toj či roditelji jego, že slěpym se narodil?
3 Odpověděl Jezus: Ni toj sgrěšil, ni roditelji jego; Da by se okazali děla Božje na njem.
4 Mně trěba činiti děla ovogo, ktory mene poslal, poka den jest; prihodi noč, kogda ni jedin ne bude mogti ničto dělati.
5 Poka jesm na světu, jesm světlom světa.
6 To rěkši pljuval na zemje, a učinil blato iz toj sliny i pomazal ovym blatom oči slěpogo,
7 I rěkl jemu: Idi, umyj se v jezeru Siloe, čto se prěvodi poslany. Pošel togdy i umyl se, i prišel videči.
8 A tak susědi i kto jego prěd tym viděl kako slěpy, govorili: Či to ne jest toj, kto sědal i izprašal?
9 Jedni govorili: On to jest; a drugi, že jest jemu podobny. Ale on govoril jim, že on njim jest.
10 Togda jemu rěkli: Kako otvorili se oči tvoje?
11 A on odgovoril i rěkl: Člověk, kogo zovut Jezusom, učinil blato i pomazal oči moje, a rěkl mi: Idi do jezera Siloe, a umyj se; a tak pošel i umyl se, i naglo vidžu.
12 Togdy jemu rěkli: Kde on jest? Rěkl: Ne věm.
13 Togdy privedli ovogo, ktory prěd tym byl slěpy, do Farizejev.
14 A byla suboty, kogda Jezus učinil blato i otvoril oči jego.
15 Togdy go snova pytali Farizeji, kako uviděl? A on jim rěkl: Vložil mi blata na oči, i jesm umyl se i vidžu.
16 Togda něktori iz Farizejev rěkli: "Člověk toj ne jest od Boga, ibo ne strěže suboty". Drugi že govorili: "Kako može grěšny člověk take čuda tvoriti?" I bylo razděljenje medžu njimi.
17 Rěkli togdy slěpomu povtorno: "Ty čto govoriš o njem, kak otvoril oči tvoje?" A on rěkl: "Prorok jest".
18 A ne věrili Židu o njem, že byl slěpym i že uviděl, až kazali do sebe roditeljev ovogo, ktory uviděl.
19 I pytali jih "Jest li syn vaš, o ktorom vy povědate, že se slěpo narodil? Kako že vidi nyně?"
20 Odgovorili jim roditelji jego i rěkli: "Věmo, že to jest syn naš, i že se slěpo narodil;
21 Ale kako nyně vidi, ne věmo, ili kto otvoril oči jego, my ne věmo; imaje lěta, pytajte jego, on sam o sobě pově".
22 Tako govorili roditelji jego, že se bojali Židov; ibo Židi rěšili, aby ktokoli by jego Hristosom izznačal, byl iz svetilišča izključeny.
23 Zato rěkli roditelji jego: "Imaje lěta, pytajte jego".
24 Togda kazali do sebe povtorno člověka ovogo, ktory byl slěpy, i rěkli jemu: "Daj slavu Bogu; my věmo, že člověk toj jest grěšny".
25 A on odgovoril: "Jestli grěšny jest, ne věm; toliko věm, že byvši slěpym, nyně vidžu".
26 I rěkli jemu snova: "Čto ti učinil? Kako otvoril oči tvoje?"
27 Odgovoril jim: "Uže vam skazal, a jeste ne slyšali; Čemu že snova slyšati hčete? Vy hčete li byti učenikami jego?"
28 Togda mu prokleli i rěkli: "Ty budi učenikom jego; ale my jesmo učenikami Mojzesa.
29 My věmo, že Bog do Mojzesa govoril; ale toj, odkud by byl, ne věmo".
30 Odgovoril člověk jim: "To jest zapravdu rěč divna, že vy ne věte, odkud jest, a otvoril oči moje".
31 A věmo, že Bog grěšnikov ne slušaje, ale jestli někto jest čestiteljem Boga i volju jego čini, togo slušaje.
32 Od věka ne slyšano bylo, aby někto otvoril oči slěpo rodženomu.
33 Jestli by sej ne byl od Boga, ne by mogl ničto učiniti.
34 Odgovorili jemu: Ty jesi urodil v grěhah, a ty nas učiš? I izgnali jego von.
35 A uslyšavši Jezus, že jego izgnali von, strětl go, rěkl jemu: Věriš li v Syna Božjego?
36 On odgovoril: A ktory jest, Gospodine, aby ja věril v njego?
37 I rěkl jemu Jezus: Jesi viděl jego, i ktory govori s toboju, jest njim.
38 A on odpověděl: Věru, Gospodine! I poklonil se jemu.
39 I rěkl jemu Jezus: Na sud ja prišel na sej svět, aby ti, ktori ne videt, viděli, a ti, ktori videt, byli slěpymi.
40 I uslyšali to něktori iz Farizejev, ktori byli s njim, i rěkli jemu: Či i my slěpi jesmo?
41 Kazal jim Jezus: Jestli byste byli slěpymi, byste ne iměli grěha, no nyně govorite, že vidimo. Ibo grěh vaš ostava.

## Razděl 10

1 Istinno, istinno povědam vam: Kto ne vhodi dverami do ovčarnji, a vhodi inače,  jest zlodějem i razbojnikom;
2 Ale kto vhodi dverami, pastyrem jest ovc.
3 Tomu vratnik odkryva, i ovce slyšet jego glasa, a on svoje vlastne ovce po imenam zove i izvodi je.
4 A kogda izpusti svoje ovce, ide prěd njimi, a ovce idut za njim, bo znajut jego glas.
5 Ale za čudžim ne idut, no utěkajut od njego, bo ne znajut glasa čudžih.
6 Tu pripověst Jezus jim pověděl, a oni ne razuměli togo, čto jim govoril.
7 Rěkl jim togdy Jezus: Istinno, istinno povědaju vam, že ja jesm dverami ovc.
8 Vsi, koliko jih prěd mnoju prišlo, zlodějami sut i razbojnici, ale jih ne slyšali ovce.
9 Ja jesm dverami; jestli kto črěz mene pojde, izbavjeny bude, vojde i vyjde, a pastvišče najde.
10 Zloděj ne prihodi, jedino da by kradl, a ubil i niščiti; jesm prišel, da by život iměli, i bujnost iměli.
11 Ja jesm dobry pastyr; dobry pastyr dušu svoju davaje za ovce.
12 A najemnik i toj, ktory ne jest pastyrem,ktorogo ne sut ovce vlastne, vidi volka prihodečego, ostavi ovce i utěkaje, a volk odnosi i razsypaje ovce.
13 A najemnik utěkaje, že jest najemnikom i ne ima staranja o ovcah.
14 Ja jesm dobry pastyr i znam moje, a moje me tož znajut.
15 Kako me zna Otec i ja znam Otca, i dušu moju kladu za ovce.
16 I imam druge ovce, ktore ne sut iz ovčarnji, i tož trěba mi jih privesti; i glasu mojemu poslušati budut, a bude jedna ovčarnja i jedin pastyr.
17 Za to mene ljubi Otec, že ja kladu dušu moju, da byh ju nazad vzel.
18 Nijedin jej ne bere od mene, ale ja kladu ju sam od sebe; imam moč položiti ju i imam moč nazad vzeti ju. To razkazanje jesm vzel od Otca mojego.
19 Togdy se stalo snova razděljenje medžu Židami poradi tyh slov.
20 I govorilo mnogo iz njih: Črt ima i šalěje; čemu jego slušajete?
21 Drugi govorili: Te slova ne sut črta; či može črt slěpyh oči otvarjati?
22 A bylo v Jeruzalemu osvečanje svetilišča, a zima byla.
23 I hodil Jezus v svetilišču, v salě Salomona.
24 Togda jego obstupili Židi i rěkli jemu: Na čto čekaš? Jestli ty jesi Hristosom, skaži nam javno.
25 Odgovoril jim Jezus: Jesm pověděl vam, a ne věrite; děla, ktore ja činu v imenu Otca mojego, o mně svědčet.
26 Ale vy ne věrite; bo ne jeste iz ovc mojih, kako jesm vam pověděl.
27 Ovce moje glasu mojemu slušajut, a ja je znam i idut za mnoju;
28 A ja život věčny dam jim i ne pogynut na věky, nijedin jih vozme iz ruky mojej.
29 Otec moj, ktory mi je dal, je boljšim jest nad vsim, a žaden ne može jih vzeti iz ruky Otca mojego.
30 Ja i Otec jedno jesmo.
31 Vzeli Židi snova kamenje, da by jego kamenovali.
32 Odgovoril jim Jezus: Mnogo dobryh děl jesm ukazal vam od Otca mojego, za ktoro iz tyh děl kamenujete mene?
33 Odpověděli jemu Židi: Ne za dobro dělo kamenujemo te, ale za bogohulstvo, to jest, že ty, byvši člověkom, činiš se samym Bogom.
34 Odgovoril jim Jezus: Či ne jest pisano v zakonu vašem: Ja jesm rěkl: Bogi jeste?
35 Jestli on tyh nazval bogami, do ktoryh prišlo slovo Božje, a ne možno odstaviti Pisma;
36 A mně, kogo Otec osvetil i poslal na svět, vy govorite: Bogohuliš, že jesm rěkl: Jesm Syn Božji?
37 Jestli ne činju děl Otca mojego, ne věrite mi.
38 A jestli činju, hot byste mi ne věrili, věrite dělom, da by poznali i věrili, že Otec jest vo mně, a ja vo njem.
39 Togdy snova iskali, kako by jego pojmati; ale ušel iz ruk jih.
40 I odšel snova za Jordan na ono město, kde najprvo Joan krestil, i tam že žil.
41 A mnogo jih prihodilo  do njego i govorili: Joan ni jedinogo čuda ne učinil.
42 Vse, čto Joan o tom pověděl, pravdivo bylo. I mnogo jih uvěrilo v njego.

## Razděl 11

1 A byl někaky boljny Lazar iz Betaniji, iz grada Mariji i Marty, sestry jego.
2 (A to byla Marija, ktora pomazala Gospoda mastju i utirala nogy jego vlasami svojimi. Jej brat Lazar hvoroval.)
3 Poslali togdy sestry do njego, govoreči: Gospodine! Vot toj, kogo ljubiš, bolěje.
4 A uslyšavši to Jezus, rěkl: Ta bolěznj ne jest na smrt, ale za slavu Božju, aby byl obožany Syn Božji črěz nju.
5 A Jezus ljubil Martu i sestru jej, i Lazara.
6 A kogdy uslyšal, že bolěje, togdy ostal črěz dva dni na tomže městu.
7 Ale potom rěkl učenikom svojim: Idemo do židovskoj zemji.
8 Rěkli jemu učenici: Učitelju! Tutčas iščut te Židi, kako by te kamenovali, a  tam ideš?
9 Odgovoril: Či ne dvanadset jest časin dnja? Jestli kto hodi vo dne, ne urazi se; bo vidi světlo světa togo.
10 A jestli kto hodi v noči, urazi se; bo v njem světla něma.
11 To pověděvši, potom rěkl jim: Lazar, prijatelj naš, spi; ale idu, aby jego iz sna budil.
12 Togdy rěkli učeniki jego: Gospodine! Jestli že spi, bude zdrav.
13 Ale Jezus govoril o smrti jego; oni mněli, že o zaspanju snom govoril.
14 Togdy jim rěkl Jezus javno: Lazar umrl.
15 I raduju se dlja vas (byste věrili), že jesm tam ne byl; ale pojdemo do njego.
16 Rěkl že Tomas, ktory byl znany kako Didymus, drugym učenikam: Pojdemo, da by my s njim umrli.
17 I prišel togda Jezus, našel jego už četyri dni ležavšego v grobu.
18 A byla Betanija blizko Jeruzalemu, tak na petnadset stadij.
19 A prišlo mnogo Židov do Marty i Mariji, da by jih utěšali po bratu jih.
20 Marta že, slyšavša, že Jezus ide, běgala do njego; Marija že sěděla v domu.
21 I rěkla Marta Jezusu: Gospodine! Jestli bys tut byl, ne umrl by brat moj.
22 Ale i nyně věm, že o čtokoli bys prosil Boga, da ti to Bog.
23 Rěkl jej Jezus: Vstane brat tvoj.
24 Odgovorila jemu Marta: Věm, že vstane v vozkrešenju v poslědnom dnju.
25 I rěkl jej Jezus: Ja jesm vozkrešenje i život; kto věri vo mně, jestli tož umre, žiti bude.
26 A každy, kto žive i věri vo mně, ne umre na věky. Věriš li tomu?
27 Rěkl jemu: Da Gospodine! Ja uvěrila, že ty jesi Hristos, Syn Božji, ktory iměl prijdti na svět.
28 A to rěčevši, pošla i tajno kazala do sebe Mariju, svoju sestru, govoreči: Tut jest učitelj, i kaže tebe do sebe.
29 Ona uslyšala, skoro vstala i pošla do njego.
30 (A Jezus ješče ne prišel do grada, ale byl na tomže městu, kde Marta do njego prišla.)
31 Židi že, ktori s njeju byli v domu i těšili ju, viděvši Mariju, že skoro vstala i vyšla, šli za njeju I govorili: „Ide k grobu, aby tam plakala.“
32 Ale Marija, kogda tam prišla, kde byl Jezus, viděvši jego, pripadla k nogam jego i rěkla: „Gospodine! Kak by jesi tu byl, ne umrl by moj brat.“
33 Jezus že, kogda ju viděl plačuču i Židov, ktori s njeju prišli, plakali, smekčal se v duhu i razčulil se,
34 i rěkl: „Kde jeste jego položili?“ Rěkli jemu: „Gospodine! Pojdi i ogledaj.“
35 I zaplakal Jezus.
36 Židi rěkli: „Ogledajte! Kak jego ljubil!“
37 A něktori iz njih govorili: „Či ne mogl on, ktory otvoril oči slěpogo, učiniti, aby sej ne umrl?“
38 Ale Jezus razčulil se v sobě, prišel k grobu; a byla jama, a kamen byl položen na njej.
39 I rěkl Jezus: „Odimajte sej kamen!“ Rěkla jemu Marta, sestra onogo mrtvogo: „Gospodine! Už smrdi; bo uže četyri dni v grobu.“
40 Pověděl jej Jezus: „Či jesm ti ne rěkl, že jestli uvěriš, ugledaš slavu Božju?“
41 Odjeli že kamen, kde byl mrtvy položeny. A Jezus voznesl oči svoje v goru, rěkl: „Otče! Dekuju tobě, že jesi mene izslušal.
42 A ja jesm věděl, že mene vsegda izslušaš; ale jesm to rěkl radi naroda, ktory okolo stoji, aby věrili, že ty jesi mene poslal.“
43 I to rěkl, kazal do sebe glasom velikym: „Lazare! Izojdi vně!“
44 I vyšel toj, ktory byl umrl, imal svezane ruky i nogy tkaninoju, a lice jego bylo tkaninoju ovinuto. Rěkl jim Jezus: „Razvezite jego, i nehaj ide.“
45 Mnogi že iz Židov, ktori prišli do Mariji i viděli to, čego Jezus učinil, uvěrili vo njego.
46 Něktori takože šli farizejev i pověděli jim, čto Jezus učinil.
47 Togda se sobrali starši svečenniki i farizeji v radu i govorili: "Čto učinimy? Ibo sej člověk mnogo div čini.
48 A jestli jego tako ostavimo, vsi věret v njego, i prijdut Rimjani i vozmut nam to město naše i ljud."
49 A jedin iz njih, Kajfas, byvši vysokym svečennikom ovogo lěta, rěkl jim: "Vy ničto ne znate,
50 I ne myslite, že jest nam koristno, da by jedin člověk umrl za ljud, a da by ves narod ne pogynul."
51 A togo ne govoril sam od sebe, ale byvši vysokym svečennikom ovogo lěta, prorokoval, že Jezus iměl umrti za toj narod,
52 a ne toliko za toj narod, ale da by takože syni Božji razsypani v jedno sobral.
53 Od ovogo dnja planovali, da by jego ubili.
54 A Jezus ne hodil javno medžu Židami, ale odtud odšel do kraja, ktory jest blizko pustynje, do města, ktoro zovut Effrem, i tam žil s svojimi učenikami.
55 A byla blizko židovska Paša, a mnogo jih šlo do Jeruzalema iz ovogo kraja prěd Pašeju, da by se očistili.
56 I iskali Jezusa i govorili jedin k drugym, stoječi v svetilišču: "Čto vy myslite, že ne prišel na prazdnik?"
57 A starši svečenniki i farizeji izdali razkazanje: "Jestli by se kto dověděl, kde on jest, da by oglasil, da by jego pojmali."

## Razděl 12

1 I togdy šest dni prěd Pašeju prišel Jezus do Betaniji, kde byl Lazar, ktory umrl i ktorogo On vozkresil iz mrtvyh.
2 Tam mu pripravili večeru, a Marta služila, a Lazar byl jedin iz tyh, ktori s njimi za stolom sěděl.
3 A Marija, vzela funt oleja špikanardovogo velmi dragocěnnogo, pomazala nogy Jezusu i utrla je svojimi vlasami, i napolnil se dom zapahom togo oleja.
4 I rěkl jedin iz jego učiteljev, Judas Iskarjotsky, ktory jego iměl izdati:
5 Čemu jesi togo oleja ne prodala za trista grošev i ne dala ubogym?
6 A to rěkl ne, da mu bylo žalj ubogyh, ale bo byl zlodějem i iměl měšek, i čto v njego vkladali, to on nosil.
7 I rěkl Jezus: Ostavi ju; na den pogreba mojego ona to shovala.
8 Bo ubogyh vsegda so soboju imate, ale mene ne vsegda iměti budete.
9 Dověděl se veliky narod židovsky, že on tam jest, i prišli ne toliko radi Jezusa, ale takože da by Lazara viděli, ktorogo on vozkresil iz mrtvyh.
10 I pomyslili svečenniki, da by i Lazara ubili.
11 Bo mnogo Židov dlja njego odstupili i věrili v Jezusa.
12 Na drugy den veliky narod, ktory prišel na prazdnik, slyšavši, že Jezus ide do Jeruzalema,
13 vzeli větky palmy i pošli do njego i govorili glasno: Hosanna! Blagoslovjeny, ktory ide v imeni Gospodnym, car Izraelsky!
14 A našel Jezus osla, usědl na njego, kako jest napisano:
15 Ne boj se, dočero Syjonjska! Vot car tvoj ide, sědeči na oslu.
16 Togda že ne razuměli jego učeniki od prva, no kogda byl Jezus proslavjeny, togda spomněli, že to bylo o njem napisano, i že to jemu učinili.
17 Svědčil že narod, ktory s njim byl, že on Lazara kazal do sebe iz groba i budil jego iz mrtvyh.
18 Zato izšel protiv njemu narod, bo slyšal, že on to čudo učinil.
19 Togda govorili farizeji medžu soboju: Vidite, že ničego ne uspějete; ugledajte, cěly svět za njim ide.
20 A byli něktori Greki iz tyh, ktori prišli do Jeruzalema, aby se moliti v svetku.
21 Ti že prišli do Filipa, ktory byl iz Betsajdy Galilejskoj, i prosili jego: Pane, hčemo Jezusa viděti.
22 Prišel Filip i pověděl to Andreju, a Andrej i Filip to pověděli Jezusu.
23 A Jezus odpověděl jim: Prišla časina, byh byl obožany Syn člověčsky.
24 Istinno, istinno vam povědam: Jestli by zrno pšenice padlo do zemji, ne umrlo, ono samo osta; no jestli by umrlo, veliki plod prinosi.
25 Kto ljubi dušu svoju, izgubi ju, a kto nenavidi dušu svoju na ovom světu, do věčnogo života strěže ju.
26 Jestli někto mně služi, nehaj že za mnoju ide, a kde jesm ja, tam i sluga moja bude; a jestli někto mně služiti bude, proslavi jego Otec moj.
27 Tutčas že duša moja trevožna jest; i čto že rěku? Otče! izbavi mene od toj časiny; Ale zato jesm prišel na tu časinu.
28 Otče! proslavi ime tvoje. Prišel že glas iz neba: Jesm obožal i ješče obožaju.
29 A narod toj, ktory stal i slyšal, govoril: gremělo; a drugi govorili: Angel do njego govoril.
30 Odpověděl Jezus i rěkl: Ne dlja mene toj glas prišel, no dlja vas.
31 Nyně jest sud světa, nyně knezi světa sego izkydani budut.
32 A ja, jestli budu povyšeny od zemji, tegnu vse k sobě.
33 (A to govoril I ukazal, kaku smrt iměl umreti.)
34 Odgovoril jemu narod: My slyšali iz zakona, že Hristos trvaje na věky; a kako že ty govoriš, že budeš povyšeny byti kako Syn člověčsky? Kaky že to jest Syn člověčsky?
35 Togdy jim rěkl Jezus: Jestli do malogo vrěmene jest s vami světlo; hodite že, poka světlo imate, da vas tma ne obsegnula; bo kto v tmě hodi, ne vě, kudy ide.
36 Poka světlo imate, věrite v světlo, da budete synami světla. To pověděl Jezus I pošel shraniti se od njih.
37 A kogdy toliko čuda učinil prěd njimi, ne uvěrili v njego,
38 Da by se izpolnilo slovo Izaijaša proroka, ktory pověděl: Gospodine! I kto uvěril propověd našu? A rame Gospodina komu jest objavjeno?
39 Zato ne mogli uvěriti, že ješče pověděl Izaijaš:
40 Zaslěpil oči jih, i zatvrdil srdce jih, da očami ne viděli i srdcem ne razuměli, i ne obratili se, da by jih uzdravil.
41 To pověděl Izaijaš, kogda viděl slavu jego, i govoril o njem.
42 I jednako iz knezev mnogo jih v njego uvěrilo; ale radi Farizejev ne vyznavali, da by iz svetilišča ne byli izključeni.
43 Bo ljubili slavu ljudsku više, než slavy Božjej.
44 I Jezus govoril: Kto věri v mene, ne v mene věri, ale v ovogo, ktory mene poslal.
45 I kto mene vidi, vidi ovogo, kto mene poslal.
46 Ja světlo, jesm prišel na svět, da by nikto, kto věri v mene, ne ostal v tmah.
47 A jestli by kto slyšal slova moje, a ne uvěril by, ja jego ne sudžu; bo ne jesm prišel, da byh sudil svět, ale da byh izbavil svět.
48 Kto mene grdi, a ne prijma slov mojih, ima, kto by jego sudil; slova, ktore ja govoril, one jego osudet v poslědnjem dnju.
49 Bo ja od sebe samogo ne govoril, ale toj, ktory mene poslal, Otec, on mi razkaz dal, čto byh ja imal govoriti i povědati;
50 I věm, že razkaz jego jest věčny život; A to, čto ja vam govorju, tako govorju, kako mi povědal Otec.

## Razděl 13

1 A prěd svetom dnjem Pašy, věděl Jezus, že prišla jego časina, da by prěšel iz sego světa k Otcu. Ljubivši svojih, ktori byli na světu, ljubil jih do konca.
2 I kogda byla večera, a črt uže vložil ruku v srdce Judasa, syna Simona Iškariotskogo, da by jego izdal;
3 Věděl Jezus, že vse Otec podal do jego ruky, i že od Boga izšel i k Bogu ide,
4 Vstal od večery i složil oděvanje, vzel platno, ovinul se.
5 Potom nalil vody do misky, i načel nogy umyvati učenikam i utirati platnom, ktorym byl ovinuty.
6 Togda prišel do Simona Petra; a on mu rěkl: Gospodi! Či ty mně nogy umyvaješ?
7 Odgovoril Jezus i rěkl mu: Čto ja činju, ty ne znaješ tutčas, ale se potom dověš.
8 Rěkl mu Petr: Ne budeš ty nog mojih umyvati na věky. Odpověděl mu Jezus: Jestli tebe ne umyju, ne budeš iměti děl so mnoju.
9 Togda mu rěkl Simon Petr: Gospodi! Ne jedino nogy moje, ale i ruky, i glavu.
10 Rěkl mu Jezus: Kto jest umyty, ne trěbuje, jedino da by nogy umyl, bo čisty jest ves; i vy jeste čisti, ale ne vsi;
11 Ibo věděl, ktory jego izdati iměl; do togo rěkl: Ne vsi jeste čisti.
12 Kogda že umyl nogy jih i vzel oděvanje svoje, sěděl nazad za stolom, rěkl jim: Znajete li, čto jesm vam učinil?
13 Vy mene nazyvajete učiteljem i Gospodinom, a dobro govorite; bo jim jesm.
14 Jestli jesm umyl nogy vaše, Gospod i učitelj, jeste povinni jedni drugym nogy umyvati.
15 Ibo jesm dal vam priklad, da byste kak ja vam učinil, činili.
16 Istinno, istinno povědam vam: Ne jest sluga boljša od Gospodina svojego, ni poslanec jest boljši od ovogo, kto jego poslal.
17 Jestli to věte, blagoslavjani jeste, jestli to učinite.
18 Ne o vsih vas govorju, ja věm, kogo jesm izbral; ale aby se izpolnilo Pismo: „Kto je so mnoju hlěb, voznese protiv mně grst svoju.“
19 Tutčas vam povědam, prěd tym, než to se stane, byste, kogda se to stane, uvěrili, že ja jesm.
20 Istinno, istinno povědam vam: Kto prijma togo, kogo byh poslal, mene prijma; a kto mene prijma, ovogo prijma, kto mene poslal.
21 To rěkl Jezus, smutil se v duhu, i objavil i rěkl: Istinno, istinno povědam vam, že jedin iz vas izda mene.
22 Togda učeniki gleděli po sobě, sumněvali se, o kom by to govoril.
23 A byl jedin iz učenikov jego, ktory se položil na lono Jezusa i ktorogo ljubil Jezus.
24 Togdy na togo kyvnul Simon Petr, aby se spytati, ktory by to byl, o kom govoril.
25 A on opiral se o Jezusa, rěkl jemu: Gospodine! Kto že to jest?
26 Odgovoril Jezus: „Toj jest, komu ja močeny hlěb, podam.“ A močeny hlěb, dal Judasu, synu Simona, Iskarjotskomu.
27 A momentalno po ovom kusu hlěba vstupil v njego běs. Togda jemu rěkl Jezus: „Čto činiš, čini skoro.“
28 A togo nikto ne razuměl iz vsih, načto jemu to rěkl.
29 Ibo něktori myslili, bo Judas iměl měšek, že jemu rěkl Jezus: „Kupi, čego nam trěba na sveto, ili aby dati ubogym.“
30 Kogda on sjel toj kus hlěba, zaraz izšel; a noč byla.
31 A kogdy on izšel, rěkl Jezus: Nyně jest proslavjeny Syn člověčsky, i Bog jest proslavjeny v njem.
32 A jestli že Bog proslavjeny jest v njem, tože jego Bog proslavi sam v sobě, i skoro proslavi jego.
33 Syni! Ješče malo jesm s vami; budete mene iskati, ale jest tak kak že rěkl Židam: Kudy ja idu, vy prijdti ne možete; tako i vam nyně povědam.
34 Zapověd novu dam vam, da byste jedin drugogo ljubili; kako ja vas ljubil, tak byste jedin drugogo ljubili.
35 Po tom poznajut vsi, že jeste učenikami mojimi, jestli že ljubov iměti budete vzajemno.
36 Rěkl jemu Simon Petr: Gospodine! Kudy že ideš? Odpovědal jemu Jezus: Kudy ja idu, ty nyně za mnoju idti ne možeš, ale potom pojdeš za mnoju.
37 Togdy jemu rěkl Petr: Gospodine! Čemu že nyně za toboju idti ne mogu? Dušu moju za tebe položu.
38 Odpovědal jemu Jezus: Dušu tvoju za mene položiš? Istinno, istinno povědam ti: Ne pěva kokot, poka ty mene ne trikratno odkažeš.

## Razděl 14

1 Nehaj ne straši se srdce vaše; věrite v Boga i v mene věrite.
2 V domu Otca mojego mnogo jest města; a jestli ne, byh vam pověděl.
3 Idu vam gotoviti město; a kogda odidu i prigotovju vam město, prijdu snova i vozmu vas do sebe, byste byli tam kde ja.
4 A dokud ja idu, znate, i stežku znate.
5 Rěkl jemu Tomas: Gospodi! ne věmo, dokud ideš, a kako možemo stežku znati?
6 Rěkl jemu Jezus: Jam jesm ta stežka, i pravda, i život; nikto ne prihodi k Otcu bez mene.
7 Da byste mene znali, i Otca byste tož mojego znali; i už go v tutom momentu znate i jeste viděli go.
8 Rěkl jemu Filip: Gospodi! pokaži nam Otca. To dostatočno nam.
9 Rěkl jemu Jezus: Črěz tak dolgo vrěme jesm iz vami, a ne poznali se mene? Filipe! kto mene vidi, vidi i Otca mojego; kako ty govoriš: Pokaži nam Otca?
10 Ne věriš, že jesm ja v Otcu, a Otec v mene? Slova, ktore ja vam govorju, ne od samogo sebe govorju, a Otec, ktory vo mně žive, čini ti děla.
11 Věrite mi, že jesm ja v Otcu, a Otče vo mně; prinajmenje črěz same děla věrite mi.
12 Zapravdu, zapravdu povědam vam: Kto věri vo mně i děla ktore ja činju, tož je činiti bude, i daže boljše než te činiti bude; bo ja pojdu k Otcu mojemu.
13 A o čtokoli že prositi budete v imenu mojem, to učinju, aby byl obožany Otec v Synu.
14 Jestli o čem budete prositi v imenu mojem, ja učinju.
15 Jestli mene ljubite, zapovědi moje shranite.
16 A ja budu prositi Otca, aby inogo dal vam, ktory by vas utěšil i by s vami prěbyval na věky,
17 Duha istiny, ktorogo svět ne može prijati; bo jego ne vidi,i jego ne zna; ale vy jego znajete, bo u vas prěbyva i vo vas bude.
18 Ne ostavju vas sirotami, prijdu do vas.
19 Ješče malo, a svět mene uže ne uzri; ale vy mene uzrite; bo ja živu, i vy budete žiti.
20 V tom dnju vy poznajete, že ja jesm v Otcu mojem, a vy vo mně, i ja v vas.
21 Kto ima zapovědi moje i zadrži je, toj jest, kto mene ljubi; a kto mene ljubi, moj Otec bude jego ljubiti; i ja jego ljubiti budu, i objavju jemu samogo sebe.
22 Rěkl jemu Judas, ne Iskarjotsky: Gospodine! Čto jest, že sebe nam objaviti imaš, a ne světu?
23 Odgovoril Jezus i rěkl jemu: Jestli někto mene ljubi, slovo moje zadržati bude; i Otec moj bude jego ljubiti, i do njego prijdemo I budemo u njego žiti.
24 Kto mene ne ljubi, slov mojih ne zadržati; a slovo, ktore slyšite, ne jest moje, ale ovogo, ktory mene poslal. Otca.
25 To vam jesm rěkl, u vas prěbyvajuči.
26 Ale utěšitelj, Duh Svety, ktorogo posle Otec v imenu mojim, vas nauči vsego, i pripomni vam vse, čto jesm vam rěkl.
27 Mir ostavju vam, mir moj davaju vam; ne kako davaje svět, ja vam davaju; nehaj že se ne nepokoji srdce vaše, i ne boji se.
28 Jeste slyšali, že jesm vam rěkl: Odhodžu, i snova prijdu do vas. Kogda byste mene ljubili, vsi byste se radovali, že jesm rěkl: Idu do Otca; bo Otec moj je večši než ja.
29 I nyně jesm vam rěkl, prěd tym, než se to stane, da byste, kogda se to stane, uvěrili.
30 Uže dalje s vami mnogo govoriti ne budu; bo ide knez světa sego, a vo mně ničego ne ima;
31 No aby poznal svět, že ljubim Otca, i kako mi kazal Otec, tako činju. Vstanite, idemo od sego města.

## Razděl 15

1 Ja jesm vino istinno, a Moj Otec jest vinogradnikom.
2 Každy rastok, ktory ne prinosi u mene ploda, on odsěka, a každy, ktory prinosi plod, očisti jego, da by boljše ploda prinosil.
3 Vy jeste čistymi dlja slov, ktore jesm vam govoril.
4 Jeste žili u mene, a ja u vas; kak rastok ne može prinositi ploda sam od sebe, jestli ne bude trvati u vinny lozy, tako vy tož ne, jestli u mene žiti ne budete.
5 Ja jesm vinna loza, a vy jeste rastkami; kto žiti bude u mene, a ja u njego, toj prinosi mnogo ploda; bo bez mene ničto učiniti ne možete.
6 Jestli by kto ne žil u mene, on izkydany bude kako rastok, i izsohne; i sberut je i do ognja izkydnut, i spali se.
7 Jestli u mene žiti budete i slova moje u vas žiti budut, čtokoli byste hotěli, prosite, a stane se vam.
8 V tom bude proslavjeny Otec moj, kogda mnogo ploda prinesete, budete mojimi učenikami.
9 Kako mene ljubil Otec, tako i jesm ljubil vas; trvajte u mojej milosti.
10 Jestli prikazy moje shranite, trvati budete u mojej milosti, kako i jesm shranil prikazy Otca mojego i trvam u jego milosti.
11 To vam jesm pověděl, da by veselje moje u vas trvalo, a veselje vaše bylo izpolnjeno.
12 To jest prikaz moj, da byste se vzajemno ljubili, kako i ja vas jesm ljubil.
13 Boljše milosti nad tym nikto ne imaje, jedino jestli by kto dušu svoju položil za prijatelji svoje.
14 Vy jeste prijateljami mojimi, jestli činiti budete, čegokoli ja vam zapovědam.
15 Už vas dalje ne budu nazyvati slugami; bo sluga ne vě, čto čini Pan jego; a vas jesm nazval prijateljami, bo vse, čegokoli jesm slyšal od Otca mojego, jesm objavil vam.
16 Ne vy jeste izbrali mene, ale jesm vas izbral; i jesm ustanovil, da byste  pošli i prinosili plod, a plod vaš by trval, i o čem že byste prosili Otca v imenu mojem, da by vam dal.
17 To vam prikazyvaju, da byste se vzajemno ljubili.
18 Jestli vas svět nenavidi, znajte, že mene prvo neželi vas iměl v nenavisti.
19 Da byste byli iz světa, svět, ktory jest jego, ljubil by vas; a ne jeste iz světa, ale ja vas izbral iz světa, zato vas svět nenavidi.
20 Spomnite na slovo, ktoro ja vam pověděl: Ne jest sluga večši než pan svoj. Jestli mene ogorčali, i vas ogorčati budut; jestli slova moje shranili, i vaše shraniti budut.
21 Ale vam to vse činiti budut radi imene mojego, bo ne znajut ovogo, ktory mene poslal.
22 Da byh ne prišel, a ne govoril jim, ne iměli by grěha; a nyně ne imajut izgovorka od grěha svojego.
23 Kto mene nenavidi, Otca mojego nenavidi.
24 Da byh tyh dělov ne činil medžu njimi, ktoryh ni jedin ini ne činil, grěha by ne iměli; no nyně viděli i nenaviděli mene i Otca mojego.
25 Ale da by se izpolnilo slovo, ktoro jest v zakonu jih napisano: Že mene nadarmo iměli v nenavisti.
26 A kogda prijde utěšitelj, ktorogo ja vam poslju od Otca, Duh pravdy, ktory od Otca prihodi, on o mně svědčiti bude.
27 Ale i vy svědčiti budete; bo so mnoju od početka jeste.

## Razděl 16

1 O tom jesm vam rěkl, byste se ne goršili.
2 Izključet vas iz svetilišču; ale prijde čas, že každy, ktory vas ubije, bude mysliti, že Bogu službu čini.
3 A to vam učinju, bo ne poznali Otca I ne mene.
4 Ale vam jesm rěkl, byste, kogda prijde ta časina, spomněli to, čto jesm vam pověděl; a togo vam od početka ne jesm povědal, bo jesm byl s vami.
5 A tutčas idu k tomu, ktory mene poslal, a žaden iz vas ne pyta mene: Kudy ideš?
6 Ale jesm vam to rěkl, žalost napolnila srdce vaše.
7 A ja vam pravdu govorju: vam to koristno jest, byh ja odšel; bo jestli ja ne odidu, utěšitelj on ne prijde k vam, a jestli odidu, poslu jego k vam.
8 A on, kogdy prijde, bude karati svět iz grěha i iz spravědlivosti, i s suda;
9 Iz grěha govorju: že ne uvěrili v mene;
10 Iz spravědlivosti: že k Otcu mojemu idu, a uže mene ne uzrite;
11 Iz suda: knez togo světa uže jest osudžany.
12 Imam vam ješče mnogo govoriti, ale tutčas snesti ne možete.
13 A kogda prijde on Duh pravdy, nauči vas v každoj pravdě; bo ne sam od sebe govoriti bude, ale čtokoli uslyši, govoriti bude, i čto prijdti ima, oglasi vam.
14 On mene obožaje; bo iz mojego vozme, a pověda vam.
15 Vse, čto ima Otec, moje jest; dlja togo jesm rěkl: Že iz mojego vozme, a vam pověda.
16 Ješče malo, i ne uvidite mene, i snova ješče malo časa, i uvidite mene; bo ja idu do Otca.
17 Govorili togdy něktori iz učenikov jego medžu soboju: Čto to jest, čto nam govori: Ješče malo, i ne uvidite mene, i snova ješče malo časa, i uvidite mene, a že ja idu do Otca?
18 Togda govorili: Čto to jest, čto govori: Malo? Ne znamo, čto govori.
19 Togdy Jezus poznal, že jego pytati htěli, i rěkl jim: O tom se pytate medžu soboju, i jesm rěkl: Ješče malo, i ne uvidite mene, i snova ješče malo časa, i uvidite mene.
20 Istinno, istinno povědam vam: Či vy budete plakati i narěkati, a svět se bude veseliti; vy smutni budete, ale smutok vaš obrati se vam v veselje.
21 Nevěsta, kogda rodi, smutok ima, bo prišla jej časina; a kogda porodi děte, uže ne pameta bolja črěz radost, že se člověk na svět narodil.
22 I vy nyně smutok imate; ale snova uzrim vas, a bude se radovati srdce vaše, a radosti vašej nikto ne odojme od vas.
23 A dnja ovogo ne budete mene o ničto pytati. Istinno, istinno povědam vam: O čegokoli byste prosili Otca v imeni mojem, da vam.
24 Poka jeste o ničto ne prosili v imeni mojem; prosite že, a vozmete, aby radost vaša byla doskonala.
25 To vam črěz prěpovest jesm govoril; ale ide časina, kogda uže dalje ne črěz prěpovesti govoriti vam budu, ale jasno o Otcu mojem objavim vam.
26 V on den v imeni mojem prositi budete; a ne govorju vam: Ja budu Otca prositi za vami;
27 Ibo sam Otec ljubi vas, že vy mene jeste ljubili i uvěrili, že jesm ja od Boga prišel.
28 Izšel jesm od Otca, a prišel jesm na svět; i snova ostavjam svět, a idu k Otca.
29 Rěkli jemu učeniki jego: Vot nyně jasno govoriš, a nijednoj prěpovesti ne povědaš;
30 Nyně znamo, že vse věš, a ne trěbuješ, aby tebe někto pytal; črěz to věrimo, že jesi od Boga izšel.
31 Odgovoril jim Jezus: Nyně věrite?
32 Vot prijde časina, da každy bude razsějany, a mene samogo ostaviti; a ne jesm sam, bo Otec jest so mnoju.
33 To jesm vam pověděl, da byste vo mně mir iměli. Na světu muku iměti budete; ale dověrite, jesm pobědil svět.

## Razděl 17

1 To govoril Jezus voznesl svoje oči k nebu i rěkl: Otče! Prišla je čas, proslavi Syna tvojego, da by i Syn tvoj proslavil tebe.
2 Kako jesi mu dal moč nad každym tělom, da by vsim, ktoryh jesi mu dal, dal věčny život.
3 A to jest věčny život, da by poznali tebe jedinogo pravdivogo Boga, i ktorogo jesi poslal, Jezusa Hristosa.
4 Jesm tebe proslavil na zemji i dokončil dělo, ktoro jesi mi dal. 
5 A nyně proslavi mene, Otče u sebe samogo slavoju, ktoru ja iměl u tebe, prědže než svět byl.
6 Jesm odkryl ime tvoje ljudam, ktoryh jesi mi dal iz světa; tvoji byli i jesi dal mi je, i oni shranili slova tvoja.
7 A nyně poznali, že vse, čto jesi mi dal, od tebe jest.
8 Bo slova, ktore jesi mi dal, jesm dal jim; a oni je prijali, i poznali istinno, že jesm od tebe izšel, a uvěrili, že jesi ty mene poslal.
9 Ja za njimi prošu, a ne za světom prošu, ale za tyh, ktoryh jesi mi dal; bo tvoji sut.
10 I vse moje jest tvoje, a tvoje moje, i jesm se proslavil v njih.
11 A ne jesm više na světu, ale oni sut na světu, a ja idu do tebe. Otče svety, shrani jih v imeni tvojem, ktore jesi mi dal, da by byli jedno, kako i my.
12 Kogdy ja byl s njimi na světu, ja jih shranil v imeni tvojem, ktoro jesi mi dal; jesm ohranil jih i ni jedin iz njih ne izgynul, toliko syn izguby, da by se Pismo napolnilo.
13 Ale tutčas idu do tebe i govorju to na světu, da by iměli radost moju doskonalu v sobě.
14 Jesm jim dal slovo tvoje, a svět je iměl v nenavisti; bo ne sut iz světa, kako i ja ne jesm iz světa.
15 Ne prošu, da bys je vzel iz světa, ale da bys je shranil od zlogo.
16 Ne sut od světa, kako i ja ne jesm od světa.
17 Posveti jih v tvojej pravdě; tvoje slovo jest pravda.
18 Kako že ty jesi mene poslal na svět, tako i ja posylaju jih na svět.
19 A ja posvečaju samogo sebe za njih, aby i oni posvečeni byli v pravdě.
20 Ne toliko za tyh prošu, ale i za ovyh, ktori črěz slovo jih uvěret v mene;
21 Aby vsi byli jedno, kako ty, Otče, vo mně, a ja v tobě; aby i oni v nas jedno byli, aby svět uvěril, že ty jesi mene poslal.
22 A ja jesm dal jim slavu, ktoru jesi mi dal, aby byli jedno, kako my jedno jesmo;
23 Ja v njih, a ty vo mně, aby byli doskonalymi v jedno, a by svět poznal, že jesi mene poslal i jih poljubil, kak jesi mene poljubil.
24 Otče! Ktory jesi dal mi, hču, byh kde jesm ja, oni byli so mnoju, aby ogledali slavu moju, ktoru jesi mi dal; bo jesi mene poljubil prěd založenjem světa.
25 Otče spravědlivy! I svět tebe ne poznal; ale jesm tebe poznal i ti poznali, da jesi poslal mene.
26 I jesm oglasil jim tvoje ime i oglašu, aby ljubov, ktoroju jesi mene poljubil, v njih byla, a ja v njih.

## Razděl 18

1 I rěkši to, Jezus vyšel s svojimi učenikami za potok Cedron, kde byl sad, do ktorogo on vstupil i jego učeniki.
2 A znal i Judas, ktory jego izdal, to město; bo često tam shodil Jezus s svojimi učenikami.
3 I tak Judas vzel vojakov i slugov od glavnyh svečennikov i farizejev, prišel tam s světilkami i s fakljami, i s oružjem.
4 Togda Jezus, věděvši vse, čto nyně imělo prijdti, izšel i rěkl jim: Kogo iščete?
5 Odgovorili jemu: Jezusa Nazaretskogo. Rěkl jim Jezus: To ja jesm. A stal s njimi i Judas, ktory jego izdal.
6 A kako jim rěkl: To ja jesm, odstupili nazad i padli na zemju.
7 Togda jih snova spytal: Kogo iščete? A oni rěkli: Jezusa Nazaretskogo.
8 Odgovoril Jezus: Jesm rěkl vam, že ja jesm; jestli tako mně iščete, dopustite tym odidti;
9 By se izpolnili slova, ktore rěkl: Ne jesm gubil nikogo iz tyh, ktoryh jesi mi dal.
10 Togda Simon Petr imajuči meč, iztegnul jego, i udaril slugu najvysšego svečennika, i urězal jemu uho pravo; a tomu slugě ime bylo Meleh.
11 I rěkl Jezus Petru: Vloži meč tvoj v nožnicu; či ne imam piti čašky toj, ktoroj mi dal Otec?
12 Vojini togda i jih načelnik, i židovski slugy shvatili Jezusa i svezali go.
13 I vedli jego naprěd do Annasa; bo byl test Kajfasa, ktory byl najvysšim svečennikom ovogo lěta.
14 A Kajfas byl tym, ktory Židam radil, že koristno jest, da by jediny člověk umrl za narod.
15 I šel za Jezusom Simon Petr i drugi učenik. A toj učenik byl znajemy najvysšemu svečenniku, i všel s Jezusom do dvora najvysšego svečennika.
16 Ale Petr stal pri dverah na dvore. Vyšel togdy drugy učenik, ktory byl znajemy najvysšemu kaplanu, i govoril s dverničkoju, i vvedl tam Petra.
17 Togdy rěkla Petru dvernička: Či i ty ne jesi od učenikov ovogo člověka? On odgovoril: Ne jesm.
18 Stali togdy slugy i čeljad u vuglja tvorivši ognj, bo bylo zimo; i grěli se; byl tož s njimi Petr, stoječi i grějuči se.
19 A tak najvysši kaplan pytal Jezusa o jego učenikov i o nauku jego.
20 Odgovoril mu Jezus: Ja javno govoril světu; Ja vsegda učil v svetilišču, kde  vsi Židi shodet, a tajemno ničto jesm ne govoril.
21 Čego mene pytaješ? Pytaj tyh, ktori slyšali, čto jesm jim govoril; ti to vědut, čto ja govoril.
22 A kogda on to govoril, jedin iz slugov, ktory tam stal, udaril po licu Jezusa, govoreči: I tako odpovědaš najvysšemu kaplanu?
23 Odgovoril mu Jezus: Jestli jesm zlo rěkl, daj svědočstvo o zlom, a jestli jesm rěkl dobro, po čto mene biješ?
24 I odslal go Annan svezany do Kajfasa, najvysšego kaplana.
25 A Simon Petr stal i grěl se. I rěkli do njego: Či že i ty ne jesi od učenikov jego? A on zaprěčil, govoreči: Ne jesm.
26 Rěkl mu něktory iz slugov kaplana najvysšego srodnik togo, komu Petr odrězal uho: Či že jesm ja tebe ne viděl v sadu s njimi?
27 Zaprěčil že Petr, a neočekyvano kokot pěval.
28 Vedli togda Jezusa od Kajfasa do ratuš, a bylo rano. I ne vošli sami do ratuša, aby se ne sramili i mogli sjesti barana Pašy.
29 Togdy vyšel do njih Pilat, i rěkl: Kaku težbu prinosite protiv člověku tomu?
30 Odgovorili mu: Kogda by toj ne byl zločincem, byhmo tebe jego ne podali.
31 I rěkl Pilat: Vy vozmite jego i po vašemu zakonu sudite jego. Rěkli jemu Židi: Nam ne godi se ubivati nikogo;
32 I izpolnjajut se slov Jezusa, ktore rěkl objavjajuči, kakoju smrtju iměl umrti.
33 Togda snova všel Pilat do ratuša i zval Jezusa i rěkl jemu: Či ty jesi židovsky kralj?
34 Odgovoril jemu Jezus: Či sam ty to od sebe govoriš, ili ini pověděli ti o mně?
35 Odgovoril Pilat: Či ja jesm Židom? Narod tvoj i starši svečenniki podali mi te; čto jesi učinil?
36 Odgovoril Jezus: Carstvo moje ne jest od togo světa; jestli by carstvo moje od togo světa bylo, to moji slugy by mně obranjali, da byh ja ne byl izdany Židam; no tutčas carstvo moje ne jest odsud.
37 Togda rěkl jemu Pilat: To že ty jesi kraljem? Odgovoril jemu Jezus: Ty povědaš, že jesm kraljem. Ja se na to rodil i na to prišel na svět, da by ja svědočstvo dal pravdě; každy, ktory jest od pravdy, sluša glasa mojego.
38 Rěkl jemu Pilat: Čto jest pravdoju? I rěkl to, vyšel snova do Židov i rěkl jim: Ja v njim ne najdu nijednoj viny.
39 No u vas jest obyčaj, da byh ja vam jedinogo pustil na Pašu; želate li togdy, da byh ja vam pustil ovogo židovskogo kralja?
40 Togda snova kazali glasno: Ne ovogo, toliko Barabasa! A toj Barabasa byl razbojnikom.

## Razděl 19

1 Togdy Pilat vzel Jezusa i bičeval jego.
2 A vojaki spletli věnec iz trna i položili na jego glavu i plaščem purpurnym oděli jego,
3 A govorili: Budi pozdravjeny, kralju židovsky! i bili jemu v lice.
4 I snova izšel Pilat na dvor i rěkl jim: Vot jego vam izvedu na dvor, da byste věděli, že v njem nikakoj viny ne najdu.
5 Togdy Jezus izšel na dvor, nesl toj věnec iz trna i plašč purpurny; i rěkl jim Pilat: Vot člověk!
6 A kogda jego uzrěli vrhovni svečenniki i slugy jih, kazali glasno: Ukrižuj, ukrižuj go! Rěkl jim Pilat: Vozmite go, a ukrižujte, bo ja v njem nikakoj viny ne najdu.
7 Odgovorili jemu Židi: My zakon imamo i po našemu zakonu on ima umrti; bo se činil Synom Božjim.
8 A kogda Pilat uslyšal te slova, silněje se prěstrašil.
9 I všel snova do ratuša i rěkl Jezusu: Odkud že ty jesi? Ale Jezus mu ne dal odvěta.
10 Togdy mu rěkl Pilat: Ne govoriš s mnoju? Ne věš, že imam moč ukrižovati te i imam moč pustiti te?
11 Odgovoril Jezus: Ne bys iměl nikakoj moči nad mnoju, jestli by tobě ona ne byla dana iz gory; itak, kto mene tobě izdal, boljši grěh ima.
12 Odtud Pilat staral se o to, kako by jego izpustil; ale Židi kazali glasno: Jestli jego izpustiš, ne jesi prijateljem cěsara; bo každy, kto se kraljem čini, protivi se cěsaru.
13 A Pilat uslyšavši te slova, izvedl Jezusa na dvor i sědl na stolici, na městu, ktore zove se Litostrotos, a po židovsku Gabbata.
14 A bylo to v dnju prigotovjenja prěd Pašeju, okolo šestoj časiny, i rěkl Pilat Židam: Vot vaš kralj!
15 A oni kazali: Von s njim, von s njim! Ukrižuj jego! Rěkl jim Pilat: Vašego kralja ukrižu? Odgovorili vrhovni svečenniki: Ne imamo kralja, toliko cěsara.
16 Togda on jim jego izdal, da by byl ukrižovany. I vzeli Jezusa i izvedli.
17 I on, nesl svoj križ, izšel na to město, ktoro nazyvalo se Město čerepa, a po židovsku nazyvaje se Golgota;
18 Tam, kde jego ukrižovali, byli s njim dva ini s oboh stran, a posrěd njih Jezus.
19 Napisal že Pilat napis, i postavil nad križem; a bylo napisano: Jezus Nazaretsky, car židovsky.
20 I toj napis čitalo mnogo Židov; bo blizko grada bylo to město, kde byl ukrižovany Jezus; a bylo napisano po židovski, po grečsku i po latinsku.
21 Togda rěkli Pilatu vrhovni svečenniki židovski: Ne piši: „Car židovsky“, ale že on povědal: „Jesm car židovsky“.
22 Odpověděl Pilat: Čto jesm napisal, to jesm napisal.
23 A kogda vojaki Jezusa ukrižovali, vzeli jego oděž i učinili iz njej četyri česti, každomu vojaku jednu čest, i vzeli suknju; a ta suknja ne byla šita, ale iz jednoj tkaniny.
24 Togda rěkli jedni k drugym: Ne krojimo jej, ale o nju kydnemo losi, čija ona povinna byti; tako se Pismo izpolnilo, ktore govori: Podělili medžu soboju moju oděž, a o suknju kydnuli los. To že učinili vojaki.
25 A stojali pri križu Jezusa jego mati i sestra jego materi, Marija Kleofasova, i Marija Magdalena.
26 Togda Jezus, videči svoju mati i učenika tu stoječego, ktorogo ljubil, rěkl svojej materi: Ženo, vot syn tvoj!
27 Potom rěkl učeniku: Vot mati tvoja! A od togo času vzel ju učenik do sebe.
28 Potom věděl Jezus, že uže vse se izpolnilo, aby se izpolnilo Pismo, rěkl: Žedaju.
29 A jemu postavjena byla posuda s octom; togda oni, napolnili gubku octom i dali ju na rozgu i podali ju jego ustam.
30 A kogda Jezus vkusil ocet, rěkl: Izpolnilo se; i naklonivši svoju glavu, oddal duha.
31 Togdy Židi, da by těla na križu na subotu ne ostali, prosili Pilata, da jim kolěna lamali, i sjeli je, bo byl den prigotovjenja.
32 Prišli togdy vojaki, a prvomu pravdě zlomili kolěna i drugomu, ktory s njim byl ukrižovany.
33 Ale do Jezusa priševši uzrěli, že už umrl, i ne lamali jemu kolěn.
34 No jedin iz vojakov kopjem otvoril bok jego, a už izšla krov i voda.
35 A toj, ktory to viděl, svědčil o tom i pravdivo jest svědočstvo jego; a on vě, že pravdu pověda, da byste věrili.
36 Ibo se to stalo, da by se izpolnilo Pismo: Kost jego ne bude slomjena.
37 I tož drugo Pismo govori: Uzret, kogo bodnuli.
38 A potom prosil Pilata Jozef iz Arimateji, (ktory byl učenikom Jezusa, ale tajnym iz bojaznji Židov), čto by sjel tělo Jezusa. I pozvolil Pilat. Pošel togdy i sjel tělo Jezusa.
39 Prišel tož i Nikodem, (ktory prědtym prišel v noči do Jezusa), nesl směs mirry i aloe, okolo sto funtov.
40 Vzeli togdy tělo Jezusa i svezali jego v platno s ovymi věčami vonjajučimi, kako jest obyčaj Židam umrělyh hovati.
41 A byl na onom městu, kde byl ukrižovany, sad, a v sadu grob novy, v ktorom ješče nikto ne byl položeny.
42 Togda tam dlja dnja prigotovjenja židovskogo, bo grob byl blizko, položili Jezusa.

## Razděl 20

1 A prvogo dnja po subotě Marija Magdalena prišla rano do groba, kogda ješče bylo temno, i uzrěla kamen vzety od groba.
2 Běgala u prišla do Simona Petra i do ovogo drugogo učenika, kogo ljubil Jezus, i rěkla jim: Vzeli Gospoda iz groba, a ne znamo, kde jego položili.
3 Togda izšel Petr i drugi učenik i šli do groba.
4 I běgli oba razom; ale drugi učenik byl skorějši od Petra i prvy prišel do groba.
5 A klonil se, uzrěl ležeče platno; ale tudy ne všel.
6 Prišel takože Simon Petr, iduči za njim, i všel do groba, i uzrěl platno ležeče,
7 I naglavnu nametku, ktora byla na glavě jego, ne s platnami položena, ale osobna na jednom městu byla.
8 Potom všel i drugi učenik, ktory prvy prišel do groba, i uzrěl i uvěril.
9 Ibo ješče ne razuměli Pisma, že iměl vozkresnuti.
10 I odšli učeniki do domu.
11 Ale Marija stala pri grobu na dvoru plačuča; a kogda plakala, sklonila se v grob.
12 I uzrěla dvoh Angelov v běli sědeči, jednogo u glavy, a drugogo u nog, tam kde bylo položeno tělo Jezusa.
13 Jej rěkli: Ženo! čemu plačeš? Rěkla jim: Bo vzeli Gospoda mojego, a ne znam, kde jego položili.
14 A to rěkši, obratila se nazad i uzrěla Jezusa stoječego; a ne znala, že to Jezus byl.
15 Rěkl jej Jezus: Ženo! čemu plačeš? Kogo iščeš? A ona myslila, že byl to sadovnik. Rěkla jemu: Pane! jestli jesi jego vzel, skaži mi, kde jesi go položil, a ja jego vozmu.
16 Rěkl jej Jezus: Marijo! Ona obratila se, rěkla jemu: Rabbuni! čto znači: Učitelju!
17 Rěkl jej Jezus: Ne dotyči mene, bo ješče ne vstupil do Svojego Otca; ale idi do mojih bratov i skaži jim: Ja vstupaju do Svojego Otca i do vašego Otca, do  Svojego Boga i do vašego Boga.
18 Togda prišla Marija Magdalena, oglasila učenikam, že viděla Gospoda, i to, čto on jej pověděl.
19 A kogda byl večer ovogo prvogo dnja po subotě, a dveri byli zamknute, bo učeniki bojali se židov, prišel Jezus i stanul posrěd njih i rěkl jim: Mir vam!
20 I pověděvši to, pokazal jim Svoje ruky i Svoj bok. I radovali se učeniki, viděvši Gospoda.
21 Rěkl jim snova Jezus: Mir vam! Kako Me Otec poslal, takože ja vas posylaju.
22 I pověděvši to, dal dyh na njih i rěkl jim: Prijmite Duha Svetogo.
23 Ktoryh grěhy odpustite, sut jim odpuščene, a ktoryh zatrimate, sut zatrimane.
24 A Tomas, jedin iz dvanadset, kogo zovut Didymus, ne byl s njimi, kogda prišel Jezus.
25 I rěkli jemu drugi učeniki: Viděli jesmo Gospoda. Ale on jim rěkl: Jestli ne uzrju v Jego rukah znakov gvozdev, i ne vložu prsta Svojego v znaky gvozdev, i ne vložu ruky Svoje v Jego bok, ne uvěrju.
26 A po osm dnjah byli snova Jego učeniki v domu, i Tomas s njimi. I prišel Jezus, kogda dveri byli zamknute, i stanul posrěd njih, i rěkl: Mir vam!
27 Potom rěkl Tomasu: Daj prst svoj i ogledaj Moji ruky, i daj ruku svoju i vloži ju v Moj bok, i ne budi nevěrnym, ale věrnym.
28 Togda odgovoril Tomas i rěkl jemu: Gospodi Moj i Bože Moj!
29 Rěkl jemu Jezus: Jesi Mene viděl, Tomase, jesi uvěril; blagoslovjeny ti, ktori ne viděli i uvěrili.
30 Mnogo i inyh div tvoril Jezus prěd očami Svojih učenikov, ktore ne sut napisane v tyh knigah.
31 Ale to jest pisano, aby vy věrili, že Jezus jest Hristos, Syn Božji, i byste věreči život iměli v imenu jego.

## Razděl 21

1 Potom se ukazal Jezus svojim učenikom pri morju Tiberijadskom, i ukazal se tako.
2 Byli razom Simon Petr i Tomas, kogo zovut Didymus, i Natanael, ktory byl iz Kany Galilejskoj, i syni Zebedeja, i drugi dva iz jego učenikov.
3 Rěkl jim Simon Petr: Idu loviti ryby. Govorju mu: Idemo i my s toboju. I izšli, i skoro vstupili v čolna, a v ovoj noči ničto ne lovili.
4 A kogdy uže bylo rano, stanul Jezus na brěgu; nikto ne věděl iz učenikov, že to jest Jezus.
5 Rěkl jim togdy Jezus: Děti! Či imate ryby? Odgovorili mu: Ne imamo.
6 A on jim rěkl: Zapustite sět po pravoj straně lodi, i najdete. I zapustili, a juže dalje ne mogli jej tegnuti prěd množinstvom ryb.
7 I rěkl učenik, kogo ljubil Jezus, Petru: To jest Gospod. Simon Petr, uslyšavši, že to jest Gospod, oděl se košuljeju, (bo byl nagy) i kydnul se v more.
8 A drugi učeniki priplyvli v čolnu; (bo nedaleko bylo od brěga, ale kako na dvěstě laktev) tegnuči sět s rybami.
9 A kogdy vstupili na brěg, uzrěli vugolj položeny, i rybu na njih ležečų i hlěb.
10 Rěkl jim Jezus: Prinesite iz tyh ryb, ktore jeste v tutom momentu lovili.
11 Vstupil Simon Petr i iztegnul sět na zemju, polnu velikyh ryb, ktoryh bylo sto petdeset tri; a hot jih tak mnogo bylo, ne uniščila se sět.
12 Rěkl jim Jezus: Pojdite, obědajte. I nijedin iz učenikov ne směl jego pytati: Ty kto jesi? Znajuči, že to jest Gospodin.
13 Togdy prišel Jezus i vzel hlěb, i dal jim, takože i rybu.
14 A uže tretji raz ukazal se Jezus svojim učenikam po vozkrešenju.
15 A kogdy oběd jedali, rěkl Jezus Simonu Petru: Simone synu Joana, či ljubiš me boljše než oni? Rěkl mu: Jest tako, Gospodine! Ty znaješ, že te ljubju. Rěkl mu: Pasi baranky moje.
16 Rěkl jemu povtorno: Simone, synu Joana! Či ljubiš mene? Rěkl jemu: Da, Gospodine! Ty znaješ, že ja tebe ljubju. Rěkl jemu: Pasi ovce moje.
17 Rěkl jemu po tretji raz: Simone, synu Joana! Či ljubiš mene? I smutil se Petr, že jemu po tretji raz rěkl: Či ljubiš mene? I odgovoril jemu: Gospodine! Ty vse znaješ, ty znaješ, že ja tebe ljubju. Rěkl jemu Jezus: Pasi ovce moje.
18 Istinno, istinno povědam tobě: Kogdy jesi byl mlady, sam jesi oděval se i hodil, kudy jesi htěl; no kogdy budeš stary, iztegneš ruky tvoje, a iny tebe oděvati bude i provodi, kudy bys ne htěl.
19 A to pověděl, čto by znal, kakoju smrtju iměl by proslaviti Boga. A to povědavši, rěkl jemu: Idi za mnoju.
20 A Petr obratil se, uzrěl ovogo učenika, za soboju idučego i kogo ljubil Jezus, ktory se položil pri večerji na grudi jego, i rěkl: Gospodine! Kto jest on, kto te izda?
21 Togdy jego uzrěvši Petr rěkl Jezusu: Gospodine! A on čto?
22 Rěkl jemu Jezus: Jestli ja hču, aby on ostal, až prijdu nazad, čto tobě do togo? Ty idi za mnoju.
23 I izšla ta pověst medžu bratov, že učenik umrti ne iměl. No ne rěkl Jezus, že ne iměl umrti; ale: Jestli ja hču, aby on ostal, až prijdu nazad, čto tobě do togo?
24 On jest učenikom, ktory svědči o tom, i to napisal; a věmo, že pravdivo jest svědočstvo jego.
25 Jest tož ješče i inyh mnogo věčij, ktore činil Jezus; ktore kak by byli vse napisane, myslju, i sam svět ne mogl by pojmati knig, ktore by se imělo napisati.

# Dějanja Apostolov

## Razděl 1

1 V prvoj knigě jesm pisal, o Teofilě, o vsem, čto načel Jezus tvoriti i učiti,
2 do dnja ovogo, kogda dal zapověd apostolam, ktoryh izbral črěz Svetogo Duha, I byl vzety v goru.
3 Jim po stradanju svojem živym ukazal se s različnymi dovodami. Črěz četyrideset dni ukazal se jim i povědal o kraljevstvu Božjem.
4 I s njimi jedavši, prědskazal jim, daby ne odšli iz Jeruzalema, ale daby čekali oběčanje otcevskogo, o ktoroj jeste slyšali od mene.
5 Joan krestil vodoju, ale vy budete kreščeni Svetym Duhom po nemnogo dnjah.
6 A tako oni sjedinivši se, pytali jego: Gospodine, či v tom času vratiš kraljevstvo Izraelsko?
7 On že rěkl jim: Ne jest vaša věč, znati vrěme i časiny, ktore Otec v svojej moči izbral.
8 Ale prijmete moč Svetogo Duha, ktory prijde na vas; i budete mi svědkami v Jeruzalemu, i v cěloj Judeji, i v Samariji, do poslědnjej granice zemji.
9 I rěkl to, kogda oni gleděli, stal vozneseny v goru, i oblak vzel Go od očij jih.
10 I kogda za njim v nebu idučim spěšno zrěli, vot, dva muži stali pri njimi v bělyh oděžah,
11 i rěkli: Muži galilejski, začto stojite, zreči v nebo? Toj Jezus, ktory vzety jest od vas v nebo, tako prijde, kako Go jeste viděli idučego v nebo.
12 Togda se vratili do Jeruzalema od gory, ktoru zovut Olivnoju i jest blizko Jeruzalema, imajuči put jedinoj suboty.
13 I kogda izšli, vstupili do večernoj komnaty, kde žili Petr i Jakob i Joan i Andrej i Filip i Tomas, Bartolomej i Matej, Jakob Alfeus, i Simon Zelot i Judas Jakob.
14 Vsi ti jedinodušno byvali v molitvě i prosbah, s ženami i s Marijeju, materju Jezusa, i s bratami jego.
15 I v ovyh dnjah, vstal Petr v posrěd učenikov i rěkl: (A bylo mnogo ljudij. Okolo stu dvadeset ljudij).
16 Brati. Trěba izpolniti ovo pismo, ktoro prědskazal Duh Svety črěz usta Davida o Judasu, ktory byl vodžem tyh, ktori pojeli Jezusa;
17 on byl jedin iz nas I tož dostal tu službu.
18 On že dostal polje iz zaplaty za nečestnogo děla, pověsil se, prsknul na pol i vyšli vse vnutrnosti jego.
19 I bylo to javno vsim žiteljam v Jeruzalemu, tako že nazvali ovo polje na svojem jezyku Hakeldama, to jest polje krvi.
20 Ibo jest napisano v knigah Psalm: Nehaj bude kvartira jego pusta, i daby ne bylo nikogo, kto by v njem žil, i biskupstvo jego daby vzel iny.
21 Jedin iz tyh mužev, ktori s nami byvali po cěle vrěme, kogda Gospodin Jezus prěbyval medžu nami,
22 ktory od kreščenja Joana až do togo dnja, v ktorym Go vzeli do neba od nas, byl s nami svědkom vozkrešenja jego.
23 I postavili dva: Jozefa, ktorogo zvali Barabasom, ktorogo tož nazyvali spravědlivogo, i Mateja.
24 I molili se i govorili: Ty, Gospodine, ktory znaš srdca vsih, okaži iz tyh dvoh jedinogo, ktorogo jesi izbral,
25 aby prijel město služby i apostolstva, iz ktorogo izpadl Judas, aby pošel na město svoje.
26 I metali prěznačenje za njih. I padlo prěznačenje na Mateja, i stal se jednym iz jedinnadset apostolov.

## Razděl 2

1 I kogda prišel den petdesety, byli vsi na jednom městu.
2 Togdy vniknul skoro iz neba šum, kakoby pripadal větr nasilny, i napolnil cěly dom, kde sěděli.
3 I ukazali se jim razděljene jezyky oblika ognja, ktory usědl na každom iz njih.
4 I napolnjeni sut vsi Duhom Svetym, i načeli govoriti inymi jezykami, kako jim Duh daval izgovarjati.
5 A byli v Jeruzalemu Židi, muži bogati, iz každogo naroda tyh, ktori sut pod nebom.
6 A kogda stal se toj glas, nabralo se mnogo ljudij i bojali se, da každy iz njih slyšal jih govoreči vlastnym svojim jezykom.
7 I začudili se vsi, i divili se, govoreči jedni k drugym: Či vsi ti, ktori govoret, ne sut Galilejci?
8 A kako každy iz nas svoj vlastny jezyk od njih slyši, v ktorom že jesmo se urodili?
9 Parti i Medi, i Elamiti, i ti, ktori živut v Mesopotamiji, v Judejskoj zemji, i v Kapadokiji, v Pontu, i v Aziji;
10 V Frigiji, i v Pamfiliji, v Egiptu, i v stranah Libiji, ktora jest pri Kireně, i ljudi rimski; 
11 Židi, i novo obračeni; Kretenčici, i Arabi; slyšimo jih, govoreči jezykami našimi velike děla Božje.
12 I začudili se vsi, i divili se, govoreči jedin k drugomu: Čto že to imaje byti?
13 No drugi zasmějajuči se, govorili: Ti sladkym vinom se popili.
14 A stal Petr iz jedinnadset, voznesl glas svoj i kazal jim: Muži Judejski i vsi, ktori živete v Jeruzalemu! Nehaj vam to javno bude, a prijmete v ušah slova moje.
15 Oni ne sut, kako vy mněvate, pijani, ibo toliko jest tretja časina.
16 Ale to jest ovo, čto bylo kazano črěz proroka Joela:
17 I bude v poslědnje dni, (govori Bog): Izliju Duha mojego na vsako tělo, i prorokovati budut syni vaši i dočery vaše, i mladenci vaši viděnja viděti budut, i staršim vašim sny budut.
18 V ove dni na slugy moje i na služebniče moje izliju Duha mojego, i budut prorokovati;
19 I pokažu čudesa na nebesah i znamenja na zemji. Krov, i ogonj, i několiko dyma.
20 Solnce se obrati v temnotě, a měsec v krov, prědže než prijde den Gospodina veliki i znamenity.
21 I stane se, da každy, ktore krikne ime Gospodina, bude spaseny.
22 Muži Izraelski! Slušajte slova te Jezusa, ovogo iz Nazareta, muža od Boga proslavjenogo u vas silami i čudesami, i znamenjami, ktore tvoril Bog črěz Njego posrěd vas, kako vy sami znate;
23 Togo po razloženym ukazom, ktoromu prězrěnje Božje bylo dano, črěz ruky bezbožnikov ukriževavši, jeste ubili.
24 Togo Bog vozbudil, izpustil iz bolja smrti: kako bylo to nepodobne, aby od njego iměl byti zadržany.
25 O njem govori David: Jesm viděl vsegda Gospodina prěd licem mojem; ibo mi jest po pravici, aby jesm klatil se.
26 Tomu se razveselilo srdce moje i razradoval se jezyk moj, i tělo moje odpočne v naději;
27 I ne ostaviš duše mojej v pekli, a ne daš svetomu tvojemu ogledati dekompoziciji.
28 Jesi oglasil mi dragy života, a napolniš mene radostju prěd licem tvojem.
29 Brati! Mogu bezpečno govoriti do vas o patriarhu Davidu, da umrl i pogrebeny jest, a grob jego jest u nas až do dnja dnešnjego.
30 Buduči prorokom i veduči, da mu Bog prisegnul, daby usědl potomka na tronu jego.
31 Prědviděvši to, on rěkl o vozkrešenju Hristosa, da ne ostavjena jest duša jego v peklu, ni tělo jego ne vidělo gnitja.
32 Togo Jezusa vozkresil Bog, čego my vsi jesmo svědkami.
33 Po pravici Božja byvši vozvyšeny, i oběčanje Svetogo Duha prijevši od Otca, izlil to, čto vy nyně vidite i slyšite.
34 Ibo David ne vstupil do neba, no sam pověda: Rěče Gospodin Gospodu mojemu, sědi po pravici mojej,
35 až položu vragov tvojih pri podnožju nog tvojih.
36 Nehaj togdy vě věrno cěly dom Izraelsky, da jego Bog Gospodinom i Hristosom učinil, togo Jezusa, kogo vy ukrižovali.
37 A to slyšavši, byli smutni v srdcah i rěkli Petru i drugym apostolom: Čto imamo činiti, brati?
38 Togdy Petr rěkl jim: Pokajanje činite, i nehaj každy iz vas bude kreščeny v ime Jezusa Hristosa na odpuščanje grěhov, i prijmete dar Svetogo Duha.
39 Ibo vam jest to oběčanje i dětam vašim, i vsem, ktori daleko sut. Kogokoli označi Gospodin, Bog naš.
40 I mnogo inymi slovami posvědčal i napominal jih, govoreči: Izbavjajte se od togo pokoljenja nemoralnogo.
41 Kto togdy prijel slova jego, byl kreščeny, i prišlo dnja ovogo okolo tri tyseči duš.
42 I byvali v naukě apostolskoj i v spoločnosti, i v lamanju hlěba, i v molitvah.
43 I prišel strah na vsake duše, a mnogo znamenij i čudes odbyvalo se črěz děla apostolov v Jeruzalemu i byla velika bojaznj vo vsih.
44 A vsi, ktori uvěrili, byli zajedno, i vse iměli razom.
45 A iměnja prodavali, i dělili to s inymi, kako komu bylo trěba.
46 I každy den trvali soglasno v crkvi i hlěb lamajuči v domah, prijmali jedlo s radostju i v prostosti srdečnoj.
47 Hvaleči Boga i imajuči milost u vsego naroda. A Gospodin privedl v crkvu na každy den tyh, ktori iměli byti spaseni.

## Razděl 3

1 A Petr i Joan vstupali do crkvi v devetoj časině molitvy.
2 A něktory muž byl hromy od života materi svojej i nosili jego. Každy den jego sadili pri dverah crkovnyh, ktore nazyvali se Krasnymi, aby prosil o milostynje od tyh, ktori vhodili do crkvi.
3 On, viděvši Petra i Joana, čto htěli idti do crkvi, prosil jih o milostynje.
4 A Petr i Joan na njego gleděli i rěkli: Zri na nas!
5 On gleděl na njih, nadějuči se, aby něčto od njih vzeti.
6 A Petr rěkl: Srěbra i zlata ne imam; ale čto imam, to tobě dam: V imeni Jezusa Hristosa Nazaretskogo vstani i hodi!
7 I prijavši jego za pravu ruku, voznesl jego, i už prišla sila v jego nogy i kosti.
8 I vozskočivši, stal i hodil, i vstupil s njimi do crkvi, hodeči i skakajuči i hvaleči Boga.
9 A vsaki ljudi viděli jego hodečego i hvalęčego Boga.
10 I poznali, da to byl on, ktory za milostynje sěděl u Krasnyh crkovnyh dverah, i napolnili se strahom i udivjenjem nad tym, čto se mu stalo.
11 A kogda on hromy, držal Petra i Joana, priběgli k njemu vsi ljudi do saly, ktora nazyvala se Salomonovoju, udivivši se.
12 Kogda Petr to viděl, kazal ljudam: Muži Izraeljski! Čemu se tomu divite, abo čemu gledate na nas, kakoby naša sila abo moč to učinili, aby on hodil?
13 Bog Abrahama i Isaaka i Jakoba, Bog otcev naših, proslavil Jezusa, Syna svojego, ktorogo vy jeste prědali i kogo jeste odrěkli prěd licem Pilata, ktory myslil, da on zasluživaje izpuščenje.
14 Ale vy jeste odrěkli se ovogo svetogo i spravědlivogo i jeste prosili o ubijcu, aby vam byl darovany.
15 I jeste ubili daritelja života, ktorogo Bog vozkresil od mrtvyh, čemu my svědkami jesmo.
16 A črěz věru v jego ime, togo, kogo vy vidite i znajete, utvrdilo se ime jego; věra, ktora črěz njego jest, dala tomu to doskonalo zdravje prěd licem vas svih.
17 Ale nyně, brati! Věm, da jeste to iz nesvědomosti učinili, kako i načelniki vaši.
18 No Bog, ktori črěz usta prorokov svojih prědpověděl, da Hristos Jego stradati bude, tak to izpolnil.
19 Činite pokajanje, a odvratite se, aby byli izgladženi grěhy vaše.
20 Kogdy by prišli časy ogledanja lica Gospodina, by poslal ovogo, ktory vam povědany jest, Jezusa Hristosa.
21 Zaisto nebesa ima objeti do vrěmene popravjenja svih věčij, čto prědpověděl Bog črěz usta svojih svetyh prorokov od věkov.
22 Už Mojzes do otcev rěkl: Proroka vam vozbudi Gospodin, Bog vaš, iz bratov vaših, kako mene; ovogo slušati budete vo vsem, čto do vas govoriti bude.
23 I stane se, da každa duša, ktora by ne slušala togo proroka, bude izgladžena iz naroda.
24 I vsi proroki od Samuela i iny po njem, ktori izstupili, prědpověděli tož te dni.
25 Vy jeste synami prorokov i testamenta, ktoro postanovil Bog s otcami našimi, govoreči do Abrahama: A v sěmeni tvojem blagoslovjene budut vse narody zemji.
26 Vam najprvo Bog vozbudil Syna svojego Jezusa i poslal jego, aby vam blagoslovil; daby se každy iz vas odvratil od zlosti svojej.

## Razděl 4

1 I kogda oni govorili k ljudu, prišli do njih svečenniki i vojevody crkovni, i sadukeji.
2 Razgněvani byli, že učili ljudij, i povědali v Jezusu vozkrešenje iz mrtvyh.
3 I pojmali jih, i dali je do tjurmy do zautra; ibo už byl večer.
4 A mnogi iz tyh, ktori ovo slovo slyšali, uvěrili; i bylo čislo mužev okolo pet tyseč.
5 I stalo se zautra, da se sobrali načelniki jih i starši, i učeni v Pismu v Jeruzalemu,
6 I Annas, vrhovny svečennik, i Kajafas, i Joan, i Aleksandr, i koliko jih bylo iz roda vrhovnyh svečennikov;
7 I postavivši je v srědinu, pytali jih: Kakoju siloju i kakym imenem to jeste učinili?
8 Togda Petr, buduči polny Duha Svetogo, rěkl jim: Načelniki ljudski i starši izraelski!
9 Kak my dnes imajemo byti sudženi za dobrodějstvo čelověku hvoromu učinjenogo, čto by on byl uzdravjeny;
10 Nehaj vam vsim vědomo bude i vsemu ljudu izraelskomu, že v imene Jezusa Hristosa Nazaretskogo, ktorogo jeste ukrižovali, ktorogo Bog vozbudil iz mrtvyh, črěz Togo ov stoji prěd vami zdravy.
11 To jest kamen kydnuty črěz vas budujučih, ktory se stal glavoju ųgolnoju.
12 I ne jest v nijednom inom spasenju; ibo ne jest nikogo inogo imena pod nebom, danogo ljudam, črěz kogo byste smogli byti spaseni.
13 Videči bezpečnost Petra i Joana, i razuměvši, že on byli ljudami neučenymi i prostakami, divili se i poznali, da oni byli s Jezusom.
14 Videči tož ovogo čelověka s njimi stoječego, ktory byl uzdravjeny, ne iměli čto protiv tomu govoriti.
15 A razkazyvali jim izstupiti iz rady, radili se medžu soboju,
16 Govorili: Čto imajemo dělati s tymi ljudami? Ibo znamenje činjeno jest črěz nje, to vsem byvajučim v Jeruzalemu jest vědomo, a ne možemo to zaprěčiti.
17 Ale aby se to više ne razglasilo medžu ljudami, zagrozimo jim silno, aby više v tom imeni nikomu ne govorili.
18 A prizvavše jih, zakazali jim, aby už ne govorili, ni učili v imeni Jezusa.
19 Ale Petr i Joan rěkli jim: Da li to spravědlivo prěd licem Božjim, vašim kazanjam bolje slušati než kazanij Boga? Razsudite.
20 Ibo my ne možemo togo, čto jesmo viděli i slyšali, ne govoriti.
21 A oni zagrozivše jim, pustili je, ničego ne naševši, kako by je pokarati, ibo narod hvalil za to, čto se stalo.
22 Ibo ovomu člověku bylo više než četyrideset let, ktoromu se stalo to znamenje izcěljenja.
23 A kogda je pustili, prišli k svojim i oglasili jim, vse čto jim vyšni svečenniki i starši govorili.
24 Slyšavši to, jedninoju myslju vozdvignuli glas svoj k Bogu i rěkli: Gospodine! ty jesi Bog, ktory učinil nebo i zemju, i morje i vse, čto v njih jest:
25 Ktory Duhom Svetym črěz usta Davida, slugi svojego, pověděl: Čego se pobudžali narody, a narody prazdne věči myslili?
26 Stanuli kralji zemji i knezi sobrali se razom protiv Gospodinu i protiv namazaniku jego.
27 Ibo se sobrali pravdivo protiv svetomu Synu tvojemu Jezusu, ktorogo namazal, Herod i Poncky Pilat s poganami i s narodom Izraelskym.
28 Aby učinili, vse čto ruka tvoja i rada tvoja prěd tym postavila, aby se stalo.
29 I nyně, Gospodine! gledni na grozby jih, a daj slugam tvojim so vsim bezpečnost, aby govoriti slovo tvoje,
30 Segnuvši ruku tvoju k izcěljenju i k činjenju znamenij i čudes, črěz ime svetogo Syna tvojego Jezusa.
31 I kogda oni se molili, potresalo se ovo město, na ktorom byli sobrani, i napolnjeni byli vsi Svetym Duhom i govorili slovo Božje s bezpečnostju.
32 A u ovogo množstva věrečih bylo srdce jedno i duša jedna, a ni jedin iz iměnij svojih ne zval ničto svojeju vlastnoju, ale iměli vse věči razom.
33 A velikoju siloju Apostoli davali svědočstvo o voskorěšenju Gospodina Jezusa i byla velike milosrdje nad njimi vsimi.
34 Ibo ni jednogo ne bylo medžu njimi nikogo v potrěbě; ibo ktokoli iměl polja abo domy, prodaval i prinesl groše za to, čto prodal,
35 I kladli prěd nogami apostolam, i razdavano to bylo každomu, koliko komu bylo trěba.
36 Togdy Jozef, ktory nazvany jest od Apostolov Barnabasom, (to jest syn razkoš), Levit, rodom iz Cypra,
37 Imajuči polje, prodavši je, prinesl groše i položil je u nog apostolskyh.

## Razděl 5

1 Jedin muž, imenom Ananijas, s ženoju svojeju Safiroju, prodal polje,
2 i odjel něčto od tyh pěnezy za sebe, o čem jego žena znala, i prinesl něktoru čest, položivši ju k nogam apostolov.
3 I rěkl Petr: „Ananijase, čemu že Satan napolnil tvoje srdce, dabys lgal Svetomu Duhu i odjel od pěnezy za polje?
4 Či že to, čto jesi iměl, ne bylo tvoje? A čto jesi prodal, ne v tvojej oblasti ostavalo? Čemu že jesi dopustil taku věč k tvojemu srdcu? Ne jesi lgal ljudam, ale Bogu.“
5 Čujuči to, Ananijas padl i umrl. I prišel veliky strah na vsih, ktory to čul.
6 A vstavši, mladenci vzeli jego na bog i iznesli, pogrebali.
7 I stalo se po někakom vrěmeni, približno po treh časinah, da i jego žena, ne znajuči, čto se stalo, prišla.
8 I rěkl jej Petr: „Rěči mi, či za toliko jesti prodali to polje?“ A ona rěkla: „Da, za toliko.“
9 I rěkl jej Petr: „Čemu že jeste se dogovorili, dabyste pokusili Duha Gospodina? Vot nogy tyh, ktori pogrebali tvojego muža, sut pri dverah i tebe iznesut.“
10 I padla ona naglo pri jego nogah i umrla. A mladenci našli ju mrtvu, i iznesli, pogrebali ju blizko jej mužu.
11 I prišel veliki strah na cělu parafiju i na vsih, ktori to čuli.
12 Potom že črěz ruky apostolov dějalo se mnogo znamenij i čudes medžu ljudami, (a vsi oni byli soglasno razom v salě Salomona.
13 A od inyh nikto ne iměl smělosti približiti se jim, no ljudi vysoko jih ocěnjali.
14 I pribyvalo mnogo věrečih Gospodina, mužev i žen).
15 Takože iznosili boljnyh na ulice i kladli jih na posteljah i ložah, daby kak Petr prišel, zatmil těnjem svojim něktoryh iz njih, aby jih izcěliti.
16 Prišlo tož mnogo iz okolnyh měst do Jeruzalema, prinoseči boljnyh i imajuči v sobě nečisti duhy; i vsi ti byli uzdravjeni.
17 Togda vstal najvysši svečennik i vsi, ktori s njim byl, ktori byli iz sekty Saducejev, napolnjeni sut zavistju;
18 I shvatili Apostolov i dali jih do obyčajnogo vezenje.
19 Ale Angel Gospodnji v noči otvoril dveri vezenja, i izvedši jih rěkl:
20 Idite že, govorite k ljudam v crkvi vse slova togo života.
21 Togda oni uslyšavši to, vošli na svitanju do crkvi i učili. A priševši najvysši svečennik i ti, ktori s njim byli, sozvali sovět i vsih starějših synov Izraelskyh, i poslali do vezenja, aby Apostoli byli izsmějani.
22 A kogda slugi prišli, ne našli jih v vezenju, i vrativši se, objavili:
23 Vezenje jest zamknuto so vsakoju marlivostju, i straže na dvore prěd dverami stojet, no otvorivši, nikogo jesmo v njem ne našli.
24 A kogda te slova uslyšali najvysši svečennik, i hetman crkovny, i vyšni svečenniki ne znali, čto bude iz togo.
25 A prišel někto, objavil jim: Vot muži, ktoryh jeste dali do vezenja, stojet v crkvi, i učet ljud.
26 Togda pošel hetman s slugami i privedl jih bez nasilja; (ibo se ljudu bojali, aby ne byli kamenovani.)
27 A privedši jih, postavili jih prěd sovětom; i pytal jih najvysši svečennik:
28 Či jesmo vam strogo ne zakazali, byste v tom imeni ne učili? A jeste napolnili Jeruzalem naukoju vašeju i hčete na nas privesti krov člověka togo.
29 Togda odgovorili Petr i Apostoli: Boljše trěba slušati Boga, než ljudij.
30 Bog otcev naših vozbudil Jezusa, kogo jeste ubili, pověsivši na drěvu.
31 Togo Bog kako kneza i izbavitelja vozvysil po pravici svojej, daby dano bylo ljudu Izraelskomu pokajanje i odpuščenje grěhov.
32 A my jesmo svědkami jego v tom, čto govorimo, takože i Duh Svety, kogo dal Bog tym, ktori jemu poslušni sut.
33 A oni to slyšavši, srdili se i radili o tom, kako by jih ubiti.
34 Togdy vstal v radě něktory Farizej, imenom Gamalijel, učitelj zakona, považany  u vsego naroda, prikazal, aby na maly čas izvedli Apostolov;
35 I rěkl jim: Muži Izraelski! imějte se na pozornosti s strany tyh ljudij, čto byste iměli činiti.
36 Prěd tymi dnjami vstal Teodas, izobrazivši se za čto, do kogo se privezalo mužev okolo četyristo; kogo ubili, a vsi, ktori s njim občili se, razsypani sut.
37 Po njem vstal Judas Galilejski za dni čisljenje ljuda i rukovodil mnogo naroda za soboju; ale i on umrl, i vsi, ktori s njim občili se, razsypani sut.
38 Nyně povědam vam: Dajte pokoj tym ljudam i ostavite jih; abo jestli jest od ljudij ta rada ili to dělo, propade;
39 Ale jestli jest od Boga, ne budete mogli togo niščiti, byste ne našli v boju s Bogom.
40 I uslyšali jego. I kazali do sebe Apostolov i bivši jih, zakazali, aby ne govorili v imeni Jezusa; i izpustili jih.
41 A tako oni izšli iz ovoj rady, radujuči se, da se stali godnymi trpěti dlja imena Jezusa.
42 I dalje na každy den v crkvi i po domah učili i povědali o Jezusu Hristosu.

## Razděl 6

1 A v ove dni, kogda kolikost učenikov rastla, vozneslo se roptanje Grekov protiv Židam, dabyly zanedbane vdovy jih v dostavjenju jedenjem.
2 I tako ovi dvanadset zvali do sebe množstvo učenikov, rěkli: Ne jest pravo, by my ostavili slovo Božje i služili stolam.
3 Izberite, brati, medžu soboju sedm mužev, imějučih dobro svědočstvo, polnyh Duha Svetogo i mudrosti, ktore postavimo nad tym dělom.
4 A my molitvy i poslušnost slova budemo dbati.
5 I podobalo se slovo vsemu množstvu. I izbrali Ščepana, muža polnogo věry i Duha Svetogo, i Filipa, i Prohora, i Nikanora, i Timona, i Parmena, i Nikola, proselyta Antiohijskogo.
6 Tyh postavili prěd Apostolami, ktori molivši se, položili na njih ruky.
7 I rastlo slovo Božje, i množilo se velmi čislo učenikov v Jeruzalemu; i veliko množstvo svečennikov bylo poslušno věrě.
8 A Stepan, polny věry i sily, tvoril čudesa i znamenja velike medžu ljudami.
9 I vstali něktori iz tyh, ktori byli iz synagogy, ktoru zovut synagogoju Libertincov i Kirenčanov, i Aleksandrijcov, i tyh, ktori byli iz Kilikiji i Aziji, i sporili se s Ščepanom.
10 Ale ne mogli protivstati se mudrosti i duhu, ktory govoril.
11 Togda najeli mužev, ktori pověděli: My slyšali jego govorečego bogohulne slova protiv Mojzesu i protiv Bogu.
12 I vozbudili ljudi i starših, i učiteljev Zakona; i shvatili jego i privedli do rady.
13 I postavili lživyh svědkov, ktori rěkli: Toj člověk ne prěstane govoriti bogohulnyh slov protiv tomu svetomu městu i zakonu.
14 Ibo my slyšali jego govorečego: Toj Jezus Nazaretsky unišči to město i izměni zakony, ktore nam dal Mojzes.
15 A vsi, sědeči v radě, vgleděvši se na njego, viděli lice jego kako lice angela.

## Razděl 7

1 Togdy rěkl vysši kaplan: A tako jest to?
2 A on rěkl: Brati i otci, slušajte! Bog slavy pokazal se otcu našemu Abrahamu, kogdy byl v Mesopotamiji, prědže než byl v Haraně.
3 I rěkl jemu: Izojdi iz zemji tvojej i od tvojej rodiny, i idi do zemji, ktoru ti pokažu.
4 Togdy izševši iz zemji Haldejskoj, byl v Haraně, a odtud, kogdy umrl otec jego, prěnesl jego Bog do zemji toj, v ktoroj vy tutčas byvate.
5 I ne dal jemu v njej naslědovanja ni navet širokosti nogy, hot mu ju oběčal dati v naslědovanju, i potomkom jego po njem, kogdy ješče ne iměl potomka.
6 I govoril mu tako Bog: Potomki tvoje budut čudžincami v čudžej zemji budut v nevolji, i zlo jim bude črěz četyrista let.
7 Ale toj narod, komu služiti budut, ja budu sudil, rěkl Bog; a potom izojdut i služiti mně budut na tem městu.
8 I dal jemu testament obrězanja; i tako Abraham splodil Izaka i obrězal jego dnja osmogo, a Izak Jakoba, a Jakob dvanadset patriarhov.
9 A patriarhi nenaviděli Jozefa, prodali jego do Egipta; ale Bog byl s njim.
10 I izrval jego iz vsih jego morjenja, a dal jemu lasku i mudrost prěd Faraonom, kraljem Egiptskym, ktory postavil jego načelnikom nad Egiptom i nad vsim domom svojim.
11 Potom prišel glad na cělu zemju Egiptsku i Hananejsku, i veliko morjenje, i ne nahodili jedenja otci naši.
12 A kogdy uslyšal Jakob, že žita byli v Egiptu, poslal otcev naših prvy raz.
13 A za vtorym razom Jozefa brati jego poznali i poznal Faraon izvodženje Jozefa.
14 Togda Jozef, prizval otca svojego Jakoba i cělu svoju rodinu sedmdeset pet duš.
15 I stupil Jakob do Egipta, i tam umrl on i otci naši.
16 I prěnesli se do Sihema, i položili v grob, ktory kupil Abraham za pěnezy u synov Hemora, otca Sihema.
17 A kogda se približil čas oběčanja, o ktorom prisegal Bog Abrahamu, rastl narod i razmnožil se v Egiptu.
18 Až nastal iny car, ktory ne znal Jozefa.
19 On hytrym sposobom gnetl naš narod i mučil naših otcev tako, by iměli opuščati děti svoje, by ne žili i ne uveličalo se pleme.
20 V to vrěme rodil se Mojzes, i byl prěkrasny prěd Bogom. On byl tri měseče hranjeny v domu otca jego.
21 A kogda go opuščalo, vzela jego dočera Faraona i vozpitala jego kako syna.
22 I naučil se Mojzes cěloj egiptskoj mudrosti, i byl silny v besědah i dělah.
23 A kogda mu bylo četyrideset lět, htěl, aby navědil bratov svojih, synov Israelskih.
24 I viděl jedinogo maltretovanogo, zastupil se za njego i odmstiti se maltretovanomu, ktory stradal nepravo, ubivši Egipčanina.
25 Dumal sobě, že brati jego razumějut, že Bog črěz njego da jim izbavjenje, no oni togo ne razuměli.
26 A na drugy den pokazal se jim, kogda se s soboju bili, i podgovoril jih k miru: Bratami jeste! Začto krivdite jedin drugogo?
27 Jedin že, ktory krivdi bližnjego, izpihal go: Kto te postavil knezem i sudjeju nad nami?
28 Či me hčeš ubiti, kako včera jesi ubil Egipčanina?
29 I utekl Mojzes pri slyšanju tyh slov i byl čudžincem v Madjanskoj zemji, kde splodil dva syni.
30 A kogda se izpolnilo četyrideset lět, izjavil mu se na pustynji gory Sinaj Angel Gospodnji v plamenju ognja v kustu.
31 A Mojzes viděvši to, divil se tomu viděnju; a kogdy pristupil, aby na to pogledati, objavil se jemu glas Gospodnji:
32 Ja jesm Bog otcev tvojih, Bog Abrahama, Bog Isaaka i Bog Jakoba. A Mojzes, zadržavši, ne směl se pogledati.
33 I rěkl jemu Gospodin: Razděvaj obuv s nog tvojih, ibo město, na ktorom stojiš, jest zemjeju sveta.
34 Jesm viděl stradanja naroda mojego, ktory jest v Egiptu, i jesm slyšal vozdyhanje jego, i jesm sošel, dabyh jego izbavil; nyně pojdi, izšlju te do Egipta.
35 Togo Mojzesa, ktorogo se odrěkali: Kto tebe postavil knezem i sudjeju? Togo Bog poslal knezem i izbaviteljem črěz ruky Angela, ktory se jemu ukazal v kustu.
36 I on jih izvedl, tvoril čudesa i znamenja na zemji Egiptskoj i na morju Črvenom, i na pustynji, črěz četyrideset lět.
37 To jest Mojzes, ktory rěkl synam Izraelskym: Proroka vam vozdvigne Gospod, Bog vaš, iz bratov vaših, kako mene, jego budete slušati;
38 To jest, ktory byl v gromadženju na pustynji s Angelom, ktory govoril jemu na gorě Sinaj, i s otcami našimi, ktory prijel slova Božje žive, aby jih nam podal.
39 Ktoromu ne htěli byti poslušni otci naši, ale jego odkydnuli i obratili se srdcami svojimi do Egipta.
40 Govorili Aaronu: Sdělaj nam bogov, ktori by šli prěd nami; ne věmo. Čto se stalo s Mojzesom, ktory nas izvedl iz zemji Egiptskoj.
41 I sdělali v ove dni tele i prinosili žrtvu tomu idolu, i veselili se v dělah ruk svojih;
42 I odvratil se Bog i prědal jih, aby služili vojsku nebeskomu, kako jest napisano v knigah proročskyh: Či jeste prinosili mně podarky i ine žrtvy na pustynji črěz četyrideset lět, dome Izraelsky?
43 Jeste nosili palatka Moloha i nebesno tělo boga vašego Remfana. Ti obrazy, ktore jeste sobě stvorili, aby se jim klanjati; za to ja vas izgonu za Babylon.
44 Palatka svědočstva iměli otci naši na pustynji, kako Bog jim kazal, ibo pověděl Mojzesu, aby jego stvoril po obrazu, ktory viděl.
45 Otci naši ju vnesli s Josuem tam, kde byla zemja poganov, ktoryh Bog izgnal od obličja otcev naših, do dni Davida;
46 Toj našel milost prěd licem Božjim i prosil, da najde palatku za Boga Jakoba.
47 A Salomon jemu postavil dom.
48 Ale Najvysši ne prěbyva v svetiliščah rukami tvorjenyh, kako prorok skazal:
49 Nebesa sut tronom mojim, a zemja podnožje nog mojih. Kaky dom mně sbudujete, govori Gospodin, ili ktore jest město pokoja mojego?
50 Či ruka moja ne učinila vse to?
51 Tvrdošije i neobrězani srdcem i ušami! Vy se vsegda protivite Svetomu Duhu, kako otci vaši, tako i vy.
52 Kogo iz prorokov ne gonili otci vaši? I ubili tyh, ktori proročili o prihodu Spravědlivogo, ktorogo nyně jeste stali izdajnikami i ubijcami?
53 Jeste prijeli zakon črěz angelov, a jeste go ne strěgli.
54 Togda poslušali to, srdili se v srdcah svojih i skripěli na njego zubami.
55 A on byl polny Svetogo Duha, spěšno gleděl v nebo, viděl slavu Božju i Jezusa stoječego po pravici Božjej.
56 I rěkl: "Gledajte, vidžu nebesa otvorjene i Syna člověčskogo stoječego po pravici Božjej."
57 A oni kriknuli glasnym glasom, držali uši svoje i kydnuli se na njego jedinosmyslno.
58 I gonili jego iz města, kamenovali; a svědki položili oděži svoje pri nogah mladčika, kogo zvali Saulom.
59 I kamenovali Ščepana molivšego se i rěkuči: "Gospodine Jezus, prijmi duha mojego!"
60 A kleknul na kolěna, kazal glasnym glasom: "Gospodine, ne počitaj jim togo za grěh!" A to rěkuči, zasnul.

## Razděl 8

1 A Saul dopustil ubitje jego. I vozneslo se ovogo dnja veliko gonjenje v svetilišču, ktoro bylo v Jeruzalemu, i razběgli se vsi po krajah zemji Judejskoj i Samarijskoj, kromě Apostolov.
2 I pogrebli Ščepana muži bogoboječi i učinili nad njim plač veliky.
3 A Saul niščil crkov, vhodeči v domy i iztegnul mužev i žen, podaval je do vezenja.
4 A ti, ktori razběgli, hodili I povědali slovo Božje.
5 No Filip pošel do grada glavnogo Samariji i povědal jim o Hristosu.
6 A narod iměl povagu jedinosmyslno na to, čto Filip govoril, slušajuči i videči čudesa, ktore dělal.
7 Zato duhy nečiste od mnogyh tyh, ktori je iměli, glasnym glasom izhodili. A mnogo vozduhom porušenyh i hromyh byli uzdravjeni.
8 I stala se radost velika v ovom gradu.
9 A něktory muž, imenem Simon, byl prěd tym v ovom gradu čaroval i narod Samarijsky provedl v blud, povědajuči byti někym velikym.
10 Jego považali vsi od najmenšego až do največšego i rěkli: To jest ova velika moč Božja.
11 A považali jego, da od nemalogo času mamil čarami svojimi.
12 A kogda pověrili Filipu, povědajučemu kraljevstvo Božje i ime Jezusa Hristosa, krestili se muži i ženy.
13 Togdy i sam Simon pověril, a pokrestivši se,i považal Filipa. Videči čudesa i moči velike, ktore se děli, divil se.
14 A kogda Apostoli, ktori byli v Jeruzalemu, uslyšali, čto Samarija prijela slovo Božje, poslali do njih Petra i Joana.
15 Kogda prišli, molili se za njimi, aby prijeli Duha Svetogo.
16 (Duh ješče na nijednogo iz njih ne stupil; toliko kreščeni byli v ime Gospodina Jezusa.)
17 Togda vkladali na njih ruky, i oni prijeli Duha Svetogo.
18 A kogdy Simon viděl, da črěz vkladanje apostolskyh ruk možna polučiti Duha Svetogo, prinesl jim pěnezy.
19 Kazal: Dajte i mně tu moč, daby jestli na kogo-nebud vložu ruky, prijel Duha Svetogo.
20 I rěkl mu Petr: Pěneze tvoje da s toboju pogyne, da mysliš, da dar božji može byti kupjeny za pěneze.
21 Ne imaješ v toj věči česti, ni losa, ibo srdce tvoje ne jest prosto prěd licem Božjim.
22 Itak pokajaj se iz svojej zlosti, i prosi Boga; može byti odpuščeny tvoj zamysl srdca.
23 Ibo vidžu, čto ty jesi v gorkosti i v zlosti.
24 Odgovoril togda Simon: Molite se vy za mnoju prěd Gospodinom, daby na mene ničto ne prišlo iz tyh věči, ktore jeste rěkli.
25 A tako oni objavivši i pověděvši slovo Gospodina, vratili do Jeruzalema i v mnogyh gradah Samarytanskyh Evangelije objavili.
26 No Angel Gospodina rěkl Filipu: Vstani, i idi k poldnju na dragu, ktora od Jeruzalema ide k Gazě, ktora jest pusta.
27 A on vstal i pošel. A gledaj, muž iz Etiopiji, upravitelj kralice Kandaces, ktory uredžati cěly jej skarby, prišel do Jeruzalema, daby se molil;
28 I vračal, sědeči na vozu svojem, i čital Izaiji proroka.
29 I rěkl Duh Filipu: Pristupi, i podključaj se tomu vozu.
30 A priběgl Filip, uslyšal jego čitajučego Izaiji proroka i rěkl: Razuměješ li, čto čitaš?
31 I on rěkl: "Kako že mogu razuměti, jestli by mi kto ne izložil?" I prosil Filipa, daby vzel i sěděl s njim.
32 A město ovogo Pisma, ktoro čital, bylo: "Kako ovca do ubitja vedena jest, i kako baranok němy jest prěd tym, kto jego striže, tako ne otvoril ust svojih;
33 V poniženju jego sud sneseny jest. A rod jego kto opiše? Ibo sneseny byl iz zemji život jego."
34 A odgovoril muž Filipu: "Prošu te, o kom to prorok govori? Sam o sobě, ili o kom inym?"
35 Togda otvorivši Filip usta svoje, a počevši od togo Pisma, pověděl jemu o Jezusu.
36 A kako jehali po dragě, prijehali k jednoj vodě. Togda rěkl muž: "Gledaj, voda! Čto na prěponě, daby ja ne iměl byti kreščeny?"
37 I rěkl Filip: "Jestli věriš iz cělogo srdca, volno ti." A on odgovoril: "Věru, da Jezus Hristos jest Syn Božji."
38 I kazal stanuti vozu; i vstupili oba v vodu, Filip i muž, i pokrestil jego.
39 A kako izstupili iz vody, shvatil Filipa Duh Gospodnji, i ne viděl jego više muž, ale jehal po svojej dragě, radujuči se.
40 A Filip byl najdeny v Azotu, a hodeči kazal Evangelje po vsih gradah, až prišel do Kesarije.

## Razděl 9

1 A Saul, dyhaje grozboju i ubijstvom protiv učenikom Gospodoina, prišel do najvysšego kaplana.
2 I prosil jego o pisma do Damaska do synagog, da, jestli by tam našel tyh privržencev novoj dragy, mužev ili žen, daby jih svezano privedl do Jeruzalema.
3 I kogdy jehal, stalo se, kogda se približal do Damaska, da skoro osvětilo jego světlo s neba.
4 I padl na zemju, uslyšal glas k sebe govoreči: Saule! Saule! čemu mně goneš?
5 Togdy rěkl: Kto ty jesi, Gospodine? A Gospod rěkl: Ja jesm Jezus, kogo ty goneš.
6 A Saul držeči bojal se, rěkl: Gospodine! čto hčeš, daby ja učinil? A Gospodin odgovoril jemu: Vstani, a idi do grada, a tam ti kažut, čto bys iměl činiti.
7 A muži, ktori s njim byli na putovanju, stali, divili se; glas toliko slyšali, ale nikogo ne viděli.
8 I vstal Saul s zemji, a otvorivši oči svoje, nikogo ne viděl. Togdy vzeli jego za ruku; vedli go do Damaska,
9 Črěz tri dni ne viděl, i ne jel ni pil.
10 A byl něktory učenik v Damasku, imenem Ananijas; i rěkl Gospodin jemu v viděnju: Ananijasu! A on rěkl: Tu jesm, Gospodine!
11 A Gospod rěkl jemu: Vstani, i idi na ulicu, ktoru zovut prostu, a zapytaj v domu Judovym Saula imenem Tarzenika; ibo on se moli.
12 I viděl v viděnju muža, imenem Ananijas, vhodečego i ruku na njego kladučego, daby snova viděl.
13 I odpověděl Ananijas: Gospodine! Jesm slyšal od mnogyh o tom mužu, kako mnogo zlogo činil svetym tvojim v Jeruzalemu.
14 I tu ima možnost od najvysših kaplanov, daby vezal vsih pozyvajučyh ime tvoje.
15 I rěkl jemu Gospodin: Idi, ibo on jest mně izbranym instrumentom, daby nosil ime moje prěd poganami i kraljami, i prěd synami Izraelskymi.
16 Ibo ja jemu pokažu, koliko mu bude trěba stradati za moje ime.
17 Pošel Ananijas i vstupil do ovogo domu, i kladl na njego ruky, rěkl: Saule, brate! Gospodin poslal mene, Jezus, ktory se ti pokazal na dragě, po ktoroj jedeš, daby jesi snova viděl, i byl napolnjeny Svetym Duhom.
18 I naglo spadli s očij jego kako lusky i skoro snova viděl, i vstal, i stal kreščeny.
19 I vzel jedenje, silil se. I byl Saul s učenikami, ktori byli v Damasku, několiko dni.
20 I skoro pověděl v synagogah o Hristosu, že on jest Syn Božjim.
21 I divili se vsi, ktori jego slyšali, i govorili: Či to ne jest on, ktory prěslědoval v Jeruzalemu tyh, ktori pozyvali ime togo? I tu prišel, daby jih svezal i vedl do vysokyh svečennikov?
22 A Saul tym lěpje izstupil i zaměšal Židov, ktori žili v Damasku, dokazyvajuči, da toj jest Hristos.
23 A kogda prěšlo nemalo dni, izdumali Židi medžu soboju, daby jego ubili.
24 Ale se dověděl Saul o planah jih. čuvali tož vrata vo dnje i v noči, daby jego ubili.
25 A učeniki vzeli jego v noči, spustili jego po povrazu na stěnah grada v košu.
26 A kogda prišel Saul do Jeruzalema, htěl podključati se učenikom; ale se jego vsi bojali, ne věreči, daby byl tož učenikom Jezusa.
27 No Barnabas vzel jego, privedl jego Apostolom i pověděl jim, kako na dragě viděl Gospodina, da govoril jemu, i kako v Damasku bezstrašno govoril vo imeni Jezusa.
28 I žil s njimi v Jeruzalemu.
29 A bezstrašno govoril vo imeni Gospoda Jezusa, govoril i gadal s Grekami; a oni se starali, kako by jego ubiti.
30 O čem dovědali se brati, provodili jego do Cesarije i odslali jego do Tarsa.
31 I tako crkvy po vsej Judejskoj zemji i Galileji i Samariji iměli mir, budovali se i hodili v strahu Gospodina, i črěz utěšenje Svetogo Duha razmnožili se.
32 I stalo se, kogda Petr posětil vse, prišel tož do svetyh, ktori žili v Liddě.
33 Tam že našel člověka něktorogo, imenom Eneas, od osm let na ložu ležečego, ktory byl vozduhom poraženy.
34 I rěkl jemu Petr: Eneaše, uzdravja te Jezus Hristos; vstani že i posteli sobě. I zaraz vstal.
35 I viděli jego vsi, ktori žii v Liddě i v Saroně, ktori se odvratili k Gospodinu.
36 A byla v Joppu něktora učenika imenom Tabita, čto znači po grečsku Dorkas; ta byla polna dobryh dělov i milostynji, ktore činila.
37 I stalo se v ove dni, da horovala i umrla; Umyli ju i položili na salě.
38 A ibo Lidda byla blizko Joppy, učeniki uslyšalo, da tam jest Petr, poslali k njemu dvoh mužev, proseči jego, aby se ne kolěbal prijdti do njih.
39 Togdy vstal Petr, šel s njimi; a ibo prišel, provodili jego do saly i obstupili jego vse vdovy, plačuče i ukazyvajuče suknje i plašče, ktore jim Dorkas dělala, kogda byla s njimi.
40 A Petr izgnavši vsih, kleknul na kolěna i molil se, a obrativši se k ovomu tělu, rěkl: Tabito, vstani! a ona otvorila oči svoje i uzrěvša Petra, sěděla.
41 A on podavši jej ruku, vozdvignul ju, a kazal do sebe svetyh i vdov, postavil ju živoju.
42 I proslavilo se to po vsej Joppě, i mnogo jih uvěrilo v Gospodina.
43 I stalo se, da črěz mnogo dni ostal Petr v Joppě u někakogo Šimona, kožuhara.

## Razděl 10

1 A v Cezariji byl muž něktory, imenom Kornelijus, kapitan, iz armiji, ktoru zvali Italijskoju;
2 nabožny i bojal se Boga s vsim domom svojim, i čineči milostynje velike ljudu.
3 A on se vsegda Bogu moleči, viděl javě v viděnju, o devetoj časině v dnju, Angela Božjego, da vstupil do njego i mu rěkl: Kornelije!
4 A on spěšno na njego žreci, zastrašeny byvši, rěkl: Čto jest, Gospodine? I rěkl mu: Molitvy tvoje i milostynje tvoje vstupili na pamet prěd obličjem Božjem.
5 I tutčas pošli muži do Joppy, i prizvali Šimona, kogo zovut Petrom.
6 On ima gostinnost u někakogo Šimona, kožeděla, ktory ima dom nad morjem; on ti pově, čto bys iměl činiti.
7 A kogda odšel Angel, ktory govoril s Kornelijem, kazal do sebe dvoh slugov svojih i vojina nabožnogo iz tyh, ktori pri njem byli;
8 a povědavši jim vse, poslal jih do Joppy.
9 A zautra, kogda byli v dragě, a približali se do grada, vstupil Petr na strěhu, by se molil okolo časiny šestoj.
10 A byvši gladny htěl jesti; a kogda mu oni gotovili, pripadlo na njego zahvat.
11 I uzrěl nebo otvorjeno i stupajuče se sodržnik někaky, kako by platno veliko, za četyri rogy vezano i spuščeno na zemju;
12 v ktorom byli vse zemne četyrinoge zvěri, i gady i ptaky nebeske.
13 I stal se glas k njemu: Vstani Petre! rěži, i jedi.
14 A Petr rěkl: Nikako že, Gospodine! ibo jesm někogda ne jel ničto obyčnogo abo nečistogo.
15 Togdy se snova povtorno stal glas k njemu: Čto Bog očistil, ty ne iměj za nečisto.
16 Tože se stalo po trikratno. I vzeto směsta sodržnik do neba.
17 A kogda Petr sam v sobě mněval, čto to bylo za viděnje, ktore viděl, to už byli tu ti muži, ktori byli poslani do Kornelijusa, pytajuči o dom Šimona, stali prěd dverami;
18 I kriknuli, i pytali, či tam Simon, kogo zovut Petrom, tu gostil.
19 A kogda Petr myslil o ovom viděnju, rěkl jemu Duh: Vot, tebe tri muži iščut.
20 Itak vstani, a idi s njimi, ničego ne sumněvajuči se, ibo ja jih poslal.
21 Tože Petr pošel do ovyh mužev, ktori od Kornelijusa do njego poslani byli, rěkl: Vot ja jesm, kogo iščete. Čto za pričina, za ktoru jeste prišli?
22 A oni rěkli: Kornelijus kapitan, muž pravy i boječi se Boga i imajuči dobre svědočstvo od vsego židovskogo naroda, v viděnju jest od Angela svetogo napomněny, aby tebe pozval v svoj dom i slušal slov od tebe.
23 Tože kazal jih do domu, prijel je v gosti. A drugogo dnja Petr šel s njimi i něktori iz bratov iz Joppy šli s njimi.
24 A zautra vošli do Kesariji. A Kornelijus čekal jih, pozvavši svojih rodin i blizkyh prijateljev.
25 I stalo se, kogda vhodil Petr, prišel jemu Kornelijus, pripadl do nogu jego i poklonil se.
26 Ale go Petr vozdvignul, govoreči: Vstani! I ja tož jesm člověkom.
27 A razgovarjajuči s njim, vstupil i našel mnogo tyh, ktori byli sobrani.
28 I rěkl do njih: Vy znate, že ne naleži mužu Židovskomu besědovati s poganom ili posěčati pogana; no mene Bog ukazal, daby ja nikogo člověka ne nazyval čudžim abo nečistym.
29 Zato jesm tož ne sumněvajuči prišel, pozvany buduči; pytaju togdy, za čego jeste mene pozvali?
30 A Kornelijus rěkl: Od četvrtogo dnja až do togo časa jesm postil, a o devetoj časině jesm molil se v domu mojem, a vot muž něktory stal prěd mnoju v oděžju jasnoj,
31 I rěkl: Kornelije! Izslušana jest molitva tvoja, a milostynja tvoja došla na pamet prěd lice Božje.
32 Zato pošli do Joppy, a prizovi Šimona, ktorogo nazyvajut Petra; on imaje gostincu v domu Šimona, kožuhara, pri morju, ktory prijde, i bude govoriti s toboju.
33 Segda jesm poslal k tebe, a ty jesi dobro učinil, da jesi prišel. Nyně jesm vsi prěd licem Božjim svědomi, daby jesmo slyšali vse, čto ti bylo prikazano od Boga.
34 Togda Petr otvorivši usta, rěkl: Istinno poznaju, že Bog ne gleda na osoby;
35 Ale v každom narodu, ktory se jego boji i čini spravědlivost, jest jemu prijemno.
36 To jest slovo, ktoro Bog poslal synom Izraelskym, oglasil mir črěz Jezusa Hristosa, ktory jest Gospodinom vsih,
37 Vy znate, čto se stalo po vsej Judeji, počevši od Galileji, poslje kreščenja, ktoro Joan prědpověděl;
38 Kako Jezusa iz Nazareta pomazal Bog Svetym Duhom i močju; on hodil, čineči dobro i ozdravil vsih ovladnutyh od běsa; ibo Bog byl s njim.
39 A my jesmo svědkami vsego togo, čto on činil v judejskoj zemji i v Jeruzalemu, ktorogo ubili, pověsivši na drěvu.
40 Ovogo Bog sbudil tretjego dnja i učinil, daby byl objavjeny;
41 Ne vsemu narodu, ale svědkam prěd tym izbranym od Boga, nam, kto s njim jel i pil poslje jego vozkrešenja.
42 I prikazal nam, daby jesmo opověděli narodu i svědčili, da on jest ovym postavjenym od Boga sudjeju živyh i mrtvyh.
43 Jemu vsi proroki svědočstvo davajut, da črěz jego ime odpuščenje grěhov prijme každy, ktory v njego věri.
44 A kogda Petr ješče govoril se slova, sošel Svety Duh na vsih slyšečyh slova.
45 I divili se ti, ktori s Petrom prišli i byli iz obrězanja věrečimi, da i na pogani dar Duha Svetogo lije se.
46 Ibo slyšali jih govoreči raznymi jezykami i hvaleči Boga. Togda kazal Petr:
47 Či može kto zabraniti vodu, daby se ne pokrestili ti, ktori prijeli Svetogo Duha tako že, kako i my?
48 I pověděl jih pokrestiti v ime Gospodina. I prosili jego, daby u njih ostal na několiko dni.

## Razděl 11

1 I uslyšali apostoli i brati, ktori byli na Judejskoj zemji, da i pogani prijeli slovo Božje.
2 A kogda Petr prišel do Jeruzalema, sporili s njim ti, ktori byli iz obrězanja,
3 govoreči: Jesi izšel do mužev neobrězanyh, i jesi jel s njimi.
4 Togda načevši Petr, pověděl jim redom:
5 Jesm byl v gradu Joppe, molil se; i jesm viděl v zahvatu viděnje, sodržnik někaky stupajuči se kako platno veliko, za četyri rogy vezano, i spuščeno s neba, i prišlo až do mene.
6 V ktore spěšno pogledavši, jesm viděl četveronogo zemne zvěri, i gadi, i ptaky nebeske;
7 I jesm uslyšal glas govoreči do mene: Vstani, Petre; gledaj, a jedi.
8 I jesm rěkl: Nikako, Gospodine! ibo nikogda ničto obyčnogo ili nečistogo ne vhodilo v usta moje.
9 Togda mi odgovoril snova glas s neba: Čto Bog očistil, ty ne iměj to za nečisto.
10 A to se stalo po tretje i to vse vozdvignulo do neba.
11 A vot naglo tri muži stanuli prěd domom, v ktorom jesm byl, poslani byli do mene iz Cezariji.
12 I rěkl mi Duh, aby jesm s njimi šel, ničto ne sumněvajuči. Šli tož so mnoju i ti šest brati, I jesm vstupili do doma ovogo muža;
13 On nam oglasil, kako viděl Angela v domu svojem govorečego do njego: Pošli mužev do Joppy, a prizovi Šimona, kogo zovut Petrom.
14 On ti pově slova, črěz ktore spaseny budeš i cěly dom tvoj.
15 A kogda jesm počel govoriti, pripadl Duh Svety na nje, kako i na nas na početku.
16 I jesm spomněl slovo Gospodina, kako On rěkl: Joan krestil vodoju, a vy budete pokreščeni Svetym Duhom.
17 Kako že jim Bog dal jednakovy dar, kako že i nam, věrečim v Gospodina Jezusa Hristosa, i kto jesm ja, da byh mogl zabraniti Bogu?
18 Slyšavši to, utišili i hvalili Boga, rěkli: Tož i poganam Bog dal pokajanje k životu.
19 Ti že, ktori byli razsypani črěz ogorčenje, ktoro se stalo radi Ščepana, došli až do Feničije i Kypra, i do Antiohije, nikomu ne povědajuči slova Božjego, než samym Židam.
20 A byli něktori muži iz Kypra i iz Kireny, ktori prišli do Antiohije, govorili Grekam, povědajuči o Gospodinu Jezusu.
21 I byla s njimi ruka Gospodina, i veliko čislo uvěrilo, obratilo se k Gospodinu.
22 I došla o njih věst do ušij svetilišča, ktoro bylo v Jeruzalemu, i poslali Barnabasa, aby pošel až do Antiohije.
23 Ktory tam prišel i uzrěvši milosrdje Božje, obradoval se i napominal vsih, aby v prědprijemstvu srdca trvali pri Gospodinu.
24 A byl muž dobry i polny Svetogo Duha i věry. I pribylo veliko množstvo k Gospodinu.
25 Potom odšel Barnabas do Tarsa, by iskal Saula, a našel jego, privedl jego do Antiohije.
26 I byli tam cěly rok pri toj crkvi, i učili veliko množstvo; a najprvo v Antiohiji učeniki nazvani sut Hristijanami.
27 V ti dni prišli proroki iz Jeruzalema do Antiohije.
28 A vstavši jedin iz njih imenem Agabus, oglasil Duhom, že iměl byti glad veliky po vsem zemnym okrugu, ktory byl za rimskogo cěsara Klavdijusa.
29 Togda učeniki, každomu iz njih po silě svojej, postanovili poslati na pomoč bratam, ktori žili v Judejskoj zemji.
30 Tože učinili, poslavši k načelnikam črěz ruky Barnabasa i Saula.

## Razděl 12

1 I v tutom času poslal kralj Herod, daby mučili něktoryh iz crkvi.
2 I ubil Jakoba, brata Joana, mečem.
3 I viděvši, že to godi Židam, htěl pojmati i Petra: (a byli dni kyslyh hlěbov).
4 Jogo pojmavši, poslal do vezenja, prědal jego šestnadset stražam, daby jego strěgli, ibo htěl jego po Velikonoči izsmějati prěd ljudom.
5 Togdy strěgli Petra v vezenju, a molitva neprěstanno dějala se v crkvi do Boga za njego.
6 A kogdy jego už iměl izsmějati Herod, v ovoj noči spal Petr medžu dvoma stražami, svezany dvoma lancuhami, a straže prěd dverami strěgli vezenje.
7 A vot Angel Gospodnji pristupil, a světlo se razsvětlilo v gradu; a državši v bok Petra, sbudil jego, govoril: Vstani skoro! I opadli lancuhy iz ruk jego.
8 I rěkl Angel jemu: Oděvaj se. I učinil tak. I rěkl mu: Oděvaj se v plašč tvoj, i pojdi za mnoju.
9 Togdy izšel Petr, šel za njim, a ne věděl, že to dějalo se po pravdě, čto dějalo se črěz Angela; no mněl, že viděnje viděl.
10 A kogdy minuli prvu i vtoru stražu, prišli do vrat želěznyh, ktora vede do grada; a ta se jim sama črěz sebe otvorila. A izšli, prěšli jednu ulicu, a už odstupil Angel od njego.
11 Togdy Petr prišel, rěkl: Nyně znam pravdivo, že poslal Gospodin Angela svojego i izrval mene iz ruky Heroda i iz vsego očekyvanja naroda židovskogo.
12 A pametal se, prišel do doma Marije, matere Joana, kogo nazyvali Markom, kde mnogo jih se sobralo i molilo se.
13 A kogdy Petr stukal pri dverah, vyšla žena, imenom Rode, daby poslušala:
14 A poznavši glas Petra, od radosti ne otvorila dveri, ale oglasila, da Petr stoji pri dverah.
15 A oni rěkli jej: Gluposti govoriš! No ona tvrdila, da tako jest. A oni rěkli: Angel jego jest.
16 Ale Petr ne prěstaval stukati; i kogda otvorili, uviděli jego i divili se.
17 A mahajuči na njih rukoju, aby molknuli, pověděl jim, kako jego Gospodin izvedl go iz vezenja i rěkl: Kažite to Jakobu i bratam. A izšel, šel na ino město.
18 A kogda byl den, stal se nemaly nepokoj medžu vojevnikami o to, čto se s Petrom stalo.
19 Ale Herod, kogda se o njem izpytyval, a ne našel, učinivši sud o stražah, kazal jih ubiti; Potom izšel iz Judejskoj zemji do Cezarii, žil tam.
20 A Herod srdil se o Tyrijcah i Sidoncah; ale oni jedinosmyslno prišli do njego, a dobyli Blasta, upravitelja kraljevskogo, prosili o mir, ibo krajina jih iměla jedenje iz državy kraljevskoj.
21 A jedinogo dnja Herod v paljtu kraljevskom i sěděl na tronu, i učinil rěč jim.
22 A ljudi kazal: Glas Božji, a ne člověčski!
23 A v tutom momentu udaril go Angel Gospodnji, ibo ne dal hvaly Bogu, a byvši sjedeny od črvov, umrl.
24 A slovo Gospodina razrastalo se i razmnožilo se.
25 A Barnabas i Saul vratili iz Jeruzalema, izpolnivši slugu, vzevši s soboju Joana, kogo nazyvali Markom.

## Razděl 13

1 A byli v Antiohiji v crkvi, ktora tam byla, něktori proroki i učitelji kako Barnabas i Simon, ktory nazyvano Nigerom, i Lucijus Kirěnejski, i Manahen, ktory byl vozpityvani s Herodem Tetrarhom, i Saul.
2 A kako oni službu Gospodina javno odpravjali i postili, rěkl jim Duh Svety: Odděljajte mně Barnabasa i Saula do togo děla, do ktorogo jesm jih pozval.
3 Togdy postili i molili se, i vkladajuči na njih ruky, odpravili jih.
4 Oni togdy poslani byvši od Duha Svetogo, prišli do Seleuciji, a odtud pluli do Kipra.
5 A kako byli v Salamisu, povědali slovo Božje v židovskyh synagogah, a iměli s soboju Joana do služby.
6 A prěsedši ov ostrov až do Pafa, našli tam někakogo čaroděja, falšivogo proroka, Žida, komu ime bylo Barjezus.
7 On byl pri naměstniku, Sergiju Pavlu, mužu razumnym. Toj prizvavši Barnabasa i Saula, želal slyšati slovo Božje.
8 No jim se protivil Elymas, čaroděj, (abo se tako izkladaje ime jego), starajuči se, kako by naměstnika od věry odvratil:
9 Togdy Saul, (ktorogo zovut Pavlom) napolnjeny byvši Duhom Svetym, a spěšno na njego zrěl,
10 Rěkl: O obmanniče hytry i nebogy, synu djabelsky, vragi vsakoj spravědlivosti! ne prěstaneš li bezpokojiti prostyh drag Gospodina?
11 A vot ruka Gospodina prijde nad toboju: i budeš slěpym, ne uzriš solnca až do vrěmene. A v tutom momentu pripadla na njego oblaka i tma, a bludeči išče, kto by jego vodil za ruku.
12 Togdy viděl naměstnik, čto se stalo, uvěril I divil se nad naukoju Gospodina.
13 A odšel Pavel iz Pafa i ti, ktori s njim byli, prišli do Pergi. A Joan odševši od njih, vratil do Jeruzalema.
14 A oni odševši iz Pergi, prišli do Antiohiji Pisidijskoj, a vševši do synagogy v subotu, sědli.
15 A po pročitanju zakona i prorokov, poslali do njih starših synagogy, govoreči: Brati! jestli imate slovo do utěšenja naroda, govorite.
16 Togdy vstavši Pavel i mahnuvši rukoju rěkl: Muži izraelski i vy, ktori se bojite Boga, slušajte!
17 Bog naroda sego izraelskogo izbral otcev naših i vozdvignul narod, no byli čudžincami v zemji egiptskoj, i izvedl jih iz njej.
18 I v vrěmeni četyrideseti lět trpěl obyčaje jih v pustynji.
19 I zatopivši sedm narodov v zemji hananojskoj, razdělil medžu njimi zemju jih.
20 A potom okolo četyristo i petdeset lět daval jim sudjev až do Samuela proroka.
21 A od ovogo vrěmene prosili o kralja. I dal jim Bog Saula, syna Kisa, muža iz kolěna Benjamina, črěz četyrideset lět.
22 A kogda jego odvrgnul, vozdvignul jim Davida za kralja, komu tož svědočstvo davajuči rěkl: Našel Davida, syna Jesse, muža po srdcu mojemu, ktory bude tvoriti volju moju vo vsim.
23 Iz jego potomkov Bog po oběčanju dal Izraelju spasitelja Jezusa.
24 Prěd prihodom kogo Joan kazal kreščenje na pokajanje vsakomu narodu izraelskomu.
25 A kogda Joan dokončil běg svoj, rěkl: Za kogo mně imate? Ne jesm tym, za ktorogo vy mene imate, ale ide za mnoju, u kogo nog obuvky ne jesm dostojny razvezati.
26 Brati, syni naroda Abrahama i vy, ktori medžu vami se Boga bojite, vam slovo spasenja poslano jest.
27 Ibo ti, ktori živut v Jeruzalemu i jih načelniki, ne znajuči sego Jezusa i glasov prorokov, ktore črěz každu subotu byvajut čitane, izpolnili jih, osudivši jego.
28 A nikakoj pričiny do smrti v njem ne najduči, prosili Pilata, aby go ubiti.
29 A kogda izpolnili vse, čto o njem bylo napisano, vzeli jego s drěva, položili jego do groba.
30 Ale jego Bog vozdvignul iz mrtvyh.
31 I viděli Go črěz mnogo dnev ti, ktori s njim razom prišli iz Galileje do Jeruzalema i sut svědkami jego prěd ljudom.
32 I my vam povědajemo to oběčanje, ktoro se otcam stalo, že jego Bog izpolnil nam, dětam jih, vozbudivši Jezusa.
33 Kako tož v psalmu vtorom napisano jest: Syn moj jesi ty, ja tebe dnes splodil.
34 A že jego vozbudil od mrtvyh, aby više ne vratil do gnitja, to rěkl: Dam vam svete dobrodějanja Davida.
35 Itak pověděl: Ne daš Svetomu tvojemu viděti gnitja.
36 Ibo David za věky svojej služby voli božjej, zasnul i podključeny jest do otcev svojih, a viděl gintje.
37 A toj, ktorogo Bog vozbudil, ne viděl gnitja.
38 Nehaj že vam togdy bude vědomo, brati, že se vam črěz togo povědaje odpuščanje grěhov:
39 I od vsego od čego jeste ne mogli byti črěz zakon Mojzesa opravdani, črěz togo každy věreči opravdany bude.
40 Vot uvažate, aby na vas ne prišlo to, čto pověděno v prorokah:
41 Vidite vy prězirajuči. Divite se, a v kompletno obratite se; ibo ja dělam dělo v dni vaših, dělo, ktoromu ne věrite, kak by vam kto o njem pověděl.
42 A kogda oni izhodili iz synagogy židovskoj, prosili jih pogani, aby i v drugu subotu govorili do njih tož ti slova.
43 A po razpuščenju sobranja, pošlo mnogo Židov i nabožnyh novověrnikov za Pavlom i Barnabasom, ktori govorili s njimi, radili jim, aby trvali v laskě božjej.
44 A v drugu subotu nemalo cěly grad se sobral na slušanje slova božjego.
45 Togdy Židi videči ljud, napolnjeni byli zavistju i sprotivili se tomu, čto Pavel povědal, govoreči protiv tomu i ogovoreči o tom.
46 A Pavel i Barnabas, smělo rěkli: Vam najprvo imělo byti povědano slovo Božje; ale ibo jego odvrgajete, a sudite sebe byti nedostojnymi věčnogo života, to vračamo se k poganam.
47 Ibo nam tako prikazal Pan, govoreči: Jesm sdělal tebe světlom poganov, daby jesi tvoril spasenje až do granice zemji.
48 A slušajuči to pogani, radovali se i hvalili slovo Gospodina, i uvěrili, koliko jih bylo prigotovjenyh do věčnogo života.
49 I raznosilo se slovo Gospodina po vsej ovoj krajině.
50 A Židi podstrěknuli ženy nabožne i dvorjanske, i prvyh v gradu; a vozbudili gonjenje protiv Pavlu i protiv Barnabasu, i izgnali jih iz zemej svojih.
51 A oni drli prah iz nog svojih i došli do Ikonija.
52 A učeniki byli napolnjeni radostju i Svetym Duhom.

## Razděl 14

1 I stalo se v Ikoniji, da razom pošli do židovskoj synagogy, i tako govorili, da uvěrilo jim mnogo Židov i Grekov.
2 Ale Židi, ktori ne uvěrili, srdili se črěz srdca poganov protiv brati.
3 I byli tam dolgo vrěme, bezpečno govorili v Panu, ktory daval svědočstvo slovu milosrdja svojego i tvoril to, da se děli znamena i čudesa črěz ruky jih.
4 I razdělila tolpa grada, jedni byli s Židami a drugi s Apostolami.
5 A kogda buntovali se pogani i Židi s načelnikami svojimi, aby jih maltretovati i kamenovali:
6 Razuměvši to, utekli do grada Likaonskogo, do Listry i do Derby, i do okoličnyh zemej,
7 A tam pověděli Evangelje.
8 A muž něktory v Listrě boljny na nogah sěděl, byvši hromy od života materi svojej i nikogda ne hodil.
9 Toj slušal Pavla govorečego; ktory na njego spěšno zrěl i viděl, da iměl věru, aby mogl byti uzdravjeny,
10 Rěkl velikym glasom: Stani prosto na nogy tvoje; i skočil i hodil.
11 A narod viděl, čto Pavel učinil, vozdvignuli glas svoj, govoreči po likaonsku: Bogi stali se podobni ljudam, stupili do nas.
12 I nazvali Barnabasa Jupiterom, a Pavla Merkurijusom, ibo vedl rěč.
13 Togdy kaplan Jupitera, ktory byl prěd gradom jih, voli s věncami do vrat privedl, htěl žrtvu s narodom dělati.
14 Koda uslyšali Apostoli Barnabas i Pavel, razdirati oděž svoju, vpadli medžu narod I kazali,
15 I govoreče: Muži! Čto vy tvorite? I my jesmo ljudami, imajemo za vas Evangelje. Povědamo vam, byste se od tyh falšivyh bogov odvratili do Boga živučego, ktory učinil nebo i zemju i morje, i vse čto v njih jest.
16 Bog v poslědnyh věkah dopustil vsim poganam hoditi po svojih dragah.
17 Jednako ostavil samogo sebe bez svědočstva, čini dobro, davaje nam s neba děla dobre i dožd, napolnjaje krmoju i radostju srdca naše.
18 I to govoreče uspokojili ljud, da ne požrtvovali jim.
19 A prišli iz Antiohiji i iz Ikonija Židi, ktori podgovorili ljud i kamenovali Pavla, izvlěkali za město, mysleče, daby umrl.
20 No sobrali se u njego učeniki, vstal všel v grad, a zautra odšel s Barnabasom do Derbije.
21 I povědavše Evangelje tomu gradu, mnogo ljudij učil, vratil se do Listry, do Ikonija i do Antiohiji;
22 Utvrdil duše učenikov i napominal, daby ostali v věrě, i govoreči: Črěz mnogo trudov nam trěba vhoditi do kraljevstva Božjego.
23 I kako jih pozvali starši v každoj crkvi molili se s postami, prěporučali jih Gospodinu, v ktorogo uvěrili.
24 I prěsedši Pisidiju, prišli do Pamfiliji.
25 I povědavši slovo Božje v Pergě, pošli do Ataliji.
26 I odtud pluli do Antiohiji, odkud byli oddani milosrdju Božjem k tomu dělu, ktoro završili.
27 I kako tam prišli sobrali parafiju, oglasili, čto Bog črěz njih učinil, da poganam dveri věry otvoril.
28 I žili tam nemalo vrěme s učenikami.

## Razděl 15

1 I něktori prišli iz Judejskoj zemje naučiti bratov: Kak ne obrěžete se po obyčaju Mojzesa, ne možete byti spaseni.
2 Črěz to iměli Pavel i Barnabas nemaly spor s njimi, postanovili, aby Pavel i Barnabas i něktori drugi iz njih šli do Apostolov i do starših do Jeruzalema, s radi togo spora.
3 Oni togdy byli proščani od parafiji, šli črěz Feniciju i Samariju, povědajuči o odvračenju poganov i učinili veliku radost vsim bratam.
4 A kogda prišli do Jeruzalema, byli prijeti od parafiji i od Apostolov, i starših, i pověděli, čto Bog črěz njih činil.
5 Ale vstali něktori iz sekty Farizejev, ktori uvěrili, govoreči: Da jih trěba obrězati i prikazati jim, aby hovali zakon Mojzesa.
6 Sobrali se togdy Apostoli i starši, aby mysliti o tom dělu.
7 A kogda byl veliki spor o tom, vstal Petr, rěkl jim: Brati! vy věte, da od davnyh dni Bog mene izbral medžu vami, aby črěz usta moje pogani slušali slovo Evangelja i uvěrili.
8 A Bog, ktory zna srdca, izdal jim svědočstvo, davši jim Duha Svetogo, kako i nam.
9 I ne učinil nikakoj raznici medžu nami a njimi, kak věroju očistil srdca jih.
10 I tak v tutom momentu, za čto pokušate Boga, kladuči jarmo na šiju učenikov, ktorogo ni otci naši, ni jesmo smogli nesti?
11 Ale črěz milosrdje Gospodina Jezusa Hristosa věrimo, da budemo spaseni tym sposobom, kako i oni.
12 I molčala cěla tolpa, a slušali Barnabasa i Pavla, ktori pověděli, kako veliki znamena i čudesa činil Bog črěz njih medžu poganami.
13 A kogda oni molčali, odgovoril Jakob, govoreči: Brati! slušajte mene.
14 Simon pověděl, kako Bog najprvo prišel do poganov, aby iz njih sdělal narod imena svojego.
15 A s tym soglaset se slova prorokov, kako jest napisano:
16 Potom vrnu, i postavju palatku zgubjenu Davida postaviti.
17 Daby ti, ktori ostali iz ljudij, iskali Gospodina, i vse narody, nad ktorymi prizyvano ime moje, govori Gospodin, ktory to vse čini.
18 Znane sut od věka vse jego děla Bogu.
19 Zato moje mněnje jest, daby ne trevožiti tyh, ktori se iz poganov k Bogu odvračajut.
20 Ale povinno pisati jim, daby se strimali od molitvy do falšivyh bogov i od bluda, i od věčij udušenyh, i od krvi.
21 Ibo Mojzes od davnyh věkov ima v každom gradu tyh, ktori jego povědajut i jego v synagogah na každu subotu čitajut.
22 Togda se podobalo Apostolam i staršim i cěloj parafiji, daby izbrani byli muži, i poslati jih do Antiohiji s Pavlom i s Barnabasom, to jest Judasa, ktorogo zvali Barabasom, i Silasa. Muži znamenitymi medžu bratami.
23 I dali jim pismo do ruky: Apostoli i starši bratam, ktori sut iz poganov I sut v Antiohiji i v Syrii, i v Kiliciji, zdravja želajemo;
24 ibo jesmo čuli, da něktori izševše od nas, trevožili vas slovami svojimi, oslabjajuči duši vaše, a govoreči, že trěbujete se obrězati i zakon hovati, čego jesmo jim ne kazali sdělati.
25 Stalo se nam jedinosmyslno sobranym, poslati do vas mužev izbranyh s milymi našimi, Barnabasom i s Pavlom,
26 S ljudami, ktori izdali duše svoje za imene Gospodina našego, Jezusa Hristosa.
27 Ibo posljemo Judasa i Silasa, ktori vam to ustami tože povědut.
28 Stalo se Duhu Svetomu i nam, daby ne kladli na vas nikakogo brěmena, kromě tyh věčij potrěbnyh;
29 Da byste se strimati od žrtv za falšivyh bogov, i od krvi, i od věčij udušenyh, i od bluda. Jestli togo ježe se strimate, dobro učinite. Imějte se dobro.
30 A tako oni byli odpravjeni, prihodiši do Antiohiji, a kak sobrali parafiju, oddali list.
31 I kogda pročitali to, radovali se.
32 A Judas i Silas, buduči takože prorokami, dolgymi slovami napominali bratov i utvrdžali jih.
33 A živši tam nemalo vrěme, byli odpravjeni s želanjem mira od bratov k Apostolam.
34 No Silas htěl tam ostati.
35 Takože Pavel i Barnabas žili v Antiohiji, učeči i povědajuči s mnogymi inymi ljudami slovo Gospodina.
36 A po několiko dnjah rěkl Pavel Barnabasu: Vrnimo se, navědimo bratov naših po vsih gradah, v ktoryh jesmo pověděli slovo Gospodina, kak jim se vede.
37 Togdy Barnabas radil, daby s soboju vzeli i Joana, ktory byl zvany Marko.
38 No Pavel ne htěl vzeti s soboju togo, ktory odšel od njih iz Pamfilije, a ne htěl jim pomogti s trudom.
39 I medžu njimi byl veliky spor i odšel jedin od drugogo, a Barnabas vzel s soboju Marka, plul do Cypry.
40 No Pavel izbravši sebe Silasa, izšel, buduči poručeny milosrdju Božjej od bratov:
41 I prěhodil črěz Siriju i Ciliciju, utvrdžajuči parafije.

## Razděl 16

1 I prišel do Derby i do Lystry, I vot, byl učenik někaky, imenom Timoteus, syn někakoj ženy židovkoj věrnoj i otca Greka.
2 O njem svědčili brati, ktori byli v Lystrě i v Ikoniji.
3 Htel že Pavel, aby on šel s njim, i vzel jego, obrězal jego radi Židov, ktori sut v ovom městu; ibo vsi věděli, že jego otec byl Grekom.
4 I kako hodili po gradah, prědavali jim do hranjenja rěšenja, ktore byly ustanovjene od Apostolov i starših iz Jeruzalema.
5 I tak crkvi utvrdžali v věrě i uveličali jih v čislom každom dnjem.
6 Kogda prěšli Frygiju i Galatsku krajinu, kazal jim Duha Svety, aby ne pověděli slova Božjego v Aziji,
7 prišli do Miziji, probovali pojdti do Bitiniji, no jim Duh Jezusa ne dopustil.
8 I prěševši Miziju, se spustili do Troady.
9 I ukazalo se Pavlu v noči viděnje: muž někaky Makedonec stoječi, proseči jego i govoreči: Prijdi do Makedoniji i pomoži nam.
10 I viděvši to viděnje, jesmo se starali o to, kako by my mogli pojdti do Makedoniji, buduči uvěrjeni, da nas Gospodin pozval, aby my jim kazali Evangelje.
11 Odplyvši iz Troady, pravo běgali do Samotraciji, i zautra do Neapoli.
12 I odtud do Filipi, do grada v prvom dělu Makedoniji v novom poseljenju; I jesmo ostali v tom gradu několiko dni.
13 I v den suboty jesmo izšli prěd grad k rěkě, kde obyčajno byvajut molitvy, i seduči my govorili k ženam, ktore tam byli sobrane.
14 I něktora žena, imenom Lidija, ktora purpur prodavala v gradu Tjatirskom, Boga boječa se, poslušala; I Gospod otvoril jej srdce, aby spěšno poslušala to, čto Pavel govoril.
15 I kako se pokrestila ona i dom jej, prosila, govoreči: Kak mně jeste posudili věrnoju byti Gospodinu. Prijdite do doma mojego žiti; i prinudžala nas.
16 I stalo se, kogdy jesmo pošli na molitvu, da něktora děvka, ktora iměla duha jasnovidca i svojim gospodinam prinosila veliku lihvu, běgala nam.
17 Ta hodeči za Pavlom i za nami, kazala, govoreči: „Ti ljudi sut slugami Boga Najvysšego, ktori nam povědajut put izbavjenja.“
18 A to činila črěz mnogo dni; ale Pavel srdil se nad tym i rěkl ovomu duhu: „Prikažu ti v imeni Jezusa Hristosa, aby ty izšel iz nje.“ I izšel v ovoj že časině.
19 A viděli gospodini jej, da izgynula naděja lihvy jih, pojmavši Pavla i Silasa, tegnuli jih na trg prěd ured,
20 A postavivši jih prěd uredom, rěkli: „Ti ljudi činet zaměšanje v našem gradu, buduči Židami:
21 I povědajut obyčaje, ktoryh se nam ne godi prijmati i ne zahovati, ibo jesmo Rimjanami.“
22 I vstal narod protiv njim, a ured kazali jim razdrti oděž jih, bičevati rozgami.
23 A kogdy jim mnogo ran zadali, kydnuli jih do vezenja, kazali vezenskoj straži, aby jih dobro strěgl.
24 Ibo prijel taky razkaz, vsadil jih do najglubšego vezenja, a nogy jih zaključil v kladě.
25 A o polnoči Pavel i Silas molili se, hvalili Boga pěsnjami, tako že jih slyšali vezni.
26 I stalo bystro veliki zemjetresenje, da se porušili zemja vezenja, i v tutom momentu se otvorili vse dveri, i vsih byli voljni.
27 A probudivša se vezenska straža i uzrěvša otvorjene dveri u vezenja, iztegnul meč, I htěl sam sebe ubiti, mněvajuči, da vezni utekli.
28 Ale Pavel kriknul glasom velikym, govoreči: „Ne čini sobě ničego zlogo: ibo jesmo tu.“
29 A prikazavši zasvětiti, vpadl tam, a držeči se pripadl k nogam Pavla i Silasa:
30 A izvedši jih iz vezenja, rěkl: „Gospodine! Čto imam činiti, byh byl izbavjeny?“
31 A oni rěkli: Věri v Gospodina Jezusa Hristosa, i budeš spaseny, ty i tvoj dom.
32 I pověděli jemu slovo Gospodina i vsim, ktori byli v domu jego.
33 A vzel jih v ovoj časině v noči do sebe, omyl rany jih i dal sebe pokrestiti i cěly dom jego.
34 A vvedši jih do domu svojego, gotovil jim jedu i veselil se so vsim domom svojim, uvěrivši Bogu.
35 A kogdy byl den, poslal načelnik grada slugi suda, govoreči: Izpustite ovyh ljudij.
36 I oglasila straža te slova Pavlu, da načelnik grada poslal, aby byli izpuščeni: izojdite, idite v pokoju.
37 Ale jim Pavel rěkl: bičevali nas javno rozgami ne osudženyh, hot jesmo Rimjanami, kydnuli do temnice; a tutčas nas tiho izganjajut? Ničto iz togo; ale sami nehaj prijdut i izvedut nas.
38 Togdy pověděli načelniku grada slugi suda te slova. I bojali se, uslyšavši, da byli Rimjanami.
39 A prišli, poprosili jih, a izvedši jih, prosili jih, aby izšli iz grada.
40 Izševši že iz temnice, pošli do doma Lidiji. Posěčajuči bratov, utěšili jih i odšli.

## Razděl 17

1 A prěševši Amfipol i Apoloniju, prišli do Fesaloniki, kde byla židovska synagoga.
2 Togda Pavel po svojemu obyčaju všel do njih, i črěz tri suboty kazal jim iz Pisma.
3 Pokazal to, da Hristos iměl stradati i vstati od mrtvyh, i da Jezus jest Hristosom, o ktorom ja vam povědam.
4 I uvěrili něktori iz njih, podključili se Pavlu i Silasu, i tož velika tolpa nabožnyh Grekov, i žen dvorjanskyh nemalo.
5 Ale Židi, ktori ne uvěrili, iměli zavist, vzeli k sobě něktoryh legkomyslnyh i zlyh mužev, a sobravši gromadu učinili razdor v gradu. Prišli do doma Jazona, iskali jih, aby jih izvedli prěd ljud.
6 A ne našli jih, tegnuli Jazona i něktoryh bratov do starših grada, kriknuli: "Vot ti, ktori cěly grad razčulili, i tu tož prišli;
7 I tyh prijel Jazon; a ti vsi činet protiv carskyh dekretov, povědajuči, da jest iny car, Jezus."
8 A tako razčulili prosty ljud i starših grada, ktori to slyšali.
9 Ale kogdy prijeli dostatočne zaručenje od Jazona i od inyh, pustili jih.
10 A brati skoro v noči poslali Pavla i Silasa do Berei; Kogdy oni tam prišli, vošli do židovskoj synagogy.
11 A oni byli bolje dvorjanski než ti, ktori byli v Fesaloniki, ktori prijeli slovo Božje s vsimi radostami, v každy den čitali Pismo, či ono tož tak mysli.
12 Zato mnogo jih iz njih uvěrilo, i tož greckyh žen dvorjanskyh i mužev nemalo.
13 A kogda Židi iz Fesaloniki se dověděli, čto v Berei povědano bylo slovo Božje od Pavla, prišli tudy, podstrěknuli prosty ljud.
14 Ale brati skoro poslali Pavla, aby šel do morja; a Silas i Timoteus tam ostali.
15 A ti, ktori vodili Pavla, provodili go až do Atena, a cělo prikazanje do Sila i do Timoteusa, aby čim skorěje prišli do njego, odšli.
16 I poka Pavel čekal na njih v Atenah, jego duh v njim se porušil, ibo viděl ov grad oddany osvečanju falšivyh bogov.
17 I tako on iměl razgovory s Židami i s nabožnymi ljudami, v synagogě i na trgu v každy den.
18 Togda něktori iz epikurejcev i stoikov sporili se s njim, a něktori govorili: Čto že tut toj donositelj hče govoriti? A drugi: On oglasiteljem novyh bogov; ibo jim o Jezusu i vozkrešenju pověděl.
19 I hvatili jego, vedli do Areopaga, govoreči: Možemo li věděti, čto to jest za nova nauka, ktoru ty povědaš?
20 Ibo někake čudže věči prinosiš do ušij naših; hčemo tako věděti, čto že iz togo imaje byti?
21 (A vsi Atenjani i čudži gosti ničim inym se ne bavili, toliko povědanjem abo slušanjem novin.)
22 Togda Pavel, stanuvši v srědě Areopaga, rěkl: Muži Atenjski! Iz každoj měri vas vidžu nadměrno nabožnyh.
23 Ibo prěhodeči se i zirknuči na vaši obrazy bogov, jesm našel oltar, na ktorom napisano: Neznajemomu Bogu. Ktorogo tako ne znajuči hvalite, togo ja vam povědam.
24 Ibo Bog, ktory učinil svět i vse, čto na njem, toj byvši Gospodinom neba i zemji, ne žive v crkvah rukami činjenyh.
25 Ni rukami ljudskymi hvaleny byvaje, kakoby čego potrěboval. On da vsim život i dyh, i vse.
26 I učinil iz jednoj krvi cěly narod ljudski, aby žil po vsem licu zemji, razlagal prěd tym časy i razlagal granice žitja na njih;
27 Aby iskali Gospodina, aby jego čuli i našli, hot od každogo iz nas ne jest daleko.
28 Ibo v njem živemo i divimo se, i jesmo, kako i něktori iz vaših poetov pověděli: Jesmo i jesmo rodinoju jego.
29 Byvši takoju rodinoju Božja, ne imamo mysliti, aby on byl podobny zlatu abo srěbru, abo hudožstvo ljudskomu, abo izmyslu člověčskomu.
30 Tako prěgledal Bog časy toj nevědomosti, ale tutčas oglasi ljudam vsim vesde, aby pokajali se;
31 Iže on ustanovil den, v ktorom on bude sudil cěly svět v spravědlivosti po mužu, kogo on naznačil na to. Aby každy o tom uvěril, vozkresil jego od mrtvyh.
32 A uslyšavši o vozkrešenju, jedni se zasmějali, a drugi govorili: „Budemo te snova o tom slušati.“
33 I tako Pavel izšel iz srědišča jih.
34 A něktori muži podključali se jemu i uvěrili, medžu ktorymi byl Dionizijus Areopagit i žena imenom Damara i drugi s njimi.

## Razděl 18

1 Potom Pavel odšel iz Ateny i prišel do Korinta;
2 i našel něktorogo žida, imenom Akvila, rodom iz Ponta, ktory nedavno prišel iz Italije s Priskilloju, ženoju svojeju (ibo Klavdijus htěl, aby vsi židi odšli iz Rima), i prišel do njego;
3 Ibo byl on togo samogo remesla, žil pri njih i rabotal; ibo remeslo jih bylo dělati palatky.
4 I iměl on besědu v synagogě na každu subotu i obratil židov, i grekov.
5 A kogda prišli iz Makedonije Silas i Timoteus, Pavel byl gorlivy v duhu, oglasil židam, da Jezus jest Hristosom.
6 A kogda oni protivrěkli i ogovorili, držal prah iz oděži, rěkl jim: Krov vaša prijde na glavu vašu; ja jesm čisty, od togo času pojdu k poganam.
7 A odvedši odtud vstupil do doma někakogo člověka, imenom Justus, služečego Bogu, čijego dom byl blizko synagogy.
8 A Krispus, starši synagogy, uvěril v Gospodina s cělym domom svojim, i mnogo iz Korinta slušajuči, uvěrili i byli pokreščeni.
9 Potom Gospodin rěkl Pavlu v noči v viděnju: Ne boj se, ale govori, i ne molči.
10 Ibo ja jesm s toboju, i nikto ne bude tknuti tebe, aby ti zlo učiniti; ibo ja imam veliki narod v tom gradu.
11 I žil tam god i šest měsecev, učil u njih slovo Božje.
12 A kogda Galion byl načelnikom grada v Achaji, vstali jedinosmyslno židi protiv Pavlu i privedli jego k sudu, govoreči:
13 On podgovori ljudij, aby protiv zakonam Boga hvalili.
14 A kogda Pavel iměl usta otvoriti, rěkl Galion k židam: O židi! Kogdy by se vam  prěstupjenje stalo, abo krivda, pravedno by ja vas slušal;
15 Ale jestli jest někaky spor o slovah i o imenah i o zakonu vašem, sami togo razrěšite; ibo ja ne hču byti sudjeju togo.
16 I izgnal on jih od sudje trona.
17 Togdy hvatili vsi Sostena, starějšego synagogy, bili jego prěd tronom sudje, a Galion ne dbal za ničto.
18 A Pavel pobivši tam ješče několiko dnev, proščavši se s bratami, odplul do Syrije, a s njim Priskilla i Akvila, strigl svoju glavu v Kenchrejah, ibo učinil zarok.
19 Potom prišel do Efeza i tam jih ostavil, a sam vhodil do synagogy, iměl razgovor s Židami.
20 A kogda jego prosili, aby u njih na dolžejši čas pobyl, ne htěl;
21 Ale proščavši se s njimi, rěkl: Vratim, jestli bude taka Božja volja. I odplul iz Efeza.
22 A kogda prišel do Cesarije, vhodil do Jeruzalema i pozdravivši crkvu, šel do Antiohije.
23 I pobyvši tam něktory čas, izšel obhodivši Galatsku zemju i Frygiju, potvrdžajuči vsih učenikov.
24 A Žid někaky imenom Apollos, rodom iz Aleksandrije, muž zlatousty, prišel do Efeza. Byl silny v Pismah.
25 On byl poučeny v puti Gospodina, i goril v duhu, govoril i učil spěšno o Gospodinu, znajuči toliko o kreščenju Joana.
26 On začel smělo govoriti v synagogě. Kogdy uslyšali Akvila i Priskilla go, prijeli jego do sebe i dostatočněje mu izložili put Božji.
27 A kogda htěl idti do Ahaje, napominavši jego brati pišajuči do učenikov, aby jego prijeli; Kogda tam prišel, mnogo pomagal tym, ktori uvěrili v milost Božju.
28 Ibo silno Židov svrgali argumentami, javno dokazyvajuči črěz Pismo, da Jezus jest Hristosom.

## Razděl 19

1 I stalo se, kogda Apollos byl v Korintě, da Pavel, obhodivši vrhne kraje, došel do Efeza; i našel tam něktoryh učenikov,
2 rěkl jim: Či jeste prijeli Duha Svetogo, da jeste uvěrili? A oni mu rěkli: Ni jesmo slyšali, či jest Duh Svety.
3 Togdy rěkl jim: V čto jeste kreščeni? A oni rěkli: V kreščenju Joana.
4 Zato rěkl Pavel: Joan krestil kreščenjem pokajanja, govoreči narodu, aby v ovogo, ktory iměl prijdti po njem, uvěrili, to jest v Jezusa Hristosa.
5 A uslyšavši to, dali se kresti v ime Gospodina Jezusa.
6 A kogda na njih vložil Pavel ruky, stupil na njih Duh Svety i govorili jezykami i prorokovali.
7 A bylo vsih mužev okolo dvanadset.
8 A vhodili v synagogu, govorili bezpečno črěz tri měseče, učili i podgovarjali jih do kraljevstva Božjego.
9 A kogda něktori zatvrdili se, ibo věriti ne hotěli, zlo govorili o toj dragě Božjej prěd tolpoju, odstupivši od njih, odpravil učenikov, v každy den učil jih v školě něktorogo Tyranna.
10 A to se dějalo črěz dva lěta, tak da vsi, ktori žili v Aziji, slyšali slovo Gospodina Jezusa. Židi, tako i Greki.
11 A nemale čuda činil Bog črěz ruky Pavla;
12 Tak že horam prinosili tkaniny od těla jego, i odšli od njih hvoroby, i duhi zli izhodili iz njih.
13 Togdy něktori iz čarodějev židovskyh, ktori bavili se zaklinanjem, važili se izzvati ime Gospodina Jezusa nad tymi, ktori iměli duhy zle, govoreči: Zaklinujem vas črěz Jezusa, ktorogo Pavel pověda.
14 A bylo jih sedm synov, ovogo žida, imenem Skevas, največšego kaplana, ktori to činili.
15 Togdy odgovoril duh zly: Znam Jezusa i znam Pavla; ale vy kym jeste?
16 I kydnul se na njih človek, v ktorom byl zly duh, i sovladyval njih, posilil se protiv njimi, tako že nagi i ranjeni izběgli iz ovogo domu.
17 I bylo to vědomo vsim, i Židam i Grekam, ktori žili v Efezu; i pripadl strah na njih vsih, i bylo proslavjeno ime Gospodina Jezusa.
18 I mnogo iz tyh, ktori uvěrili, prihodili, priznali i izvěstovali svoje děla.
19 I mnogo iz tyh, ktori se nepotrěbnymi naukami bavili, iznesli knigy i spalili je prěd vsimi, a kogda izkalkulovati jih cěnu, našli petdeset tyseč dinarov.
20 Tako moguči rastlo slovo Gospodina i krěpilo se.
21 A kogda se to dokonalo, postanovil Pavel v duhu, da prěsedši Makedoniju i Ahaju, pojde do Jeruzalema, govoreči: Iže potom, kogda tam budu, trěba mně i Rim uviděti.
22 A poslavši do Makedonije dvoh iz tyh, ktori mu služili, Timoteja i Erasta, sam nemalo vrěmena ostal v Aziji.
23 A v tutom času stalo se nemalo bunt okolo Božjej dragě.
24 Ibo něktory koval zlata, imenem Demetrijus, ktory dělal srěbrne crkvi Dijany, nemalu lihvu privodil remeslnikam;
25 On sobral jih i inyh, ktori takože remeslo dělali, rěkl: Muži! Věte, da iz togo remesla mamo naše lihvy.
26 A vidite i slyšite, da ne toliko v Efezu, ale malo ne po vsej Aziji toj Pavel podgovoril i odvratil velike ljudy, govoreči: To ne sut bogi, ktori sut rukami učinjeni.
27 Ne toliko naše remeslo v legko uvažanje prijde, ale da i crkva velikoj bogyni Dijany za ničto ne bude uvažany. Prijde do pogoršenja dostojenstvo jej, ktoru vsaka Azija i ves svět hvali.
28 A slušate to i byvajuči polni gněva, kriknuli, govoreči: Velika jest Dijana Efeska!
29 I bylo polno po vsem gradu zaměšanje, i vpadli jednoglasno na teatr, odnesli Gaja i Aristarha, Makedoncev, tovariši putovanja Pavla.
30 A kogda Pavel htěl vstupiti do naroda, ne dopustili mu učeniki.
31 I něktori tož od važnějših mužev Azijskyh, byli jego prijateljami, poslavši do njego. Prosili jego, daby ne vhodil do teatra.
32 Togdy jedni tak, a drugi inače kriknuli; ibo to sobranje bylo zaměšano, a više jih ne vědělo, po čemu se sobrali.
33 A od togo sbora iztegnuli Aleksandra, kogo phnuli Židi; a Aleksander mahnuvši rukoju, htěl dati odgovor ljudam.
34 Ale kogda poznali, da byl Židom, počel se jednostajny glas od vsih. Kriknuli črěz dvě časiny: Velika jest Dijana Efeska!
35 Togdy pisatelj grada uspokajal to sobranje i rěkl: Muži Efeski! I kde jest člověk, ktori by ne znal, da grad Efesky opekaje se o crkvi velike bogyni Dijany, ktora jest dočerju Jupitera?
36 Tomu nikto se ne može protiviti. Trěba, da byste se uspokojili, a ničto naglo ne činili.
37 Ibo jeste privedli tyh mužev, ktori ne sut ni světokradcami, ni bogohulnikami vašej bogynji.
38 A jestli Demetrijus i ti, ktori s njim sut remeslnikami, imajut něčto protiv komu, byvajut prava. Sut teže načelniki grada, nehaj jedni drugyh obvinet.
39 Jestli se tož o čem inom pytajete, to se može v zakonoměrnom sobranju odpraviti.
40 Ibo trěba se bojati, da byhmo obvinjeni ne byli za narušenje prav, ibo ne jest ni jednoj pričiny, za ktoru byhmo mogli dati odgovor, da jesmo se tu sobrali. A to rěkši, razpustil to sobranje.

## Razděl 20

1 I kogdy toj bunt skončil se, Pavel sobral učenikov, dal jim kazanja i proščal se s njimi, izšel odtud, aby pošel do Makedonije.
2 A prěsedši ove kraje i napominavši učenikov širokymi slovami, prišel do Grecije.
3 A tam byvši tri měseče, kogda iměl pluti do Sirije, Židi planovali jego ubiti. Itak postanovil vratiti črěz Makedoniju.
4 I šel s njim až do Azije Sopater, Berejec, a iz Tesaloniky Aristarh i Sekund, i Gajus Derbe, i Timoteus;
5 A iz Azije Tihik i Trofim, ktori naprěd poševši, čekali nas v Troasu.
6 A po dnjah bezkyslnyh hlěbov jesmo odpluli iz Filipov i jesmo prišli do njih do Troas za pet dnev, kde my byvali sedm dnev.
7 Togda v prvi den po subotě, kogda se učeniki sobrali na lomjenju hlěba, Pavel razgovarjal s njimi, imajuči idti zautra, i prodolžal besědu až do polnoči.
8 A bylo mnogo světilnikov v ovoj komnatě, kde byli sobrani.
9 Tam seduči něktory mlady muž, imenem Eutih, na oknu, byvši težkym snom objety, kogda tako Pavel dolgo govoril, snom nadigrany padl na dol iz tretjego etažu. Kogda go vozdvignuli, byl mrtvy.
10 A Pavel izstupivši na dol, pripadl na njego, a uviděvši, rěkl: Ne bojite se; ibo v njem jest duša jego.
11 A vozošel, lomil hlěb i jel, i kazal jim dolgo až do svitanja; potom odšel.
12 I privedli ovogo mladogo muža živogo, i byli velmi radostni.
13 A my priševši naprěd do koraba, jesmo pluli do Assona, byhmo odtud vzeli Pavla; ibo tako nam kazal, ibo htěl pěše pojdti.
14 A kogda prišel do nas v Assoně, jesmo vzeli jego, jesmo prijehali do Mityleny.
15 A odtud odpluvši, drugogo dnja jesmo prišli mimo Hijosa, a tretjego dnja jesmo pripluli do Samosa, a pobyvši v Trogille, utrom jesmo prišli do Mileta.
16 Ibo Pavel htěl minuti Efes, da ne iměl by on časa tratiti v Aziji, ibo on spěšil. Jestli jemu bylo možno, da na svetočny den by byl v Jeruzalemu.
17 Togda iz Mileta poslavši do Efesa, prizval k sobě starših crkvi.
18 Kogda k njemu prišli, rěkl jim: Vy znajete od prvogo dnja, kogda jesm prišel do Aziji, kako jesm s vami po cělom času byl,
19 Služil Gospodinu s pokornostju i s mnogymi solzami i pokušenjami, ktore na mene prišli iz zasad židovskyh.
20 Kako jesm se ne hranil ničego, čto by bylo koristno, da byh vam oglasil i učil vas javno i v domah.
21 Svědočstvo davajuči i Židam, i Grekam o pokajanju k Bogu i o věrě v Gospodina našego Jezusa Hristosa.
22 A nyně ja, buduči svezany duhom, idu do Jeruzalema, ne věduči, čto tam na mene prijdti ima.
23 Toliko čto Duh Svety po městah davaje mně svědočstvo, povědajuči, da mene vezenje i trud čekajut.
24 Togo vsego ne boju se i ne domněvam žitja mojego za važno. Kogda toliko běg moj s radostju i službu slova izpolnju, ktoru jesm vzel od Gospodina Jezusa na oglašenje Evangelja milosti Božjej.
25 A nyně ja věm, že už vy vsi, s ktorymi jesm hodil kažuči kraljevstvo Božje, više ne uzrite lica mojego.
26 Ibo oglašu vam dnja dnešnjego, da jem jest čisty od krvi vsih.
27 Ibo jesm ne hranil se, daby jesm vam oglasiti cěloj rady Božjej.
28 Strěžite togdy samyh sebe i cělo stado, v ktorom vas Duh Svety postavil biskupami, da byste pasli crkvu Božju, ktorogo dobyl črěz vlastnu krov.
29 Ibo ja to věm, da po odidenju mojem prijdut medžu vas volki okrutni, ktori stado poščediti ne budut.
30 A iz vas samyh povstanut muži, govoreči věči falšive, daby tegnuli za soboju učenikov.
31 Čujte, pametajuči, da jesm črěz tri leta v noči i v dnje ne prěstaval napominati so solzami každogo iz vas.
32 A tutčas, brati! poručaju vas Bogu i slovu milosrdja jego, ktory može budovati i dati vam dětinstvo medžu vsimi posvečenymi.
33 Srěbra i zlata, ili oděž jesm ne požedal od nikogo.
34 Sami znate, da mojim potrěbam i tyh, ktori su s mnoju, služili te ruky.
35 Vsem vam jesm pokazal, da tak dělajuči, trěba pomogti slabym, a pametati slova Gospodina Jezusa, da on rěkl: Jest bolje blagoslavjano davati, než brati.
36 A to rěkši, kleknul na kolěna svoje i molil se s vsimi.
37 I stal se veliki plač u vsih, a padajuči na šiju Pavla, cělovali jego;
38 Žalujuči se silno, največšej tyh slov, ktore jim rěkl, da už ne budut viděti lica jego. I provodili jego do koraba.

## Razděl 21

1 I kogda my odjezdili i razlučili se s njimi, prosto iduči, prijezdili do Kosa, a zautra do Rodosa, a odtud do Patary.
2 I tam jesmo našli korab, ktory uměl pluti do Feničije, jesmo vstupili v njego, i izjezdili.
3 I kogda se nam ukazal Cypr, togda ostavivši jego po lěvoj straně, jesmo pluli  do Syrije i pripluli do Tyra; ibo tam imělo se tovary koraba ostaviti.
4 I našli učenikov, jesmo žili tam sedm dnev; Oni govorili Pavlu črěz duha, daby ne pošel do Jeruzalema.
5 I kogda skončili se te dni,jesmo pošli, i vsi nas provodili s ženami i s dětami až za město, i klenovši na kolěnah na brěgu, jesmo molili se.
6 I proščavši se jedin k drugomu, jesmo vstupili v korab, a oni se vratili do domov.
7 A jesmo postanovili pluti iz Tyra do Ptolemaidy, a pozdravivši bratov, jesmo žili u njih črěz jedin den.
8 A zautra izševši Pavel i my, ktori s njim byli, jesmo prišli do Cesarije, a vševši v dom Filipa Evangelista, ktory byl jedin iz tyh sedm, jesmo ostali u njego.
9 A toj iměl četyri dočery. Děvy, ktore prorokovali.
10 I kogda jesmo tam črěz nemalo dnev žili, prišel iz Judejskoj zemje prorok něktory, imenom Agabuš.
11 Toj priševši do nas i vzevši pas Pavla, i svezavši sobě ruky i nogy, rěkl: To govori Duh Svety: Muža, čijego jest toj pas, svežut v Jeruzalemu Židi i podadut jego v ruky poganam.
12 I kogda jesmo to uslyšali, jesmo prosili tyh, ktori na tom městu byli, aby on ne hodil do Jeruzalema.
13 Togda odgovoril Pavel: Čto tvorite plačuči i srdce mi kazeči? Ibo ja ne toliko gotovy svezany byti, ale i umrti jesm gotovy v Jeruzalemu za imene Gospodina Jezusa.
14 I kogda on ne dal se podgovoriti, jesmo dali pokoj, govoreči: Nehaj se stane volja Gospodina.
15 I po tyh dnjah, vzevši věči svoje, jesmo pošli do Jeruzalema.
16 I pošli s nami něktori učeniki iz Cezarije, veduči s soboju togo, u kogo jesmo iměli gostiti, někakogo Mnazona Ciprijca, starogo učenika.
17 A kogda jesmo prišli do Jeruzalema, brati nas srdečno prijeli.
18 A zautra Pavel pošel s nami do Jakoba, kde sobrali se vsi starši.
19 Jih pozdravivši, izpověděl jim vse, čto Bog učinil medžu poganami črěz službu jego.
20 Čto oni slyšavši, hvalili Gospodina i rěkli jemu: Vidiš, brate! kako jest mnogo tyseč Židov, ktori uvěrili; a vsi ti gorlivi sut za zakon.
21 Ale o tobě slušali, da odvodiš od Mojzesa vsih tyh Židov, ktori sut medžu poganami, govoreči, da ne imajut obrězati dětij, ni imajut hoditi po zakonnyh obyčajah.
22 Čto jest? Nužno jest, da se sobral narod; ibo uslyšet, da jesi prišel.
23 A itak čini to, čto ti govorimo; imajemo tu četyri mužev, ktori na sobě prisegu imajut;
24 tyh vzevši do sebe, očisti se s njimi i učini naklad na njih, da ogolet glavy; a poznajut vsi, da to, čto o tobě slyšali, falšive jest, čto ty sam  zakon držiš.
25 A o tyh, ktori uvěrili iz poganov, jesmo pisali, ustavjajuči, daby se strěgli togo, čto jest požrtvovanjem idolam i od krvi, i od dušenogo, i od bluda.
26 Togda Pavel vzevši s soboju ovyh mužev, zautra očistil se s njimi, pošel do crkvi, povědajuči izpolnjenje dnev očiščenja, kogda za každogo iz njih oddana bude žrtva.
27 A kogda imělo skončiti se sedm dnev, něktori Židi iz Azije, uviděvši jego v crkvi, vozbudili ves narod i kladli na njego ruky,
28 kriknuli: Muži Israeliski, pomožite! To jest člověk, ktory protiv narodu i zakonu, i městu tomu na cělom světu uči. navet Greki vvedl v crkvu i oskvrnil to sveto město.
29 Ibo prěd tym viděli s njim v gradu Trofima Efeskogo, o ktorom myslili, da jego Pavel vvedl v crkvu.
30 I srdil se cěly grad, i sobral se narod; a pojevši Pavla, izvlěkli jego von iz crkve, a zato zaraz dveri zamknuli.
31 A kako iskali, kako by jego ubili, pokazali hetmanu vojska, da se razčulil cěly Jeruzalem.
32 Toj tutčasno vzevši s soboju vojakov i kapitanov, priběgl k njim. A oni uzrěvši hetmana i vojakov, prěstali Pavla biti.
33 Togdy hetman približivši se, pojmal jego i kazal jego dvoma lancuhami svezati, i zapytal go, kto by to byl i čto on učinil?
34 A jedni tako, drugi inače medžu ljudami kriknuli; a kako se ničego istogo črěz golk dověděti ne mogl, razkazal jego vesti do tabora.
35 A kogda byl pri stupenišču, pridalo se, da jego vojaki nesli iz povoda naplyva nasilnogo ovogo naroda.
36 Ibo veliky narod šel za njim, kriknul: Von s njim.
37 Ibo iměli Pavla vesti do tabora, rěkl hetmanu: Či godi mi se něčto rěkti k tobě? A on rěkl: Uměješ po grečsku govoriti?
38 I ne jesi li toj Egipčanin, ktory prěd tymi dnjami učinil razdor i izvedl na pustynju četyri tyseč mužev razbojnikov?
39 A Pavel rěkl: Jesm Žid iz Tarsus, gradžan, gradžanin iz slavnogo grada v Ciliciji: zato že prošu te, dopusti mi rěkti k ljudami.
40 A kako on dopustil, Pavel stoječi na stupenišču, mahal rukoju narodu. A kako bylo veliko molčanje, učinil rěč k njim židovskym jezykom, rěkl:

## Razděl 22

1 Brati i otci! Slušajte moju obranu, ktoru ja nyně vam pověm.
2 A kogdy uslyšali, da jim govoril židovskym jezykom, tym se ješče bolje utišali. I rěkl:
3 Ja jesm muž Židom, rodženy v Tarsusě Cilickym, ale vozpitany v tom gradu pri nogah Gamalijelovyh, učeny dostatočno v zakonu otcevskom. Jesm byl gorlivy za zakon, kako vy vsi dnes jeste.
4 Jesm prěslědoval tu dragu až do smrti, vezal i prědaval do vezenja mužev i ženy,
5 Mi najvysši kaplan jest svědkom i vsi starši, od ktoryh tož jesm listy polučil, jesm jehal do Damaska do bratov, da byh tyh, ktori tam byli, svezal i privedl do Jeruzalema, daby byli karani.
6 I stalo se, kogdy jesm jehal i se približal do Damaska okolo poludnja, da naglo obsegnula mene světlo veliko s neba.
7 I jesm upadl na zemju, uslyšal glasa, ktory govoril k mně: Saule! Saule! Čemu mene prěslěduješ?
8 A ja jesm odgovoril: Kto jesi, Gospodine? I rěkl k mně: Ja jesm Jezus Nazarejsky, ktorogo ty prěslěduješ.
9 A ti, ktori byli s mnoju, viděli světlo i prěstrašili se, ale glasa ne slyšali ovogo, ktory s mnoju govoril.
10 I jesm rěkl: Čto imam učiniti, Gospodine? A Gospodin rěkl k mně: Vstani; idi do Damaska, a tam ti kažut o vsem, čto jest rěšeno, da bys ty učinil.
11 A kogdy jesm byl slěpy iz povoda jasnosti světa ovogo, ti ktori byli s mnoju, vzeli mene za ruku i tak jesm prišel do Damaska.
12 Tam někaki Ananijas, muž nabožny zakonu, imaje svědočstvo od vsih Židov tam živučih,
13 On pristupil do mene, rěkl mi: Saule brate, vidi! A jesm v tutom momentu mogl jego viděti.
14 A on rěkl: Bog otcev naših izbral tebe, da bys poznal volju jego i da bys ogledal ovogo spravědlivogo i slušal glasa iz ust jego.
15 Ibo ti budeš jego svědkom u vsih ljudij togo i jim kažeš, čto jesi viděl i slyšal.
16 Čto kolěbaš se? Vstani, i pokresti se, i izmyj grěhy tvoje, klicavši ime Gospodina.
17 I stalo se potom, kogda jesm se vratil do Jeruzalema, i molil se v crkvi, da jesm byl v zahvatu.
18 I jesm viděl jego govorečego do mene: Spěši se; i izojdi skoro iz Jeruzalema, ibo svědočstva tvojego ne prijmut o mně.
19 A jesm rěkl: Gospodine! oni vědut, da jesm ja podaval do vezenja i bil v synagogah tyh, ktori dověrjali v tebe.
20 I kogda izlivali krov Ščepana, svědka tvojego, jesm tož pri tom stal i dopustil na ubitje jego, i strěgl šaty tyh, ktori jego ubivali.
21 I rěkl do mene: Idi že, ibo tebe do poganov daleko poslju.
22 A slušali jego až do togo slova; i vozdvignuli glas svoj, govoreče: Von iz zemji s takym; ibo ne pravo, aby iměl žiti.
23 A kogda oni kričali i metali šaty i prah v vozduh,
24 Razkazal general vesti jego do lagera i kazal jego bičevati, daby se dověděl za ktory povod na njego tako kričet.
25 A kogda jego vezali, aby jego bičami bili, rěkl Pavel do generala, ktory tu stojal: Či vam se godi čelověka Rimjanina ne osudženogo bičami biti?
26 Kogdy to uslyšal hetman, pristupivši do generala, pověděl jemu, govoreči: Posmotri, čto činiš; ibo sej čelověk jest Rimjaninom.
27 A pristupivši hetman, rěkl jemu: Skaži mi, či ty jesi Rimjaninom? A on rěkl: Tako jest.
28 I odgovoril hetman: Jesm za veliku sumu to pravo gradžansko dostal. A Pavel rěkl: A jesm Rimjaninom urodil se.
29 I odstupili od njego ti, ktori jego iměli bičevati. Tož hetman se bojal, dovědavši se, da byl Rimjaninom, a jego kazal svezati.
30 A tako zautra htěl se isto dověděti togo, o čto byl obvinjeny od Židov, osvobodil jego od okovov i razkazal kaplanam i vsej radě sobrati se izvedši Pavla i postavil jego prěd njimi.

## Razděl 23

1 A Pavel gleděl na radu i rěkl: Brati! Ja v dobroj sověsti hodil prěd Bogom do togo dnja.
2 Togda Ananijas, vysši svečennik, povědal tym, ktori stojali blizko njego, biti jego po licu.
3 Togda rěkl Pavel jemu: Udari te Bog, stěno běljena! I ty sědiš, sudiš mene po zakonu, a povědaš mene biti protiv zakonu?
4 Zato ti, ktori tam stojali, rěkli: Vysšemu svečenniku Božjemu bogohuliš?
5 A Pavel rěkl: Ne jesm věděl, brati! Da on jest vysšim svečennikom; ibo jest napisano: Zastupnika naroda tvojego ne budeš rušiti.
6 A poznavši Pavel, da jedna čest iz njih byla Saducejami a druga Farizejami, kazal v toj radě: Brati! Ja jesm Farizejem, syn Farizeja: za naděju i  vozkrešenje mrtvyh tu dnes mene sudet.
7 A kogda on to govoril, počel se spor medžu Farizejami i Saducejami, i razdělila se ta tolpa.
8 Ibo Saduceji govoret, da ne jest vozkrešenja, ni Angela, ni duha; ale Farizeji to oboje iznajmut.
9 I počel se krik veliky. A povstali učitelji Pisma od strony Farizejev, sporili se, govoreči: Ničego zlogo ne jesmo našli v tom člověku; i jestli by mu to rěkl duh ili Angel, ne borimo se s Bogom.
10 A kogda se počel veliky spor, boječi se hetman, aby Pavla medžu soboju ne razdrli, pověděl idti vojinam na dol, a hvatiti jego iz srědiny jih i odvesti do lagera.
11 A v drugoj noči stanuvši pri njem Gospodin, rěkl: Budi dobrogo srdca, Pavle! Ibo kako ty o mně svědčil v Jeruzalemu, tako trěba tobě svědčiti i v Rimu.
12 A kogda byl den, sjedinivši se něktori iz Židov, prisegnuli, govoreči: Da ne imějut jesti ni piti, až by Pavla ubili.
13 A bylo jih bolje než četyrideset, ktori to prisegu učinili.
14 Ti priševši do prědnyh svečennikov i do starših, rěkli: Jesmo prisegnuli, da ničego ne sjesti I piti, až byhmo Pavla ubili.
15 Zato nyně dajte znati hetmanu s pozvoljenjem vsej rady, aby jego zautra do vas izvedl, kako byste se htěli dostatočněje dověděti o dělah jego. A my, prědže než tu prijde, jesmo gotovi jego ubiti.
16 A kogda Pavlovoho netij uslyšal o tom zamahu, prišel, i vstupivši do lagera, kazal to Pavlu.
17 Togda Pavel pozvavši jednogo iz polkovnikov, rěkl: Vedi togo mladenca do hetmana, ibo on něčto imaje povědati.
18 I tak on vzevši jego, vedl jego do hetmana i rěkl: Pavel, zaključilnik, prosil, byh ja togo mladenca privedl do tebe, ktory imaje něčto povědati.
19 Togda hetman vzevši jego za ruku i ustupivši na stranu, pytal go: Čto to jest, čto mi imaš povědati?
20 A on rěkl: Postanovili Židi prositi tebe, aby jesi zautra izvedl Pavla prěd radu, kako by oni htěli čego dostatočnějšego dovědati o njem.
21 Ale ty ne dopusti jim togo; ibo tam čekajut bolje než četyrdeset mužev, ktori prisegnuli, da ne imajut ni jesti ni piti, až by jego ubili; i sut uže v gotovosti, čekajuči od tebe odpovědi.
22 Togda hetman odpustil ovogo mladenca, prikazavši mu, aby togo prěd nikom ne pověděl, da on mu to skazal.
23 A pozvavši dvoh něktoryh iz polkovnikov, rěkl: Prigotovite dvěstě vojakov, aby šli až do Cesarije; do togo sedmdeset jezdcev i dvěstě vojakov s kopijeju na tretju časinu v noči;
24 Prigotovite tož govedo, aby vsadivši Pavla na nje, zdravo jego provedli do Feliksa naměstnika;
25 Napisavši pismo takym sposobom:
26 Klavdij Lizijas najmožnějšemu naměstniku Feliksu zdravja želaje.
27 Togo muža, zahvačanego od Židov, oni už htěli ubiti. S vojskom jesm go izbavil, dovědavši se, da jest Rimjaninom.
28 Ja htěl věděti povod, za ktory go htěli suditi, zato jesm privedl jego prěd jih radu;
29 I jesm našel, da htěli go suditi s povoda spora iz strany zakona jih, a ne s povoda někakoj viny, za ktoru on by byl godny smrti abo vezenja.
30 A ibo mi pověděno o zamahu, ktory iměli učiniti Židi na togo muža, už jesm jego poslal do tebe, povědavši tož tym, ktori žalet se na njego, aby prěd toboju govorili to, čto by protiv njemu imajut. Imaj se dobro.
31 Vojaki tako, kako jim bylo razkazano, vzevši Pavla, vedli jego nočju do Antipatrisa.
32 A na drugy den pustili jezdcev, aby s njim jehali i vratili do lagera.
33 Kogdy prijehali do Kesariji, a oddavši pismo naměstniku, postavili prěd njim Pavla.
34 A naměstnik pismo pročitavši, spytal jego, iz ktoroj by byl zemji, ibo razuměl, da byl iz Kilikiji,
35 rěkl: Budu te slušati, kogda že pribudut ti, ktori na tebe žalet se. I razkazal jego strěgti v sudu Herodesa.

## Razděl 24

1 I po peti dnjah prišel vrhovny svečennik Ananijas s staršimi i s Tertullom, někakym govoriteljem, ktori stanuli prěd naměstnikom protiv Pavlu.
2 A kogdy byl pozvany, načel na njego žalovati Tertullus, govoreči:
3 Navet my velikogo pokoja dostignuli i mnogo se dobrogo tomu narodu stalo prěz tvoju opeku, vsegda i vesde to s velikym dekovanjem priznajemo, velomožny Felikse!
4 Ale že by ja tebe dolgo ne sodržali, prošu, bys nas kratko poslušal po tvojej milosrdju.
5 Navet jesmo iznašli togo muža kako čuma i tvoritelja buntov medžu vsimi Židami po cělom sveti, i načelnika toj sekty Nazarejcev.
6 On proboval tož oskvrniti crkvu; jesmo go hvatili i po našemu zakonu htěli suditi.
7 Togdy prišel hetman Lizijas s velikoj močju, vzel jego iz ruk naših.
8 Razkazavši tym, ktori na njego žalet, idti do tebe. Od njego ty sam možeš se, dověděti vsego, za čto my jego sudimo.
9 To podkrěpili Židi, govoreči, da to tako jest.
10 Togdy Pavel odpověděl, kogdy na njego naměstnik mahnul, aby govoril: Od mnogyh lět znajuči tebe byti sudju tomu narodu, s ohotoju dam pravdu o tom, čto mene dotyče.
11 Daže ty znaješ, da ne jest bolje dnev než dvanadset, odkud ja prišel do Jeruzalema, daby ja se molil.
12 Do togo ne našli mene v crkvi s kym govorečego abo buntovavšego ljud, ni v synagogah, ni v gradu;
13 Togo ne mogut dokazati, za čto tu tutčas na mene žalet.
14 To jedino prěd toboju priznaju, da po toj naukě, ktoru oni povědajut byti heretičnoju, služu otcevskomu Bogu. Věru vse, čto napisano v zakonu i v tekstah prorokov,
15 Imajuči naděju v Bogu, da bude, na čto i oni čekajut, vozkrešenje pravednyh, i nepravednyh.
16 I sam staraju se o to spěšno, byh vsegda iměl sověst bez pogrěšky prěd Bogom i prěd ljudami.
17 A po mnogyh godah jesm prišel, byh prinesl milosti mojemu narodu i požrtvovati.
18 Pri tom našli mene v crkvi očiščenogo (ne s ljudami ni s buntom) něktori Židi iz Azije.
19 Ti iměli stati prěd toboju i žalovati se, jestli by něčto iměli protiv mene.
20 Ili nehaj ti sami povědut, jestli našli vo mně kakoju nepravost, kogda jesm stojal prěd radoju;
21 Kromě toliko jednogo glasa, da jesm medžu njimi stoječi, kazal: Za vozkrešenja mrtvyh ja dnes sudženy jesm od vas.
22 A uslyšavši to Feliks, ktory znal novu dragu dobro, pověděl: Kogda tu hetman Lizijas prijede, razsudžu vaše věči.
23 I razkazal generalu, aby strěgl Pavla i lagodno odnosil do njego. Aby ne zabranil nikomu iz jego prijateljev posluživati jemu.
24 A po několiko dnjah priježdžal Feliks s Drusilloju, ženoju svoju, ktora byla Židovkoju, kazal kazati do sebe Pavla i slušal jego o věrě v Hristosa.
25 A ibo on govoril o spravědlivosti i o čistosti i o budučem sudu, prěstrašil se Feliks i odgovoril: Už nyně odidi, a kogdy najdu čas, kažu tebe do sebe.
26 A pri tom očekyval, da mu Pavel da pěnezy, aby jego pustil; zatože tym čestěje jego kazal do sebe, razgovarjal s njim.
27 A po dvoh letah iměl po sobě Feliks naslědnika, Porcija Festa; a hčuči sobě Feliks laska iziskati u Židov, ostavil Pavla v vezenju.

## Razděl 25

1 I kogda Festus, prijel v gubernatorstvo, po treh dnjah prišel do Jeruzalema iz Cezareje.
2 I stanuli prěd njim najvysši svečenniki i glavnějši od Židov protiv Pavlu, i prosili jego,
3 daby on učinil lasku protiv njemu, daby on kazal privesti jego do Jeruzalema, učinivši atak, by jego ubili na dragě.
4 Ale Festus rěkl: „Pavel jest pod stražeju v Cezareji, a ja sam tudy skoro pojdu.“
5 „Kto iz vas jest dostatočny,“ rěkl on, „nehaj ide s nami; a jestli jest někaka vina v tom mužu, nehaj žalujut na njego.“
6 A byvavši u njih ne bolje než deseti dnev, on odjehal do Cezareje, a zautra sěděvši na tronu suda, kazal Pavla privesti.
7 I kogdy on prišel, obstupili jego ti Židi, ktori prišli iz Jeruzalema, prinesli mnogo i težkyh žalob protiv Pavlu, ktoryh dokazati ne mogli;
8 kogda on daval odgovor o sobě: „Jesm ni protiv židovskomu zakonu, ni protiv crkvi, ni protiv cěsaru ničego ne sgrěšil.“
9 Ale Festus hčuči sobě dostati lasku u Židov, odgovoril Pavlu: „Hčeš li idti do Jeruzalema, a tam o tyh věčah byti sudženy prěd mnoju?“
10 Ale Pavel rěkl: „Prěd carskym sudom stoju, kde mene suditi trěba; Židov ja v ničem ne krivdil, kako i ty bolje znaš.
11 Ibo jestli jesm v čem ne pravy i čto zasluživajuče smrti učinil, ne odkažu se umrti; ale jestli ne jest ničego takogo iz tyh věči, o ktoryh na mně se žalujut, nikto mene jim izdati ne može; apeluju do cěsara.“
12 Togdy Festus posovětovavši se s radoju, odvětoval: „Do cěsara jesi apeloval? Do cěsara pojdeš!“
13 A po několiko dnjah, kralj Agripa i Bernike prišli do Cezareje, privitati Festa.
14 A po nemalo dnjah, Festus položil prěd kralja dělo Pavla, govoreči: „Někaky muž ostavjeny jest od Feliksa v vezenju.
15 Iz povoda jego, kogda jesm byl v Jeruzalemu, stanuli prěd mnoju najvysši svečenniki i starši židovski, proseči o dekret protiv njemu.“
16 Na to jesm jim odgovoril, da ne jest obyčaj pri Rimjanah, aby kakogo člověka izdali na smrt, až obvinjeny ne iměje prěd soboju tyh, ktori na njego se žalujut, i ne bude mu dano možlivosti odgovoriti na to, v čem jego obvinjajut.
17 I tako, kogda se tu sobrali, směsta v nastupnom dnju sěděvši v sudu, jesm kazal privesti togo muža.
18 Ti protiv njego ne žalovali se nikakoj viny o njem, kak jesm očekyval.
19 Jedino někake spory o svojim zakonu iměli protiv njemu i o někakom Jezusu mrtvym, o ktorom Pavel tvrdi, da živy jest.
20 Jesm ne razuměju se na tom, o čem byl spor. Togda jesm rěkl: Či by htěl pojdti do Jeruzalema, aby tam byl sudženy?
21 No jednako Pavel apeloval, aby Avgustus o tom sudil. Jesm kazal go hraniti, až jego ne poslju do cěsara.
22 Togda Agripa rěkl Festusu: Jesm by htěl slyšati togo člověka. A on rěkl: Zautra jego uslyšiš.
23 Zautra kogda prišel Agripa i Bernike s velikoju pyšnostju, i vošli v sudny dom s vojvodami i mužaki prvymi ovogo grada, na kazanje Festusa privedli Pavla.
24 I rěkl Festus: Kralju Agripa i vsi muži, ktori jeste tu s nami! Vidite togo, o kogo mene cěly židovsky narod prosil, i v Jeruzalemu i tu. Kričeči, da ne jest pravedno, aby on dalše živy byl.
25 A ja myslim, da ne učinil ničego smrti dostojnogo. Ibo on sam apeloval k Avgustu, jesm učinil dekret, aby byl poslany.
26 Čto byh iměl cěsaru pisati, ne věm. Zato jesm kazal jego prěd vas privesti, a največšej prěd tebe, kralju Agripo! Aby jesm, po izslušanju jego věči črěz vas, by iměl, čto pisati.
27 Ibo mi se ne pravedno vidi, poslati veznja, a o čem jego obvinjajut, ne deklarovati.

## Razděl 26

1 Togda Agripa rěkl Pavlu: Dopušča se tobě, bys sam za sebe govoril. Togda Pavel, iztegnul ruku, taku obranu podal:
2 Za to vse, čim mene obvinjajut Židi, kralju Agripo! Uvažaju se byti udačlivym, da dnes imam odgovoriti prěd toboju.
3 A doskonalo jest, da ty znaješ vse obyčaje i spory, ktore sut medžu Židami; zato te molju, bys ty mene trpělivo poslušal.
4 Moje žitje od mladosti, kako bylo od načetka posrěd mojego naroda v Jeruzalemu, znajut vsi Židi,
5 buduči svědkami mojimi od davna, (jestli by svědočstvo dati hotěli), da po najstrožějšej sektě našej religije, jesm žil, buduči Farizejem.
6 A tutčas s povoda naději ovogo oběčanja Boga otcam našij, stoju prěd sudom;
7 Za ktoro dvanadset naših plemen v neustalosti dnem i nočju služili Bogu. Črěz tu naděju oni to učinili; o tu naděju žalujut se na mene Židi, o kralju Agripo!
8 Čemu do věry nepodobno sudite, da Bog mrtvyh vozkreša?
9 I tož jesm dumal, čto povinen protiv imena Jezusa Nazaretskogo mnogo falšivyh děl činiti.
10 Jesm činil to v Jeruzalemu, i mnogo jesm ja svetyh sudil do vezenja, vzevši moč od najvysših svečennikov; a kogdy iměli byti ubiti, jesm glasoval protiv njim.
11 I po vsih synagogah često jih pokaral, jesm podstrěkal jih ogovarjati, a vse bolje gorlivo jih gnati. Jesm prěslědoval jih až i do čudžih gradov.
12 Kogdy jesm do Damaska jehal, imajuči vlast i nakaz od najvysših svečennikov,
13 v poldnju, v dragě buduči, jesm viděl, o kralju! světlo iz neba, jasnějše nad jasnostju solnca, ktoro osvětilo mene i tyh, ktori jehali so mnoju.
14 A kogdy jesmo vsi upadli na zemju, jesm uslyšal glasa govoreči do mene i govoreči židovskym jezykom: Saule! Saule! Po čto jesi prěslěduješ? Trudno tobě protiv bodcev izbivati.
15 A jem rěkl: Kto jesi, Gospodine? A on rěkl: Jesm Jezus, kogo ty prěslěduješ.
16 Ale vstani i stoj na nogah tvojih; ibo jesm se tobě pokazal, da byh učinil te slugoju i svědkom tako toj věči, ktoroj jesi viděl, kako i drugyh, v ktoryh se tobě pokažu.
17 oddělju tebe od togo naroda i od poganov, do ktoryh te nyně posylaju,
18 Da bys otvoril oči jih, daby se obratili od tmy do světla, a od oblasti djabolskoj do Boga, daby tako prijeli odpuščenje grěhov i naslědstvo posrěd svetyh črěz věru v mene.
19 Zato, o kralju Agripo! Jesm byl pokorny tomu nebeskomu javjenju.
20 Ale najprvo tym, ktori sut v Damasku i v Jeruzalemu, i vo vsej zemji židovskoj, i poganam jesm povědal, daby pokajali se i obratili se do Boga, čineči děla dostojne pokajanja.
21 Za te věči Židi v crkvi mene pojmavši, htěli mene ubiti.
22 Ale za pomočju Božju ješče do dnešnjego dnja stoju, svědčeči i malomu, i velikomu, ničto ne govoreči kromě togo, čto povědali proroki i Mojzes, da se imělo stanuti;
23 To jest, da Hristos iměl stradati, a byvši prvym od vozkrešenja povědati iměl světlo narodu tomu i poganam.
24 Ibo on to v obraně svojej pověděl, rěkl Festus glasom velikym: Šalěješ, Pavle! Velika nauka privodi te do šalěnja.
25 Ale on rěkl: Ne šalěju, najsilnějši Feste! Ale istinne i zdrave slova povědaju.
26 Vědě i kralj o tyh věčah, prěd ktorym bezstrašno govorju, ibo ne myslju, daby něčto iz tyh věčij u njego bylo tajno. Ibo to se ne v kutu dělalo.
27 Věriš, kralju Agripo, prorokam? Věm, da věriš.
28 Zato Agripa rěkl do Pavla: Malo bys mene ne podgovoril, da byh stal se hristijaninom.
29 Ale Pavel rěkl: Jesm byh želal od Boga, da skoro ne toliko ty, ale i vsi, ktori mene dnes slušajut, stali se takymi, kakym i ja jesm. Volny iz tyh lancuhov.
30 A kogdy on to rěkl, vstal kralj i naměstnik, i Bernike, i ti, ktori sěděli s njim.
31 Odstupivši bokom, rěkli jedni k drugym, govoreči: „Ničto zasluživajuče smrti ili temnice ne čini toj čelověk.“
32 Agripa že rěkl Festu: „Mogl by toj člověk byti osvobodženy, daby ne apeloval cěsaru.“

## Razděl 27

1 Po tym, kogda bylo rěšeno, da imajemo pluti do Italije. Prědali Pavla i něktoryh inyh veznjev polkovniku po imenu Julius iz vojska Avgusta.
2 Togda jesmo vstupili na korab Adrumitensky, imajuči pluti podle krajin Azije. Jesmo odpluli od brěga, a s nami byl Aristarhus, Makedonec iz Salonika.
3 A drugogo dnja my pripluli do Sidona, kde Julius čestno postupal s Pavlom i dozvolil jemu pojdti k prijateljam, bys odpočel.
4 A od tam odpluvši, my jesmo pripluli pod Cypr, ibo byli větry protivni.
5 A prěpluvši ovo morje, ktoro jest podle Cilicije i Pamfilije, jesmo pribyli do Mira, grada Lystry.
6 A tam polkovnik našel korab Aleksandrijsky, ktory plul do Italije, i vsadil nas do njego.
7 A kogda jesmo črěz mnogo dnev pomalo pluli i ledva protiv Knida prijehali, nam už větr ne dopustil, my popluli pod Kreto podle Salmona.
8 A Ledva jih preminuvši, jesmo došli do gradaa něktorogo, ktorogo nazyvajut Krasnymi Portami, od ktorogo blizko byl grad Laseja.
9 A kogda čas nemaly minul i už bylo nebezpečno pluti, ibo už post prěšel, Pavel napominal jim:
10 "Muži, vidžu ja, da nebezpečnostju i s velikym poškodženjem ne toliko tovarov i korabov, ale takože duš naših ta jezda nam grozi.".
11 Jednako polkovnik boljše věril korabniku i sterovniku než tomu, čto Pavel povědal.
12 A kogda ne bylo porta sposobnogo za zimovanja, mnogo ljudij radilo odpluti odtud, aby kako mogli prěpluti do Fenicije i prězimovati v Kretskym portu, ktory leži medžu větrom južnym i zapadnym.
13 A kogda dul větr od juga, myslili, da svoje prědprijemstvo mogut dostignuti, odpluvši od brěga, pluli blizko Krety.
14 Ale ne dolgo potom udaril na njih větr silny, ktory nazyvajut Euroklidon.
15 A kogda korab byl vozneseny i ne mogl se oprěti větru, jesmo se oddali i pluli.
16 I kogda my pripluli pod někaky maly ostrov, ktory zovut Kauda, ledva jesmo mogli korab zadržati.
17 Kogdy vozdvignuli to, pomočju uživali, napinavši šnury okolo koraba, a boječi se, aby ne vpadl na hak, spustivši větrilo, tako pluli.
18 Ibo nami burja mnogo metala, zautra tovary jesmo izkydnuli.
19 A tretjego dnja rukami našimi koraby orudovanje jesmo izkydnuli.
20 Ale kogda se ni solnce, ni zvězdy črěz mnogo dnev ne ukazali, a burja nemala nalegala, na konec odjeta byla vsaka naděja, aby jesmo mogli byti prěžiti.
21 Ibo jesmo dolgo ne jedli, Pavel stoječi posrěd jih rěkl: Byste iměli uslyšati mene i ne puščati se od Krety, a tak obhoditi toj strah i škodu.
22 Ale i tutčas napominam vas, byste byli dobroj mysli; ibo ne sgne iz vas nijedna duša, kromě koraba.
23 Ibo stanul pri mně toj noči Angel Boga togo, ktorogo ja jesm i ktoromu služu;
24 Govoreči: Ne boj se, Pavle! trěba tobě stavati se prěd cěsara, a vot daroval ti Bog vsih, ktori plovut s toboju.
25 Zato budte dobroj mysli, muži! ibo věrju Bogu, da tak bude, kako mi pověděno.
26 A trěba dostavati se na někaky ostrov.
27 A kogda prišla noč četyrinadseta, a jesmo su blukali po morju Adryjatyckom, okolo polnoči stalo se morjeplavateljam, da se jim okazyvala někaka krajina.
28 Togdy spustivši šnur s olovom, našli gluboke dvadeseti nitok; a ne daleko, snova spustili olovo i našli petnadseti nitok.
29 A boječi se, byhmo na měst ostryh ne vpadli, izkydnuli četyri kotvy iz zada koraba, očekyvali, aby den byl.
30 A kogda morjeplavatelji htěli iz koraba utekti i spustili lodku na more, htěli kako se tvrdi od prěda koraba izkydnuti kotvy,
31 Rěkl Pavel polkovniku i vojinam: „Jestli se ti ne ostanut v korabu, vy ne možete byti spaseni.“
32 Togda vojini odsěkli šnury u koraba i dopustili jemu odpasti.
33 A medžu tym, poka ne nastupil den, napominal Pavel vsim, aby prijeli jedu, govoreči: „Dnes jest četyrinadseti den, kako čekajuči trvajete bez jedy, ničego ne jeduči.
34 Zato prošu vas, byste prijeli jedu; ibo to služi k vašemu spasenju i nijednomu iz vas vlas iz glavy ne opade.
35 A to revši i hlěb vzevši, podekoval Bogu prěd vsimi i slomil go i počel jesti.
36 Potom vsi, byvši lěpšego smysla, i sami krmili se.
37 A bylo nas vsih duš v korabu dvěstě sedmdeset i šest.
38 Byvši tu jedoju nasyčeni, oblegčenje činili korabu,ibo izkydnuli zrno v morje.
39 A kogda byl den, ne poznali zemji; no zauvažili brěg, k komu radili, jestli jest možlivo, pribiti korab.
40 A iztegnuvši kotvu, pustili se na morje; a razpustivši ster i vozdvignuli větrilo po větru, napravjati se do brěga;
41 Ale napadši na město, ktoro imělo iz oboju stran morje, razbil se korab; a prěd koraba zatknul i ostal se, a zad razbil se od nasilnyh valov.
42 Togda vojini radili, aby vezenjev ubili, daby nikto izplyvši ne utekl.
43 Ale polkovnik htěl hraniti Pavla, obstanovil jih od togo děla i razkazal tym, ktori mogli plavati, aby se najprvo v morje pustili i na brěg izšli;
44 Něktori na doskah, a něktori na čestah koraba. I tak se stalo, da vsi zdravo izšli na zemju.

## Razděl 28

1 Jesmo byli spaseni i poznali, da toj ostrov Maltoju nazyvajut.
2 Ale ov gruby narod pokazal nam nemalo ljudskosti; ibo zapalivše stog drěv, prijeli nas vsih radi dožda padajučego i radi zimy.
3 A kogdy Pavel nahvatal kupu hrusta i kladl na ogonj, prišla zmija iz povoda žara, pripela se k rukě jego.
4 A kogdy ov narod uzrěl ovogo gada visečego u ruky jego, govorili jedni k drugym: „Istinno toj člověk jest ubijceju; ibo črěz to,čto iz morja ušel, mu pomsta živym byti ne dopustila.“
5 No on otresavši ovogo gada v ogonj, ničego zlogo ne utrpěl.
6 A oni čekali, aby opuhnul, abo naglo upadl mrtvy; a kogdy togo dolgo čekali, a viděli, čto mu se ničego zlogo ne stalo, izměnivši se, govorili, da jest Bogom.
7 A pri ovyh městah iměl folvarky najbogatějši ovogo ostrova, imenom Publijus, ktory prijevši nas, črěz tri dni prijateljsko gostil.
8 I stalo se, da otec ovogo Publijusa, imajuči gorečku i diareju, ležal; k njemu Pavel postupil, aby moliti se, i vloživši na njego ruky uzdravil jego.
9 Kogda to se stalo, prihodili drugi, ktori byli bolězlivi na ovom ostrovu, i byli uzdravjeni;
10 ktori nam tož veliku vdečnost pokazyvali. Kogda jesmo proč pluti iměli, nakladali nam, čego bylo trěba.
11 A po treh měsecah jesmo pustili se na korabu Aleksandrijskom, ktory zimoval na ovom ostrovu, imějučim za gerb Kastora i Polluksa.
12 A pripluvši do Sirakusa, jesmo žili tam tri dni.
13 A odtud jesmo pluti kolom, jesmo pribyli do Regium, a po jednom dni, kogdy povstal větr jugovy, jesmo pluli vtorogo dnja do Puteoli.
14 Tam jesmo našli bratov. Prosili nas byti u njih, byhmo žili u njih črěz sedm dnev; a tako jesmo šli do Rima.
15 Odtud, kde uslyšali brati o nas, izšli naprotiv nas až do trga Apii i do Trěh Krčem; ktoryh kogdy Pavel jih uzrěl, podekovavši Bogu, vzel smělost.
16 A kogda jesmo prišli do Rima, polkovnik Pavlu dopustili byvati samym s vojinom, ktory jego strěže.
17 I stalo se po trěh dnjah, da kazal do sebe Pavel najbogatějših od Židov; a kogda se sjedinili, rěkl jim: Brati! ja ničego ne učinivši protiv ljudu i obyčajem otcev, byl svezany v Jeruzalemu, prědany v ruky Rimjanov;
18 Kogda izslušali mene, htěli mene izpustiti, ibo vo mně nikakoj viny godnoj smrti ne bylo.
19 No kogda se tomu protivili Židi, mně bylo trěba apelovati do cěsara; ne, da byh iměl narod moj v čem obvinjati.
20 Iz togo povoda jesm kazal vas do mene, byh se s vami viděl i razgovoril; ibo za naděju naroda Izraelskogo tu jesm v lancuhah.
21 No oni rěkli jemu: Jesmo ni pism dostali o tobě iz židovskoj zemji, ni někto od bratov prišel objaviti abo govoriti o tobě něčego zlogo.
22 A hčemo od tebe slyšati, čto dumaješ; ibo o toj sektě věmo, da vsego protiv njej ljudi govoret.
23 A postanovivši jemu den, prišlo jih jemu do kvartiry nemalo, s ktorymi s izkušenjem izkladal kraljevstvo Božje, podgovoriti jih do tyh věčij, ktore sut o Jezusu, iz zakona Mojzesa i iz prorokov, od utra až do večera.
24 Togdy něktori uvěrili tomu, čto govoril, a něktori ne uvěrili.
25 A byvši nejedinomyslnymi medžu soboju, razdělili se, kogda Pavel rěkl to jedno slovo: Dobro Duh Svety pověděl črěz Izaiasa proroka, do otcev naših,
26 Govoreči: Idi do togo naroda, a govori: Ušami slušati budete, ale ne razumějete, a očami viděti budete, ale ničego ne uzrite;
27 Ibo otvrdělo se srdce naroda togo, a težko ušami slušali i zamknuli oči svoje, aby očami ne viděli, a ušima ne slyšali, i srdcem ne razuměli, i ne odvratili se, byh jih uzdravil.
28 Nehaj že vam togdy vědomo bude, da poganam poslano jest to spasenje Božje, a oni slušati budut.
29 A kogda on to rěkl, odšli Židi, imajuči medžu soboju veliky spor.
30 I byval Pavel črěz cěle dva lěta v najemnoj kvartirě svojej, i prijmal vsih, ktori prihodili do njego;
31 Prědpovědajuči o kraljevstvu Božjem i učeči voljno tyh věčij, ktore sut o Panu Jezusu Hristosu, bez prěpon.

# Apendiks

## Rozvěnec

### Znak križa

V ime Otca i Syna i Duha Svetego. Amen.

### Apostolsko Vyznanje Věry 

Věrju v Boga Otca vsemogučego, Tvorca neba i zemje, i v Jezusa Hristosa, Syna Jego jedinogo, Gospodina našego, ktory se počel iz Duha Svetogo. Narodil se iz Marije Děvice, stradal pod Ponckym Pilatom, byl razpinan na križu, umrl i byl pogreben, stupil do pekol, tretjego dnja vozkresnul, vstupil na nebesa, sědi po pravici Boga Otca vsemogučego, odtud prijde suditi živyh i mrtvyh. 
Věrju v Duha Svetogo, svetu crkov vsesvětnu, svetyh občinu, grěhov odpuščenje, těla vozkrešenje, věčny život. Amen.

### Ave Marijo

Ave Marijo, milosti polna, Gospodin s Toboju. Blagoslavjana Ty medžu ženami i blagoslavjany plod života Tvojego, Jezus. Sveta Marijo, Mati Božja, moli se za nami grěšnymi, tutčas i v časinu smrti našej. Amen.

### Otče naš

Otče naš,
ktory jesi v nebesah,
sveti se ime Tvoje,
prijde kraljevstvo Tvoje,
bud volja Tvoja, kako v nebu, tako i na zemji.
Hlěb naš každodenny daj nam tutdenj,
i odpusti nam naše grěhy,
kako i my odpuščamo našim vinnikam.
I ne vedi nas v pokušenje,
ale nas izbavi od zlogo.
Amen.


### Slava Otcu i Synu, i Duhu Svetomu

Slava Otcu i Synu, i Duhu Svetomu, kako byla na početku, tutčas i vsegda, i na věky věkov. Amen. 


### O moj Jezuse

O moj Jezuse, odpusti nam naše grěhy, shrani nas od ognja peklnogo, provodi vse duše do neba i pomoži osoblivo tym, ktori največe trěbujut Tvojego milosrdja.

### Pod Tvoju obranu

Pod Tvoju obranu utěkajemo se, Sveta Mati Božja, našimi prosbami ne prěziraj v potrěbah naših, ale od vsakyh nebezpečnosti vsegda nas izbavjaj. Děvo slavna i blagoslavjana. O Gospodynjo naša, Zastupničko naša, Posrědničko naša, Obradovničko naša. So Synom Tvojim nas pomiri, Synu Tvojemu nas rekomenduj, Synu Tvojemu nas oddavaj. Amen.



### Tajna rozvěnca 

Ponedělok – tajna radostne 
Vtornik – tajna bolěsne 
Srěda - tajna hvalebny
Četvrtok – tajna světla
Petok - tajna  bolěsne
Subota – tajna  radostne
Nedělja - tajna hvalebne

#### Tajna radostne:

Blagověščenje Najsvetějši Mariji Gospodynji.
Navědžanje svetoj Elžběty.
Narodženje Gospodina Jezusa.
Požrtvovanje Jezusa v Svetilišču.
Najdene Jezusa v Svetilišču.


#### Tajna světla:

Kreščenje Gospodina Jezusa v Jordaně.
Projavjenje Gospodina Jezusa v Kaně Galilejskoj.
Glašenje Božjego carstva i izzvanje do obračanja.
Prěměnjenje Gospodina na gorě Tabor.
Ustanovjenje Evharistije.

#### Tajna bolěsne:

Molitva Gospodina Jezusa v Getsemanskom sadu.
Bičevanje Gospodina Jezusa.
Koronovanje trnom Gospodina Jezusa.
Krestna draga Gospodina Jezusa.
Razpinanje na križ i smrt Gospodina Jezusa.

#### Tajna hvalebne:

Vozkrešenje Gospodina Jezusa.
Voznesenje Gospodina Jezusa.
Izsylanje Duha Svetogo.
Vnebovzetje Najsvetějšej Mariji Děvy.
Koronovanje Marije na kraljevu neba i zemji.

## Korunica božjemu milosrdju 

*Na velikyh zrnah:*

Věčny Otče, žrtvujų Tobě Tělo i Kròv, Dušų i Božstvo ljubimogo Syna Tvojego, Gospodja našego, Isusa Hristosa, k izvinjenju grěhov naših i vsego světa.

*Na malyh zrnah:*

Za jego bolezno trpenje, bųdi milosrdny nam i vsemu světu.


*Konečno pętoj desętki, dodati trikråtno:*

Svęty Bože, svęty Silny, svęty i bezsmrtny, pomiluj nas i cěly svět!


*Libovoljno:* 
O, Krvi i Vodo, iztekše iz Srdca Isusa kako izvor milosrdja nam – dověrjajemo tobě.


*Libovoljno:*

Isuse, dověrjam Tobě! *x3* 

## Tebe, Bože

Tebe, Bože, hvalimo, 
Tebe, Gospodine, proslavjamo.
Tobě, Otče prědčasny,
vsa zemja čest oddava.
Tobě vsi Angeli,
Tobě nebesa i vse Moči:
Tobě Herubiny i Serafiny neprěstanno pěvajut: 
Svety, Svety, Svety, Gospodin Bog Nebesnyh Sil!
Polne sut nebesa i zemja veličstva slavy Tvojej. 
Tebe prěslavny hor Apostolov, 
Tebe Prorokov hvalebno čislo. 
Tebe hvali Mučenikov světla armija. 
Tebe po vsej zemji proslavja Crkov sveta: 
Otca bezměrny veličstva, godnogo obožanja, 
istinnogo i Jedinogo Tvojego Syna, 
Svetogo takože Duha Obradovnika. 
Ty jesi Kraljem slavy, o Hriste, 
Ty jesi Otca Synom prědčasnym. 
Ty, za spasenje našego prijevši člověčstvo, 
jesi ne kolěbal se v lože Děvy vstupiti. 
Ty, lamavši želo smrti, 
jesi otvoril věrečim kraljevstvo nebes. 
Ty po pravici Boga sědiš v Otcevskoj slavě. 
Ty prijdeš kako sudja: tak vsi věrimo. 
Umoljamo Tebe itak: 
pomoži svojim slugam, ktoryh najdražějšeju krovju jesi izkupil. 
Sčisli jih medžu svetymi Tvojih, v věčnoj slavě.
Shrani narod svoj, o Gospodine, i blagoslavjaj naslědstvo svoje. 
I vladaj njimi, i vozvyšaj jih na věky. 
Po vse dni blagoslovimo Tebe, 
i proslavjamo ime Tvoje na věky, na věky bez konca. 
Bud milostivy, Gospodine, v tutdennom dnju shranjati nas od grěha. 
Pomiluj nas, Gospodine, pomiluj nas. 
Nehaj milosrdje Tvoje, 
Gospodine, izjavi se nad nami, 
kako my v Tobě dověrjamo: 
V Tobě, o Gospodine, jesm položil naděju, ne budu sramjeny na věky.

## Jezusova molitva

Gospodine Jezuse Hriste, Syne Božji, pomiluj me grěšnogo

