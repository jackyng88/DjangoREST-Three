from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter

from profiles.models import Profile, ProfileStatus
from profiles.api.serializers import (ProfileSerializer,
                                      ProfileAvatarSerializer,
                                      ProfileStatusSerializer)
from profiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly


class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    # overriding the get_object method
    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object

class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
    # Filtering using a search filter
    filter_backends = [SearchFilter]
    search_fields = ['city']


class ProfileStatusViewSet(ModelViewSet):
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    """
    Considering that we want to automatically connect new profile status
    instances to the profile of the user making the request, we need to
    override the perform_create method.
    """

    def get_queryset(self):
        # Overriding the get_queryset method to allow for 'filtering'.
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
