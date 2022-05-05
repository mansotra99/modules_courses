from django.db import models

class TimeStampModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Module(TimeStampModel):
    # module_id
	# module_title
	# module_description
	# estimated_time_to_complete
	# module_points
    title = models.TextField()
    description = models.TextField()
    estimated_time_to_complete = models.TimeField(auto_now_add=False)
    points = models.IntegerField()
    
    class Meta:
        db_table = 'module'


class Chapter(TimeStampModel):
	# chapter_id
    # module_id
	# title
	# description
	module = models.ForeignKey(Module, blank=False, null=False, on_delete=models.CASCADE)
	title = models.TextField()
	description = models.TextField()

	class Meta:
		db_table = 'chapters'


class Quiz(TimeStampModel):
	# quiz_id
    # module_id
	# question,
	# answer_option,
	# answer_explanation
	# points:
	# options:["1","2","3"],
	module = models.ForeignKey(Module, blank=False, null=False, on_delete=models.CASCADE)
	points = models.IntegerField()
	explanation = models.TextField()
	question = models.TextField()
	correct_option = models.IntegerField()
	options = models.JSONField()

	class Meta:
		db_table='quiz'


class User(TimeStampModel):
	# user_id
	# email_id
	# password_hash
	# points
	# active
	# completed
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=50)
	total_points = models.IntegerField()
	is_active = models.BooleanField(default=True)

	class Meta:
		db_table='users'

    


class UserModule(TimeStampModel):
    # user_id
	# module_id
	# module_points_acheived
	# quiz_points_acheived
	# chapter
	# question
	# status ["started", "quiz_pending","completed"]
	STATUS_CHOICES = (
		('STARTED','STARTED'),
		('COMPLETED','COMPLETED'),
		('PENDING','PENDING'),
		('UNSEEN', 'UNSEEN')
	)
	user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
	module = models.ForeignKey(Module, blank=False, null=False, on_delete=models.CASCADE)
	chapter = models.ForeignKey(Chapter, blank=False, null=False, on_delete=models.CASCADE)
	module_points_acheived = models.IntegerField()
	quiz_points_acheived = models.IntegerField()
	module_status = models.CharField(max_length=15,choices=STATUS_CHOICES, default='STARTED')

	class Meta:
		db_table = 'user_modules'
