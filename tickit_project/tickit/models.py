from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=200)
    location = models.TextField()
    capacity = models.PositiveIntegerField()
    website_url = models.TextField()
    venue_description = models.TextField()
    image_url = models.TextField(null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    ticket_price = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    image_url = models.TextField(null=True)
    event_description = models.TextField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name
