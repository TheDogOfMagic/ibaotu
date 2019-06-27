'use strict'

//alert('11111')
$(document).ready(function(){
    $('button').click(function(){
        var text = $.ajax('/api/ibaotu', {data:{'baotu':$('.edit-font').text()}}).done(function (data) {
                alert('成功：'+SON.stringify(data));
            }).fail(function (xhr, status) {
                alert('失败: ' + xhr.status + ', 原因: ' + status);
            }).always(function () {
//                alert('请求完成: 无论成功或失败都会调用');
            });
            });
});

