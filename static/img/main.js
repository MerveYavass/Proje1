$(document).ready(function(){
    $(".header-toggle").hide();
    $(".middle2").hide();
    $("#btn-toggle").click(function(event){
        event.stopPropagation();
        $(".middle").hide();
        $(".middle2").toggle(200);
        $(".header-toggle").toggle(200);
    });
    $(document).click(function(){
        $(".header-toggle").hide();
        $(".middle2").hide();
        $(".middle").show();
    });
    $(".header-toggle").click(function(event){
        event.stopPropagation();
    });
    $(".middle2").click(function(event){
        event.stopPropagation();
    });
});



// toggle-map butonuna onclick özelliği ekleyin
document.getElementById("toggle-map").onclick = function() {
  
    // Açılacak olan sayfanın URL'sini oluşturun
    var url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d47188.93559118784!2d27.183796923038354!3d38.44877885820846!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14b962cbbad43d9f%3A0x149fffcb050e5d0a!2sPark%20414!5e0!3m2!1str!2str!4v1682939871998!5m2!1str!2str";
    
    // Yeni sayfayı açın
    window.open(url);
    
  }


//? Navbar Carousel

const categoryScroller = document.getElementById('categoryScroller');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const scrollAmount = 300; // Kaydırma miktarı (px)

// Kategori carousel'ını başlangıçta odalar kategorisiyle başlatmak için aşağıdaki kodu ekleyin:
categoryScroller.scrollLeft = 0;

prevBtn.addEventListener('click', () => {
  categoryScroller.scrollLeft -= scrollAmount;
  if (categoryScroller.scrollLeft < 0) {
    categoryScroller.scrollLeft = 0;
  }
});

nextBtn.addEventListener('click', () => {
  categoryScroller.scrollLeft += scrollAmount;
  if (categoryScroller.scrollLeft > categoryScroller.scrollWidth - categoryScroller.clientWidth) {
    categoryScroller.scrollLeft = categoryScroller.scrollWidth - categoryScroller.clientWidth;
  }
});


//? Navbar Carousel


// FOOTER
$(document).ready(function(){

    //DESTEK VE KAYNAKLAR BUTONU
    $("#resources").hide();
    $(".btn3").click(function(){
        $("#resources").toggle(200);
        $(".footerBar").toggle(200);
        
    });

    //CLOSE BUTONU AKSİYONU
    $("#resourcesClose").click(function(){
        $("#resources").toggle(200);
        $(".footerBar").toggle(200);
    });

});





//? NAVBAR JS
// ------ bölgeler----------------
$(document).ready(function(){
    $(".header-toggle").hide();
    $(".middle2").hide();
    $(".navbar-carousels").show();
    $(".bolgeler").hide();
    $(".takvim").hide();
    $(".misafir").hide();
    $("#yer").click(function(event){
        event.stopPropagation();
        $(".card").css("opacity","0.6");
        $(".takvim").hide();
        $(".card-para").hide();
        $(".navbar-carousels").hide();
        $(".misafir").hide();
        $(".middle").hide();
        $(".middle2").show();
        $(".header-toggle").toggle(200);
        $(".bolgeler").toggle(200);
    });
    $(document).click(function(){
        $(".card").css("opacity","1");
        $(".card-para").show();
        $(".navbar-carousels").show();
        $(".header-toggle").hide();
        $(".middle2").hide();
        $(".middle").show();
        $(".bolgeler").hide();
    });
    $(".header-toggle").click(function(event){
        event.stopPropagation();
    });
    $(".middle2").click(function(event){
        event.stopPropagation();
    });
});


// --Misafirler
$(document).ready(function(){
    $(".header-toggle").hide();
    $(".middle2").hide();
    $(".bolgeler").hide();
    $(".takvim").hide();
    $(".navbar-carousels").show();
    $(".misafir").hide();
    $("#misafirler").click(function(event){
        event.stopPropagation();
        $(".card").css("opacity","0.6");
        $(".bolgeler").hide();
        $(".card-para").hide();
        $(".navbar-carousels").hide();
        $(".takvim").hide();
        $(".middle").hide();
        $(".middle2").show();
        $(".header-toggle").toggle(200);
        $(".misafir").toggle(200);
    });
    $(document).click(function(){
        $(".card").css("opacity","1");
        $(".navbar-carousels").show();
        $(".header-toggle").hide();
        $(".middle2").hide();
        $(".middle").show();
        $(".misafir").hide();
        $(".card-para").show();
    });
    $(".header-toggle").click(function(event){
        event.stopPropagation();
    });
    $()
    $(".middle2").click(function(event){
        event.stopPropagation();
    });
    $("#sub").click(function(event){
        event.stopPropagation();
    });
    $("#add").click(function(event){
        event.stopPropagation();
    });
    $("#sub2").click(function(event){
        event.stopPropagation();
    });
    $("#add2").click(function(event){
        event.stopPropagation();
    });
    $("#sub3").click(function(event){
        event.stopPropagation();
    });
    $("#add3").click(function(event){
        event.stopPropagation();
    });
    $("#sub4").click(function(event){
        event.stopPropagation();
    });
    $("#add4").click(function(event){
        event.stopPropagation();
    });
});



