from django.contrib import admin
from . import models


class Table(admin.StackedInline):
    model = models.Table
    extra = 1


class Chart(admin.StackedInline):
    model = models.Image
    extra = 1
    fk_name = 'page_id'
    exclude = ['profession_id']


class Image(admin.StackedInline):
    model = models.Image
    extra = 1
    fk_name = 'profession_id'
    exclude = ['page_id']


@admin.register(models.Page)
class AdminPage(admin.ModelAdmin):
    inlines = [Table, Chart]


@admin.register(models.Profession)
class AdminProfession(admin.ModelAdmin):
    inlines = [Image,]
