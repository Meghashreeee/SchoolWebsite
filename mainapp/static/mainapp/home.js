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





