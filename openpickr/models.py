from django.db import models
from django.contrib.auth.models import Permission, User
from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=256)
    likes = models.BigIntegerField(default=0)
    comment = models.CharField(max_length=256,blank=True)
    image = models.ImageField(upload_to='images/')
    #image = ProcessedImageField(upload_to='avatars',processors=[ResizeToFill(350, 200)],format='JPEG',options={'quality': 60})
    image_thumbnail = ImageSpecField(source='image',processors=[ResizeToFill(350, 200)],format='JPEG',options={'quality': 60})
    is_like = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + ' - ' + self.comment
