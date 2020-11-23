<template>
  <div class="home">
    <div class="container mt-2">
      <div v-for="(question, questionid) in questions" :key="questionid">
        <p class="mb-0">Posted by:
          <span class="author-name">{{ question.author }}</span>
        </p>
        <h2>
          <router-link
            class="question-link"
            :to="{name: 'question', params: {slug: question.slug}}">
            {{ question.content }}
          </router-link>
        </h2>
        <p>Answers: {{ question.answers_count }}</p>
        <hr>
      </div>
      <div class="my-4">
        <p v-show="loadingQuestions">... loading... </p>
        <button v-show="next" @click="getQuestions" 
          class="btn btn-sml btn-outline-success">
          Load more
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService }  from '@/common/api.service'

export default {
  name: 'Home',
  components: {

  },
  data(){
    return {
      questions: [],
      next: null,
      loadingQuestions: false,
    }
  },
  created(){
    this.getQuestions()
    console.log(this.questions)
    document.title = 'QuestionTime'
  },
  methods: {
    getQuestions(){
      let endpoint = '/api/questions/'
      if (this.next){
        endpoint = this.next
      }
      this.loadingQuestions = true
      apiService(endpoint)
        .then(data => {
          this.questions.push(...data.results)
          if(data.next) {
            this.next = data.next
          } else{
            this.next = null
          }
          this.loadingQuestions = false
        })
    }
  },
}
</script>

<style>
.author-name{
  font-weight: bold;
  color: #DC3545;
}
.question-link{
  font-weight:bold;
  color:black;
}
.question-link:hover{
  font-weight:bold;
  color:#343A40;
  text-decoration:none;
}
</style>