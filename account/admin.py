from django.contrib import admin
from .models import basicInfo, additionalInfo, userInfo

# Register your models here.
admin.site.register(userInfo)
admin.site.register(additionalInfo)
admin.site.register(basicInfo)