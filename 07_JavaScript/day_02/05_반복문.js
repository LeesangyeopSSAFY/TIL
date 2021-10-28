const numbers = [1, 2, 3, 4, 5]

for (let number of numbers) {
  console.log(number)
}

const person = {
  name: 'Bob',
  age: '77'
}
for (const key in person){
  console.log(key, person[key])
}