% Definición de categorías de animales
mamifero(elefante).
mamifero(leon).
mamifero(delfin).
mamifero(tigre).
mamifero(perro).
mamifero(vaca).
mamifero(gato).


ave(aguila).
ave(paloma).
ave(pinguino).

reptil(cocodrilo).
reptil(serpiente).
reptil(tortuga).

pez(salmon).
pez(tiburon).
pez(dorado).

/* guapo(elefante).
guapo(leon).
guapo(delfin).
guapo(tigre).
guapo(perro).
guapo(vaca).
guapo(gato).
guapo(aguila).
guapo(paloma).
guapo(pinguino).
guapo(cocodrilo).
guapo(serpiente).
guapo(tortuga). */

% Reglas generales
es_mamifero(X) :- mamifero(X).
es_ave(X) :- ave(X).
es_reptil(X) :- reptil(X).
es_pez(X) :- pez(X).
/* es_gaupo(X) :- guapo(X). */