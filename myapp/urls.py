from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

    path('',views.home,name='home'),
    path('storetext',views.storetext,name='storetext'),
    path('display1',views.display1,name='display1'),
    path('storeImage',views.storeImage,name='storeImage'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)