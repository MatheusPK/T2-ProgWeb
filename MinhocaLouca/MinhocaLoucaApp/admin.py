from django.contrib import admin

# Register your models here.

from MinhocaLoucaApp.models import Player, EasyScore, NormalScore, HardScore

admin.site.register(Player)
admin.site.register(EasyScore)
admin.site.register(NormalScore)
admin.site.register(HardScore)