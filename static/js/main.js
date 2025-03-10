/*** DASHBOARD VERTICAL TABS  ***/

//var tab_btns = document.getElementsByClassName('tab-btn');

// Object.keys(tab_btns).forEach(key => {
//     let btn = tab_btns[key]
//     console.log(btn.innerHTML)
// })

let tab_btns = document.querySelectorAll(".tab-btn");
let tab_pane = document.querySelectorAll(".tab-pane");

tab_btns.forEach((btn) => {
  btn.addEventListener("click", () => {
    tab_btns.forEach((x) => x.classList.remove("vertical-tab-active"));
    tab_pane.forEach((pane) => pane.classList.remove("pane-active"));
    btn.classList.add("vertical-tab-active");

    let targetTab = btn.getAttribute("data-tab");
    document.getElementById(targetTab).classList.add("pane-active");
  });
});

// horizontal tabs
// TASKS TABLES

let tasks_tab_btns = document.querySelectorAll(".tasks-tab-btn");
let tasks_tab_pane = document.querySelectorAll(".tasks-tab-content");

tasks_tab_btns.forEach((tab, index) => {
  tab.addEventListener("click", () => {
    tasks_tab_btns.forEach((t_tab) => {
      t_tab.classList.remove("horizontal-tab-active");
    }); // removing the active classs
    tab.classList.add("horizontal-tab-active"); // adding active class when btn is clicked

    tasks_tab_pane.forEach((content) => {
      content.classList.remove("horizontal-pane-active");
    });
    tasks_tab_pane[index].classList.add("horizontal-pane-active");
  });
});

//USERS TABS
let user_tab_btns = document.querySelectorAll(".users-tab-btn");
let user_tab_content = document.querySelectorAll(".user-content");

user_tab_btns.forEach((tab, index) => {
  tab.addEventListener("click", () => {
    user_tab_btns.forEach((user_tab) => {
      user_tab.classList.remove("users-tab-active");
    });
    tab.classList.add("users-tab-active");

    user_tab_content.forEach((content) => {
      content.classList.remove("user-content-active");
    });
    user_tab_content[index].classList.add("user-content-active");
  });
});

///// MOUSE OVER FUCTIONALITY
function mouseOver() {
  document.querySelector(".profile-box").style.display = "block";
}

function mouseOut() {
  document.querySelector(".profile-box").style.display = "none";
}
