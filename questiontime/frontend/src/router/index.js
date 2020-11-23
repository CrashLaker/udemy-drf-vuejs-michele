import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Question from '../views/Question.vue'
import QuestionEditor from '../views/QuestionEditor.vue'
import AnswerEditor from '../views/AnswerEditor.vue'
import NotFound from '../views/NotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/question/:slug',
    name: 'question',
    component: Question,
    props: true
  },
  {
    path: '/ask/:slug?',
    name: 'question-editor',
    component: QuestionEditor,
    props: true
  },
  {
    path: '/answer/:id',
    name: 'answer-editor',
    component: AnswerEditor,
    props: true,
  },
  {
    path: '*',
    name: 'page-not-found',
    component: NotFound
  }
]

console.log(process.env.BASE_URL)

const router = new VueRouter({
  mode: 'history',
  //base: process.env.BASE_URL,
  base: '',
  routes
})

export default router
