var app = new Vue({
    el: '#app',
    data: {
        message: 'Press button to know how long bot work'
    },
    methods: {
        reverseMessage: function () {
              this.message = this.message.split('').reverse().join('')
          },
        getBotUpTime: function() {
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
                    app.message = xmlHttp.responseText;
            }
            xmlHttp.open("POST", "/bot_time", true); // true for asynchronous
            xmlHttp.send(null);
    }
  }
});
