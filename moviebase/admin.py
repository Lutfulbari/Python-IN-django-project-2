from django.contrib import admin
from moviebase.models import Actor,Director,Gender,Movie

admin.site.register(Gender)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie)

# Register your models here.
