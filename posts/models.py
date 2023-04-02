from django.db import models


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    desc = models.CharField(max_length=200, default='SOME STRING')

    def __str__(self):
        return self.title


class Slide(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Cover(models.Model):
    cover_text = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cover_text


class PortImage(models.Model):
    category = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.category


class AboutFirstImage(models.Model):
    dummy = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.dummy


class AboutSecondImage(models.Model):
    dummy = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.dummy


class AboutGallery(models.Model):
    galleryText = models.TextField(null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.galleryText



