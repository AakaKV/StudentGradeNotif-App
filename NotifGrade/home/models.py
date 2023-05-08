from django.db import models
#imports the calendar logic as calogic for brevity. Note that directory is placed then a dot

# Create your models here.
class Calendar(models.Model):
	# objects = CalendarManager()
	# account = models.ForeignKey(Account)
	uri = models.CharField(max_length = 255, unique = True)
	title = models.CharField(max_length = 100)
	where = models.CharField(max_length = 100, blank = True)
	timezone = models.CharField(max_length = 100, blank = True)
	summary = models.TextField()
	feed_uri = models.CharField(max_length = 255, blank = True)