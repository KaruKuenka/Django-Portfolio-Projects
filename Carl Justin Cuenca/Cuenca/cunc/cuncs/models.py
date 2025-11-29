from django.db import models

# Create your models here.


class dataClassas(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    hobbies = models.CharField(max_length=200, null= True, blank=True)

    def __str__(self):
        return f'{self.name}'

class clientData (models.Model):
    accountData = models.ForeignKey(dataClassas, on_delete=models.DO_NOTHING)
    nameData = models.CharField(max_length=200)


class Skill(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    
    def __str__(self):
        return self.title