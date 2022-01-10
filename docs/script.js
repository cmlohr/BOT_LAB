
// Burger menu
function toggleMobileNavState() {
    const a = document.querySelector("body");
    a.classList.toggle("nav--active");
  }
  function initBurger() {
    const a = document.querySelector(".burger");
    a.addEventListener("click", toggleMobileNavState);
  }
  initBurger();
  

  // Secret message
  window.onload = function message() {
  console.info("Hey there! ʕ•́ᴥ•̀ʔっ"),
    console.info("Got a cool project you want to chat about?  Maybe something else?"),
    console.info("Ping me on Twitter! @cmlohr"),
    console.info("Mail me @ hello@cmlohr.dev"),
    console.info("Check out my frontend stuff on CodePen! https://codepen.io/cmlohr"),
    console.info("Slide over to my GitHub for everything else!  https://github.com/cmlohr")
  console.info("(✿◠‿◠) Thanks for stopping by!");
  }
