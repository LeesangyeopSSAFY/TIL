/*
식별자 규칙
1. 반드시 문자, $, _로 시작한다. (숫자로 시작x)
2. 대소문자를 구분
3. 예약어 사용불가

식별자 작성 스타일

camelCase : 변수, 상수, 함수명

PascalCase : 클래스, 생성자

UPPER_SNAKE_CASE : 상수(절대로 변하면 안되는 값)



*/

// let => 재할당 가능, 재선언 불가능
let x = 1

x = 2

// let x = 3 => 이건 안 돼

// const => 재할당 불가능, 재선언 불가능
const y = 1

y = 2 // 이거 안 돼

const y = 2 // 얘도 안 돼

// 블록 스코프 중괄호
const greeting = 'hi'

if (true) {
  console.log(greeting)
  let name = 'Bob'
}

console.log(name)  //블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

// var : 재할당, 재선언 모두 가능, 호이스팅, 함수스코프

var z = 1

z = 10

var z = 11 // 이건 된다.

// 호이스팅 : 호이스팅되면 밑에 작성되있더라도 올라가서 읽어버린다.
console.log(username) // 이렇게 해도 에러는 안 난다.
var username = 'Bob'
// -----------------------------
// 자바스크립트가 인식하는 코드
var username
console.log(username) // undefined (undefined가 뜨는 이유는 그냥 선언만 해놨기 때문에)
username = 'Bob'
console.log(username) // Bob

// let과 const 둘 다 마찬가지 에러
console.log(age)
let age = 99 // 이건 let이라 호이스팅이 안 된다. 그래서 에러가 발생