const clock = document.querySelector("h2#clock");

function getClock(){
    const date = new Date();
    const hours = date.getHours().toString().padStart(2,"0")
    const minutes = String(date.getMinutes()).padStart(2,"0")
    const seconds = String(date.getSeconds()).padStart(2,"0")
    clock.innerText = `${hours}:${minutes}:${seconds}`;
}
// 열자마자 바로 Clock 시작 될 수 있도록
getClock();
setInterval(getClock, 1000);