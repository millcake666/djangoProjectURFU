from django.contrib import admin
from . import models


class File(admin.StackedInline):
    model = models.File
    extra = 1


@admin.register(models.Profession)
class AdminProfession(admin.ModelAdmin):
    inlines = [File]


admin.site.register(models.File)
