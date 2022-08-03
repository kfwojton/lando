"""lando URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import *
from core.models import *

class CreateNewProduct(CreateView):
    template_name = "createproduct.html"
    model = Products
    fields = ['price' , 'description']
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(CreateNewProduct, self).get_context_data(**kwargs)
        # context['server_name'] = os.environ.get('SERVER_NAME')
        context['object_list'] = Products.objects.all()

        return context


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', ListView.as_view(template_name="index.html", model = Products)),
    path('', CreateNewProduct.as_view())

]
