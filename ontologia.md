graph TD
    %% Definición de estilos
    classDef concepto fill:#1e463a,stroke:#1e463a,stroke-width:2px,color:#ffffff,rx:5px,ry:5px;
    classDef instancia fill:#ffffff,stroke:#3b7a57,stroke-width:2px,stroke-dasharray: 5 5,color:#1e463a;
    classDef prop fill:#f7f9f8,stroke:#a3b8ad,stroke-width:1px,color:#333333;

    %% Grupos y Subgrupos
    G_Mamifero[Grupo: Mamífero]:::concepto
    G_Ave[Grupo: Ave]:::concepto
    
    S_Carnivoro[Subgrupo: Carnívoro]:::concepto
    S_Ungulado[Subgrupo: Ungulado]:::concepto
    S_Rumiante[Subgrupo: Rumiante]:::concepto

    %% Jerarquía de Grupos (es_un)
    S_Carnivoro -->|es_un| G_Mamifero
    S_Ungulado -->|es_un| G_Mamifero
    S_Rumiante -->|es_un| S_Ungulado

    %% Animales (Instancias)
    A_Guepardo([Guepardo]):::instancia
    A_Tigre([Tigre]):::instancia
    A_Jirafa([Jirafa]):::instancia
    A_Cebra([Cebra]):::instancia
    A_Pinguino([Pingüino]):::instancia
    A_Albatro([Albatro]):::instancia
    A_Delfin([Delfín]):::instancia
    A_Tiburon([Tiburón]):::instancia
    A_Vaca([Vaca]):::instancia
    A_Toro([Toro]):::instancia
    A_Bisonte([Bisonte]):::instancia

    %% Pertenencia a grupos (pertenece_a)
    A_Guepardo -.->|pertenece_a| S_Carnivoro
    A_Tigre -.->|pertenece_a| S_Carnivoro
    
    A_Jirafa -.->|pertenece_a| S_Rumiante
    A_Cebra -.->|pertenece_a| S_Rumiante
    A_Vaca -.->|pertenece_a| S_Rumiante
    
    A_Pinguino -.->|pertenece_a| G_Ave
    A_Albatro -.->|pertenece_a| G_Ave
    
    A_Delfin -.->|pertenece_a| G_Mamifero

    %% Relaciones: Características (tiene_caracteristica)
    A_Guepardo -.->|tiene| C_Leonado[leonado]:::prop
    A_Tigre -.->|tiene| C_Leonado
    
    A_Guepardo -.->|tiene| C_Manchas[manchas]:::prop
    A_Jirafa -.->|tiene| C_Manchas
    
    A_Tigre -.->|tiene| C_Rayas[rayas]:::prop
    A_Cebra -.->|tiene| C_Rayas
    
    A_Jirafa -.->|tiene| C_Cuello[cuello largo]:::prop
    
    A_Pinguino -.->|tiene| C_Natacion[natacion]:::prop
    A_Pinguino -.->|tiene| C_BlancoNegro[blancoNegro]:::prop
    
    A_Albatro -.->|tiene| C_VuelaBien[vuela bien]:::prop
    
    A_Delfin -.->|tiene| C_Acuatico[acuatico]:::prop
    A_Delfin -.->|tiene| C_Espiraculo[espiraculo]:::prop
    A_Delfin -.->|tiene| C_CHorizontal[c_horizontal]:::prop
    
    A_Tiburon -.->|tiene| C_Branquias[tiene branquias]:::prop
    A_Tiburon -.->|tiene| C_CVertical[c_vertical]:::prop
    
    A_Vaca -.->|tiene| C_Hembra[hembra]:::prop
    A_Vaca -.->|tiene| C_Ubres[ubres]:::prop
    A_Vaca -.->|tiene| C_LecheComercial[leche_comercial]:::prop

    %% Relaciones: Vínculos de las entrevistas (confunde_con)
    A_Delfin -.->|confunde_con| A_Tiburon
    A_Vaca -.->|confunde_con| A_Toro
    A_Vaca -.->|confunde_con| A_Bisonte