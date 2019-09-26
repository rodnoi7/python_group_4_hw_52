"""trecker URL Configuration

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
from django.contrib import admin
from django.urls import path
from main.views import IssueListView, IssueDetailView, IssueCreateView, IssueDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IssueListView.as_view(), name='index'),
    path('issue_view/<int:pk>', IssueDetailView.as_view(), name='view'),
    path('issue/create', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='del_issue'),


]
urlpatterns += staticfiles_urlpatterns()