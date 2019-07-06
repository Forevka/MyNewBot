<template>
  <div class="login">
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
      desccription: 'It will open dialog to login :D',
      approve_code: ''
    }
  },
  methods: {
    login_user: function () {
      AxiosInstance.post('/login_user')
        .then(response => window.open(response.data.url, '_blank'))
    },
    approve_user: function (user) {
      var headers = {
        'Content-Type': 'application/json',
        'auth-token': typeof localStorage.token === 'undefined' ? '' : localStorage.token
      }
      AxiosInstance.post('/approve_user', user, {headers: headers})
        .then(response => {
          if (response.data.status === 'ok') {
            localStorage.token = response.data.token
            this.$router.push('admin')
          } else {
            this.show_notify()
          }
        })
    },
    user_loged: function (user) {
      console.log(user)
      this.approve_user(user)
    },
    show_notify: function () {
      this.$notify({
        type: 'warn',
        group: 'foo',
        title: 'Can`t login',
        text: 'Something went wrong, you cant login. Try again or wait'
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
a {
  color: #42b983;
}
.login {
margin: auto;
}
</style>
