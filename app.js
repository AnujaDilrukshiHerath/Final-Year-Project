$(document).ready(function() {

  // Submit form
  $('#transliteration-form').submit(function (event) {
    event.preventDefault();
    var inputText = $('#input-text').val();

    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:5000/tanglish/test',
      contentType: 'application/json',
      data: JSON.stringify({'text': inputText}),
      success: function (response) {
        var outputText = response['result'];
        $('#output-text').val(outputText);
      },
      error: function () {
        alert('Error: Failed to connect to server.');
      }
    });

  });

  // Get suggestions
  $('#suggestion-form').submit(function (event) {
    event.preventDefault();
    var suggestionText = $('#suggestion-input').val();

    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:5000/suggestions',
      contentType: 'application/json',
      data: JSON.stringify({'text': suggestionText}),
      success: function (response) {
        var suggestionList = response['suggestions'];
        var suggestionHTML = '';
        for (var i = 0; i < suggestionList.length; i++) {
          suggestionHTML += '<li>' + suggestionList[i] + '</li>';
        }
        $('#suggestion-list').html(suggestionHTML);
      },
      error: function () {
        alert('Error: Failed to connect to server.');
      }
    });

  });

});