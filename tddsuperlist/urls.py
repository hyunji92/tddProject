"""tddsuperlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# lists 앱 패키지의 views.py를 가져와 엘리어스로(as) lists_views로 지정해 사용하도록 한다.
from lists import views as lists_views


urlpatterns = [
    url(r'^$', lists_views.home_page, name='home')
    #url(r'^$', 'lists.views.home_page', name='home') 문자열로 부르는것이 버전 업뎃 되면서 deplicate되었더.
    #url(r'^admin/', admin.site.urls),
]
