from django.contrib import admin
from .models import Ricetta, Preferito, Concorrente, Chef

class RicettaAdmin(admin.ModelAdmin):
    filter_horizontal = ('giudici',)
    
# Register your models here.
admin.site.register(Concorrente)
admin.site.register(Chef)
admin.site.register(Ricetta,RicettaAdmin)
admin.site.register(Preferito)