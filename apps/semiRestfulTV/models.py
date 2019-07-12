from django.db import models

class showManager(models.Manager):
    def basic_validator(self, showData):
        errors = {}

        if len(showData['title']) < 2:
            errors["title"] = "TV Show Name must be at least two [2] characters"
        if len(showData['network']) < 3:
            errors["network"] = "Network Name must be at least three [3] characters"
        if len(showData['description']) < 10:
            errors["description"] = "TV Show Description must be at least ten [10] characters"
        return errors



class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    releaseDate = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)
    objects = showManager()
