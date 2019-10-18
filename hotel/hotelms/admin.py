from django.contrib import admin

# Register your models here.
from.models import Hotel,Manager,Room,Guest,Record

class HotelAdmin(admin.ModelAdmin):
    list_display = ('name','city',)

class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name','cancel_booking',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('number','type_of_room','price','availability','no_of_beds',)

class GuestAdmin(admin.ModelAdmin):
    list_display = ('name','phone_no','address',)

class RecordAdmin(admin.ModelAdmin):
    list_display = ('guest_name','room_no','booking_date','canceling_date',)


admin.site.register(Hotel,HotelAdmin)
admin.site.register(Manager,ManagerAdmin)
admin.site.register(Room,RoomAdmin)
admin.site.register(Guest,GuestAdmin)
admin.site.register(Record,RecordAdmin)
