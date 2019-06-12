from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, mixins

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


class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    """
    Considering that we want to automatically connect new profile status
    instances to the profile of the user making the request, we need to
    override the perform_create method.
    """

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
