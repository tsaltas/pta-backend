from django.conf.urls import patterns, include, url
from lessons import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'activities', views.ActivityViewSet)
router.register(r'steps', views.StepViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ptalessons.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 	url(r'^', include(router.urls))
 )
