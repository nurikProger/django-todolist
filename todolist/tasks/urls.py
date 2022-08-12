from django.urls import path
from . import views


urlpatterns = [
path('', views.index, name='index'),
path('changestatus/<int:id>', views.changestatus, name="changestatus"),
path('delete/<int:id>', views.delete, name="delete"),
path('add/', views.add, name='add'),
path('add/addrecord/', views.addrecord, name="addrecord"),
path('update/<int:id>', views.update, name="update"),
path('update/updaterecord/<int:id>', views.updaterecord, name="updaterecord")
]