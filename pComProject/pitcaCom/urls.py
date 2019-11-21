"""pitcaComProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from . import views

app_name = 'pitcaCom'

urlpatterns = [
    path('reg/', views.regPitcaCom, name='reg'),
    path('regCon/', views.regConPitcaCom, name='regCon'),
    path('all/', views.reaPitcaComAll, name='comAll'),
    path('<str:name>/det/', views.detPitcaCom, name='comDet'),
    path('<str:name>/mod/', views.reaPitcaComOne, name='comMod'),
    path('modCon/', views.modConPitcaCom, name='modCon'),
    path('<str:name>/del/', views.delconPitcaCom, name='comDel'),
]
