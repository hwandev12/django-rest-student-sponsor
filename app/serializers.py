from rest_framework import serializers
from .models import Student, Sponsor, SponsoredStudents
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()


class SponsoredStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsoredStudents
        fields = ['student', ]

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    my_user_data = serializers.SerializerMethodField(read_only=True)
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Student
        fields = ['id', 'reason', 'first_name', 'last_name',
                  'phone_number', 'specification', 'created', 'email', 'my_user_data']
        
    def get_my_user_data(self, obj):
        return {
            "username": obj.owner.full_name,
            "email": obj.owner.email
        }
        

class SponsorSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HyperlinkedIdentityField(view_name='app:student-detail')
    sponsored_students = SponsoredStudentsSerializer(many=True, required=False)
    
    def create(self, validated_data):
        student_data = validated_data('sponsored_students')
        sponsor = Sponsor.objects.create(**validated_data)
        for student in student_data:
            d=dict(student)
            SponsoredStudents.objects.create(sponsor=sponsor, student=d['student'])
        return sponsor

    class Meta:
        model = Sponsor
        fields = ['id', 'first_name', 'last_name',
                  'age', 'work_degree', 'student', 'sponsored_students']



class UserSerializer(serializers.ModelSerializer):
    students = serializers.HyperlinkedIdentityField(view_name='app:student-detail')

    class Meta:
        model = User
        fields = ['id', 'email', 'is_admin', 'is_staff', 'date_of_birth', 'full_name', 'city', 'address', 'students']
        
# count number of info of website
class TotalStudentSponsorSerializer(serializers.Serializer):
    total_student = StudentSerializer(many=True, read_only=True)
    total_sponsor = SponsorSerializer(many=True, read_only=True)
        
