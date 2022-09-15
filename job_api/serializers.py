from rest_framework import serializers
from .models import JobAdvert, JobApplication

class JobAdvertSerializer(serializers.ModelSerializer):
    Job_applicants_count = serializers.ReadOnlyField()

    class Meta:
        model = JobAdvert
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    Job = serializers.ReadOnlyField()

    class Meta:
        model = JobApplication
        fields = '__all__'