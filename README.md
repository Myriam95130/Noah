# Noah : Comparateur phonologique arabe/hébreu

## Pourquoi Noah ? 

L'outil Noah est nommé en référence au personnage biblique Noé, dont le fils Sem est considéré comme l'ancêtre éponyme des peuples sémitiques, parmi lesquels les Arabes et les Hébreux, dont les langues sont au cœur de cet outil.

Noah est un outil de linguistique computationnelle comparée pour l'analyse des distances
phonologiques entre l'arabe et l'hébreu, deux langues sémitiques partageant
un système de racines trilitères commun.

## Motivation

L'arabe et l'hébreu sont deux langues sœurs issues du proto-sémitique. Elles
partagent un vaste vocabulaire commun, des racines trilitères simialaires
et une morphologie similaire. Pourtant, des siècles d'évolution
séparée ont introduit des divergences phonologiques systématiques et des
glissements sémantiques.

Noah est un outil pour **quantifier et visualiser** ces correspondances et
divergences de façon computationnelle.

## Fonctionnalités prévues

- **Dictionnaires phonologiques** --> alphabet arabe et alphabet hébreu
  entièrement transcrits en IPA
- **Table de correspondances** --> correspondances phonétiques régulières
  arabe/hébreu issues de la linguistique historique comparée
- **Calculateur de distance phonologique** --> mesure de proximité entre
  deux racines basée sur les phonèmes IPA
- **Comparateur de racines** --> alignement lettre par lettre avec score
  de similarité
- **Lexique comparatif** --> base de données de paires arabe/hébreu annotées
  avec racine, schème, catégorie, traductions

## Correspondances phonétiques régulières arabe vs hébreu moderne

| Arabe | Hébreu | IPA arabe | IPA hébreu | Exemple |
|-------|--------|-----------|------------|---------|
| ث | ש | /θ/ | /ʃ/ | ثلاثة / שלוש |
| ق | ק | /q/ | /k/ | قدم / קדם |
| ع | ע | /ʕ/ | /ʕ/ | عين / עין |
| ح | ח | /ħ/ | /ħ/ | حياة / חיים |
| ذ | ז | /ð/ | /z/ | ذهب / זהב |
| ض | צ | /dˤ/ | /ts/ | أرض / ארץ |
| غ | ע | /ɣ/ | /ʕ/ | — |
| و | ו | /w/ | /v/ | — |



## Concepts linguistiques clés

**Racine trilitères** : En arabe et en hébreu, les mots sont formés
à partir de triplés ordonnés consonnatiques, autrement dit, des racines de trois consonnes (parfois même quatre) à laquelle
on applique un motif vocalique. Ex : k-t-b --> كتب (arabe) / כתב (hébreu)
= écrire.

**Correspondances phonétiques régulières** : En linguistique historique,
les changements phonétiques sont systématiques. Une lettre arabe correspond
souvent à une lettre hébraïque similaire d'un point de vu articulatoire dans les mots apparentés. 
Ces correspondances sont des lois intrinsèques à la grammaire comparée sémitique.

**Distance phonologique** : mesure de similarité entre deux sons basée
sur leurs traits articulatoires (lieu d'articulation, mode d'articulation,
voisement). Deux sons identiques = distance 0.

## Pistes de développement

- [ ] Calcul de distance de Levenshtein phonologique sur les racines
- [ ] Visualisation des correspondances sous forme de graphe
- [ ] Extension à d'autres langues sémitiques (amharique, assyrien, araméen, maltais, arabe chypriote)
- [ ] Interface web interactive

## Créateur
*Myriam Ben Hadj Sghaier — M1 TAL, INALCO / Sorbonne Nouvelle / Paris Nanterre (2025/2026)*
