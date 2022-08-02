<script>
$('#submit').on('click', function(){
	var name = $('#name').val()
	var description = $('#description').val()
	var owner = $('#owner').val()
	var student = $('#student').val()
	$.ajax({
		type: "POST",
		url: '/api/v1/user/group/create/',
		data:JSON.stringify({
			student:student,
			name:name,
			owner:owner,
			description:description,
			csrfmiddlewaretoken: csrftoken
		}),
		contentType: "application/json; charset=utf-8",
		dataType: "json",
		beforeSend: function (xhr) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		},
		success: function(data){
			window.location = '/user/student-groups'
		}
	})
});
</script>