// ------- Takvim -----------------
$(document).ready(function(){
    $(".header-toggle").hide();
    $(".middle2").hide();
    $(".bolgeler").hide();
    $("takvim").hide();
    $(".misafir").hide();
    $("#hafta").click(function(event){
        event.stopPropagation();
        $(".card").css("opacity","0.6");
        $(".misafir").hide();
        $(".card-para").hide();
        $(".navbar-carousels").hide();
        $(".bolgeler").hide();
        $(".middle").hide();
        $(".middle2").show();
        $(".header-toggle").toggle(200);
        $(".takvim").toggle(200);
    });
    $(document).click(function(){
        $(".card").css("opacity","1");
        $(".header-toggle").hide();
        $(".card-para").show();
        $(".navbar-carousels").show();
        $(".middle2").hide();
        $(".middle").show();
        $(".takvim").hide();
    });
    $(".header-toggle").click(function(event){
        event.stopPropagation();
    });
    $(".middle2").click(function(event){
        event.stopPropagation();
    });
});

// --- Scroll İşlemleri
$(window).scroll(function() {
    let scrollTop = $(this).scrollTop();
    let windowHeight = $(this).height();
    if (scrollTop >0 && windowHeight < 0) {
      $('.misafir').hide();
    } else {
      $(".card").css("opacity","1");

      $(".header-toggle").hide();
      $(".middle2").hide();
      $(".middle").show();
      $(".navbar-carousels").show();
      $(".card-para").show();
    }
  });
$(window).scroll(function() {
    let scrollTop = $(this).scrollTop();
    let windowHeight = $(this).height();
    if (scrollTop >0 && windowHeight < 0) {
      $('.bolgeler').hide();
    } else {
      $(".card").css("opacity","1");
      $('.bolgeler').hide();
      $(".header-toggle").hide();
      $(".middle2").hide();
      $(".middle").show();
      $(".navbar-carousels").show();
      $(".card-para").show();
    }
  });
$(window).scroll(function() {
    let scrollTop = $(this).scrollTop();
    let windowHeight = $(this).height();
    if (scrollTop >0 && windowHeight < 0) {
      $('.takvim').hide();
    } else {
      $(".card").css("opacity","1");
      $('.takvim').hide();
      $('.misafir').hide();
      $(".header-toggle").hide();
      $(".middle2").hide();
      $(".middle").show();
      $(".navbar-carousels").show();
      $(".card-para").show();
    }
  });


// ----- Yer ara tıkla
$(document).ready(function(){
    
    $(".yer-ara").click(function(event){
        event.stopPropagation();
        $(".kişi-ekle").hide();
        $(".takvim").hide();
        $(".bolgeler").toggle(200);

    });   
});




// ----- Takvim ac
$(document).ready(function(){
    $(".tarih").click(function(event){
        event.stopPropagation();
        $(".bolgeler").hide();
        $(".misafir").hide();
        $(".kişi-ekle").hide();
        $(".takvim").show(200);
    });
});


// ---- kişi ekle

$(document).ready(function(){
    $(".kişi-ekle").click(function(event){
        event.stopPropagation();
        $(".bolgeler").hide();
        $(".takvim").hide();
        $(".misafir").toggle(200);
    });
});


// Misafir ekle arttırma-azaltma
let addBtn = document.querySelector('#add');
		let subBtn = document.querySelector('#sub');
		let qty = document.querySelector('#qtyBox');
		
		addBtn.addEventListener('click',()=>{
			qty.value = parseInt(qty.value) + 1;
		});

		subBtn.addEventListener('click',()=>{
			if (qty.value <= 0) {
				qty.value = 0;
			}
			else{
				qty.value = parseInt(qty.value) - 1;
			}
		});

let addBtn2 = document.querySelector('#add2');
		let subBtn2 = document.querySelector('#sub2');
		let qty2 = document.querySelector('#qtyBox2');
		
		addBtn2.addEventListener('click',()=>{
			qty2.value = parseInt(qty2.value) + 1;
		});

		subBtn2.addEventListener('click',()=>{
			if (qty2.value <= 0) {
				qty2.value = 0;
			}
			else{
				qty2.value = parseInt(qty2.value) - 1;
			}
		});

