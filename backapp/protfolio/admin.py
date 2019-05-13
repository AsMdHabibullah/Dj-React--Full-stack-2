from django.contrib import admin
from .models import(
    FontModel,
    TagModel,
    AboutModel,
    SkillsModel,
    ClientsModel,
    TeamMembers,
    ProjectsModel,
    BlogPostModel,
    ExperiencesModel,
    EducationModel,
    ReferenceModel,
    SocialModel,
    FooterModel
)

admin.site.register(FontModel)
admin.site.register(TagModel)
admin.site.register(AboutModel)
admin.site.register(SkillsModel)
admin.site.register(ClientsModel)
admin.site.register(TeamMembers)
admin.site.register(ProjectsModel)
admin.site.register(BlogPostModel)
admin.site.register(ExperiencesModel)
admin.site.register(EducationModel)
admin.site.register(ReferenceModel)
admin.site.register(SocialModel)
admin.site.register(FooterModel)
