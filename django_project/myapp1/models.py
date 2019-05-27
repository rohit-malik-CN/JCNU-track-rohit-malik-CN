from django.db import models

# Create your models here.


class Person(models.Model):
    person_name = models.CharField(max_length=200)


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_users = models.ManyToManyField(Person, through='ProjectUser', related_name='project')


class ProjectUser(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    is_mentor = models.BooleanField(default=False)



