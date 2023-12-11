/*404 - не найдено:( 
    
---\ Свитчер для тем*/
const toggle = document.getElementById("toggle");
const theme = window.localStorage.getItem("theme");

if (theme === "dark") document.body.classList.add("dark");

toggle.addEventListener("click", () => {
   document.body.classList.toggle("dark");
   if (theme === "dark") {
     window.localStorage.setItem("theme", "light");
   } else window.localStorage.setItem("theme", "dark");
});

function chatsf() {
    window.location.href = 'chats.html';
}

function myprojectsf() {
    window.location.href = 'myprojects.html';
}

function supportf() {
    window.location.href = 'support.html';
}


