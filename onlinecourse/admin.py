from django.contrib import admin
from .models import Question, Choice
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner


# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ChoiceInline]


# <HINT> Register Question and Choice models here


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
