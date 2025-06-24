from django.urls import path
from .views import home, records # Import all needed views

app_name = 'sales'

urlpatterns = [
    path('', home, name='home'),                          # e.g., /sales/
    path('records/', records, name='records'),            # e.g., /sales/records/

]
