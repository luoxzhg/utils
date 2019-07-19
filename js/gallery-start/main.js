var displayedImage = document.querySelector('.displayed-img');
var thumbBar = document.querySelector('.thumb-bar');

var btn = document.querySelector('button');
var overlay = document.querySelector('.overlay');

/* Looping through images */
for (var i=1; i < 6; i++){
   let thumb = document.createElement("img");
   thumb.src = "images/pic_.jpg".replace("_", i.toString());
   thumbBar.appendChild(thumb);
}

thumbBar.addEventListener('click', function(e){
   displayedImage.src = e.target.src;
})

/* Wiring up the Darken/Lighten button */
btn.addEventListener('click', function(e){
  let flip = e.target.className;
  if (flip === "dark"){
     btn.innerText = "Lighten";
     btn.className = "light";
     overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
  }
  else if (flip === "light"){
      btn.innerText = "Darken";
      btn.className = "dark";
      overlay.style.backgroundColor = "rgba(0, 0, 0, 0)";
  }
})

print();