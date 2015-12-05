$('#checkbox').bind('click', function () {
    if ($('#checkbox').prop('checked')) {
        $('#register_btn').prop('disabled', false).css('cursor', 'pointer');
    } else {
        $('#register_btn').prop('disabled', true).css('cursor', 'not-allowed');
    }
});

function register() {
    username = $('#username').val();
    password1 = $('#password1').val();
    password2 = $('#password2').val();
    checkcode = $('#checkcode').val();
    checkbox = $('#checkbox').prop("checked");
    Data = {
        username: username,
        password1: password1,
        password2: password2,
        checkcode: checkcode,
        checkbox: checkbox
    };
    $.post("/register/",
        Data,
        function (data) {
            if (data.state == 0) {
                window.location.href = "/";
            }
            else {
                //alert(data.msg);
                changeImg();
                document.getElementById("formerror").innerHTML = data.msg;
            }
        });
}
function changeImg(){
    $('#verifyImg').attr("src", "/verify/");
    //改变图片路径就能更换验证图片
}