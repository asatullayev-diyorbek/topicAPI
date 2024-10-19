from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Topic(Base):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='topic/', null=True, blank=True)

    class Meta:
        verbose_name = "Mavzu"
        verbose_name_plural = "Mavzular"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return self.image.url
        return None

class Comment(Base):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='comment/', null=True, blank=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ['-created_at']

    def __str__(self):
        return self.user.get_full_name() + ' ' + self.topic.title + ' ' + self.created_at.strftime("%m/%d/%Y, %H:%M:%S")

    def get_image(self):
        if self.image:
            return self.image.url
        return None


        
