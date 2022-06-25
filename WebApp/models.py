from django.db import models

# Create your models here.


class Info(models.Model):
    # Images
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
