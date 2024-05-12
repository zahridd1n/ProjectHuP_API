from django.db import models


class Home(models.Model):
    image = models.ImageField(upload_to='media/home/')
    body = models.TextField()


class Portfolio(models.Model):
    image = models.ImageField(upload_to='media/portfolio/')
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    image = models.ImageField(upload_to='media/team/')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    job_title = models.CharField(max_length=255)
    working_day = models.IntegerField()
    working_time = models.CharField(max_length=255, blank=True, null=True)
    requirements = models.TextField(blank=True)
    tasks = models.TextField(blank=True)
    technology = models.CharField(max_length=255)
    salary = models.CharField(max_length=255, blank=True, null=True)


class Resume(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cv = models.FileField(upload_to='media/resume/')

    def __str__(self):
        return self.full_name
