function onLoginIn() {
    userName = $("#name").val();
    password = $("#pw").val();
    checkCode = $("#checkcode").val();
    ifSave = $("#checkbox").prop("checked");
    postData = {
        'userName': userName,
        'password': password,
        'checkCode': checkCode,
        'ifSave': ifSave
    };
    $.post("/login/",
        postData,
        function (data) {
            if (data.state == 0) {
                window.location.href = "/";
            }
            else {
                var p_error=document.getElementById("formerror");
                p_error.innerHTML = data.msg;
            }
        });

}
function changeImg(){
    $('#verifyImg').attr("src", "/verify/");
    //改变图片路径就能更换验证图片
}