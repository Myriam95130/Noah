from phonemes import arabe, hebreu_biblique, hebreu_moderne, traits_phonemes

def distance_phonemes(p1, p2):
    """
    Calcule la distance phonologique entre deux phonèmes.
    p1, p2 : chaînes IPA ex: '/b/', '/p/'
    Retourne : nombre de traits différents (entre 0 et 7)
    """

    vecteur1 = traits_phonemes[p1]
    vecteur2 = traits_phonemes[p2]
    compteur = 0
    for t1, t2 in zip(vecteur1, vecteur2):
        if t1 != t2:
            compteur += 1
    return compteur 
    
def dst_racines_hst(r_arabe, r_hebreu): # calcule la distance historique entre deux racines 
    """
    Distance historique entre deux racines.
    Pour chaque paire de lettres alignées :
    - côté arabe : arabe[lettre][1] → correspondant historique hébreu
    - côté hébreu : hébreu[lettre] → phonème hébreu actuel
    """

    distance_historique = 0
    phonemes_ar = []
    phonemes_hbw = []
    for lettre_ar, lettre_hbw in zip(r_arabe, r_hebreu):
            # <---- on récupère les phonèmes ---->
            phonemes_ar.append(arabe[lettre_ar][1]) # index à 1 car dans le dico arabe chaque valeur 
                                                    # = un tuple de deux phonèmes // Ici on récupère le correspondant hébreu historique
            phonemes_hbw.append(hebreu_biblique[lettre_hbw]) 

    for p_ar, p_hbw in zip(phonemes_ar, phonemes_hbw): # on boucle sur les phonèmes récupérés
        distance_historique += distance_phonemes(p_ar, p_hbw) # on incrémente en appelant la fonction 
                                                        #précédente sur nos deux phonèmes
    return distance_historique

def dst_racines_sync(r_arabe, r_hebreu): # calcule la distance synchronique entre racines
    """
    Distance synchronique entre deux racines.
    Compare les phonèmes actuels des deux langues.
    """
    phonemes_ar = []
    phonemes_hbw = []
    distance_synchronique = 0
    for lettre_ar, lettre_hbw in zip(r_arabe, r_hebreu):
        phonemes_ar.append(arabe[lettre_ar][0])
        phonemes_hbw.append(hebreu_moderne[lettre_hbw])
    for p_ar, p_hbw in zip(phonemes_ar, phonemes_hbw):
        distance_synchronique += distance_phonemes(p_ar, p_hbw)
    return distance_synchronique

print(dst_racines_sync('قلب', 'קלב'))   # /q/ vs /k/
print(dst_racines_hst('قلب', 'קלב'))   # /q/ vs /k/

print(dst_racines_sync('حكم', 'חכם'))   # /ħ/ vs /χ/
print(dst_racines_hst('حكم', 'חכם'))   # /ħ/ vs /χ/

print(dst_racines_sync('غرب', 'ערב'))   # /ɣ/ vs /ʕ/
print(dst_racines_hst('غرب', 'ערב'))   # /ɣ/ vs /ʕ/

print(arabe['ق'])           # tuple arabe
print(hebreu_biblique['ק']) # phonème biblique