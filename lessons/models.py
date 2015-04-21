from django.db import models

# Create your models here.


class Activity(models.Model):
	"""
	An activity is a collection of steps
	"""

	# REQUIRED
	title = models.CharField(max_length=100, unique=True)
	language = models.CharField(max_length=15)
	votecount = models.IntegerField(default=0)

	#OPTIONAL
	level = models.CharField(max_length=10, blank=True, null=True)

	# activities have a collection of steps - access through Activity.steps
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Activities"
		

class Step(models.Model):
	"""
	A step is the atomic unit of instruction
	"""

	# REQUIRED
	description = models.CharField(max_length=100)
	sequence = models.IntegerField()
	activity = models.ForeignKey(Activity, related_name='steps')

	# OPTIONAL
	teachingnote = models.CharField(max_length=100, blank=True, null=True)
	imagepath = models.ImageField(upload_to="step-images", blank=True, null=True)

	def __unicode__(self):
		return self.description

class Tag(models.Model):
	"""
	A tag is applied to an activity
	"""

	# REQUIRED
	description = models.CharField(max_length=20)
	activity = models.ForeignKey(Activity, related_name='tags')

	def __unicode__(self):
		return self.description



