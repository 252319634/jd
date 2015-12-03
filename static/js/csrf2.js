/*====================django ajax ======*/
$.ajaxSetup({

    headers: {
            "X-CSRFToken": $("input[name=csrfmiddlewaretoken]").val()
            }

     //beforeSend: function(xhr, settings) {
     //    alert(settings.data);
     //    settings.data=settings.data+'&csrfmiddlewaretoken='+$("input[name=csrfmiddlewaretoken]").val();
     //    alert(settings.data);
     //}
});
/*===============================django ajax end===*/
