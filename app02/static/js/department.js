const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
layui.use(['element', 'layer', 'util'], function () {
  var element = layui.element;
  var layer = layui.layer;
  var util = layui.util;
  var $ = layui.$;

  util.on('lay-on', {
    promptForDept: function (que) {
      const { title } = que.data()
      layer.prompt({ title: '添加部门', formType: 0, value: title || '' }, function (text, index) {
        layer.close(index);
        const body = new FormData()
        body.append('deptName', text)
        fetch('/api/dept', {
          method: 'POST',
          headers: { 'X-CSRFToken': csrftoken },
          body,
        }).then(res => res.json()).then(async () => {
          layer.msg('添加成功', { time: 1500 }, function () {
            location.reload()
          })
        })
      });
    },
    deleteDept: (element) => {
      const { id, title } = element.data()

      const body = new FormData()
      body.append('id', id)
      layer.confirm(`是否删除【${title}】`, {
        btn: ['确定', '取消'] //按钮
      }, function (test) {
        fetch('/api/dept', {
          method: 'DELETE',
          headers: { 'X-CSRFToken': csrftoken },
          body,
        }).then(res => res.json()).then(async () => {
          layer.msg('删除成功', { time: 1500 }, function () {
            location.reload()
          })
        })
      });
    },
    updateDept: (que) => {
      const { id, title } = que.data()
      layer.prompt({ title: '修改部门名称', formType: 0, value: title }, function (text, index) {
        layer.close(index);
        const body = new FormData()
        body.append('id',id)
        body.append('deptName', text)
        fetch('/api/dept', {
          method: 'PUT',
          headers: { 'X-CSRFToken': csrftoken },
          body,
        }).then(res => res.json()).then(async () => {
          layer.msg('修改成功', { time: 1500 }, function () {
            location.reload()
          })
        })
      });
    }
  })

  //头部事件
  util.event('lay-header-event', {
    menuLeft: function (othis) { // 左侧菜单事件
      layer.msg('展开左侧菜单的操作', { icon: 0 });
    },
    menuRight: function () {  // 右侧菜单事件
      layer.open({
        type: 1,
        title: '更多',
        content: '<div style="padding: 15px;">处理右侧面板的操作</div>',
        area: ['260px', '100%'],
        offset: 'rt', // 右上角
        anim: 'slideLeft', // 从右侧抽屉滑出
        shadeClose: true,
        scrollbar: false
      });
    },

  });
});