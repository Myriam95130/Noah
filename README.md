# Samedi 4 avril 2026

## Journal de bord 

L'arabe et l'hébreu sont deux langues sœurs issues du proto-sémitique. Elles partagent un système de racines trilitère commun et une morphologie similaire. Des siècles d'évolution séparée ont introduit des divergences phonologiques. Noah est un outil pour **quantifier** ces correspondances et divergences de façon computationnelle.

## Étape 1 — Les dictionnaires phonologiques

### Décision
Créer trois dictionnaires de base :
- `arabe` : alphabet arabe avec tuples `(phonème arabe actuel, correspondant proto-sémitique hébreu)`
- `hébreu_biblique` : alphabet hébreu avec phonèmes IPA de l'hébreu ancien (aussi dit biblique)
- `hébreu_moderne` : alphabet hébreu avec phonèmes IPA de l'hébreu contemporain

### Pourquoi des tuples dans `arabe` ?
Chaque entrée du dict `arabe` est un tuple de deux phonèmes :
```python
'ث': ('/θ/', '/θ/'),  # (phonème arabe actuel, correspondant proto-sémitique)
'ق': ('/q/', '/q/'),
'و': ('/w/', '/w/'),
```
Ce choix encode directement la **correspondance historique**. Il est important de prendre en compte le fait que la trace écrite des sons primaires est préservée dans les graphèmes même lorsque les phonèmes ont divergé. 

Par exemple `ث` arabe `/θ/` correspond à `ש` hébreu `/ʃ/` : deux réalisations différentes du même son sémitique.

### Pourquoi deux dictionnaires hébreu ?

L'hébreu biblique et l'hébreu moderne présentent des divergences importantes :

| Lettre | Biblique | Moderne |
|--------|----------|---------|
| `ו` | `/w/` | `/v/` |
| `ח` | `/ħ/` | `/χ/` |
| `ע` | `/ʕ/` | `/∅/` (muet) |
| `ק` | `/q/` | `/k/` |
| `ת` | `/θ/` | `/t/` |

Ces deux dictionnaires permettent de calculer deux types de distances différentes permettant ainsi, deux analyses : l'une historique, l'autre synchronique.

## Étape 2 : Les vecteurs de traits distinctifs

### Problème initial

Pour calculer une distance phonologique, comparer les phonèmes IPA comme des chaînes de caractères ne suffit pas : `/q/` et `/k/` seraient à distance maximale alors qu'ils sont très proches articulatoirement.

### Solution : vecteurs de traits binaires

Inspiration de Chomsky & Halle : chaque phonème est représenté par un vecteur binaire de traits articulatoires :

```python
#              voisé  labial  coronal  dorsal  pharyngal  nasal  continu  uvulaire  emphatique
'/b/':        [  1,     1,      0,       0,       0,        0,      0,      0,        0   ],
'/q/':        [  0,     0,      0,       1,       0,        0,      0,      1,        0   ],
'/k/':        [  0,     0,      0,       1,       0,        0,      0,      0,        0   ],
```

### Traits retenus (9)

| Trait | Description |
|-------|-------------|
| `voisé` | cordes vocales vibrent |
| `labial` | lèvres impliquées |
| `coronal` | pointe de langue |
| `dorsal` | dos de langue |
| `pharyngal` | pharynx impliqué |
| `nasal` | passage nasal ouvert |
| `continu` | flux d'air continu (fricatives) |
| `uvulaire` | articulation uvulaire |
| `emphatique` | consonnes emphatiques sémitiques |

### Problème rencontré : `/q/` vs `/k/` indistinguables

Avec 7 traits initiaux, `/q/` et `/k/` avaient le même vecteur --> distance 0.

**Solution** : ajout du trait `uvulaire` (8ème) puis `emphatique` (9ème) pour distinguer les consonnes sémitiques spécifiques qui présentent des caractéristiques articulatoires similaires entre elles.

## Étape 3 : La fonction `distance_phonemes`

### Code
```python
def distance_phonemes(p1, p2):
    """
    Calcule la distance phonologique entre deux phonèmes.
    p1, p2 : chaînes IPA ex: '/b/', '/q/'
    Retourne : nombre de traits différents (entre 0 et 9)
    """
    vecteur1 = traits_phonemes[p1]
    vecteur2 = traits_phonemes[p2]
    compteur = 0
    for t1, t2 in zip(vecteur1, vecteur2):
        if t1 != t2:
            compteur += 1
    return compteur
```

