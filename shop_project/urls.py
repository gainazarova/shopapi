
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from order.views import CreateOrderView, UserOrderList, UpdateOrderStatusView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
    path('api/v1/account/', include('account.urls')),
    path('api/v1/basket/', include('basket.urls')),
    path('api/v1/orders/', CreateOrderView.as_view()),
    path('api/v1/orders/own/', UserOrderList.as_view()),
    path('api/v1/orders/<int:pk>/', UpdateOrderStatusView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
