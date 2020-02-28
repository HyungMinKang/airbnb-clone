from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book",)}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths",)}),
        (
            "More About the Spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenties", "facilities", "house_rules",),
            },
        ),
        ("Last Detail", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenties",
    )
    ordering = (
        "name",
        "price",
        "bedrooms",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "city",
        "room_type",
        "amenties",
        "facilities",
        "house_rules",
        "country",
    )

    search_fields = (
        "=city",
        "^host__username",
    )

    filter_horizontal = (
        "amenties",
        "facilities",
        "house_rules",
    )

    def count_amenties(self, obj):
        return obj.amenties.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    pass
