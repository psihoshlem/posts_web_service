<template>
    <div class="post">
      <h4>{{ post.title }}</h4>
      <p>{{ post.text }}</p>
      <p class="date">{{ post.date }}</p>
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
.post{
  background-color: #fff;
  margin: 20px;
  padding: 20px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
}
.date{
  color: rgb(161, 161, 161);
}
</style>