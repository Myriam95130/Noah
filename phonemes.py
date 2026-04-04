arabe = {'ا': ('/aː/', '/aː/'),    # alif — voyelle longue
    'ب': ('/b/', '/b/'),
    'ت': ('/t/', '/t/'),
    'ث': ('/θ/', '/ʃ/'),      # arabe : th, hébreu : sh
    'ج': ('/dʒ/', '/g/'),     # arabe : dj, hébreu : g
    'ح': ('/ħ/', '/ħ/'),
    'خ': ('/x/', '/x/'),
    'د': ('/d/', '/d/'),
    'ذ': ('/ð/', '/z/'),      # arabe : dh, hébreu : z
    'ر': ('/r/', '/r/'),
    'ز': ('/z/', '/z/'),
    'س': ('/s/', '/s/'),      # attention : pas /ʃ/ en hébreu moderne
    'ش': ('/ʃ/', '/ʃ/'),
    'ص': ('/sˤ/', '/ts/'),    # emphatique arabe --> tsadé hébreu
    'ض': ('/dˤ/', '/ts/'),
    'ط': ('/tˤ/', '/t/'),     # emphatique arabe --> t hébreu
    'ظ': ('/ðˤ/', '/ts/'),
    'ع': ('/ʕ/', '/ʕ/'),
    'غ': ('/ɣ/', '/ʕ/'),      # arabe : gh, hébreu : ayin
    'ف': ('/f/', '/f/'),
    'ق': ('/q/', '/q/'),      # arabe : qaf, hébreu : kaf
    'ك': ('/k/', '/k/'),
    'ل': ('/l/', '/l/'),
    'م': ('/m/', '/m/'),
    'ن': ('/n/', '/n/'),
    'ه': ('/h/', '/h/'),
    'و': ('/w/', '/v/'),      # arabe : w, hébreu : v (hébreu moderne)
    'ي': ('/j/', '/j/'),
    'ء': ('/ʔ/', '/ʔ/'),      # hamza / alef
    'ة': ('/a/', '/—/'),      # tāʾ marbūṭa
}

hebreu_moderne = {'א': '/ʔ/',      # alef — occlusive glottale
    'ב': '/b/',      # bet (avec dagesh) / '/v/' (sans dagesh)
    'ג': '/g/',      # gimel
    'ד': '/d/',      # dalet
    'ה': '/h/',      # he
    'ו': '/v/',      # vav (hébreu moderne)
    'ז': '/z/',      # zayin
    'ח': '/χ/',      # het — fricative vélaire (≈ /ħ/ en hébreu biblique)
    'ט': '/t/',      # tet
    'י': '/j/',      # yod
    'כ': '/k/',      # kaf (avec dagesh) / '/x/' (sans dagesh)
    'ך': '/x/',      # kaf final
    'ל': '/l/',      # lamed
    'מ': '/m/',      # mem
    'ם': '/m/',      # mem final
    'נ': '/n/',      # nun
    'ן': '/n/',      # nun final
    'ס': '/s/',      # samekh
    'ע': '/ʕ/',      # ayin (hébreu biblique) / '/∅/' (hébreu moderne)
    'פ': '/p/',      # pe (avec dagesh) / '/f/' (sans dagesh)
    'ף': '/f/',      # pe final
    'צ': '/ts/',     # tsadi
    'ץ': '/ts/',     # tsadi final
    'ק': '/k/',      # qof
    'ר': '/r/',      # resh
    'ש': '/ʃ/',      # shin / '/s/' (sin)
    'ת': '/t/',      # tav (hébreu moderne) / '/θ/' (hébreu biblique)
}

