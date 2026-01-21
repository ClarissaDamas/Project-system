from django.contrib import admin
from System.models import Project , ProjectItem

#Registrar os models criados e registrados no SQlite
admin.site.register(Project)
admin.site.register(ProjectItem)


