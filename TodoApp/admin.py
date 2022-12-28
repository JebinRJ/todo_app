from django.contrib import admin
from TodoApp.models import *

class ModelAdmin(admin.ModelAdmin):
    Info=['name','email']
admin.site.unregister(User)
admin.site.register(User,ModelAdmin)
admin.site.register(UserProfile)
admin.site.register(CreateTodo)
# Register your models here.
