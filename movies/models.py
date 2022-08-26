from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    movie_year = models.CharField(max_length=120)
    movie_director = models.CharField(max_length=120)
    movie_image = models.ImageField(upload_to="movies_pic", null=True)

    def __str__(self):
        return self.movie_name

    def average_rating(self):
        reviews = self.review_set.all()
        if reviews:
            rating_sum = sum([review.rating for review in reviews])
            return rating_sum / len(reviews)
        else:
            return 0

    def content_count(self):
        content = self.review_set.all()
        return len(content)


class Review(models.Model):
    content = models.CharField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return self.content
