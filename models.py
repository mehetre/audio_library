from django.db import models

# Create your models here.



# Create your models here.

class Song(models.Model):
    podcast='Podcast'
    song='Song'
    audiobook='AudioBook'
    audio_types=[(podcast,'Podcast'),
                 (song,'Song'),
                 (audiobook,'AudioBook')]
    title = models.CharField(max_length=100)
    audio_choice=models.CharField(max_length=50,choices=audio_types)
    songfile = models.FileField()
    seconds = models.IntegerField(default=True)
    upload_date=models.DateTimeField(auto_now=True)
    isPlaying = False
    def __str__(self):
        return self.title
