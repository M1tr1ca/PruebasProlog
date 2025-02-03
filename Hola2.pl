% SISTEMA EXPERTO DE PAÍSES
% Un programa para explorar información geográfica, económica y demográfica

% Base de conocimiento de países
% Formato: pais(Nombre, Continente, Poblacion, AreaKm2, PIB, Idioma, SistemaGobierno)
pais('Espana', europa, 47615034, 505370, 1427.380, espanol, monarquiaParliamentaria).
pais('China', asia, 1439323776, 9596961, 14342.930, chino, republicaSocialista).
pais('Brasil', sudamerica, 212559417, 8515767, 1839.760, portugues, republicaFederal).
pais('Sudafrica', africa, 59308690, 1219090, 351.431, afrikaans, republicaParliamentaria).
pais('Australia', oceania, 25499884, 7741220, 1323.421, ingles, monarquiaConstitucional).
pais('India', asia, 1380004385, 3287263, 2875.142, hindi, republicaFederal).
pais('Japon', asia, 126476461, 377975, 5081.549, japones, monarquiaConstitucional).
pais('Argentina', sudamerica, 45195774, 2780400, 449.663, espanol, republicaFederal).
pais('Rumania', europa, 19286123, 238397, 250.348, rumano, republicaSemipresidencial).
pais('Francia', europa, 65273511, 551695, 2939.821, frances, republicaSemipresidencial).


% Predicados de clasificación

% Clasificar países por población
clasificarPoblacion(Pais, Categoria) :-
    pais(Pais, _, Poblacion, _, _, _, _),
    (Poblacion > 100000000 -> Categoria = 'Megapoblado'
    ; Poblacion > 50000000 -> Categoria = 'Muy Poblado'
    ; Poblacion > 20000000 -> Categoria = 'Poblado'
    ; Categoria = 'Poco Poblado').

% Clasificar países por tamaño
clasificarTerritorioNacional(Pais, Categoria) :-
    pais(Pais, _, _, Area, _, _, _),
    (Area > 8000000 -> Categoria = 'Gigante Continental'
    ; Area > 5000000 -> Categoria = 'Gran Territorio'
    ; Area > 1000000 -> Categoria = 'Pais Extenso'
    ; Categoria = 'Pais Pequeno').

% Países por continente
paisesDelContinente(Continente, ListaPaises) :-
    findall(Pais, pais(Pais, Continente, _, _, _, _, _), ListaPaises).

% Clasificar economías
clasificarEconomia(Pais, Categoria) :-
    pais(Pais, _, _, _, PIB, _, _),
    (PIB > 10000 -> Categoria = 'Economia Desarrollada'
    ; PIB > 5000 -> Categoria = 'Economia Emergente'
    ; PIB > 1000 -> Categoria = 'Economia en Desarrollo'
    ; Categoria = 'Economia Pequena').

% Calcular densidad poblacional
densidadPoblacional(Pais, Densidad) :-
    pais(Pais, _, Poblacion, Area, _, _, _),
    Densidad is Poblacion / Area.

% Listar países con un tipo de gobierno específico
paisesPorSistemaGobierno(SistemaGobierno, ListaPaises) :-
    findall(Pais, pais(Pais, _, _, _, _, _, SistemaGobierno), ListaPaises).

% Comparar países
compararPaises(Pais1, Pais2, Aspecto) :-
    pais(Pais1, _, Poblacion1, Area1, PIB1, _, _),
    pais(Pais2, _, Poblacion2, Area2, PIB2, _, _),
    (Aspecto = poblacion, Poblacion1 > Poblacion2 -> 
        format('~w tiene mayor poblacion que ~w', [Pais1, Pais2])
    ; Aspecto = area, Area1 > Area2 -> 
        format('~w tiene mayor area que ~w', [Pais1, Pais2])
    ; Aspecto = economia, PIB1 > PIB2 -> 
        format('~w tiene mayor economia que ~w', [Pais1, Pais2])
    ; format('No se puede comparar o ~w no es mayor que ~w en ~w', [Pais1, Pais2, Aspecto])).

