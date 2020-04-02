$(document).ready(function() {
    $('#like_btn').click(function(e) {
        alert('clicked!');
        e.preventDefault();
        var catecategoryIdVar;
        catecategoryIdVar = $(this).attr('data-petid');
        alert('we get this far!');
        $.get('/purrfectpets_project/aww_pet/', {'pet_id': catecategoryIdVar}, function(data) {
                alert('success');
                alert('but not this far.');
                $('#awwCount').html(data);
                $('#like_btn').hide();
            })
    });
});