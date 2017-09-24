from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Roboczy'),
        ('publish', 'Publiczny')
    )

    author = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique_for_date='publish')
    image = models.FileField(upload_to='post/')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        ordering = ['-publish']

    def get_absolute_url(self):
        return reverse('detail', args=[self.publish.year,
                                     self.publish.strftime('%m'),
                                     self.publish.strftime('%d'),
                                     self.slug])

    def __str__(self):
        return self.title
