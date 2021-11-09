<template>
  <div id="app">
    <todo-list-input @add-todo="onAddTodo"></todo-list-input>
  </div>
</template>

<script>
import TodoListInput from './components/TodoListInput.vue'

export default {
  name: 'MyTodoList',
  components: {
    TodoListInput
  },
  methods: {
    onAddTodo: function (todoData) {
      console.log(todoData)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
