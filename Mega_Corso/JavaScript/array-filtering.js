/*
const pets = ['cat', 'dog', 'elephant']  
  
const filtered = pets.filter(function (pet) {  
  return (pet !== 'elephant')  
})  
questo restituirà nel console.log(pets) solo 'cat' e 'dog'   
*/


const numbers = [1,2,3,4,5,6,7,8,9,10];

const filtred = numbers.filter(function (number){return (number % 2) === 0})

console.log(filtred)
