// fetches and prints how to say “Hello” depending on the language


$(document).ready(function(){
    $("#btn_translate").click(function(){
        var languageCode = $("#language_code").val();
        $.ajax({
            url: "https://www.fourtonfish.com/hellosalut/hello/",
            data: { lang: languageCode },
            dataType: "json",
            success: function(response){
                var translation = response[languageCode];
                if (translation) {
                    $("#hello").text(translation);
                } else {
                    $("#hello").text("Translation not found");
                }
            },
            error: function(){
                $("#hello").text("Error fetching translation");
            }
        });
    });
});
