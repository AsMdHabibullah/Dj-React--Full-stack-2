from django.db import models



class AboutModel(models.Model):
    name = models.CharField(max_length=250, blank=False)
    thumbnail = models.ImageField(upload_to='about', blank=False)
    description = models.TextField()
    question = models.CharField(max_length=250, blank=False)
    email = models.EmailField(max_length=250, blank=False)
    ex_description = models.TextField()

    def __str__(self):
        return self.name


class FontModel(models.Model):
    name = models.CharField(max_length=250, blank=False)
    thumbnail = models.ImageField(upload_to='fontViews', blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name
        

class SocialModel(models.Model):
    social_name = models.CharField(max_length=250, blank=False)
    url = models.URLField(blank=False)

    def __str__(self):
        return self.social_name


class TagModel(models.Model):
    tag_name = models.CharField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.tag_name


class SkillsModel(models.Model):
    skill_name = models.CharField(max_length=250, blank=False)
    thumbnail = models.ImageField(upload_to='skills', blank=False)

    def __str__(self):
        return self.skill_name


class ExperiencesModel(models.Model):
    job_exp_name = models.CharField(max_length=250, blank=False)
    job_holder_title = models.CharField(max_length=250, blank=False)
    job_description = models.TextField()
    job_start_time = models.DateField(auto_now_add=False)
    job_end_time = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.job_exp_name


class EducationModel(models.Model):
    edu_name = models.CharField(max_length=250, blank=False)
    edu_description = models.TextField()
    edu_cartificate = models.ImageField(upload_to='edu', blank=True)
    edu_start_time = models.DateField(auto_now_add=False)
    edu_end_time = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.edu_name


class ReferenceModel(models.Model):
    recommend_person_name = models.CharField(max_length=250, blank=False)
    recommend_person_company_name = models.CharField(
        max_length=250, blank=False)
    recommend_person_position = models.CharField(max_length=250, blank=False)
    recommend_person_anounce = models.TextField()

    def __str__(self):
        return self.recommend_person_name


class ClientsModel(models.Model):
    client_name = models.CharField(max_length=250, blank=False)
    client_logo = models.ImageField(upload_to='client')

    def __str__(self):
        return self.client_name


class TeamMembers(models.Model):
    dev_name = models.CharField(max_length=250, blank=False)
    dev_title = models.CharField(max_length=250, blank=False)
    dev_img = models.ImageField(upload_to='teammember')
    member_description = models.TextField(blank=False)
    dev_social = models.ForeignKey(SocialModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.dev_name


class ProjectsModel(models.Model):
    title = models.CharField(max_length=250, blank=False)
    thumbnail = models.ImageField(upload_to='projects', blank=False)
    description = models.TextField()
    ex_title = models.CharField(max_length=250, blank=False)
    ex_description = models.TextField(blank=True, null=True)
    tags = models.ForeignKey(
        TagModel, on_delete=models.CASCADE, blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    developer_name = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.title


class BlogPostModel(models.Model):
    title = models.CharField(max_length=250, blank=False)
    thumbnail = models.ImageField(upload_to='blog', blank=False)
    description = models.TextField()
    ex_title = models.CharField(max_length=250, blank=True, null=True)
    ex_description = models.TextField(blank=True, null=True)
    tags = models.ForeignKey(
        TagModel, on_delete=models.CASCADE, blank=True, null=True)
    author = models.CharField(max_length=250, blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FooterModel(models.Model):
    home_address = models.CharField(max_length=250, blank=False)
    email_address = models.CharField(max_length=250, blank=False)
    contact_number = models.CharField(max_length=250, blank=False)
    dreame = models.TextField()
    focusing = models.TextField()
    copy_right = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.home_address
