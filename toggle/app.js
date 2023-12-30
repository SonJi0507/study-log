const h1 = document.querySelector("div.hello:first-child h1")

function handleTitleClick() {
    // toggle 사용 전
    // const clickedClass = "clicked";
    // if (h1.classList.contains(clickedClass)) {
    //     h1.classList.remove(clickedClass);
    // } else {
    //     h1.classList.add(clickedClass);
    // }
    // toggle 사용
    h1.classList.toggle( "clicked");

}

h1.addEventListener("click", handleTitleClick);