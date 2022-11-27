from django.contrib import admin

# Register your models here.

from MinhocaLoucaApp.models import Player, EasyScore, NormalScore, HardScore
from MinhocaLoucaApp.models import EasyScore2, NormalScore2, HardScore2

admin.site.register(Player)
admin.site.register(EasyScore)
admin.site.register(NormalScore)
admin.site.register(HardScore)

admin.site.register(EasyScore2)
admin.site.register(NormalScore2)
admin.site.register(HardScore2)