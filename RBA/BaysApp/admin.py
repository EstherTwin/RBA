from django.contrib import admin

# Register your models here.
from .models import  Department, User, Aircraft_type, Aircraft, Bay_type, Bay, Schedule

admin.site.register(Department)
admin.site.register(User)
admin.site.register(Aircraft_type)
admin.site.register(Aircraft)
admin.site.register(Bay_type)
admin.site.register(Bay)
admin.site.register(Schedule)








