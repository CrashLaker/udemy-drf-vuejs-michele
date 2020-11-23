<template>
  <div id="app">
    <NavbarComponent/>
    <router-view/>
  </div>
</template>


<script>
import { apiService } from '@/common/api.service'
import NavbarComponent from '@/components/Navbar'

export default {
  name: 'App',
  components: {
    NavbarComponent
  },
  created(){
    this.setUserInfo()
  },
  methods: {
    async setUserInfo(){
      const data = await apiService('/api/user/')
      const requestUser = data['username']
      window.localStorage.setItem('username', requestUser)
    }
  },
}
</script>

<style>
html, body {
  height:100%;
  font-family: "Playfair Display", serif;
}
</style>
