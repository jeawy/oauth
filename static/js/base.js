//############################
//验证手机号码：13,15,17,18
//###########################
function validatemobile(mobile) 
{ 
    var result={};
    if(mobile.length==0) 
    { 
       result['msg']='请输入手机号码！'; 
       result['status'] = false;
       return result;
    }    

    if(mobile.length!=11) 
    { 
        result['msg']='请输入有效的手机号码！';
        result['status'] = false;
        return result;
    } 
     
    var myreg = /^(((13[0-9]{1})|(15[0-9]{1})|(17[0-9]{1})|(18[0-9]{1}))+\d{8})$/; 
    if(!myreg.test(mobile)) 
    { 
        result['msg']='请输入有效的手机号码！';
        result['status'] = false;
        return result;
    } 
    result['status'] =true;
    return result;
} 
/* 
 * cookie
 */
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
/* 
 *返回按钮
 */


/*
* 3秒后重新加载
*/

function reload3(){
    setInterval(function(){
        window.location.reload();
    }, 3000);
}


/*  提示信息函数 */

function  promptMessage(el,msg){//el=在哪个元素后添加提示，msg=提示得内容
    el.next('.alert').remove();
    el.next('label.error').remove();//删除之前的提示
    var html =  '<div class="alert">'+msg+'</div>'//提示信息构成
    el.after(html);//添加提示
    var deleteMsg=  setTimeout(function(){ el.next('.alert').remove(); }, 5000);//5秒去掉提示
}
$(function(){
    var windowHeight= $(window).height();//浏览器可视窗口的高度
    $('body').css('min-height',windowHeight+'px');
})