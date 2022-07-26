from django.contrib import admin



from .models import Menyu, Mahsulot
@admin.register(Menyu)
class MenyuAdmin(admin.ModelAdmin):
    list_display = ['nomi']
    search_fields = ['nomi']
    
admin.site.register(Mahsulot)

    