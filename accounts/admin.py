from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','timestamp','active')
    list_display_links = ('email','first_name','last_name')
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    readonly_fields=('last_login','timestamp')
    ordering = ('timestamp',)
admin.site.register(Account,AccountAdmin)
