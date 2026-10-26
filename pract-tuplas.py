#Arturo Estrada Dominguez (23760315) 7SE
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

#consulta de hechos que utiliza una tupla (sujeto, predicado, objeto) con valores none como
# comodin para cualquier valor 
def consultar_animal(s=None, p=None, o=None):
    return [(a, b, c) for (a, b, c) in hechos 
            if s in (None, a) 
            and p in (None, b)
            and o in (None, c)]

#se extrae x si cumple la condicion, infiriendo su clasificacion
#ejemplo de reglas 
#regla 1: si tiene pelo entonces es un mamifero 
mamiferos_con_pelo = {x for (x, r, y) in hechos if r == "tiene_caracteristica" and y == "tiene pelo"}

#regla 2: si da leche entonces es un mamifero
mamiferos_por_leche = {x for (x, r, y) in hechos if r == "tiene_caracteristica" and y == "da leche"}

#regla 3: si tiene plumas entonces es un ave
aves_con_plumas = {x for (x, r, y) in hechos if r == "tiene_caracteristica" and y == "tiene plumas"}

# prueba
if __name__ == "__main__":
    animal_consulta = "vaca"

#se verifica si el animal cumple con alguna de las reglas para inferir su clasificacion
    es_mamifero = (animal_consulta in mamiferos_con_pelo) or (animal_consulta in mamiferos_por_leche)
    es_ave = (animal_consulta in aves_con_plumas)

    print(f"resultado de la consulta para el animal '{animal_consulta}':")
    print(f"  es un mamifero?: {es_mamifero}")
    print(f"  es un ave?: {es_ave}")