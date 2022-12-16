from django.contrib import admin

from .models import (
    Project,
    OpenSource,
    ScreenShot,
    SoftSkill,
    TechSkill,
    Language,
    MyInfo,
    History,
    
)


admin.site.register(Project)
admin.site.register(OpenSource)
admin.site.register(ScreenShot)
admin.site.register(SoftSkill)
admin.site.register(TechSkill)
admin.site.register(Language)
admin.site.register(MyInfo)
admin.site.register(History)
