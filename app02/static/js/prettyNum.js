const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
$(function () {
  layui.use(['element', 'layer', 'util', 'laydate'], function () {
    var element = layui.element;
    var layer = layui.layer;
    var util = layui.util;
    var form = layui.form;
    var $ = layui.$;

    util.on('lay-on', {
      mobileFunc: function (que) {
        const { id } = que.data()
        switch ($(que).attr('dispatch')) {
          case 'update':
            layer.open({
              type: 2,
              title: `编辑`,
              shadeClose: true,
              shade: 0.8,
              area: ['500px', '70%'],
              content: `/mobile/${id}`, // iframe 的 url
              end: function () {
                location.reload()
              }
            });
            return
          case 'delete':
            fetch('/mobile/list', {
              method: 'DELETE',
              headers: { 'content-type': 'application/json' },
              body: JSON.stringify({ id }),
            }).then(() => location.reload())
            return
          default:
            layer.open({
              type: 1,
              shade: false, // 不显示遮罩
              content: $('#formData'), // 捕获的元素
            });

        }

      }
    })

    form.on('submit(save)', function (data) {
      var field = data.field; // 获取表单字段值
      fetch('/mobile/list', {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken, 'content-type': 'application/json' },
        body: JSON.stringify(field),
      }).then(res => res.json()).then(async () => {
        layer.msg('添加成功', { time: 1000 }, function () {
          location.reload()
        })
      })
      return false; // 阻止默认 form 跳转
    });
  });
})