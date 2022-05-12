from django.urls import path
from measurement.views import SensorsView, SensorsInfoView, MeasurementAdd

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>', SensorsInfoView.as_view()),
    path('measurement/', MeasurementAdd.as_view())
]
