from django.db import models


class Profession(models.Model):
    title = models.CharField('Name', max_length=50)
    description = models.TextField('description')

    def __str__(self):
        return self.title


class FileProfession(models.Model):
    file = models.FileField('file')
    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)
