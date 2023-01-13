from django.db import models


class Profession(models.Model):
    title = models.CharField('Название 1 колонки', max_length=50)
    description = models.TextField('named second column')

    def __str__(self):
        return self.title


class File(models.Model):
    file = models.FileField('file')
    profession_id = models.ForeignKey(Profession, on_delete=models.CASCADE)
