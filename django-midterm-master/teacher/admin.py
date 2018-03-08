from django.contrib import admin
from teacher.models import Teacher,Students

# Register your models here.
class TeacherInline(admin.StackedInline):
    model = Students
    extra = 1

class TeacherAdmin(admin.ModelAdmin):
    fields = ['teacher_firstname', 'teacher_lastname', 'teacher_subject', 'teacher_age']
    inlines = [TeacherInline]
    list_filter = ['teacher_lastname']

admin.site.register(Teacher, TeacherAdmin)