### Tests validés

```
distance_phonemes('/b/', '/p/') --> 1  (juste le voisement) OK
distance_phonemes('/b/', '/m/') --> 1  (juste le nasal) OK
distance_phonemes('/b/', '/s/') --> 4  (voisement, labial, coronal, continu) OK
```

## Étape 4 : Les fonctions de distance entre racines

### Deux types de distances

**Distance historique** : compare le correspondant historique encodé dans le tuple arabe `[1]` avec le phonème hébreu biblique. 
--> Mesure si la correspondance est **régulière** ou **irrégulière**.

**Distance synchronique** : compare le phonème arabe actuel `[0]` avec le phonème hébreu moderne. Mesure l'**écart phonologique actuel** entre les deux langues.

### Code
```python
def dst_racines_hst(r_arabe, r_hebreu):
    """Distance historique — correspondances proto-sémitiques."""
    phonemes_ar = []
    phonemes_hbw = []
    distance_historique = 0
    for lettre_ar, lettre_hbw in zip(r_arabe, r_hebreu):
        phonemes_ar.append(arabe[lettre_ar][1])       # correspondant historique
        phonemes_hbw.append(hébreu_biblique[lettre_hbw])
    for p_ar, p_hbw in zip(phonemes_ar, phonemes_hbw):
        distance_historique += distance_phonemes(p_ar, p_hbw)
    return distance_historique // (len(r_arabe)    # normalisé entre 0 et 1

def dst_racines_sync(r_arabe, r_hebreu):
    """Distance synchronique — phonèmes actuels."""
    phonemes_ar = []
    phonemes_hbw = []
    distance_synchronique = 0
    for lettre_ar, lettre_hbw in zip(r_arabe, r_hebreu):
        phonemes_ar.append(arabe[lettre_ar][0])        # phonème arabe actuel
        phonemes_hbw.append(hébreu_moderne[lettre_hbw])
    for p_ar, p_hbw in zip(phonemes_ar, phonemes_hbw):
        distance_synchronique += distance_phonemes(p_ar, p_hbw)
    return distance_synchronique // len(r_arabe)
```

### Problème rencontré : tuple mal encodé pour `ق`
`arabe['ق']` était `('/q/', '/k/')` --> le correspondant historique hébreu était `/k/` (hébreu moderne) au lieu de `/q/` (hébreu biblique). Distance historique = 1 au lieu de 0.

**Solution** : corriger le tuple --> `('/q/', '/q/')`.

### Résultats validés
| Paire | Distance sync | Distance hst | Interprétation |
|-------|--------------|--------------|----------------|
| `قلب` / `קלב` | 1/9 | 0 | cognate, divergence moderne sur `/q/`→`/k/` |
| `حكم` / `חכם` | 2/9 | 0 | cognate, divergence sur `/ħ/`→`/χ/` |
| `غرب` / `ערב` | 2/9 | 0 | cognate, divergence sur `/ɣ/`→`/ʕ/` |
| `كتب` / `שלם` | 6/9 | — | racines sans lien |


## Étape 5 : Séparation en deux fichiers

### Décision
Séparer les données du code :
- `phonemes.py` --> tous les dictionnaires (`arabe`, `hébreu_biblique`, `hébreu_moderne`, `traits_phonemes`)
- `comparateur.py` --> toutes les fonctions, importe les données depuis `phonemes.py`

```python
from phonemes import arabe, hébreu_biblique, hébreu_moderne, traits_phonemes
```

### Avantage

Plus lisible et facilite l'extension future : ajouter l'araméen, l'assyrien, l'amharique ne touche que `phonemes.py`.

## Feuille de route

### Court terme
- [ ] Ajouter un lexique de paires arabe/hébreu annotées
- [ ] Tester sur un plus grand nombre de racines
- [ ] Gérer les racines de longueurs différentes (alignement)

### Moyen terme
- [ ] Visualisation des correspondances sous forme de graphe
- [ ] Interface en ligne de commande interactive
- [ ] Export des résultats en TSV

### Long terme
- [ ] Extension à l'araméen, l'assyrien, l'amharique
- [ ] Comparaison automatique avec un lexique proto-sémitique reconstruit
- [ ] Interface web interactive

## Créateur
Myriam Ben Hadj Sghaier — M1 TAL, INALCO / Sorbonne Nouvelle / Paris Nanterre

