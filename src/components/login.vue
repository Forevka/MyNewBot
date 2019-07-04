<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>{{ desccription }}</h2>
    <fish-form inline>
      <fish-field>
        <vue-telegram-login
        mode="callback"
        telegram-login="winprizebot"
        @callback="user_loged" />
      </fish-field>
    </fish-form>
  </div>
</template>

<script>
import AxiosInstance from '../api-comunicate'
import {vueTelegramLogin} from 'vue-telegram-login'

export default {
  name: 'login',
  components: {vueTelegramLogin},
  data () {
    return {
      msg: 'Login Page',
      desccription: 'It will open dialog with bot in telegram app',
      approve_code: ''
    }
  },
  beforeMount () {
    this.is_login()
  },
  methods: {
    login_user: function () {
      AxiosInstance.post('/login_user')
        .then(response => window.open(response.data.url, '_blank'))
    },
    approve_user: function (code) {
      AxiosInstance.post('/approve_user')
        .then(response => console.log(response))
    },
    is_login: function () {
      console.log(this.$route.query)
    },
    user_loged: function (user) {
      console.log(user)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
