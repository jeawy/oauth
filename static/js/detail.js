
$(document).ready(function(){ 
        /*
        $('.btn-book').click(function(e){
            e.preventDefault();
            var auth = $('#auth').val();
            if (auth == '0'){
                $().errormessage('请先登录...');
                setTimeout(function() {
                        window.location.href = '/users/login/?next='+window.location.pathname;
                }, 2000); 
            }else{
                $('#book').modal('toggle');  
            }
        })*/
        // step1
        name = '';//姓名
        email = '';//邮箱
        phone = '';//电话
        $('.step-content').hide();
        $('.step1-content').show();
        $('.step1-btn').click(function(){ 
            name = $.trim($('#username').val());
            email = $.trim($('#email').val());
            if (name  == '' ){
                $().errormessage('请输入姓名...');
                return
            }
            if (email == ''){
                $().errormessage('请输入邮箱...');
                return
            } 
            $('.step-content').hide();
            $('.step2-content').show('slow');
        });
        // step2-btn
        $('.step2-btn').click(function(){ 
            var code = $.trim($("#promotioncode").val());
            if (phone  == '' ){
                $().errormessage('请输入手机号码...');
                return
            }
            if (code == ''){
                $().errormessage('请输入手机验证码...');
                return
            }  
            //开始验证手机号码
            $.ajax('/users/phonecode/'+phone+'/' + code, {
                method: "get",  
                processData: false,
                contentType: false,
                success: function (data) {
                if (data['status'] == 'error') {
                        $().message(data['msg']); 
                    } 
                },
                error: function () {
                    alert('Server down...');
                }
            });
            $('.step-content').hide();
            $('.step3-content').show('slow');
        });     
        //step3-btn 
        $('.step3-btn').click(function(){  
            //finish operator
            var formData = new FormData(document.querySelector("#csrf-form"));
            formData.append('phone', phone);
            formData.append('name', name);
            formData.append('email', email);
            var productid = $('#productid').val();
            $.ajax('/product/products/'+productid+'/addatt', {
                method: "POST",
                data: formData,
                processData: false,
                contentType: false,
                success: function (data) {
                if (data['status'] == 'OK') {
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
        $('.step-btn-send-code, .a-resend').click(function(){
            //发送验证码
            phone = $.trim($("#mobilephone").val());
            if (phone  == ''){
                $().errormessage('请输入手机号码...');
                return
            }
            var formData = new FormData(document.querySelector("#signup-Form"));

            $.ajax('/users/phonecode/'+phone+'', {
                method: "POST", 
                data: formData,
                processData: false,
                contentType: false,
                success: function (data) {
                if (data['status'] == 'ok') {
                        $().message(data['msg']); 
                    }
                    else {
                        $().errormessage(data['msg']);
                    }
                },
                error: function () {
                    alert('Server down...');
                }
            });
        })
     /*
        // 提交预定情况
        $('.btn-submit').click(function(){
            var formData = new FormData(document.querySelector("#signup-Form"));
            var productid = $('#productid').val();
            var auth = $('#auth').val();
            if (auth == '0'){
                $().errormessage('请先登录...');
                setTimeout(function() {
                        window.location.href = '/users/login/?next='+window.location.pathname;
                }, 2000); 
            }
            $.ajax('/product/products/'+productid+'/addatt', {
                method: "POST",
                data: formData,
                processData: false,
                contentType: false,
                success: function (data) {
                if (data['status'] == 'OK') {
                        $().message(data['msg']);
                        setTimeout(function() {
                        location.reload();
                    }, 3000);
                    }
                    else {
                        $('body').append('<label class="err_label" >' + data['msg'] + '</label>'); //
                    }
                },
                error: function () {
                    alert('Server down...');
                }
            });
        })
        */
        
});

$('.blue-btn').mouseenter(function(){
    $(this).children('.fa-angle-double-right').fadeToggle(300);
});
$('.blue-btn').mouseleave(function(){
    $(this).children('.fa-angle-double-right').fadeToggle(300);
});
$('.grey_bg').css('min-height',$('.grey_bg').prev().height()+'px');