# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.assignproject_request import AssignprojectRequest  # noqa: E501
from swagger_server.models.createproject_request import CreateprojectRequest  # noqa: E501
from swagger_server.models.createuser_request import CreateuserRequest  # noqa: E501
from swagger_server.models.project_assignmentor_request import ProjectAssignmentorRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_assignproject_post(self):
        """Test case for assignproject_post

        Assign an existing project to users
        """
        body = AssignprojectRequest()
        response = self.client.open(
            '/myapp1/project/user/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_createproject_post(self):
        """Test case for createproject_post

        Create a new project
        """
        body = CreateprojectRequest()
        response = self.client.open(
            '/myapp1/project/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_createuser_post(self):
        """Test case for createuser_post

        Create a new user
        """
        body = CreateuserRequest()
        response = self.client.open(
            '/myapp1/user/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_assignmentor_post(self):
        """Test case for project_assignmentor_post

        Assing a mentor to an existing project
        """
        body = ProjectAssignmentorRequest()
        response = self.client.open(
            '/myapp1/project/mentor/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_by_project_id_get(self):
        """Test case for project_by_project_id_get

        Get the users and mentors of a project
        """
        response = self.client.open(
            '/myapp1/project/{project_id}/'.format(project_id=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_mentor_by_mentor_id_get(self):
        """Test case for project_mentor_by_mentor_id_get

        Get the mentees of a given mentor
        """
        response = self.client.open(
            '/myapp1/mentor/{mentor_id}/mentees/'.format(mentor_id=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_projects_by_user_id_get(self):
        """Test case for user_projects_by_user_id_get

        Get projects user is mentoring
        """
        response = self.client.open(
            '/myapp1/mentor/{mentor_id}/projects/'.format(mentor_id=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
