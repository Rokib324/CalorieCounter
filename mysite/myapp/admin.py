from django.contrib import admin
from .models import Food, Consume
# Register your models here.

admin.site.site_header = 'Calorie Counter'
admin.site.site_title = 'Calorie Counter app'
admin.site.index_title = 'Calorie Counter Management'


admin.site.register(Food)
admin.site.register(Consume)