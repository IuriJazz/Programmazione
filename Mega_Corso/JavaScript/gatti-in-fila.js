//esercizio extra - gatti in fila

var gatti = 5;
var inFila = 2;

var gatti_inFila = Math.ceil(gatti / inFila);

console.log(gatti_inFila); //numero di file

gattiMancanti = gatti_inFila * inFila - gatti;

console.log(gattiMancanti); //numero di gatti mancanti per completare la fila

console.log(gatti+' Gatti sono in '+gatti_inFila+' file. Avanzano '+gattiMancanti+' gatto/i per finire la fila.');
