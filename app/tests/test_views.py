import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Student
from ..serializers import StudentSerializer


# initialize the APIClient app
client = Client()
