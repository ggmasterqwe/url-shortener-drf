from django.db import models
from django.contrib.auth import get_user_model
import hashlib
# Create your models here.

class Url(models.Model):
    user_url = models.URLField()
    slug = models.SlugField(unique=True, max_length=30, blank=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def save(self, *args, **kwargs):
        if not self.slug:
            hash_slug = hashlib.sha1("{}{}".format(self.id, self.user_url).
                                     encode("UTF-8")).hexdigest()
            self.slug = hash_slug[:7]


        return super().save(*args, **kwargs)


