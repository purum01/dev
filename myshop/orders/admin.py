from django.contrib import admin
import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Order,OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment;filename={opts.verbose_name}.csv'
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj,field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%Y-%m-%d")
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'


@mark_safe
def order_detail(obj):
    return '<a href="{}">View</a>'.format(reverse('orders:admin_order_detail', args=[obj.id]))


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address','tel','paid','created','updated',order_detail]
    list_filter = ['paid','created','updated']
    actions = [export_to_csv]
    inlines = [OrderItemInline]

admin.site.register(Order,OrderAdmin)

