<script>
$('#submit').on('click', function(){
	var studentgroups = $('#group_select').val();
	var username = $('#username').val();
	var first_name = $('#first-name').val();
	var last_name = $('#last-name').val();
	var birthday = $('#date').val();
	var gender = $('#gender').val();
	var email = $('#email').val();
	var password = $('#password').val();
	var phone = $('#phone').val();
	var father_name = $('#father_name').val()
	$.ajax({
		type:'POST',
		url: '/api/v1/user/student/create/',
		data: {
			studentgroups:studentgroups,
			gender: gender,
			username:username,
			first_name:first_name,
			last_name:last_name,
			birthday:birthday,
			password:password,
			email:email,
			phone:phone,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
			father_name:father_name,
		},
		beforeSend: function (xhr) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		},
		success: function(data){
			{% for id in student %}
			window.location = '/user/student-list/{{ id.id }}';
			{% endfor %}

		},
		error: function(data){
			console.log(data.responseJSON.username[0])
		}
	})
});
</script>