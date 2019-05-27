from django.urls import path
from myapp1 import views

urlpatterns = [
    path('user/', views.create_user, name='Create_User'),
    path('project/', views.create_project, name='Create Project'),
    path('project/user/', views.assign_project, name='Assign Project'),
    path('project/mentor/', views.assign_mentors, name='Assign Mentor'),
    path('mentor/<int:mentor_id>/mentees/', views.get_mentees, name='Get mentees'),
    path('mentor/<int:mentor_id>/projects/', views.get_projects, name='Get Projects'),
    path('project/<int:project_id>/', views.get_users, name="Get users and mentors"),
]