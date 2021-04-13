

$(document).ready(function() {
    $("#submit").click(function() {
    var name = $("#userName").val();
    var email = $("#userEmail").val();
    var message = $("#content").val();
    var subject = $("##subject").val();
    $("#returnmessage").empty(); // To empty previous error/success message.
    // Checking for blank fields.
    if (name == '' || email == '' || content == '') {
    alert("Please Fill Required Fields");
    } else {
    // Returns successful data submission message when the entered information is stored in database.
    $.post("contact_mail.php", {
    userName: name,
    userEmail: email,
    content: content,
    subject: subject
    }, function(data) {
    $("#returnmessage").append(data); // Append returned message to message paragraph.
    if (data == "Your Query has been received, We will contact you soon.") {
    $("#contactForm")[0].reset(); // To reset form fields on success.
    }
    });
    }
    });
    });