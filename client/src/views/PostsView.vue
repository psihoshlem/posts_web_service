<template>
    <div class="posts">
        <h1>All posts by this moment</h1>
        <div v-for="post in posts" :key="post.id">
            <post :post="post" />
        </div>
    </div>
</template>
  
<script>
  import Post from "../components/Post.vue";
  import axios from 'axios';
  
  export default {
    components: {
      Post
    },
    data() {
      return {
        posts: []
      };
    },
    created() {
      this.fetchPosts();
    },
    methods: {
      fetchPosts() {
        axios.get('http://0.0.0.0:8000/posts')
          .then(response => {
            this.posts = response.data;
          })
          .catch(error => {
            console.error('Ошибка при получении списка постов', error);
          });
      }
    }
  };
</script>
  
<style scoped>
</style>
  