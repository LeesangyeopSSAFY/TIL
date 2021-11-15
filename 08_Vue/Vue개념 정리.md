### Node.js

- JavaScript Runtime Environment
- JavaScript를 브라우저 밖에서 실행할 수 있는 새로운 환경



### Babel

- JavaScript complier
- 자바스크립트의 코드를 이전 버전으로 번역/변환해 주는 도구



### Webpack

- Static module bundler
- 모듈 간의 의존성 문제를 해결하기 위한 도구



### Pass Props & Emit Events

- 부모는 자식에게 데이터를 전달하며, 자식은 자신에게 일어난 일을 부모에게 알림
- 부모는 props를 통해 자식에게 데이터를 전달, 자식은 events를 통해 부모에게 메시지를 보냄
- 모든 props는 하위 속성과 상위 속성 사이의 단방향 바인딩을 형성
- 부모의 속성이 변경되면 자식 속성에게 전달되지만, 반대 방향으로는 안 됨 => 자식 요소가 의도치 않게 부모 요소의 상태를 변경하여 앱의 데이터 흐름을 이해하기 어렵게 만드는 일을 방지한다.
- 부모 컴포넌트는 자식 컴포넌트가 사용되는 템플릿에서 v-on을 사용하여 자식 컴포넌트가 보낸 이벤트를 청취

