$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('#language_code').val();
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      success: function (data) {
        $('#hello').text(data.hello);
      },
      error: function () {
        $('#hello').text('Error: Failed to fetch translation.');
      }
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (event) {
    if (event.key === 'Enter') {
      fetchTranslation();
    }
  });
});
