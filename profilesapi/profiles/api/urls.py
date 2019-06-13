from django.urls import include, path
from rest_framework.routers import DefaultRouter

from profiles.api.views import (AvatarUpdateView,
                                ProfileViewSet, 
                                ProfileStatusViewSet)

# profile_list = ProfileViewSet.as_view({'get': 'list'})
# profile_detail = ProfileViewSet.as_view({'get': 'retrieve'})

# urlpatterns = [
#     path('profiles/', profile_list, name='profile-list'),
#     path('profiles/<int:pk>/', profile_detail, name='profile-detail'),
# ]

'''
The DefaultRouter is a feature of the Django REST framework that will
automatically generate the URLs for our viewset. When you have a viewset
you may have multiple have multiple URLs associated with that one viewset.
examples -
/api/profiles/
/api/profiles/1/
The DefaultRouter automatically registers the appropriate URLs for all
of the actions in our viewset.
'''

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'status', ProfileStatusViewSet, basename='status')

urlpatterns = [
    path('', include(router.urls)),
    path('avatar/', AvatarUpdateView.as_view(), name='avatar-update')
]