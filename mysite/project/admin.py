from django.contrib import admin
from .models import Support,Consultant,Project,Support_Status

admin.site.register(Support)
admin.site.register(Consultant)
admin.site.register(Project)
admin.site.register(Support_Status)

