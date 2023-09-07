$(document).ready(function(){
    $(document).on('input', '.text-input', function(){
    //     var first_name = $('#first_name');
    //     var last_name = $('#last_name');
    //     var email = $('#email');
        var btnElement = $('#btn');
    //     // console.log(first_name.val())
    //     // var password = $('#password');
    //     // var passwordRepeat = $('#passwordRepeat');
        
    //     if(first_name.val() && last_name.val() && email.val()) {
    //         $('#btn').prop("disabled",false);
        btnElement.css('background', '#9ea6fe');
    //         btnElement.css('cursor', 'pointer');
    //     }else{
    //         $('#btn').prop("disabled",true);
    //         btnElement.css('background', '#AFB1AF');
    //         btnElement.css('cursor', 'default');
    //     }
    })
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');
    var markers = [
        {
            csrfmiddlewaretoken:csrftoken
        }
    ];
    $("#post-form").submit(function(e){
        var strdata = $( "#post-form" ).serialize();
        // console.log(strdata)
        var first_name = $("#first_name").val();
        var last_name = $("#last_name").val();
        var email = $("#email").val();
        var password = $("#password").val();
        var passwordRepeat = $("#passwordRepeat").val();
        var error = $("#passerror");
        e.preventDefault();
        var _this = $(this);
        $('.err-msg').remove();
        var el = $('<div>');
        el.addClass("alert alert-danger err-msg");
        el.hide();
        if (_this[0].checkValidity() == false) {
            _this[0].reportValidity();
            return false;
        }
        if (password != passwordRepeat) {
            error.show();
            return false;
        } else {
            error.hide();
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:8000/account/updateprofileAPI/",
                // The key needs to match your method's input parameter (case-sensitive).
                data: JSON.stringify(
                        {Data:strdata},
                        {Markers: markers,},
                        {"formdata":{"first":first_name,
                        "last":last_name,
                        "email":email }},
                ),
                contentType: "application/json; charset=utf-8",
                dataType: "json",
                error: err => {
                    console.log(err)
                },
                success: function(resp) {
                    if (resp.status == 'success') {
                        el.removeClass("alert alert-danger err-msg");
                        location.href = "http://127.0.0.1:8000/account/";

                    } else if (resp.status == 'UpdatedPass') {
                        el.removeClass("alert alert-danger err-msg");
                        location.href = "http://127.0.0.1:8000/account/login/";
                    }else if (resp.status == 'failed' && !!resp.msg) {
                        el.text(resp.msg)
                    }  else {
                        el.text("An error occured", 'error');
                        console.error(resp)
                    }
                    _this.prepend(el)
                    el.show('slow')
                }
                });
        }
        
    });
});











// $(document).ready(function(){

//     $(document).on('input', '.text-input', function(){
//         var first_name = $('#first_name');
//         var last_name = $('#last_name');
//         var email = $('#email');
//         var btnElement = $('#btn');
//         // console.log(first_name.val())
//         // var password = $('#password');
//         // var passwordRepeat = $('#passwordRepeat');
    
//         if(first_name.val() && last_name.val() && email.val()) {
//             $('#btn').prop("disabled",false);
//             btnElement.css('background', '#9ea6fe');
//             btnElement.css('cursor', 'pointer');
//         }else{
//             $('#btn').prop("disabled",true);
//             btnElement.css('background', '#AFB1AF');
//             btnElement.css('cursor', 'default');
//         }
//     })
//     $("#post-form").submit(function(e){
//         var password = $("#password").val();
//         var passwordRepeat = $("#passwordRepeat").val();
//         var error = $("#passerror");
//         var first_name = $('#first_name');
//         e.preventDefault();
//         var _this = $(this);
//         $('.err-msg').remove();
//         var el = $('<div>');
//         el.addClass("alert alert-danger err-msg");
//         el.hide();
//         if (_this[0].checkValidity() == false) {
//             _this[0].reportValidity();
//             return false;
//         }
//         if (password != passwordRepeat) {
//             error.show();
//             return false;
//         } else {
//             error.hide();
//             $.ajax({
//                 headers: {
//                     "X-CSRFToken": '{{csrf_token}}'
//                 },
//                 url: "http://127.0.0.1:8000/account/updateprofileAPI/",
//                 data: new FormData($(this)[0]),
//                 cache: false,
//                 contentType: "application/json; charset=utf-8",
//                 processData: false,
//                 method: 'POST',
//                 type: 'POST',
//                 dataType: 'json',
//                 error: err => {
//                     console.log(err)
//                     // alert_toast("An error occured", 'error');
//                 },
//                 success: function(resp) {
//                     if (resp.status == 'success') {
//                         el.removeClass("alert alert-danger err-msg");
//                         location.href = "http://127.0.0.1:8000/account/";

//                     } else if (resp.status == 'failed' && !!resp.msg) {
//                         el.text(resp.msg)
//                     } else {
//                         el.text("An error occured", 'error');
//                         console.error(resp)
//                     }
//                     _this.prepend(el)
//                     el.show('slow')
//                 }
//             })
//         }
        
//     });
// });