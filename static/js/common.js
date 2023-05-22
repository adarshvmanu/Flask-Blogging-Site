const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".search-box"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");

toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
})

searchBtn.addEventListener("click" , () =>{
    sidebar.classList.remove("close");
})

modeSwitch.addEventListener("click" , () =>{
    const wasDarkMode = localStorage.getItem('dark')==='true';
    localStorage.setItem('dark', !wasDarkMode);
    body.classList.toggle("dark", !wasDarkMode);
    if(body.classList.contains("dark")){
        modeText.innerText = "Dark mode"; 
    }else{
        modeText.innerText = "Light mode"; 
    }
});

function onload(){
    body.classList.toggle("dark", localStorage.getItem('dark')==='true');
}