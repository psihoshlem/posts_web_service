<template>
    <div class="post">
      <h4>{{ post.title }}</h4>
      <p>{{ post.text }}</p>
      <p>Дата: {{ post.date }}</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      post: Object
    }
  };
  </script>
  
  <style scoped>
  </style>