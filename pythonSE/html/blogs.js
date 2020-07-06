var flag = true;
var imgSrc;

let eleArticle = document.getElementById("article1");
let eleTail = document.getElementById("tail1");
let eleImg = document.createElement("img");
let eleDiv = document.createElement("div");
eleDiv.setAttribute("id", "zhou1");

eleArticle.insertBefore(eleDiv, eleTail);
eleDiv.appendChild(eleImg);
eleImg.setAttribute("style", "max-height: 100%");
eleImg.src = "jl2.jpg";

function func(){
    if(flag){
        imgSrc = "jl1.jpg";
        flag = false;
    }
    else{
        imgSrc = "jl2.jpg";
        flag = true;
    }
    eleImg.src = imgSrc;
}


setInterval(func, 1000);