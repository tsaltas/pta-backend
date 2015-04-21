from django.contrib import admin
from lessons.models import Activity, Step, Tag

# Register your models here.
admin.site.register(Step)
admin.site.register(Activity)
admin.site.register(Tag)