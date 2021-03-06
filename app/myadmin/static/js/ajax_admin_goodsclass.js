
function get_val(e, target) {
    var gc_id = $(e).parent().siblings('.gc_id').text();
    var gc_pid = $(e).parent().siblings('.gc_pid').text();
    var gc_cid = $(e).parent().siblings('.gc_cid').text();
    var gc_cn = $(e).parent().siblings('.gc_cn').text();
    var gc_state = $(e).parent().siblings('.gc_state').text();
    var gc_priority = $(e).parent().siblings('.gc_priority').text();
    if (target == 'change') {
        $('#gc_id').val(gc_id);
        $('#gc_pid').val(gc_pid);
        $('#gc_cid').val(gc_cid);
        $('#gc_cn').val(gc_cn);
        $('#gc_state').val(gc_state);
        $('#gc_priority').val(gc_priority);
    }
    if (target == 'add') {
        $('#add_gc_pid').val(gc_id);
    }
}
function del(e) {
    var gc_id = $(e).parent().siblings('.gc_id').text();
    post_data = {
        'method': 'del',
        'gc_id': gc_id
    };
    $.post('',
        post_data,
        function (data) {
            if (data.state == 0) {
                alert(data.msg);
            }

        }
    );
}
function add(e) {
    var pid = $('#add_gc_pid');
    var cn = $('#add_gc_cn');
    var state = $('#add_gc_state');
    var priority = $('#add_gc_priority');
    post_data = {
        'method': 'add',
        'gc_pid': pid.val(),
        'gc_cn': cn.val(),
        'gc_state': state.val(),
        'gc_priority': priority.val()
    };
    $.post('',
        post_data,
        function (data) {
            if (data.state == 0) {
                alert(data.msg);
                pid.val('');
                cn.val('');
                state.val('');
                priority.val('');
            }

        }
    );
}
function save() {
    post_data = {
        'method': 'save',
        'gc_id': $('#gc_id').val(),
        'gc_pid': $('#gc_pid').val(),
        'gc_cn': $('#gc_cn').val(),
        'gc_state': $('#gc_state').val(),
        'gc_priority': $('#gc_priority').val()
    };
    $.post('',
        post_data,
        function (data) {
            if (data.state == 0) {
                alert(data.msg);
            }

        }
    );


}
function load(opt) {
    pid = $(opt).val();
    //alert(pid);

    if (opt.getAttribute("id") == "select_l1") {
        select = $('#select_l2').empty();
        select.append($('<option value=""></option>'));
        $('#select_l3').empty().append($('<option value=""></option>'));
    }
    if (opt.getAttribute("id") == "select_l2") {
        select = $('#select_l3').empty();
        select.append($('<option value=""></option>'));
    }
    if (opt.getAttribute("id") == "select_l3") {
        return
    }
    post_data = {
        'method': 'load',
        'pid': pid
    };
    $.post('',
        post_data,
        function (json) {
            gc_table = $('#gcs_table tbody');
            gc_tr_clone=$('tr.gc:hidden').clone();  //复制一个行模板
            gc_table.children('tr:gt(1)').remove();  //每次load清除一下表格里的内容
            data = eval("(" + json + ")");
            if (data) {
                $(data).each(function (i, e) {
                        option = $('<option value="value">text</option>');
                        option.val(e['pk']);
                        option.text(e['fields']['cn']);
                        select.append(option);
                        //下面是写列表
                        gc_tr=gc_tr_clone.clone();
                        gc_tr.children('.gc_id').html(e['pk']);
                        gc_tr.children('.gc_pid').html(e['fields']['pid']);
                        gc_tr.children('.gc_cn').html(e['fields']['cn']);
                        gc_tr.children('.gc_state').html(e['fields']['state']);
                        gc_tr.children('.gc_priority').html(e['fields']['priority']);
                        gc_table.append(gc_tr.show());
                    }
                );
            }
        }
    );

}