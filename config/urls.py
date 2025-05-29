from django.contrib import admin
from django.urls import include, path

from orders import urls as orders_urls
from tasks import urls as tasks_urls
from users import urls as users_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("django-rq/", include("django_rq.urls")),
    path("api/users/", include(users_urls)),
    path("api/orders/", include(orders_urls)),
    path("api/tasks/", include(tasks_urls)),
]
