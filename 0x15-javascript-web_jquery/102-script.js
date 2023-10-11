$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    $('DIV#hello').empty();
    const langType = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://www.fourtonfish.com/hellosalut/?lang=' + langType,
      success: function (response) {
        $('DIV#hello').append(response.hello);
      }
    });
  });
});
