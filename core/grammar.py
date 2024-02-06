TERMINALS = """
Det -> "el" | "los" | "la" | "una" | "las"
Ns -> "sol" | "pájaros" | "maria" | "playa" | "padres" | "tren" | "gato"
Ns -> "hermana" | "profesor" | "estrellas"
V -> "brilla" | "cantan" | "estudia" | "es" | "cocinaron" | "llegó" | "juega"
V -> "toca" | "explicó" | "brillan"
P -> "en" | "para" | "a" | "con" | "de"
Nc -> "cielo" | "árboles" | "universidad" | "lugar" | "estación" | "tiempo"
Nc -> "cena" | "anoche" | "estación" | "tiempo" | "bola" | "lana" | "suelo"
Nc -> "piano" | "manera" | "lección" | "cielo"
Cn -> "azul" | "nocturno"
Cd -> "matemáticas"
Pp -> "mi" | "mis"
Mod -> "favorito" | "mayor" | "increible"
Vnp -> "relajarme"
Adj -> "deliciosa" | "justo"
Ct -> "anoche"
Co -> "claridad" | "clase"
"""

NON_TERMINALS = """
F -> S V C

S -> Det Ns | Ns | Pp Ns | Pp Ns Mod

C -> CL | Cd CL | CS CL | CD CT | CL CT | CM CL | CV CM | CD CMO CL

CL -> P Det Nc Cn | P Det Nc | P Vnp | P Co

CS -> Pp Nc Mod

CD -> Det Adj Nc | Det Nc

CT -> Adj P Nc | Ct

CM -> P Det Nc CN | P Nc Mod

CN -> P Nc

CV -> Det Nc

CMO -> P Co
"""