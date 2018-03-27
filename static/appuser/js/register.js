 $(document).ready(function() {

        $('#emailcode').hide();

        // 在键盘按下并释放及提交后验证提交表单
        $("#signup-Form").validate({
            rules: {
                username: {
                    required: true,
                    minlength: 2
                },
                password: {
                    required: true,
                    minlength: 5
                },
                emailcode: {
                    required: true, 
                },
                confirm_password: {
                    required: true, 
                    minlength: 5,
                    equalTo: "#password"
                },
                phone:{
                    required: true,
                    minlength: 11,
                    number:true,
                    digits:true
                },
                email: {
                    required: true,
                    email: true
                },
                agree:{
                    required: true
                }

            },
            messages: {
                username: {
                    required: "请输入用户名",
                    minlength: "用户名必需由两个字母组成"
                },
                password: {
                    required: "请输入密码",
                    minlength: "密码长度不能小于 5 个字母"
                },
                emailcode: {
                    required: "请输入邮箱验证码",
                },
                confirm_password: {
                    required: "请输入密码",
                    minlength: "密码长度不能小于 5 个字母",
                    equalTo: "两次密码输入不一致"
                },
                phone:{
                    required: "请输入手机号",
                    minlength: "请输入正确的手机号",
                    number:"请输入正确的手机号",
                    digits:"请输入正确的手机号"
                },
                agree:{
                    required:"未同意遵守法律声明和隐私条框",
                },
                email: "请输入一个正确的邮箱",
            }
        });
       /*  $('form').submit(function(e){
            if(!$('#agree').checked){
                $().errormessage('请完善资料');
                e.preventDefault();
            } */
    //在这是样式
        var html ='<div class="alert alert-danger" role="alert">###</div>';
        //验证用户名和邮箱是否已被注册
        $("#username").blur(function(){
            var username = $.trim($("#username").val());
            $('.msg').empty();
             if(username.length == 0)
                {
                    return;
                }
            $.get('/users/usernames/'+username, {}, function(result){
                if (result['msg'] != true){
                    $('.msg').append(html.replace('###', '用户名【'+username+'】已被注册...'));
                    $("#username").val('');
                }
            });
        });

       $(document).on( 'blur',  "#emailscode",function(){
            var email = $.trim($("#email").val());
            var code = $.trim($("#emailcode").val());
           
            $('.msg').empty();
            $.get('/users/emailscode/'+email+'/'+code, {}, function(result){
                if (result != true){
                    //去页面中找这个class，就是消息被添加的位置.msg
                    $('.msg').append(html.replace('###', '邮箱验证码不正确...'));
                    $("#emailscode").val('');
                }
            });
             
       });

        $("#email").blur(function(){
            var email = $.trim($("#email").val());
            var tmp ;
            $('.msg').empty();
            if(email.length == 0)
            {
                return;
            }

            var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
               
            if(re.test(email)){
                  $.get('/users/emails/'+email, {}, function(result){
                        if (result['msg'] != true){
                            $('.msg').append(html.replace('###', '邮箱'+email+'已被注册...'));
                            $("#email").val('');
                        }
                        else{
                            //发送邮箱验证码
                            $('#emailcode').show();
                        
                            $.get('/users/emailscode/'+email, {}, function(status){
                                tmp = html.replace('###', status['msg']); 
                                if(status['status'] == 2){ 
                                    tmp = tmp.replace('danger', 'success');
                                } 
                                $('.msg').append(tmp);
                            });
                        }
                    });
            }
           
        });
    });
$('#phone,#phonecode').blur(function(){
    $('#code-error').remove();
})
$('#phonecode').focus(function(){
    $(this).siblings('.alert-danger').remove();
})