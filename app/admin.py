from django.contrib import admin

# Register your models here.
#mudar isso
from .models import SelectedField


@admin.register(SelectedField)
class SelectedFieldAdmin(admin.ModelAdmin):
    list_display = ('name',)
