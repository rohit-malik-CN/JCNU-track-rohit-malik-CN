import connexion
import six

from swagger_server.models.assignproject_request import AssignprojectRequest  # noqa: E501
from swagger_server.models.createproject_request import CreateprojectRequest  # noqa: E501
from swagger_server.models.createuser_request import CreateuserRequest  # noqa: E501
from swagger_server.models.project_assignmentor_request import ProjectAssignmentorRequest  # noqa: E501
from swagger_server import util


def assignproject_post(body):  # noqa: E501
    """Assign an existing project to users

    Assign an existing project to users # noqa: E501

    :param body: Enter the project_id and a list of user_ids
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = AssignprojectRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def createproject_post(body):  # noqa: E501
    """Create a new project

    Create a new project # noqa: E501

    :param body: Enter the name of the project
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = CreateprojectRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def createuser_post(body):  # noqa: E501
    """Create a new user

    Create a new user # noqa: E501

    :param body: Enter the name of the user
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = CreateuserRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def project_assignmentor_post(body):  # noqa: E501
    """Assing a mentor to an existing project

    Assing a mentor to an existing project # noqa: E501

    :param body: Enter the project_id and a mentor_id
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ProjectAssignmentorRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def project_by_project_id_get(project_id):  # noqa: E501
    """Get the users and mentors of a project

    Get the users and mentors of a project # noqa: E501

    :param project_id: Project id of the project
    :type project_id: int

    :rtype: None
    """
    return 'do some magic!'


def project_mentor_by_mentor_id_get(mentor_id):  # noqa: E501
    """Get the mentees of a given mentor

    Get the mentees of a given mentor # noqa: E501

    :param mentor_id: User id of the mentor
    :type mentor_id: int

    :rtype: None
    """
    return 'do some magic!'


def user_projects_by_user_id_get(mentor_id):  # noqa: E501
    """Get projects user is mentoring

    Get projects user is mentoring # noqa: E501

    :param mentor_id: User id of the user
    :type mentor_id: int

    :rtype: None
    """
    return 'do some magic!'
