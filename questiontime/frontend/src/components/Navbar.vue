<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link
        class="navbar-brand"
        :to="{name: 'Home'}">
        QuestionTime 
      </router-link>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <a class="nav-link" href="#">
              <router-link
                class="btn btn-sml btn-success"
                :to="{name: 'Home'}">
                Home
              </router-link>
              <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item mx-1">
            <a class="nav-link" href="#">
              <router-link
                class="btn btn-sml btn-danger"
                :to="{name: 'question-editor'}">
                Add Question 
              </router-link>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/accounts/logout/">
              <a class="btn btn-sml btn-outline-secondary">Logout</a>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>


<script>
import { apiService } from '@/common/api.service'

export default {
  name: "Navbar"
};
</script>


<style>
.my-navbar{
  border-bottom: 1px solid#DDD;
}
.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}
.navbar-brand:hover {
  color: #DC3545 !important;
}
</style>