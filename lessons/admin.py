from django.contrib import admin
from lessons.models import Activity, Step, Tag


class StepAdmin(admin.ModelAdmin):
    list_display = ('description', 'activity', 'sequence', 'teachingnote', 'imagepath')
    list_editable = ('description', 'activity', 'sequence', 'teachingnote', 'imagepath')
    list_filter = ('activity',)
    list_display_links = None


class StepInline(admin.TabularInline):
    model = Step
    extra = 1


class TagAdmin(admin.ModelAdmin):
    list_display = ('description', 'activity')
    list_editable = ('description', 'activity')
    list_filter = ('description', 'activity')
    list_display_links = None


class TagInline(admin.TabularInline):
    model = Tag
    extra = 1


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'level', 'votecount')
    list_editable = ('language', 'level', 'votecount')
    list_filter = ('language', 'level')
    inlines = [StepInline, TagInline]


# Register your models here.
admin.site.register(Step, StepAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Tag, TagAdmin)
