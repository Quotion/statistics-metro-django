from django.urls import path, include
from mainstat.views import *
from statisticsDJ import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPage.as_view(), name="main_page"),
    path('general/', General.as_view(), name="general"),
    path('statistics/', PageStatistics.as_view(), name="statistics"),
    path('serverjoin/', JoinServer.as_view(), name="join_server"),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
