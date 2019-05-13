from rest_framework import serializers


from protfolio.models import (
    AboutModel,
    SkillsModel,
    ClientsModel,
    ProjectsModel,
    TeamMembers,
    SocialModel,
    BlogPostModel,
    FooterModel,
    ExperiencesModel,
    EducationModel,
    ReferenceModel
)


class AboutSerializers(serializers.ModelSerializer):

    class Meta:
        model = AboutModel
        fields = ('__all__')


class ExperiencesSerializers(serializers.ModelSerializer):

    class Meta:
        model = ExperiencesModel
        fields = ('__all__')


class EducationSerializers(serializers.ModelSerializer):

    class Meta:
        model = EducationModel
        fields = ('__all__')


class ReferenceSerializers(serializers.ModelSerializer):

    class Meta:
        model = ReferenceModel
        fields = ('__all__')


class SkillsSerializers(serializers.ModelSerializer):

    class Meta:
        model = SkillsModel
        fields = ('__all__')


class ClientsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ClientsModel
        fields = ('__all__')


class ProjectsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProjectsModel
        fields = ('__all__')


class TeamMembersSerializers(serializers.ModelSerializer):

    class Meta:
        model = TeamMembers
        fields = ('__all__')


class SocialSerializers(serializers.ModelSerializer):

    class Meta:
        model = SocialModel
        fields = ('__all__')


class FooterSerializers(serializers.ModelSerializer):

    class Meta:
        model = FooterModel
        fields = ('__all__')


class BlogPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = BlogPostModel
        fields = ('__all__')
