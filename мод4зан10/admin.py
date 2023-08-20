from django.contrib import admin
from .models import Advertisment
from django.utils.html import format_html

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'undated_time', 'auction', 'get_html_image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('О товаре', {
            'fields': ('title', 'description', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        }
        )
    )


    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.display(description='фото')
    def get_html_photo(self):
        if self.image:
            return format_html(
                '<img scr"{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
            )

admin.site.register( Advertisment, AdvertisementAdmin)



