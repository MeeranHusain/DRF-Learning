from django.contrib import admin
from . models import Student

# Register your models here.

# admin.site.register(Student)    # This is the one way to see model on admin panel and the other way is to use decorator @admin.register(Student) and then create a class StudentAdmin(admin.ModelAdmin) and then define the list_display attribute to show the fields in the admin panel.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','age','standard','section','roll_number','email','phone','is_active',)