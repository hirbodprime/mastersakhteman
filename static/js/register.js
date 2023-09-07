$(document).ready(function(){
    
    $(document).on('input', '.text-input', function(){
        var usernme = $('#username');
        var password = $('#password');
        var btnElement = $('#btn');
        var passwordRepeat = $('#passwordRepeat');
    
        if(usernme.val() && password.val() && passwordRepeat.val()) {
            
            $('#btn').prop("disabled",false);
            btnElement.css('background', '#1B2052');
            btnElement.css('cursor', 'pointer');
        }else{
            $('#btn').prop("disabled",true);
            btnElement.css('background', '#AFB1AF');
            btnElement.css('cursor', 'default');
        }
    })
    $("#post-form").submit(function(e){
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
            console.log(_this[0])
            _this[0].reportValidity();
            return false;
        }
        if (password != passwordRepeat) {
            error.show();
            return false;
        } 
        
        else {
            error.hide();
            $.ajaxSetup({ 
                beforeSend: function(xhr, settings) {
                    function getCookie(name) {
                        var cookieValue = null;
                        if (document.cookie && document.cookie != '') {
                            var cookies = document.cookie.split(';');
                            for (var i = 0; i < cookies.length; i++) {
                                var cookie = jQuery.trim(cookies[i]);
                                // Does this cookie string begin with the name we want?
                                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                    break;
                                }
                            }
                        }
                        return cookieValue;
                    }
                    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                        // Only send the token to relative URLs i.e. locally.
                        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
                } 
            });
            $.ajax({
                headers: {
                    "X-CSRFToken": '{{csrf_token}}',
                },
                url: "http://127.0.0.1:8000/account/APIregister/",
                data: new FormData($(this)[0]),
                cache: false,
                contentType: false,
                processData: false,
                method: 'POST',
                type: 'POST',
                dataType: 'json',
                error: err => {
                    console.log(err)
                },

                success: function(resp) {
                    if (resp.status == 'success') {
                        el.removeClass("alert alert-danger err-msg");
                        location.href = "http://127.0.0.1:8000/";

                    } else if (resp.status == 'failed' && !!resp.msg) {
                        el.text(resp.msg)
                    } else {
                        el.text("An error occured", 'error');
                        console.err(resp)
                    }
                    _this.prepend(el)
                    el.show('slow')
                }
            })
        }
        
    });
});






