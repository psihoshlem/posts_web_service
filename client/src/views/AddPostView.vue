<template>
    <div class="add_posts">
        <h1>Creating post</h1>
        <form @submit.prevent="submitForm">
      <div>
        <label for="input1">Title:</label>
        <input type="text" id="title" v-model="title" required>
      </div>
      <div>
        <label for="input2">Text:</label>
        <input type="text" id="text" v-model="text" required>
      </div>
      <button type="submit">Submit</button>
    </form>
    </div>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        title: "",
        text: ""
      };
    },
    methods: {
        submitForm() {
            axios.post(
                'http://0.0.0.0:8000/posts',
                {
                    title: this.title,
                    text: this.text
                }
            )
            .then(response => {
            })
            .catch(error => {
                console.error('Ошибка при получении списка постов', error);
            });
            this.title = ""
            this.text = ""
        }
    }
  };
</script>
  
<style scoped>
</style>
  