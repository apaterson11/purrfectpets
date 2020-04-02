$(document).ready(function() {
    $('#like_btn').click(function(e) {
        alert('clicked!');
        e.preventDefault();
        var petIdVar;
        petIdVar = $(this).attr('data-petid');
        userIdVar = $(this).attr('data-userid')
        try {
            $.get('/purrfectpets_project/aww_pet/', {'pet_id': petIdVar, 'user_id':userIdVar}, function(data) {
               alert('success');
                alert('but not this far.');
               $('#awwCount').html(data);
                $('#like_btn').hide();
            });
            alert('noError')
        } catch (error) {
            alert(error);
        }
        

        
        
    });
});