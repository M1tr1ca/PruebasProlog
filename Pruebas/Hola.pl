% swipl
% [Hola].
% halt.

% Definición de animales
elefante(jorge).
elefante(juan).

panda(xiaoping).

% Definición de características de animales
rayas(tigre).
rayas(cebra).

dientes_grandes(tigre).
dientes_grandes(leon).

tiene_pelaje(tigre).
tiene_pelaje(leon).

tiene_garras(tigre).
tiene_garras(leon).

tiene_dientes(tigre).
tiene_dientes(leon).

garras_afiladas(tigre).
garras_afiladas(leon).

venenoso(serpiente).

% Reglas para determinar si un animal es peligroso
peligroso(X) :- dientes_grandes(X), garras_afiladas(X).

% Reglas para determinar si un animal es un felino
esFelino(X) :- tiene_pelaje(X), tiene_garras(X), tiene_dientes(X).

% Suposiciones sobre animales basadas en características
suponga(X, tigre) :- var(X), !, fail.
suponga(X, tigre) :- rayas(X), dientes_grandes(X), esFelino(X).
suponga(X, cebra) :- var(X), !, fail.
suponga(X, cebra) :- rayas(X), esFelino(X).

% Consultas de ejemplo para probar las reglas
% ?- elefante(jorge).
% ?- peligroso(X).
% ?- esFelino(X).
% ?- suponga(X, tigre).
% ?- suponga(X, cebra).



% Definición de mamíferos
mamifero(elefante).
mamifero(xiaoping).
mamifero(tigre).
mamifero(leon).
mamifero(vaca).

% Definición de reptiles
reptil(serpiente).

% Definición de aves
ave(aguila).

% Definición de características adicionales
vuela(aguila).
vive_en_agua(delfin).
vive_en_tierra(elefante).
vive_en_tierra(tigre).
vive_en_tierra(leon).
vive_en_tierra(panda).
vive_en_tierra(serpiente).

% Reglas para determinar si un animal es un mamífero
esMamifero(X) :- mamifero(X).

% Reglas para determinar si un animal es un reptil
esReptil(X) :- reptil(X).

% Reglas para determinar si un animal es un ave
esAve(X) :- ave(X).

% Reglas para determinar si un animal es terrestre
esTerrestre(X) :- vive_en_tierra(X).

% Reglas para determinar si un animal es acuático
esAcuatico(X) :- vive_en_agua(X).

% Reglas para determinar si un animal es volador
esVolador(X) :- vuela(X).

% Consultas de ejemplo para probar las reglas
% ?- esMamifero(elefante).
% ?- esReptil(serpiente).
% ?- esAve(aguila).
% ?- esTerrestre(tigre).
% ?- esAcuatico(delfin).
% ?- esVolador(aguila).