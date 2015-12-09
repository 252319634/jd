//the js file
function load() {

    //读取用户列表
}
function del(e) {
    //删除用户
    var user_id = $(e).parent().siblings('.user_id').text();
    post_data = {
        'method':'del',
        'user_id': user_id
    };
    $.post("",
        post_data,
        function (data) {
            if (data.state == 0) {
                alert(data.msg);
            }
            else {
                alert('操作失败!');
            }
        }
    );
}
function change(e) {
    //修改用户
    //$('#user_id').value =
    var id = $(e).parent().siblings('.user_id').text();
    var name = $(e).parent().siblings('.user_name').text();
    var password = $(e).parent().siblings('.user_password').text();
    //alert(id+name+password);
    $('#user_id').val(id);
    $('#user_name').val(name);
    $('#user_password').val(password);
    //alert($(e));
    //alert(.siblings('.user_id').innerHTML);
    //alert($('#t_user_id').outerHTML);
    //alert($('#user_id').val());
}
function save() {
    //保存用户修改
    var user_id = $('#user_id').val();
    var user_name = $('#user_name').val();
    var user_password = $('#user_password').val();
    post_data = {
        'method':'save',
        'user_id': user_id,
        'user_password': user_password,
        'user_name': user_name
    };
    $.post("",
        post_data,
        function (data) {
            if (data.state == 0) {
                alert(data.msg);

            }
            else {
                alert('操作失败!');
            }
        }
    );
}