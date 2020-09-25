function url_table() {
    $("table > tbody > tr.url_row").each(function() {
        let row = $(this);
        check_paused = row.find("input.pause:checked").length;
        if (! check_paused) {
            let id = row.find("td.id").text();
            $.ajax({
                url: "/urls/"+ id +"/", success: function(status_code){
                    let code_cell = row.find("td.status_code");
                    $(code_cell).html(status_code);
                    let color_class
                    if (status_code == 200) {
                        color_class = "status_code_green";
                    } else {
                        color_class = "status_code_red"
                    }
                    row.removeClass("status_code_green status_code_red").addClass(color_class);;

                }
            });
        }
    });
}


$( document ).ready(function() {
        let current_interval = setInterval(url_table, 3000);
        $("#interval").change(function(){
            clearInterval(current_interval)
            current_interval = setInterval(url_table, $("#interval option:selected" ).val() );
        });

});

