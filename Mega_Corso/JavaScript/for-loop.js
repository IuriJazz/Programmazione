/*
for (let i = 0; i < 10; i++) {  
  // log the numbers 0 through 9  
  console.log(i)  
}  

i = 0; --> l'inizio del loop

i < 10; --> condizione per verificare se il loop è in condizione vera (quindi eseguito)
oppure se è una condizione falsa (quindi viene interrotto il loop). In questo caso
verifica che i sia minore di 10.

i++ --> incrementa i di 1 ogni volta che viene eseguito il loop

*/

var total = 0;
var limit = 10;

for (let i = total; i < limit; i++)
    { total += i };
console.log(total);
