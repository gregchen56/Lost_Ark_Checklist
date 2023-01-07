from django.contrib import admin
from .models import (
    User,
    Character,
    CharDaily,
    CharWeekly,
    RosterDaily,
    RosterWeekly,
)

# Register your models here.
admin.site.register(User)
admin.site.register(Character)
admin.site.register(CharDaily)
admin.site.register(CharWeekly)
admin.site.register(RosterDaily)
admin.site.register(RosterWeekly)