from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('main_page/', levels),
    path("levels/<int:level_id>/", level_detail, name="level_detail"),
    path("level_part_info/<int:level_id>/", level_part_info, name="level_part_info"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)