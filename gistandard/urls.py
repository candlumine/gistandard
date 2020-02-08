"""gistandard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.urls import re_path, include
from django.views.static import serve
from gistandard.settings import MEDIA_ROOT

import xadmin

from users.views_user import LoginView, IndexView, LogoutView
from system.views import SystemView
from adm.views import AdmView
from personal import views as personal_views
from personal import views_work_order as order

urlpatterns = [
    re_path(r'^xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^$', IndexView.as_view(), name='index'),
    # 用户登录
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name="logout"),

    re_path(r'^system/$', SystemView.as_view(), name="system"),
    re_path(r'^system/basic/', include(('users.urls', 'system-basic'), namespace='system-basic')),
    re_path(r'^system/rbac/', include(('rbac.urls', 'system-rbac'), namespace='system-rbac')),
    re_path(r'^system/tools/', include(('system.urls', 'system-tools'), namespace='system-tools')),

    re_path(r'^adm/$', AdmView.as_view(), name="adm-main"),
    re_path(r'^adm/bsm/', include(('adm.urls', 'adm-bsm'), namespace='adm-bsm')),
    re_path(r'^adm/equipment/', include(('adm.urls_equipment', 'adm-equipment'), namespace='adm-equipment')),
    re_path(r'^adm/asset/', include(('adm.urls_asset', 'adm-asset'), namespace='adm-asset')),

    re_path(r'^personal/$', personal_views.PersonalView.as_view(), name="personal"),
    re_path(r'^personal/userinfo', personal_views.UserInfoView.as_view(), name="personal-user_info"),
    re_path(r'^personal/uploadimage', personal_views.UploadImageView.as_view(), name="personal-uploadimage"),
    re_path(r'^personal/passwordchange', personal_views.PasswdChangeView.as_view(), name="personal-passwordchange"),
    re_path(r'^personal/phonebook', personal_views.PhoneBookView.as_view(), name="personal-phonebook"),
    re_path(r'^personal/workorder_Icrt/$', order.WorkOrderView.as_view(), name="personal-workorder_Icrt"),
    re_path(r'^personal/workorder_Icrt/list', order.WorkOrderListView.as_view(), name="personal-workorder-list"),
    re_path(r'^personal/workorder_Icrt/create', order.WorkOrderCreateView.as_view(), name="personal-workorder-create"),
    re_path(r'^personal/workorder_Icrt/detail', order.WorkOrderDetailView.as_view(), name="personal-workorder-detail"),
    re_path(r'^personal/workorder_Icrt/delete', order.WorkOrderDeleteView.as_view(), name="personal-workorder-delete"),
    re_path(r'^personal/workorder_Icrt/update', order.WorkOrderUpdateView.as_view(), name="personal-workorder-update"),
    re_path(r'^personal/workorder_app/$', order.WorkOrderView.as_view(), name="personal-workorder_app"),
    re_path(r'^personal/workorder_app/send', order.WrokOrderSendView.as_view(), name="personal-workorder-send"),
    re_path(r'^personal/workorder_rec/$', order.WorkOrderView.as_view(), name="personal-workorder_rec"),
    re_path(r'^personal/workorder_rec/execute', order.WorkOrderExecuteView.as_view(), name="personal-workorder-execute"),
    re_path(r'^personal/workorder_rec/finish', order.WorkOrderFinishView.as_view(), name="personal-workorder-finish"),
    re_path(r'^personal/workorder_rec/upload', order.WorkOrderUploadView.as_view(), name="personal-workorder-upload"),
    re_path(r'^personal/workorder_rec/return', order.WorkOrderReturnView.as_view(), name="personal-workorder-return"),
    re_path(r'^personal/workorder_Icrt/upload', order.WorkOrderProjectUploadView.as_view(),
        name="personal-workorder-project-upload"),
    re_path(r'^personal/workorder_all/$', order.WorkOrderView.as_view(), name="personal-workorder_all"),
    re_path(r'^personal/document/$', order.WorkOrderDocumentView.as_view(), name="personal-document"),
    re_path(r'^personal/document/list', order.WorkOrderDocumentListView.as_view(), name="personal-document-list"),

]
