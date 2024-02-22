const slider = document.querySelector('.slider');

function activate(e) {
  const items = document.querySelectorAll('.item');
  e.target.matches('.next') && slider.append(items[0])
  e.target.matches('.prev') && slider.prepend(items[items.length-1]);
}

document.addEventListener('click',activate,false);

function validform(){
    document.getElementById("contact_form").style.opacity = "0";
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var message = document.getElementById("message").value;

    var data = {
        name: name,
        email: email,
        message: message
    }
    setRequestHeader();

    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: "/contactform/",
        context: document.body,
        cache : false,
        data: data,
        success: function (data) {
            console.log("Success:", data);
            document.getElementById("contact_form").innerHTML = "<span>Thank you for contacting us!!</span>";
            document.getElementById("contact_form").style.opacity = "1";
            alert("Message sent successfully!! ")
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(data);
        }
    });
    return false;
}




// mobile gallary start

var timeOut = 2000;
var slideIndex = 0;
var autoOn = true;

mobile_autoSlides();

function mobile_autoSlides() {
    timeOut = timeOut - 20;

    if (autoOn == true && timeOut < 0) {
        mobile_showSlides();
    }
    setTimeout(mobile_autoSlides, 20);
}

function mobile_prevSlide() {

    timeOut = 2000;

    var slides = document.getElementsByClassName("mobile-mySlides");
    var dots = document.getElementsByClassName("mobile-dot");

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        dots[i].classList.remove("mobile-active");
    }
    slideIndex--;

    if (slideIndex > slides.length) {
        slideIndex = 1
    }
    if (slideIndex == 0) {
        slideIndex = 3
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].classList.add("mobile-active");
}

function mobile_showSlides() {

    timeOut = 2000;

    var slides = document.getElementsByClassName("mobile-mySlides");
    var dots = document.getElementsByClassName("mobile-dot");
    console.log(dots);

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        dots[i].classList.remove("mobile-active");
    }
    slideIndex++;

    if (slideIndex > slides.length) {
        slideIndex = 1
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].classList.add("mobile-active");
}

// mobile gallary end