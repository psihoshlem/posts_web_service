<template>
  <div class="post">
    <div class="viewing" v-if="!edit_state">
      <h4>{{ title }}</h4>
      <p>{{ text }}</p>
      <p class="date">{{ date }}</p>
      <div class="tools">
        <button @click="toggle_state">Edit</button>
        <button @click="delete_post">Delete</button>
      </div>
    </div>
    <div class="editing" v-else>
        <input type="text" id="title" v-model="new_title" required>
        <input type="text" id="text" v-model="new_text" required>
      <p class="date">{{ date }}</p>
      <div class="tools">
        <button @click="toggle_state">Cancel</button>
        <button @click="submit">Submit</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    post: Object
  },
  data(){
    return {
      id: null,
      title: null,
      text: null,
      date: null,
      edit_state: false,
      new_title: null,
      new_text: null
    }
  },
  created(){
    this.id = this.post.id
    this.title = this.post.title
    this.text = this.post.text
    this.date = this.post.date
  },
  methods: {
    delete_post(){
      axios.delete(
        'http://0.0.0.0:8000/posts/'+this.id
      )
      .catch(error => {
        console.error('Ошибка при удалении', error);
      });
    },
    toggle_state(){
      this.new_title = this.title
      this.new_text = this.text 
      this.edit_state = !this.edit_state
    },
    submit(){
      axios.put(
        'http://0.0.0.0:8000/posts/'+this.id,
        {
          title: this.new_title,
          text: this.new_text
        }
      )
      .then(response => {
        this.title = this.new_title
        this.text = this.new_text 
        this.toggle_state()
      })
      .catch(error => {
        console.error('Ошибка при обновлении', error);
      });
    }
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