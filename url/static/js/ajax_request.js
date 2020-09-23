function url_table() {
    $.ajax({
        url: '/url_list', success: function(result){
            $("#url_info").html(result);
        }
     });
}

$( document ).ready(function() {
        url_table();
        var current_interval = setInterval(url_table, 1000);
        $("#interval").change(function(){
            clearInterval(current_interval)
            current_interval = setInterval(url_table, $("#interval option:selected" ).val() );
        });
});

