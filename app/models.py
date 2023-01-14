from django.db import models


class Profession(models.Model):
    title = models.CharField('Name', max_length=50)
    description = models.TextField('description')

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class Table(models.Model):
    title = models.CharField('Заголовк таблицы', max_length=100)
    file = models.FileField('csv данные', upload_to='csv/')

    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'


class Image(models.Model):
    img = models.ImageField('Изображение', upload_to='img/')

    page_id = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.img.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
