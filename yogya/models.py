from django.db import models
from django.contrib.auth.models import User


class Exhibit(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Talent(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exhibit = models.ForeignKey(
        Exhibit, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, null=True, blank=True)
    talent = models.ForeignKey(
        Talent, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exhibit = models.ForeignKey(
        Exhibit, on_delete=models.CASCADE, null=True, blank=True)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, null=True, blank=True)
    talent = models.ForeignKey(
        Talent, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)