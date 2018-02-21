from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    #image = models.ImageField(upload_to = 'images/', default = 'images/None/affiche-warriors-movie.jpg')
    image_lien = models.CharField(max_length=400, default = 'http://www.croiseedesclans.fr/medias/images/affiche-warriors-movie.jpeg')
    resume = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
