from django.contrib import admin
from alpha.models import DataForm, Games, AddData, FullBuild 

# Register your models here.
#admin.site.register(DataForm) #adds the ability to add forms from the admin site
admin.site.register(Games)
admin.site.register(AddData)
admin.site.register(FullBuild)

