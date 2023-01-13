
from django.contrib import admin
from django.urls import include, path
from Home.views import index_view
from CUA.views import dashboard, customerDash, developerDash, userLogout


from CUA.views import register
#from Service.views import reportServices_views


urlpatterns = [

    path('', index_view, name='index_view'),
    path('admin/', admin.site.urls),

    path('Contact/', include('Contact.urls')),
    path('Product/', include('Product.urls')),
   # path('Service/', include('Service.urls')),
    path('About/', include('About.urls')),
    path('Payments/', include('Payments.urls')),
    path('Home/', include('Home.urls')),
    path('blog/', include('blog.urls')),
    #path('test/', include('test.urls')),
    #path('user/', include('user.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('CUA/', include('CUA.urls')),
    path('logout/', userLogout,name='userLogout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('customerDash/', customerDash, name='customerDash'),
    path('developerDash/', developerDash, name='developerDash'),
    #path('CUA/register/', register, name='register'),
#    path('reportServices_views/', reportServices_views, name='reportServices_views'),




]
