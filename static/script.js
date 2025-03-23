// Dinamik Arkaplan Değişimi
const backgrounds = [
    "linear-gradient(to right, #ffafbd, #ffc3a0)",
    "linear-gradient(to right, #2193b0, #6dd5ed)",
    "linear-gradient(to right, #cc2b5e, #753a88)",
    "linear-gradient(to right, #42275a, #734b6d)",
    "linear-gradient(to right, #de6262, #ffb88c)",
    "linear-gradient(to right, #06beb6, #48b1bf)",
    "linear-gradient(to right, #eb3349, #f45c43)"
];

let currentBackground = 0;

function changeBackground() {
    document.body.style.background = backgrounds[currentBackground];
    currentBackground = (currentBackground + 1) % backgrounds.length;
}

setInterval(changeBackground, 5000);
window.onload = changeBackground;

// İçeriği sayfaya dikey ve yatay olarak ortala
document.body.style.display = "flex";
document.body.style.justifyContent = "center";
document.body.style.alignItems = "center";
document.body.style.flexDirection = "column";
document.body.style.minHeight = "100vh";
document.body.style.margin = "0";

// Ürün ekleme scripti (sadece index.html için)
if(document.getElementById('urunForm')){
    document.getElementById('urunForm').addEventListener('submit', async function(e){
        e.preventDefault();
        const isim = document.getElementById('urunIsmi').value;
        const fiyat = parseFloat(document.getElementById('urunFiyati').value);
        const response = await fetch('/urun-ekle', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ isim, fiyat })
        });
        const result = await response.json();
        const mesajDiv = document.getElementById('mesaj');
        mesajDiv.innerHTML = `<p class="success">${result.message}</p>`;
        document.getElementById('urunForm').reset();
        setTimeout(() => mesajDiv.innerHTML='', 2500);
    });
}

// Sipariş verme fonksiyonu
function siparisVer() {
    alert("Sipariş sayfasına yönlendiriliyorsunuz...");
}
