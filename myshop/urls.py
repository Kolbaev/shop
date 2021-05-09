"""myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from shop.views import LoginView, RegistrationView
from django.views.decorators.cache import cache_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', cache_page(60)(LoginView.as_view()), name='login'),
    path('registration/', cache_page(60)(RegistrationView.as_view()), name='registration'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    url(r'^orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('i18n/', include('django.conf.urls.i18n')),
    url(r'^', include(('shop.urls', 'shop'), namespace='shop')),


]


urlpatterns += i18n_patterns(
    url(r'^', include(('shop.urls', 'shop'), namespace='shop')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
