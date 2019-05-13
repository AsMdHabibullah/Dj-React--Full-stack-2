from rest_framework import routers
from protfolio.api.viewset import (
    AboutViewSet,
    SkillsViewSet,
    ClientsViewSet,
    ProjectsViewSet,
    TeamMembersViewSet,
    SocialViewSet,
    BlogPostViewSet,
    FooterViewSet,
    ExperienceViewSet,
    EducationViewSet,
    ReferenceViewSet
)

router = routers.DefaultRouter()

router.register('about', AboutViewSet, base_name='about'),
router.register('skills', SkillsViewSet, base_name='skills'),
router.register('clients', ClientsViewSet, base_name='clients'),
router.register('projects', ProjectsViewSet, base_name='projects'),
router.register('team_member', TeamMembersViewSet, base_name='team_member'),
router.register('social', SocialViewSet, base_name='social'),
router.register('blog', BlogPostViewSet, base_name='blog')
router.register('footer', FooterViewSet, base_name='footer')
router.register('experiences', ExperienceViewSet, base_name='experiences')
router.register('education', EducationViewSet, base_name='education')
router.register('reference', ReferenceViewSet, base_name='reference')
