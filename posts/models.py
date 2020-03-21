from django.db import models

# Create your models here.

class Post(models.Model):
	
	title=models.CharField(max_length=50)
	pdate=models.DateTimeField()
	pic=models.ImageField(upload_to='media/')
	desc=models.TextField()

	def __str__(self):
		return self.title

	def displaydate(self):
		return self.pdate.strftime('%b %d %Y')

	def snippet(self):
		return self.desc[:100]
