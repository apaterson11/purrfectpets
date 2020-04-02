$(document).ready(function() {

    $('#like_btn').click(function() {
        var petIdVar, userIdVar;
        petIdVar = $(this).attr('data-petid');
        userIdVar = $(this).attr('data-userid');
        try {
            $.get('/purrfectpets_project/aww_pet/', {'pet_id': petIdVar, 'user_id':userIdVar}, function(data) {
               $('#awwCount').html(data);
               document.getElementById('unlike_btn').style.visibility = "visible";
               document.getElementById('like_btn').style.visibility = "hidden";
            });
        } catch (error) {
            alert(error);
        }
    });

    $('#unlike_btn').click(function() {
        var petIdVar, userIdVar;
        petIdVar = $(this).attr('data-petid');
        userIdVar = $(this).attr('data-userid');
        try {
            $.get('/purrfectpets_project/disaww_pet/', {'pet_id': petIdVar, 'user_id':userIdVar}, function(data) {
                $('#awwCount').html(data);
                document.getElementById('unlike_btn').style.visibility = "hidden";
               document.getElementById('like_btn').style.visibility = "visible";
            })
            
        } catch (error) {
            alert(error);
        }
    });
});