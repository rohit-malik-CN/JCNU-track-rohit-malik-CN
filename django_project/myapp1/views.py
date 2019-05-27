from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import ProjectUser, Project, Person
from .error_handle import error_checks


@csrf_exempt
@error_checks
@require_http_methods(["OPTIONS", "POST"])
def create_user(request):
    if request.method == "OPTIONS":
        return HttpResponse(json.dumps({"Message": "wait"}))
    user_info = json.loads(request.body.decode('utf-8'))
    user = Person(person_name=user_info["user_name"])
    user.save()
    return HttpResponse(json.dumps(200))


@csrf_exempt
@error_checks
@require_http_methods(["OPTIONS", "POST"])
def create_project(request):
    if request.method == "OPTIONS":
        return HttpResponse(json.dumps({"Message": "wait"}))
    project_info = json.loads(request.body.decode('utf-8'))
    project = Project(project_name=project_info["project_name"])
    project.save()
    return HttpResponse(json.dumps(200))


@csrf_exempt
@error_checks
@require_http_methods(["OPTIONS", "POST"])
def assign_project(request):
    if request.method == "OPTIONS":
        return HttpResponse(json.dumps({"Message": "wait"}))
    details = json.loads(request.body.decode('utf-8'))
    project = Project.objects.get(id=details["project_id"])
    user_list = details["user_list"]
    for user_id in user_list:
        user = Person.objects.get(id=user_id)
        temp_project_user = ProjectUser(project_id=project, person_id=user)
        temp_project_user.save()
    return HttpResponse(json.dumps(200))


@csrf_exempt
@error_checks
@require_http_methods(["OPTIONS", "POST"])
def assign_mentors(request):
    if request.method == "OPTIONS":
        return HttpResponse(json.dumps({"Message": "wait"}))
    details = json.loads(request.body.decode('utf-8'))
    project = Project.objects.get(id=details["project_id"])
    mentor = Person.objects.get(id=details["mentor_id"])
    temp_project_user = ProjectUser(project_id=project, person_id=mentor, is_mentor=True)
    temp_project_user.save()
    return HttpResponse(json.dumps(200))


@csrf_exempt
@error_checks
@require_http_methods(["GET"])
def get_mentees(request,mentor_id):
    project_ids = ProjectUser.objects.filter(person_id=mentor_id, is_mentor=True).values_list('project_id', flat=True)
    project_id_list = list(project_ids)
    user_ids = ProjectUser.objects.filter(project_id__in=project_id_list, is_mentor=False).values_list('person_id', flat=True)
    user_id_list = list(user_ids)
    user_id_list = list(set(user_id_list))
    user_names = Person.objects.filter(id__in=user_id_list).values_list('person_name', flat=True)
    user_names_list = list(user_names)
    response = {
        "user ids": user_id_list,
        "user_names": user_names_list
    }
    return HttpResponse(json.dumps(response))


@csrf_exempt
@error_checks
@require_http_methods(["GET"])
def get_projects(request,mentor_id):
    project_ids = ProjectUser.objects.filter(person_id=mentor_id, is_mentor=True).values_list('project_id', flat=True)
    project_id_list = list(project_ids)
    project_names = Project.objects.filter(id__in=project_id_list).values_list('project_name', flat=True)
    project_name_list = list(project_names)
    response = {
        "project ids": project_id_list,
        "project names": project_name_list
    }
    return HttpResponse(json.dumps(response))


@csrf_exempt
@error_checks
@require_http_methods(["GET"])
def get_users(request,project_id):
    user_ids = ProjectUser.objects.filter(project_id=project_id, is_mentor=False).values_list('person_id', flat=True)
    mentor_ids = ProjectUser.objects.filter(project_id=project_id, is_mentor=True).values_list('person_id', flat=True)
    user_id_list = list(user_ids)
    mentor_id_list = list(mentor_ids)
    user_id_list = list(set(user_id_list))
    mentor_id_list = list(set(mentor_id_list))
    response = {
        "mentors": mentor_id_list,
        "users": user_id_list
    }
    return HttpResponse(json.dumps(response))



