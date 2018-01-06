$('.subscribe').click(function(){  
  
    //发送验证码
    phone = $.trim($("#phone").val());
    if (phone  == ''){
        $().errormessage('请输入手机号码...');
        return
    }
    var formData = new FormData(document.querySelector("#formsubscribe"));
    formData.append('phone', phone);
 
    var productid = $('#productid').val();
    $.ajax('/users/phonecode/'+phone+'', {
        method: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (data) {
        if (data['status'] == 'ok') {
                $().message(data['msg']);
                setTimeout(function() {
                location.reload();
            }, 3000);
            }
            else {
                $().errormessage(data['msg']);
            }
        },
        error: function () {
            alert('Server down...');
        }
    }); 
});