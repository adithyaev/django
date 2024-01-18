from django . urls import path
from . import views

urlpatterns=[
    path('addstudent',views.add_student,name='addstudent'),
    path('loadstudent',views.load_student,name='loadstudent'),
    path('deletestudent/<int:sid>',views.delete_student,name='deletestudent'),
    path('updatestudent/<int:sid>',views.update_student,name='updatestudent'),
]