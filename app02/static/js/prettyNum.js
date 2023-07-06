const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
$(function () {
  layui.use(['element', 'layer', 'util', 'laydate'], function () {
    var element = layui.element;
    var layer = layui.layer;
    var util = layui.util;
    var laydate = layui.laydate;
    var form = layui.form;
    var $ = layui.$;

    laydate.render({
      elem: '#date'
    });

    util.on('lay-on', {
      addMobile: function (que) {
        layer.open({
          type: 1,
          shade: false, // 不显示遮罩
          content: $('#add_mobile'), // 捕获的元素
          end: function () {
            // layer.msg('关闭后的回调', {icon:6});
          }
        });
      },
      employeeDetail: function (que) {
        const { id, name } = que.data()
        layer.open({
          type: 2,
          title: `编辑${name}`,
          shadeClose: true,
          shade: 0.8,
          area: ['500px', '70%'],
          content: `/employee/${id}/edit`, // iframe 的 url
          end: function () {
            location.reload()
          }
        });
      },
    })

    form.on('submit(addMobile)', function (data) {
      var field = data.field; // 获取表单字段值
      fetch('/mobile/list', {
        method: 'POST',
        headers: { 'X-CSRFToken': csrftoken, 'content-type': 'application/json' },
        body: JSON.stringify(field),
      }).then(res => res.json()).then(async () => {
        layer.msg('添加成功', { time: 1500 }, function () {
          location.reload()
        })
      })
      return false; // 阻止默认 form 跳转
    });
  });
})