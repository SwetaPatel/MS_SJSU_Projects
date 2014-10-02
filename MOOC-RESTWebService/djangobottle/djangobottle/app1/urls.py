__author__ = 'abhi'

import django.conf.urls
from django.contrib.auth.views import login, logout

urlpatterns = django.conf.urls.patterns('djangobottle.app1.views',

 django.conf.urls.url(r'^$', 'index', name='homepage_index'),
 django.conf.urls.url(r'^home/(?P<teamName>.*)/$', 'login_index', name='login_index'),
 django.conf.urls.url(r'^home/$', 'login_index', name='login_index'),
 django.conf.urls.url(r'^about/$', 'about', name='homepage_about'),
 django.conf.urls.url(r'^archive/$', 'archive', name='homepage_archive'),
 django.conf.urls.url(r'^profile/$', 'profile', name='homepage_profile'),
 django.conf.urls.url(r'^signIn/$', 'signIn', name='signIn'),
 django.conf.urls.url(r'^addCourse/$', 'addCourse', name='addCourse'),
 django.conf.urls.url(r'^listCourses/$', 'listCourses', name='listCourses'),
 django.conf.urls.url(r'^getCourse/(?P<courseId>.*)$', 'getCourse', name='getCourse'),
 django.conf.urls.url(r'^app1/views/updateCourse/$', 'updateCourse', name='updateCourse'),
 django.conf.urls.url(r'^app1/views/deleteCourse(?P<courseId>.*)$', 'deleteCourse', name='deleteCourse'),


 django.conf.urls.url(r'^listCategories/$', 'listCategories', name='listCategories'),
 django.conf.urls.url(r'^getCategory/(?P<categoryId>.*)$', 'getCategory', name='getCategory'),
 django.conf.urls.url(r'^CreateUser/$', 'createUser', name='createUser'),
 django.conf.urls.url(r'^CreateCategory/$', 'createCategory', name='createCategory'),
 django.conf.urls.url(r'^app1/views/CreateAnnouncement(?P<courseId>.*)$', 'createAnnouncement', name='createAnnouncement'),
 django.conf.urls.url(r'^app1/views/listAnnouncements/$', 'listAnnouncements', name='listAnnouncements'),
 django.conf.urls.url(r'^getAnnouncement/(?P<announcementId>.*)$', 'getAnnouncement', name='getAnnouncement'),
 django.conf.urls.url(r'^updateUser/$', 'updateUser', name='updateUser'),
 django.conf.urls.url(r'^getUser/$', 'getUser', name='getUser'),
 django.conf.urls.url(r'^app1/views/addDiscussion/$', 'addDiscussion', name='addDiscussion'),
 django.conf.urls.url(r'^app1/views/addMessage(?P<discussionId>.*)$', 'addMessage', name='addMessage'),
 django.conf.urls.url(r'^app1/views/enrollCourse/$', 'enrollCourse', name='enrollCourse'),

 django.conf.urls.url(r'^addDiscussion/addMessage/(?P<discussionId>.*)$', 'addMessage', name='addMessage'),
 django.conf.urls.url(r'^logout/$', 'logout', name='logout'),
)

'''
urlpatterns += django.conf.urls.patterns('',
 django.conf.urls.url(r'login/$', login, kwargs={'template_name': 'login.html'},
 name="homepage_login"),
 django.conf.urls.url(r'logout/$', logout, name="homepage_logout"),

)

(?P<username>\d+)
/(?P<username>\w+)
'''