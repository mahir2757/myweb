from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('storedata/',views.storedata),
    path('viewData/',views.view_data),
    path('showdata/',views.showdata),
    path('delete/<roll>', views.deldata),
    path('edit/<roll>',views.editdata),
]