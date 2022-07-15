<script>
$('#submit').on('click', function(){
		var username = $('#username').val();
		var first_name = $('#first-name').val();
		var last_name = $('#last-name').val();
		var birthday = $('#date').val();
		var gender = $('#gender').val();
		var email = $('#email').val();
		var password = $('#password').val();
		var phone = $('#phone').val();
		$.ajax({
			type:'POST',
			url: '/api/v1/user/teacher/create/',
			data: {
				gender: gender,
				username:username,
				first_name:first_name,
				last_name:last_name,
				birthday:birthday,
				password:password,
				email:email,
				phone:phone,
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
			},
			success: function(data){
				window.location = '/users/teacher-list/';
			}
		})
	});
</script>