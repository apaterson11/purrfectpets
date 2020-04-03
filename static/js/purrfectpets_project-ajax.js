// all functionality used in pet_page.html

$(document).ready(function() {

    // when like button is clicked it is set to hidden and the unlike button becomes visible
    // Also passes the user id and pet id into the awwPet view get method
    // and returns the count of the awwCount
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


    // reverse of like button
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