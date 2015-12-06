function onLoginIn() {
    username = $("#name").val();
    password = $("#pw").val();
    checkcode = $("#checkcode").val();
    ifsave = $("#checkbox").prop("checked");
    postData = {
        'username': username,
        'password': password,
        'checkcode': checkcode,
        'ifsave': ifsave
    };
    $.post("/login/",
        postData,
        function (data) {
            if (data.state == 0) {
                alert("登录成功!");
                //setTimeout('window.location.href = "/"',5000); 延时登录
                window.location.href = "/";
            }
            else {
                changeImg();
                document.getElementById("formerror").innerHTML = data.msg;
            }
        });

}
function changeImg(){
    //$('#verifyImg').hide();
    //img=$('<img src="/verify/" alt="" id="verifyImg"/>');
    //$('#verifyImg').removeAttr('src');
    //$('#verifyImg').replaceWith(img);
    //实验各种方法都不行, 函数执行完后 jq对象没有变化 就不重新渲染对象.
    $('#verifyImg').attr("src", "/verify/"+Math.random());
    //需要加上随机数字,否则浏览器认为没有变化,不请求新图片
    //$('#verifyImg').attr("src", "/verify/"); 不加随机数字只有360浏览器可以换图片
    //$('#verifyImg').show();
    //改变图片路径就能更换验证图片
}