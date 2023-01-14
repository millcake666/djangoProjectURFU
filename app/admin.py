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


@admin.register(models.Page)
class AdminProfession(admin.ModelAdmin):
    inlines = [Table, Chart]


admin.site.register(models.Profession)
