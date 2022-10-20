# for testing
from django.test import TestCase
from ..models import Student
from .test_views import client
from ..serializers import StudentSerializer
from rest_framework import status
from django.urls import reverse


# Testing API Calls
class StudentClass(TestCase):
    
    def setUp(self):
        Student.objects.create(
            reason='Poor', first_name='Omad', last_name='Nematov', phone_number=998965214587, specification='None', 
        )

    def test_get_all_students(self):
        # get API response
        response = client.get(reverse('student-list'))
        # get data from db
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)