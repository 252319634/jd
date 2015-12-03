/**
 * Created by Administrator on 2015/12/2.
 */
/*====================django ajax ======*/
$.ajaxSetup({
     beforeSend: function(xhr, settings) {
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
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             //xhr.setRequestHeader("X_CSRFTOKEN", getCookie('csrftoken'));  //这句不行
             xhr.setRequestHeader("X-CSRFTOKEN", getCookie('csrftoken'));  // 这句起作用
         }
     }
});
/*===============================django ajax end===*/