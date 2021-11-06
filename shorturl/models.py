from django.db import models
from django.contrib.auth.models import User
import random, string


class Short_URL(models.Model):
    main_url = models.URLField(blank=False, max_length=1500)
    short_url = models.CharField(max_length=50, blank=True, unique=True)
    currentuser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.short_url
    

def randomurl():
    while True:
        shortlink =''.join(random.choice(string.ascii_letters) for _ in range(8))
    
        if not Short_URL.objects.filter(short_url=shortlink).exists():
            break

    return shortlink
