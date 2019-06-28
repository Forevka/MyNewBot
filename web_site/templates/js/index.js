var app = new Vue({
    el: '#app',
    data: {
        tokenHover: true,
        uptime: 'Press button to know how long bot work',
        worktime: 'Press button to know how long bot work',
        botToken: 'Press button to know how long bot work',
        _botToken: ''
    },
    mounted: function() {this.getBotStats();},
    methods: {
        reverseMessage: function () {
              this.message = this.message.split('').reverse().join('')
          },
        getBotStats: function() {
            axios.post("/bot_stats").then(response => (this.parseStats(response.data)));
        },
        parseStats: function(stats){
            this.uptime = stats.when_start
            this.worktime = stats.up_time
            this._botToken = stats.token
            this.botToken = this._botToken.substring(0, 30) + "*".repeat(15)
        },
        showToken: function(){
            this.botToken = this._botToken
        },
        hoverToken: function(){
            this.botToken = this._botToken.substring(0, 30) + "*".repeat(15)
        }
  }
});
