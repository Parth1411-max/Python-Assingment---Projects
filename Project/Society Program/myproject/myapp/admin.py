from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(user)
admin.site.register(chairman)
admin.site.register(member)
admin.site.register(notice)
admin.site.register(notice_view)
admin.site.register(events)
admin.site.register(events_view)


