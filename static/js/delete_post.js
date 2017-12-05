$(document).ready(function() {
  var $deletePost = $('#delete-post');

  $deletePost.on('submit', function(event) {
    event.preventDefault();

    var csrftoken = $('[name=csrfmiddlewaretoken]').val();
    $.ajax({
      url: window.location.href,
      method: 'DELETE',
      headers: {
        'X-CSRFToken': csrftoken
      }

    })
    .done(function() {
      var url = window.location.href.split('/');
      window.location.href = url.slice(0, url.length - 2).join('/');
    })
    .fail(function(error) {
      console.log(error);
    });

    return false;
  });
});
