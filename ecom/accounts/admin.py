from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accounts,UserProfile
from django.utils.html import format_html


# Register your models here.
class AccountsAdmin(UserAdmin):
    list_display = ('user_name','first_name','last_name','email','last_login','date_joined','is_active')
    list_display_links = ('email','first_name','last_name')
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    thumbnail.short_description = 'Profile Picture'
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

admin.site.register(Accounts ,AccountsAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

