from django.contrib import admin

from .models import Product, Client, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'reg_date']
    ordering = ['-name']
    readonly_fields = ['reg_date']


class ProductAdmin(admin.ModelAdmin):
    @admin.display(boolean=True)
    def has_image(self, product: Product) -> bool:
        return bool(product.picture)

    list_display = ['title', 'price', 'qts', 'update_date', 'has_image']




    ordering = ['-update_date']
    readonly_fields = ['update_date', 'picture_view']

    fieldsets = [(None,
                  {
                      'classes': ['wide'],
                      'fields': ['title'],
                  },),
                 (
                     'описание',
                     {
                         'classes': ['collapse'],
                         'fields': ['description'],
                     },
                 ),
                 (
                     'картинка',
                     {
                         'classes': ['wide'],
                         'fields': ['picture_view'],
                     },
                 ),
                 (
                     'редактирование картинки',
                     {
                         'classes': ['wide'],
                         'fields': ['picture'],
                     },
                 ),
                 (
                     'финансы',
                     {
                         'fields': ['price', 'qts']
                     }
                 ),
                 (
                     'дата',
                     {
                         'fields': ['update_date'],
                     }
                 ),
                 ]


@admin.action(description="обновить сумму заказа")
def sum_update(modeladmin, request, queryset):
    for obj in queryset:
        obj.calculate_sum()
        obj.save(update_fields=['sum'])


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'sum', 'date_of_creation']
    ordering = ['-date_of_creation']
    readonly_fields = ['date_of_creation']
    list_filter = ['client', 'date_of_creation']
    actions = [sum_update]
    fieldsets = [
        (
            'продукты',
            {
                'classes': ['collapse'],
                'fields': ['products'],
            },
        ),
        (
            'клиент',
            {
                'classes': ['wide'],
                'fields': ['client'],
            },
        ),
        (
            'финансы',
            {
                'fields': ['sum']
            }
        ),
                (
            'публикация',
            {
                'fields': ['date_of_creation'],
            }
        ),
    ]



admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
