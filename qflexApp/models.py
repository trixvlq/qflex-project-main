from django.db import models
from pytils.translit import slugify

class Genre(models.Model):
    genreName = models.CharField("Genre name", max_length=255)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.genreName

    def save(self, *args, **kwargs):
        self.slug = slugify(self.genreName)
        super().save(*args, **kwargs)


class Movie(models.Model):
    movieName = models.CharField("Movie name", max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Genre")
    producer = models.CharField("Producer", max_length=255)
    cover = models.CharField("Link to cover", max_length=500)
    poster = models.CharField("Link to poster", max_length=500)
    year = models.IntegerField("Year")
    rating = models.FloatField("Rating")
    movieLink = models.CharField("Youtube movie link", max_length=500)
    description = models.TextField("Description")
    isTopTen = models.BooleanField("Is top ten", default=False, blank=True, null=True)
    isRecommended = models.BooleanField("Is Recommended", default=False, blank=True, null=True)

    def __str__(self):
        return self.movieName

    def desc(self):
        return self.description[:200]