from django.db import models
from datetime import datetime

# Create your models here.
class Pics(models.Model):
	name = models.CharField(max_length=200);
	addtime = models.DateTimeField(default=datetime.now)

	class Meta:
		db_table = "pics"
		
			