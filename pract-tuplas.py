
hechos = {
    #ontologia de grupos
    ("mamifero", "es_un", "grupo"),
    ("ave", "es_un", "grupo"),
    ("carnivoro", "es_un", "subgrupo"),
    ("ungulado", "es_un", "subgrupo"),
    ("rumiante", "es_un", "subgrupo"),

    #ontologia de animales
    ("guepardo", "es_un", "animal"),
    ("tigre", "es_un", "animal"),
    ("jirafa", "es_un", "animal"),
    ("cebra", "es_un", "animal"),
    ("pinguino", "es_un", "animal"),
    ("albatro", "es_un", "animal"),
    ("delfin", "es_un", "animal"),
    ("tiburon", "es_un", "animal"),
    ("vaca", "es_un", "animal"),

    #pertenencia de animales a grupos
    ("guepardo", "pertenece_a", "carnivoro"),
    ("tigre", "pertenece_a", "carnivoro"),
    ("jirafa", "pertenece_a", "rumiante"),
    ("cebra", "pertenece_a", "rumiante"),
    ("pinguino", "pertenece_a", "ave"),
    ("albatro", "pertenece_a", "ave"),
    ("delfin", "pertenece_a", "mamifero"),
    ("tiburon", "pertenece_a", "mamifero"),
    ("vaca", "pertenece_a", "rumiante"),

    # caracteristicas de cada animal
    ("guepardo", "tiene_caracteristica", "color leonado"),
    ("guepardo", "tiene_caracteristica", "manchas oscuras"),    
    ("tigre", "tiene_caracteristica", "color leonado"),
    ("tigre", "tiene_caracteristica", "rayas negras"),
    ("jirafa", "tiene_caracteristica", "cuello largo"),
    ("jirafa", "tiene_caracteristica", "manchas oscuras"),
    ("cebra", "tiene_caracteristica", "rayas negras"),
    ("pinguino", "tiene_caracteristica", "nada"), #nada de la accion de nadar
    ("pinguino", "tiene_caracteristica", "blanco y negro"),
    ("albatro", "tiene_caracteristica", "vuela muy bien"),
    ("delfin", "tiene_caracteristica", "acuatico"),
    ("delfin", "tiene_caracteristica", "respira por espiraculo"),
    ("delfin", "tiene_caracteristica", "cola horizontal"),
    ("tiburon", "tiene_caracteristica", "tiene branquias"),
    ("tiburon", "tiene_caracteristica", "cola vertical"),
    ("vaca", "tiene_caracteristica", "hembra"),
    ("vaca", "tiene_caracteristica", "tiene ubres"),
    ("vaca", "tiene_caracteristica", "da leche"),

    }
