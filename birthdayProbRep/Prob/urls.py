from django.contrib import admin
from django.urls import path, include # new
from Prob.views import homeView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeView), 
]
