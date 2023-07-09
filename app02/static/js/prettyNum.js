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
            fetch(`/mobile/${id}`, {
              method: 'GET',
            }).then(res => res.json()).then(async (data) => {
              Object.keys(data).forEach(item => $(`input[name=${item}]`).val(data[item]))
              $($('#formData .layui-btn')[0]).attr('lay-filter', 'update').attr('id', id)
              layer.open({
                type: 1,
                title: `编辑手机号码`,
                shade: false, // 不显示遮罩
                content: $('#formData'), // 捕获的元素
                end: () => Object.keys(data).forEach(item => $(`input[name=${item}]`).val(''))
              });
            })
            return
          case 'delete':
            fetch('/mobile/list', {
              method: 'DELETE',
              headers: { 'content-type': 'application/json' },
              body: JSON.stringify({ id }),
            }).then(() => location.reload())
            return
          default:
            $($('#formData .layui-btn')[0]).attr('lay-filter', 'save')
            layer.open({
              type: 1,
              title: `添加手机号码`,
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

    form.on('submit(update)', function (data) {
      const field = data.field; // 获取表单字段值
      const id = $(data.elem)[0].id
      fetch(`/mobile/${id}`, {
        method: 'UPDATE',
        headers: { 'X-CSRFToken': csrftoken, 'content-type': 'application/json' },
        body: JSON.stringify(field),
      }).then(res => {
        layer.msg('保存成功', { time: 1000 }, function () {
          location.reload()
        })
      })
      return false; // 阻止默认 form 跳转
    });
  });
})