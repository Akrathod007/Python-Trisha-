let amazon = document.getElementById("amazon")
console.log(amazon);

console.log(amazon.getAttribute("href"));

amazon.setAttribute("href","https://www.flipkart.com")

amazon.removeAttribute("href")

let doremon = document.getElementById("doremon")
console.log(doremon);

let btn = document.getElementById("btn")

btn.addEventListener("click",()=>{
    doremon.setAttribute("src","https://cdna.artstation.com/p/assets/images/images/026/941/604/large/kaustubh-chaudhary-doremon-pink.jpg?1590151532")
    // doremon.setAttribute("width",100)
    doremon.style.width = "300px";
    doremon.style.borderRadius = "50%"
})

let remove = document.getElementById("remove")

remove.addEventListener("click",()=>{
    doremon.removeAttribute("src");
    doremon.removeAttribute("width");
})