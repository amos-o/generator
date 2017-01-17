$(document).ready(function() {
  $("#generator-button").on("click", function(){
    $.ajax("/generate",
      {
        success: function(data) {
          $('#target').removeClass('hidden');
          $('#target').html(data.data);
        },
        error: function() {
          $('#target').removeClass('hidden');
          $('#target').text('An error occurred');
        }
      });
  });
});
