from django.contrib import admin

from .models import TransportDetail
from .models import RouteDetail
# Register your models here.
class TransportDetailAdmin(admin.ModelAdmin):
	list_display=('id','route','fees')

class RouteDetailAdmin(admin.ModelAdmin):
	list_display=('id','route_name','distance','price')

admin.site.register(TransportDetail,TransportDetailAdmin)
admin.site.register(RouteDetail,RouteDetailAdmin)