// const passwordInput = document.querySelector(".pass");
// const passwordInput = document.querySelector("#pwd1");
// const passwordInput2 =document.querySelector("#pwd2");
var x = document.getElementById("pwd1");
var y = document.getElementById("pwd2");
const eye = document.querySelector("#eye");
const eye2=document.querySelector("#eye2");
  eye.addEventListener("click", function(){
      this.classList.toggle("fa-eye-slash");
      if (x.type === "password") {
        x.type = "text";
      } else {
        x.type = "password";
      }
    })

  eye2.addEventListener("click", function(){
    this.classList.toggle("fa-eye-slash");
    if (y.type === "password") {
      y.type = "text";
    } else {
      y.type = "password";
    }
  })


