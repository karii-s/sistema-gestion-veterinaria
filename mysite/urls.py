from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [

    path("", RedirectView.as_view(url="/veterinaria/", permanent=False)),

    path("admin/", admin.site.urls),

    path("accounts/", include("django.contrib.auth.urls")),

    path("polls/", include("polls.urls")),

    path("veterinaria/", include("veterinaria.urls")),

]

urlpatterns += staticfiles_urlpatterns()