#Arturo Estrada Dominguez (23760315) 7SE

#predicados de la ontologia
predicados = {
    ("TienePelo", "pelo", "x tiene pelaje"),
    ("DaLeche", "leche", "x da leche a sus crias"),
    ("ColorLeonado", "leonado", "x tiene color leonado"),
    ("TieneManchas", "manchas", "x tiene manchas oscuras"),
    ("TieneRayas", "rayas", "x tiene rayas negras"),
    ("CuelloLargo", "cuello largo", "x posee un cuello largo"),
    ("Nada", "natacion", "x puede nadar"),
    ("Blanco y negro", "blancoNegro", "x es de color blanco y negro"),
    ("VuelaMuyBien", "vuela bien", "x tiene buena habilidad para volar"),
    ("EsAcuatico", "acuatico", "x habita en el agua"),
    ("RespiraPorEspiraculo", "espiraculo", "x respira por un espiraculo"),
    ("ColaHorizontal", "c_horizontal", "x tiene una cola horizontal"),
    ("TieneBranquias", "branquias", "x respira mediante branquias"),
    ("ColaVertical", "c_vertical", "x tiene una cola vertical"),
    ("EsHembra", "hembra", "x es de sexo femenino"),
    ("TieneUbres", "ubres", "x posee ubres"),
    ("DaLecheComercial", "leche_comercial", "x produce leche para consumo comercial")
}

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
    ("vaca", "pertenece_a", "rumiante"),

    # caracteristicas de cada animal
    ("guepardo", "tiene_caracteristica", "leonado"),
    ("guepardo", "tiene_caracteristica", "manchas"),    
    ("tigre", "tiene_caracteristica", "leonado"),
    ("tigre", "tiene_caracteristica", "rayas"),
    ("jirafa", "tiene_caracteristica", "cuello largo"),
    ("jirafa", "tiene_caracteristica", "manchas"),
    ("cebra", "tiene_caracteristica", "rayas"),
    ("pinguino", "tiene_caracteristica", "natacion"), 
    ("pinguino", "tiene_caracteristica", "blancoNegro"),
    ("albatro", "tiene_caracteristica", "vuela bien"),
    ("delfin", "tiene_caracteristica", "acuatico"),
    ("delfin", "tiene_caracteristica", "espiraculo"),
    ("delfin", "tiene_caracteristica", "c_horizontal"),
    ("tiburon", "tiene_caracteristica", "tiene branquias"),
    ("tiburon", "tiene_caracteristica", "c_vertical"),
    ("vaca", "tiene_caracteristica", "hembra"),
    ("vaca", "tiene_caracteristica", "ubres"),
    ("vaca", "tiene_caracteristica", "leche_comercial"),

    #vinculos de las entrevistas
    ("delfin", "confunde_con", "tiburon"),
    ("vaca", "confunde_con", "toro"),
    ("vaca", "confunde_con", "bisonte"),
    }

#consulta de hechos que utiliza una tupla (sujeto, predicado, objeto) con valores none como
# comodin para cualquier valor 
def consultar_animal(s=None, p=None, o=None):
    return [(a, b, c) for (a, b, c) in hechos 
            if s in (None, a) 
            and p in (None, b)
            and o in (None, c)]

#se busca la traduccion descriptiva dentro de la estructura de predicados para un predicado dado
def obtener_traduccion(valor_caracteristica):
    for nombre, valor, traduccion in predicados:
        if valor == valor_caracteristica:
            return traduccion
    return "x tiene esta caracteristica"

#se extrae x si cumple la condicion
#ejemplo de reglas para inferir hechos a partir de los hechos existentes
 
animales_validos = {x for (x, r, y) in hechos if r == "es_un" and y == "animal"}
grupo_animal = {(x, y) for (x, r, y) in hechos if r == "pertenece_a"}
caracteristicas_animales = {(x, y) for (x, r, y) in hechos if r == "tiene_caracteristica"}

# prueba
if __name__ == "__main__":
    animal_consulta = "vaca"

    #pregunta si el animal es valido
    print(f"'{animal_consulta}' es un animal valido?: {animal_consulta in animales_validos}")

    #consulta los grupos
    grupos = [y for (x, y) in grupo_animal if x == animal_consulta]
    print(f"grupo al que pertenece '{animal_consulta}': {grupos}")

    #extrae las caracteristicas del animal
    print(f"caracteristicas de '{animal_consulta}':")
    caracteristicas = [y for (x, y) in caracteristicas_animales if x == animal_consulta]
    for c in caracteristicas:
        traduccion = obtener_traduccion(c).replace("x", animal_consulta.capitalize())
        print(f"- {traduccion}")