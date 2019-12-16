
from django.contrib import admin
from django.urls import path, include
from .router import router


urlpatterns = [
    path('', admin.site.urls),
    path('laptops/', include(router.urls)),
   

]

