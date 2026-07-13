$(document).ready(function() {
    $('.col-lg-8 textarea').addClass('form-control');
    $('.col-lg-10 textarea').addClass('form-control');
    $('.col-lg-10 input').addClass('form-control');
    $('.col-lg-6 textarea').addClass('form-control');
    $('#id_summary').parent().removeClass('col-lg-4').addClass('col-lg-8');
    $('#id_summary').addClass('form-control');
    $('#id_summary').attr("rows", "10");
    $('#id_materials').attr("rows","20");
    $('.col-lg-4 :input').addClass('form-control');
    $('.col-lg-3 :input').addClass('form-control');
    // $('.wmd-panel textarea').addClass('form-control');
    // $('#id_materials_wmd_button_bar').before('<a class="pre-link pull-right various btn btn-primary btn-xs" role="button" href="#weepre" alt="点击预览微课内容">预览微课</a>');

    // var _s = $('#id_materials_wmd_preview');
    // _s.wrap('<div id="weepre" style="display: none;"></div>');
});

$(document).ready(function() {
    $('.lesson-level>div').addClass('list-inline');
});

$(document).ready(function() {
  $('.lesson-level :input').removeClass('form-control');
});


function fav(id) {
    var _s = '.fav a[rel='+id+']';
    //var $fav = jQuery(".fav");
    $.get('fav/');
        $(_s).attr('href', 'javascript:unfav('+id+')');
    $(_s).html('你已加入');
};

function unfav(id) {
    var _s = '.fav a[rel='+id+']';
    //var $fav = jQuery(".fav");
    $.get('unfav/');
        $(_s).attr('href', 'javascript:fav('+id+')');
    $(_s).html('加入学习');
};

function mfav(id) {
    var _s = '.fav a[rel='+id+']';
    //var $fav = jQuery(".fav");
    $.get('fav/');
        $(_s).attr('href', 'javascript:munfav('+id+')');
    $(_s).html('不去了');
};

function munfav(id) {
    var _s = '.fav a[rel='+id+']';
    //var $fav = jQuery(".fav");
    $.get('unfav/');
        $(_s).attr('href', 'javascript:mfav('+id+')');
    $(_s).html('我要去');
};

$(function() {
    $.scrollUp({
        scrollName: 'scrollUp',
        topDistance: '500',
        topSpeed: 300,
        animation: 'fade',
        animationInSpeed: 200,
        animationOutSpeed: 200,
        scrollText: '',
        activeOverlay: false
    });
});

/*
$(document).ready(function() {
    $(".various").fancybox({
        maxWidth        : 1024,
        maxHeight       : 640,
        autoSize        : false,
        fitToView       : false,
        width           : '100%',
        height          : '100%',
        closeClick      : false,
        openEffect      : 'none',
        closeEffect     : 'none',

    });
});
*/

//comments
$(document).ready(function() {
    $('form.form-comment').submit(function() {
        var comment=$('#id_comment').val();
        if(!comment || comment.length<4) {
            alert("你所表达的内容太过精练了吧，再想想！");
            return false;
        }
    });
});

// rm
$(document).ready(function() {
    $('.rm').click(function() {
        var msg = '删除后不能再恢复，确认删除吗？';
        if (confirm(msg) == true) {
            return true;
        }else{
            return false;
        }
    });
});

// 读取目录
function content_list(level) {
    $('div.lesson-content h' + level).each(function (index) {
        $(this).attr({'id': 'headline'+level});
        $(this).prepend(['<a class="anchor-1" name="', index+1, '"></a>'].join(''));
        $('#content-a table').append(['<tr><td><a href="#', index+1, '">', index+1, ' ', $(this).text(), '</tr></td>'].join(''));
    });
}

$(document).ready(function() {
    var header1 = $('.lesson-content h1');

    if(header1[0]) {
        content_list(1);
    }else{
        content_list(2);
    }
});

$(function () {
  $('div.thumbnail').hover(function(){
    $(this).addClass('le-border');
  }, function() {
      $(this).removeClass('le-border');
    });
});

/*
$(function () {
  $('li#draft-list').hover(
    function() {
      $(this).find('div.pull-right').removeClass('hide');
    }, function() {
      $(this).find('div.pull-right').addClass('hide');
    });
});

*/

// 编辑草稿时ajax方式进行保存

// $(document).ready(function() {
//   $('#draft-save-1').click(function() {
//     var draft_name = $('#id_name').val();
//     var draft_materials = $('#id_materials').val();
//     alert(draft_materials);
//     $.ajax({
//       url: '/lesson/'+$('#draft-save').attr("rel") + '/edit/', 
//       type: 'POST',
//       //dataType: "json",
//       data: {
// 	name: draft_name,
// 	materials: draft_materials,
// 	csrfmiddlewaretoken: '{{ csrf_token }}'
// 	},
//       success: function(msg) {
// 	$('#save-msg').removeClass('hide').html(msg).show(300).delay(2000).hide(300);

//       }
//     });
//     return false;
//   });
// });

$(document).ready(function() {
  
  $('#draft-save').click(function() {
    var draft_name = $('#id_name').val();
    var draft_materials = $('#id_materials').val();
    // alert(draft_materials);
    $.ajax({
      url: '/lesson/'+$('#draft-save').attr("rel") + '/edit/', 
      type: 'POST',
      //dataType: "json",
      data: {
	name: draft_name,
	materials: draft_materials,
	csrfmiddlewaretoken: '{{ csrf_token }}'
	},
      success: function(msg) {
	$('#save-msg').removeClass('hide').html(msg).show(300).delay(2000).hide(300);

      }
    });
    return false;
  });
});



$(document).ready(function() {
  
  var return_var = false;
  $('.lesson-publish').click(function(e) {
    var draft_name = $('#id_name').val();
    var draft_materials = $('#id_materials').val();
    
    $.ajax({
      async: false,
      url: '/lesson/'+$('#draft-save').attr("rel") + '/edit/', 
      type: 'POST',
      //dataType: "json",
      data: {
	name: draft_name,
	materials: draft_materials,
	csrfmiddlewaretoken: '{{ csrf_token }}'
	},
      success: function(msg) {

	return_val = true;
      }
    });
    return return_val;
  });
});

// 微课简介预览
$(document).ready(function() {
    $('.draft-pre').click(function() {
        var msg = '预览前，需要你完整填写了微课简介及相关内容并点击“保存”按钮进行保存，你确定你已做好了保存吗？';
        if (confirm(msg) == true) {
            return true;
        }else{
            return false;
        }
    });
});

/*
$(function () {
  $('#ls-publish').click(function() {
    var desc = $('#id_desc').val();
    if(desc || desc.length<0){
      alert('你的微课简介还没有填写完整呢！');
      return false;
      }
  });
});

*/

/*

$(function () {
  var level = $("input[name='level']:checked").val();
  $("#id_image").change(function() {
    var img_name = $(this).val();
    alert(img_name);
  });
  alert(level);
});

*/

// 微课内容中，图片超过最大尺寸时进行自动调整
$(document).ready(function() {
  var maxWidth=833;
  $(".lesson-content img").each(function(){
    var image = $(this);
    if(image.width()>=maxWidth) {
      image.width(maxWidth);
    }
  });
});

// 导航栏当前页高亮
$(function () {
  var url = window.location;
  $('ul.nav a[href="'+url+'"]').parent().addClass('active');
  $('ul.nav a').filter(function () {
    return this.href == url;
  }).parent().addClass('active');
});
  
})
