from django.contrib import admin


# Register your models here.
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Players
from .models import Matches
from .models import ClubAttendance
from .models import Updates
from .models import Slides
from .models import EBoard
from .models import Images
from .models import Practices
from .models import AttendanceHistory
from .models import OrganizationInformation
from .models import FrontPageContent

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Players)
admin.site.register(Matches)
admin.site.register(Updates)
admin.site.register(ClubAttendance)
admin.site.register(Slides)
admin.site.register(EBoard)
admin.site.register(Images)
admin.site.register(Practices)
admin.site.register(AttendanceHistory)
admin.site.register(OrganizationInformation)
admin.site.register(FrontPageContent)