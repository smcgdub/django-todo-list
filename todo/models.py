from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=200)
    done = models.BooleanField(default=False, null=False, blank=False)
    # date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
