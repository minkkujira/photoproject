from django.contrib import admin

from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス'''
    #レコード一覧にはidとusernameを表示
    list_display = ('id', 'username')
    #表示するカラムにリンクを設定
    list_display_links = ('id', 'username')

#django管理サイトにCustomUser、CustomUserAdminに登録する
admin.site.register(CustomUser, CustomUserAdmin)