from django.contrib import admin

# Register your models here.

from .models import  Flight, Aircraft_type, Aircraft, Bay_type, Schedule, BayAllocation

admin.site.register(Flight)
admin.site.register(Aircraft_type)
admin.site.register(Aircraft)
admin.site.register(Bay_type)
admin.site.register(Schedule)
admin.site.register(BayAllocation)
