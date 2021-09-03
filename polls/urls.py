from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_employee, name='show_employee'),
    path('create_emp/', views.create_employee,name='create_employee'),
    path('remove_emp/<int:id>', views.remove_employee,name='remove_employee'),
    path('edit_emp/<int:id>', views.edit_employee,name='update_employee'),
    
    

]
