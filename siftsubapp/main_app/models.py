from django.db import models
from django.contrib.auth.models import User

LOGO_CHOICES = [
    ('Adobe.svg', 'Adobe'),
    ('Ahrefs.svg', 'Ahrefs'),
    ('Airtable.svg', 'Airtable'),
    ('Amazon.svg', 'Amazon'),
    ('Apple.svg', 'Apple'),
    ('Asana.svg', 'Asana'),
    ('Calendly.svg', 'Calendly'),
    ('Canva.svg', 'Canva'),
    ('Circle.svg', 'Circle'),
    ('Dropbox.svg', 'Dropbox'),
    ('Grammarly.svg', 'Grammarly'),
    ('Invision.svg', 'Invision'),
    ('Loom.svg', 'Loom'),
    ('Microsoft.svg', 'Microsoft'),
    ('Miro.svg', 'Miro'),
    ('Monday.svg', 'Monday'),
    ('Netflix.svg', 'Netflix'),
    ('Patreon.svg', 'Patreon'),
    ('Shutterstock.svg', 'Shutterstock'),
    ('Sketch.svg', 'Sketch'),
    ('Spotify.svg', 'Spotify'),
    ('Webflow.svg', 'Webflow'),
    ('Zapier.svg', 'Zapier'),
]

SUBSCRIPTION_STATUS = [
    ('active', 'Active'),
    ('paused', 'Paused'),
    ('canceled', 'Canceled'),
]

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    renewal_date = models.DateField()
    status = models.CharField(max_length=20, choices=SUBSCRIPTION_STATUS, default='active')
    logo = models.CharField(max_length=100, choices=LOGO_CHOICES, blank=True)
    uploaded_logo = models.ImageField(upload_to='uploaded_logos/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

