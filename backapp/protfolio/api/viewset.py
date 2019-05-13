from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet


from protfolio.models import(
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

from protfolio.api.serializers import(
    AboutSerializers,
    SkillsSerializers,
    ClientsSerializers,
    ProjectsSerializers,
    TeamMembersSerializers,
    SocialSerializers,
    BlogPostSerializers,
    FooterSerializers,
    ExperiencesSerializers,
    EducationSerializers,
    ReferenceSerializers,
)


class AboutViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = AboutModel.objects.all()
    serializer_class = AboutSerializers


class ExperienceViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = ExperiencesModel.objects.all()
    serializer_class = ExperiencesSerializers


class EducationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = EducationModel.objects.all()
    serializer_class = EducationSerializers


class ReferenceViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = ReferenceModel.objects.all()
    serializer_class = ReferenceSerializers


class SkillsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = SkillsModel.objects.all()
    serializer_class = SkillsSerializers


class ClientsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = ClientsModel.objects.all()
    serializer_class = ClientsSerializers


class ProjectFilter(FilterSet):

    class Meta:
        model = ProjectsModel
        fields = ['tags']

    def filter_by_tags(self, queryset, name, value):
        tag_names = value.strip().split("-")
        tags = TagModel.objects.filter(name__in=tag_names)
        return queryset.filter(tags__in=tags).distinct()


class ProjectsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = ProjectsModel.objects.all()
    serializer_class = ProjectsSerializers


class TeamMembersViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = TeamMembers.objects.all()
    serializer_class = TeamMembersSerializers


class SocialViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = SocialModel.objects.all()
    serializer_class = SocialSerializers


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = BlogPostModel.objects.all()
    serializer_class = BlogPostSerializers


class FooterViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = FooterModel.objects.all()
    serializer_class = FooterSerializers
