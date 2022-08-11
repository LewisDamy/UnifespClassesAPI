from rest_framework import serializers
from unifespClasses.models import Subject

class SubjectSerializer(serializers.ModelSerializer):   # create class serializer
    class Meta:
        model = Subject     # point to the subject model
        fields = [      # indicate which the fields in subject model
            'subjectID',
            'subjectName',
            'category',
            'chTotal',
            'requirements',
            'semesterAvailable'
        ]