hebreu_biblique = {'א': '/ʔ/',      # alef — occlusive glottale
    'ב': '/b/',      # bet (avec dagesh) / '/β/' (sans dagesh)
    'ג': '/g/',      # guimel (avec dagesh) / '/ɣ/' (sans dagesh)
    'ד': '/d/',      # dalet (avec dagesh) / '/ð/' (sans dagesh)
    'ה': '/h/',      # he
    'ו': '/w/',      # vav semi-consonne (pas /v/ comme en moderne)
    'ז': '/z/',      # zayin
    'ח': '/ħ/',      # het : fricative pharyngale sourde (pas /χ/ comme en moderne)
    'ט': '/tˤ/',     # tet : occlusive emphatique
    'י': '/j/',      # yod
    'כ': '/k/',      # kaf (avec dagesh) / '/x/' (sans dagesh)
    'ך': '/x/',      # kaf final
    'ל': '/l/',      # lamed
    'מ': '/m/',      # mem
    'ם': '/m/',      # mem final
    'נ': '/n/',      # nun
    'ן': '/n/',      # nun final
    'ס': '/s/',      # samekh
    'ע': '/ʕ/',      # ayin : fricative pharyngale voisée (prononcé en biblique)
    'פ': '/p/',      # pe (avec dagesh) / '/f/' (sans dagesh)
    'ף': '/f/',      # pe final
    'צ': '/tsˤ/',    # tsadi : affriquée emphatique
    'ץ': '/tsˤ/',    # tsadi final
    'ק': '/q/',      # qof : occlusive uvulaire (pas /k/ comme en moderne)
    'ר': '/r/',      # resh
    'ש': '/ʃ/',      # shin / '/s/' (sin)
    'ת': '/θ/',      # tav (avec dagesh /t/) / '/θ/' (sans dagesh) — th en biblique
}

traits_phonemes = {
    #              voisé  labial  coronal  dorsal  pharyngal  nasal  continu  uvulaire  emphatique
    '/b/':        [  1,     1,      0,       0,       0,        0,      0,      0,        0   ],
    '/g/':        [  1,     0,      0,       1,       0,        0,      0,      0,        0   ],
    '/d/':        [  1,     0,      1,       0,       0,        0,      0,      0,        0   ],
    '/h/':        [  0,     0,      0,       0,       1,        0,      1,      0,        0   ],
    '/v/':        [  1,     1,      0,       0,       0,        0,      1,      0,        0   ],
    '/z/':        [  1,     0,      1,       0,       0,        0,      1,      0,        0   ],
    '/ħ/':        [  0,     0,      0,       0,       1,        0,      1,      0,        0   ],
    '/tˤ/':       [  0,     0,      1,       0,       0,        0,      0,      0,        1   ],
    '/k/':        [  0,     0,      0,       1,       0,        0,      0,      0,        0   ],
    '/q/':        [  0,     0,      0,       1,       0,        0,      0,      1,        0   ],
    '/l/':        [  1,     0,      1,       0,       0,        0,      1,      0,        0   ],
    '/m/':        [  1,     1,      0,       0,       0,        1,      0,      0,        0   ],
    '/n/':        [  1,     0,      1,       0,       0,        1,      0,      0,        0   ],
    '/s/':        [  0,     0,      1,       0,       0,        0,      1,      0,        0   ],
    '/ʕ/':        [  1,     0,      0,       0,       1,        0,      1,      0,        0   ],
    '/p/':        [  0,     1,      0,       0,       0,        0,      0,      0,        0   ],
    '/f/':        [  0,     1,      0,       0,       0,        0,      1,      0,        0   ],
    '/dˤ/':       [  1,     0,      1,       0,       0,        0,      0,      0,        1   ],
    '/r/':        [  1,     0,      1,       0,       0,        0,      1,      0,        0   ],
    '/ʃ/':        [  0,     0,      1,       0,       0,        0,      1,      0,        0   ],
    '/t/':        [  0,     0,      1,       0,       0,        0,      0,      0,        0   ],
    '/θ/':        [  0,     0,      1,       0,       0,        0,      1,      0,        0   ],
    '/ð/':        [  1,     0,      1,       0,       0,        0,      1,      0,        0   ],
    '/ðˤ/':       [  1,     0,      1,       0,       0,        0,      1,      0,        1   ],
    '/sˤ/':       [  0,     0,      1,       0,       0,        0,      1,      0,        1   ],
    '/x/':        [  0,     0,      0,       1,       0,        0,      1,      0,        0   ],
    '/χ/':        [  0,     0,      0,       1,       0,        0,      1,      0,        0   ],
    '/ɣ/':        [  1,     0,      0,       1,       0,        0,      1,      0,        0   ],
    '/ʔ/':        [  0,     0,      0,       0,       1,        0,      0,      0,        0   ],
    '/ts/':       [  0,     0,      1,       0,       0,        0,      0,      0,        0   ],
    '/tsˤ/':      [  0,     0,      1,       0,       0,        0,      0,      0,        1   ],
    '/dʒ/':       [  1,     0,      1,       0,       0,        0,      0,      0,        0   ],
    '/ʒ/':        [  1,     0,      1,       0,       0,        0,      1,      0,        0   ],
    '/j/':        [  1,     0,      1,       0,       0,        0,      1,      0,        0   ],
    '/w/':        [  1,     1,      0,       0,       0,        0,      1,      0,        0   ],
}