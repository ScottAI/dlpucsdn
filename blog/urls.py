from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^write/$','write_blog',name='write_blog'),
    url(r'^(?P<blog_id>\d+)/$','blog_view',name='blog_view'),
    url(r'^(?P<blog_id>\d+)/reply/$','create_breply',name='create_breply'),
)