from django.contrib import admin
from .models import AnnounceText,StoreImages,Dummy,Video,TimeTable
# Register your models here.
admin.site.register(AnnounceText)
admin.site.register(StoreImages)
admin.site.register(Dummy)
admin.site.register(Video)
admin.site.register(TimeTable)