graph TD
    %% Leyenda integrada dentro del diagrama
    subgraph Leyenda [Cómo leerlo]
        L1[Caja oscura: Clase]:::concepto
        L2([Ovalo punteado: Instancia]):::instancia
        L3[Caja clara: Propiedad]:::prop
    end

    %% Definición de estilos basados en la imagen proporcionada
    classDef concepto fill:#1e463a,stroke:#1e463a,stroke-width:2px,color:#ffffff,rx:5px,ry:5px;
    classDef instancia fill:#ffffff,stroke:#3b7a57,stroke-width:2px,stroke-dasharray: 5 5,color:#1e463a;
    classDef prop fill:#f7f9f8,stroke:#a3b8ad,stroke-width:1px,color:#333333;

    %% Grupos y Subgrupos (Clases - Cajas oscuras)
    G_Mamifero[Grupo: Mamífero]:::concepto
    G_Ave[Grupo: Ave]:::concepto
    
    S_Carnivoro[Subgrupo: Carnívoro]:::concepto
    S_Ungulado[Subgrupo: Ungulado]:::concepto
    S_Rumiante[Subgrupo: Rumiante]:::concepto

    %% Jerarquía de Grupos (es_un - Flechas sólidas)
    S_Carnivoro -->|es_un| G_Mamifero
    S_Ungulado -->|es_un| G_Mamifero
    S_Rumiante -->|es_un| S_Ungulado

    %% Animales (Instancias - Óvalos punteados)
    A_Guepardo([Guepardo]):::instancia
    A_Tigre([Tigre]):::instancia
    A_Jirafa([Jirafa]):::instancia
    A_Cebra([Cebra]):::instancia
    A_Pinguino([Pingüino]):::instancia
    A_Albatro([Albatro]):::instancia
    A_Delfin([Delfín]):::instancia
    A_Tiburon([Tiburón]):::instancia
    A_Vaca([Vaca]):::instancia

    %% Relaciones: Pertenencia a grupos (pertenece_a - Flechas punteadas)
    A_Guepardo -.->|pertenece_a| S_Carnivoro
    A_Tigre -.->|pertenece_a| S_Carnivoro
    
    A_Jirafa -.->|pertenece_a| S_Rumiante
    A_Cebra -.->|pertenece_a| S_Rumiante
    A_Vaca -.->|pertenece_a| S_Rumiante
    
    A_Pinguino -.->|pertenece_a| G_Ave
    A_Albatro -.->|pertenece_a| G_Ave
    
    A_Delfin -.->|pertenece_a| G_Mamifero
    A_Tiburon -.->|pertenece_a| G_Mamifero

    %% Relaciones: Características (tiene_caracteristica)
    A_Guepardo -.->|tiene| C_ColorLeonado[color leonado]:::prop
    A_Tigre -.->|tiene| C_ColorLeonado
    
    A_Guepardo -.->|tiene| C_ManchasOsc[manchas oscuras]:::prop
    A_Jirafa -.->|tiene| C_ManchasOsc
    
    A_Tigre -.->|tiene| C_RayasNegras[rayas negras]:::prop
    A_Cebra -.->|tiene| C_RayasNegras
    
    A_Jirafa -.->|tiene| C_CuelloLargo[cuello largo]:::prop
    
    A_Pinguino -.->|tiene| C_Nada[nada]:::prop
    A_Pinguino -.->|tiene| C_BlancoNegro[blanco y negro]:::prop
    
    A_Albatro -.->|tiene| C_VuelaBien[vuela muy bien]:::prop
    
    A_Delfin -.->|tiene| C_Acuatico[acuatico]:::prop
    A_Delfin -.->|tiene| C_Espiraculo[respira por espiraculo]:::prop
    A_Delfin -.->|tiene| C_ColaHoriz[cola horizontal]:::prop
    
    A_Tiburon -.->|tiene| C_Branquias[tiene branquias]:::prop
    A_Tiburon -.->|tiene| C_ColaVert[cola vertical]:::prop
    
    A_Vaca -.->|tiene| C_Hembra[hembra]:::prop
    A_Vaca -.->|tiene| C_Ubres[tiene ubres]:::prop
    A_Vaca -.->|tiene| C_DaLeche[da leche]:::prop