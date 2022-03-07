
```js
$.ajax({
  url: "http://127.0.0.1:5000/project/Test%20Project/user/newuser01",
  async: true,
    method:'POST',
  success: function(data) {
    console.log(data);
  },
  error: function(e) {alert(e);}   
});
```