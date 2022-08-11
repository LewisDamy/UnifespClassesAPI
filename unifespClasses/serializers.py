from rest_framework import serializers
from unifespClasses.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = [
            'subjectID',
            'subjectName',
            'category',
            'chTotal',
            'requirements',
            'semesterAvailable'
        ]

