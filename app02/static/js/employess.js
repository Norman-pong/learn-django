const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
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
    promptForEmployess: function (que) {
      const { title } = que.data()
      layer.open({
        type: 1,
        shade: false, // 不显示遮罩
        content: $('#Add_mployess'), // 捕获的元素
        end: function () {
          // layer.msg('关闭后的回调', {icon:6});
        }
      });
    },
  })

  form.on('submit(addEmployess)', function (data) {
    var field = data.field; // 获取表单字段值
    fetch('/api/employee/add_user', {
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