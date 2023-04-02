from django.contrib import admin

from .models import Post, PortImage, Slide, Cover, AboutFirstImage, AboutSecondImage, AboutGallery

admin.site.register(Post)
admin.site.register(Slide)
admin.site.register(PortImage)
admin.site.register(Cover)
admin.site.register(AboutFirstImage)
admin.site.register(AboutSecondImage)
admin.site.register(AboutGallery)