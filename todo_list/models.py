from django.db import models

class Todos(models.Model):
    add_item = models.CharField(max_length=200)
    added_on = models.BooleanField(default=False)

    def __str__(self):
        return self.add_item

