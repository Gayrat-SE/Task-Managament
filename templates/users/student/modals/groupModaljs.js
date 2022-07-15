<script>
	$('#submit').on('click', function(){
		var name = $('#name').val()
		var description = $('#description').val()
		var owner = $('#owner').val()
		var student = $('#student').val()
		console.log(student)
		$.ajax({
			type: "POST",
			url: '/api/v1/user/group/create',
			data:JSON.stringify({
				student:student,
				name:name,
				owner:owner,
				description:description,
			}),
			contentType: "application/json; charset=utf-8",
			dataType: "json",
			success: function(data){
				window.location = '/user/student-groups'
			}
		})
	});
</script>