<template>
  <div class="admin">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
import AxiosInstance from '../api-comunicate'

export default {
  name: 'admin',
  data () {
    return {
      msg: 'this will be admin page'
    }
  },
  mounted () {
    this.is_login()
  },
  methods: {
    is_login: function () {
      var headers = {
        'Content-Type': 'application/json',
        'auth-token': typeof localStorage.token === 'undefined' ? '' : localStorage.token
      }
      AxiosInstance.post('/admin/ping', {}, {headers: headers})
        .then(response => {
          if (response.data.status === 'unautheticated user') {
            console.log(response.data)
            localStorage.token = ''
            this.$router.push('login')
            this.show_logout_notify()
          }
        })
    },
    show_logout_notify: function () {
      this.$notify({
        type: 'warn',
        group: 'foo',
        title: 'Logout',
        text: 'Logout'
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
