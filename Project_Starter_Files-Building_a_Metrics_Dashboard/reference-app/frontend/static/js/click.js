$(document).ready(function () {

    // all custom jQuery will go here
    $("#firstbutton").click(function () {
        const button = $(this);
        button.prop("disabled", true).html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...');
        
        $.ajax({
            url: "http://localhost:8081/api",
            complete: function() {
                button.prop("disabled", false).text("Press Me For A Good Test");
            },
            success: function (result) {
                button.removeClass("btn-primary").addClass("btn-success");
            },
            error: function(xhr) {
                button.removeClass("btn-primary").addClass("btn-danger");
            }
        });
    });    
    $("#secondbutton").click(function () {
        const button = $(this);
        button.prop("disabled", true).html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...');
        
        $.ajax({
            url: "http://localhost:8082",
            complete: function() {
                button.prop("disabled", false).text("Press Me For A Good Test");
            },
            success: function (result) {
                button.removeClass("btn-primary").addClass("btn-success");
            },
            error: function(xhr) {
                button.removeClass("btn-primary").addClass("btn-danger");
            }
        });    
    });    
});