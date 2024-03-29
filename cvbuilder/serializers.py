from rest_framework import serializers

from .models import *


class ResumeSerializer(serializers.ModelSerializer):
    """ To create, update and delete Candidate Resume """

    class Meta:
        model = Resume
        fields = ["id", "profession", "summary",
                  "linkedin", "website"]


class ExperienceSerializer(serializers.ModelSerializer):
    """ To create, update and delete Resume Experince """

    class Meta:
        model = Experience
        fields = ["id", "title", "company", "address",
                  "start_date", "end_date", "description"]


class SkillSerializer(serializers.ModelSerializer):
    """ To create, update and delete Resume Skill """

    class Meta:
        model = Skill
        fields = ["id", "title"]


class EducationSerializer(serializers.ModelSerializer):
    """ To create, update and delete Resume Education """

    class Meta:
        model = Education
        fields = ["id", "university", "degree", "subject",
                  "address", "start_date", "end_date", "description"]
