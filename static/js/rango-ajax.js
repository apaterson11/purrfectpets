$(document).ready(function() {
    $('#like_btn').click(function(e) {
        e.preventDefault();
        var catecategoryIdVar;
        catecategoryIdVar = $(this).attr('data-petid');
        $.get('/purrfectpets_project/aww_pet/', {'pet_id': catecategoryIdVar}, function(data) {
                alert('success');
                $('#awwCount').html(data);
                $('#like_btn').hide();
            })
    });
});