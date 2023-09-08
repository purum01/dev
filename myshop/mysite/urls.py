from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request:redirect('shop:product_list'), name='root'),
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('coupons/', include('coupons.urls')),
    path('orders/',include('orders.urls')),
    path('qna/', include('qna.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