let addBtn3 = document.querySelector('#add3');
		let subBtn3 = document.querySelector('#sub3');
		let qty3= document.querySelector('#qtyBox3');
		
		addBtn3.addEventListener('click',()=>{
			qty3.value = parseInt(qty3.value) + 1;
		});

		subBtn3.addEventListener('click',()=>{
			if (qty3.value <= 0) {
				qty3.value = 0;
			}
			else{
				qty3.value = parseInt(qty3.value) - 1;
			}
		});

let addBtn4 = document.querySelector('#add4');
		let subBtn4 = document.querySelector('#sub4');
		let qty4 = document.querySelector('#qtyBox4');
		
		addBtn4.addEventListener('click',()=>{
			qty4.value = parseInt(qty4.value) + 1;
		});

		subBtn4.addEventListener('click',()=>{
			if (qty4.value <= 0) {
				qty4.value = 0;
			}
			else{
				qty4.value = parseInt(qty4.value) - 1;
			}
		});



        // --------------------------------- RESPONSIVE-NAVBAR -------------------------
                        // ---- responsive bolge --------

        // $(document).ready(function(){
        //     $(".responsive-misafir").hide();
        //     $(".responsive-takvim").hide();
        //     $("responsive-bolge").hide();
        //     $(".responsive-misafir2").hide();
        //     $(".responsive-takvim2").hide();
        //     $("responsive-bolge2").hide();

        //     $(".responsive-bolge2").click(function(event){
        //         event.stopPropagation();
        //         $(".responsive-bolge").toggle(200);
                
        //     }); 
        //     $(".responsive-takvim2").click(function(event){
        //         event.stopPropagation();
        //         $(".responsive-takvim").toggle(200);
        //         $(".responsive-misafir").hide();
        //         $(".responsive-bolge").hide();
                
        //     });  
        //     $(".responsive-misafir2").click(function(event){
        //         event.stopPropagation();
        //         $(".responsive-takvim").hide();
        //         $(".responsive-misafir").toggle(200);
        //         $(".responsive-bolge").hide();

        //     });           
        // });

        $(document).ready(function(){
            $(".responsive-bolge").hide();
            $(".responsive-bolge2").hide();
            $(".responsive-misafir").hide();
            $(".responsive-misafir2").hide();
            $(".responsive-takvim").hide();
            $(".responsive-takvim2").hide();
            $(".responsive-navbar").click(function(event){
                event.stopPropagation();
             $(".responsive-bolge2").show();
             $(".responsive-takvim2").show();
             $(".responsive-misafir2").show();
             $(".paraHesap").hide();
             $(".navbar-carousels").hide();
            });
            
            $(document).click(function(){
                $(".responsive-bolge").hide();
                $(".responsive-bolge2").hide();
                $(".responsive-misafir").hide();
                $(".responsive-misafir2").hide();
                $(".responsive-takvim").hide();
                $(".responsive-takvim2").hide();
                $(".paraHesap").show();
                $(".navbar-carousels").show();
            });
            $(".responsive-navbar").click(function(event){
                event.stopPropagation();
            });
           
        });
        

/* Evinizi Airbnb'ye Taşıyın Bölümü */
// Para hesaplama
let customRange1 = document.getElementById('customRange1');
let resultDiv = document.getElementById('result');
let gunSayisi = document.getElementById('gunSayisi');

customRange1.addEventListener('input', function() {
  let value = parseInt(customRange1.value);
  let total = value * 818;

  gunSayisi.innerHTML = value;
  resultDiv.innerHTML =  total;
});

function openModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "block";
  }
  
  // Modal dışına tıklama olayını dinleyin
  window.addEventListener("click", function(event) {
    var modal = document.getElementById("rezerveModal");
    if (event.target == modal) {
      modal.style.display = "none";
    }
  });
  

// ilan8 
window.addEventListener('scroll', function() {
    let scrollIndicator = document.getElementById('scroll-indicator');
    if (window.scrollY > 0) {
      scrollIndicator.style.display = 'block';
    } else {
      scrollIndicator.style.display = 'none';
    }
  });
// ilan8 

// paylaşma kısmı yönlendirmeleri
function goToLink(platform) {
    var url;

    if (platform === 'whatsapp') {
        // Whatsapp yönlendirme işlemi
        url = 'https://web.whatsapp.com/';
    } else if (platform === 'facebook') {
        // Facebook yönlendirme işlemi
        url = 'https://www.facebook.com/';
    } else if (platform === 'twitter') {
        // Twitter yönlendirme işlemi
        url = 'https://twitter.com/';
    }

    if (url) {
        window.open(url, '_blank'); // Yeni bir sekmede veya pencerede yönlendirme işlemi
    }
}