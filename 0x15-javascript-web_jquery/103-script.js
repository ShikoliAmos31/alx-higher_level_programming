$(document).ready(function(){
    function translateHello(languageCode) {
        $.getJSON("https://www.fourtonfish.com/hellosalut/hello/", function(data){
            var helloTranslation = data[languageCode];
            if (helloTranslation) {
                $("#hello").text(helloTranslation);
            } else {
                $("#hello").text("Translation not found");
            }
        });
    }

    $("#btn_translate").click(function(){
        var languageCode = $("#language_code").val();
        translateHello(languageCode);
    });

    $("#language_code").keypress(function(event){
        if (event.keyCode === 13) {
            var languageCode = $("#language_code").val();
            translateHello(languageCode);
        }
    });
});
