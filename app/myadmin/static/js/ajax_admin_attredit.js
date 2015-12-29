function save() {
    post_data = {
        'method': 'save',
        'gc_cid': $('#gc_cid').val(),
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
function del(e) {
    //删除分类
    var gc_cid = $('#gc_cid').val();
    //alert(gc_cid);
    post_data = {
        'method': 'del',
        'gc_cid': gc_cid
    };
    $.post('',
        post_data,
        function (data) {
            alert(data.msg);
            if (data.state == 0) {

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
    //alert(post_data.gc_state);
    $.post('',
        post_data,
        function (data) {
            alert(data.msg);
            if (data.state == 0) {
                cn.val('');
                state.val('');
                priority.val('');
            }

        }
    );
}

function add_attr_value(e) {
    var ga_id = $('#add_ga_id');
    var gav = $('#add_gav');
    post_data = {
        'method': 'add_attr_value',
        'ga_id': ga_id.val(),
        'gav': gav.val()
    };
    //alert(post_data.gc_state);
    $.post('',
        post_data,
        function (data) {
                alert(data.msg);
        }
    );
}

function del_attr_value(e) {
    //删除分类
    var gav_id = $(e).parent().parent().find('td:first').html();
    alert(gav_id);
    post_data = {
        'method': 'del_attr_value',
        'gav_id': gav_id
    };
    $.post('',
        post_data,
        function (data) {
            alert(data.msg);
        }
    );
}