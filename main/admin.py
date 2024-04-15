from django.contrib import admin
from .models import Tutorial

# Register your models here.

# Create a divider in DB admin
class TutoialAdmin(admin.ModelAdmin):
  fieldsets = [
    ("Title/Date", {"fields" : ["tutorial_title", "tutorial_published"]}),
    ("Content", {"fields": ["tutorial_content"]})
  ]

admin.site.register(Tutorial, TutoialAdmin)


