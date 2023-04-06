from django.db import models
from sorl.thumbnail import ImageField
from django.db import models


# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    discriptions=models.TextField(blank=False, null=False)
    image = ImageField()

    def __str__(self):
        return self.title
    


