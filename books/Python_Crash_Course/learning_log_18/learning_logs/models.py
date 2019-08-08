from django.db import models

# Create your models here.
class Topic(models.Model):
	"""User learning model"""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		"""return a string representation of the model"""
		return self.text

class Entry(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "entries"
	
	def __str__(self):
		return self.text[:50] + "..."