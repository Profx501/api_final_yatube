from rest_framework import viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from django.shortcuts import get_object_or_404

from .serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
)
from posts.models import Post, Group, Comment
from .permissions import AuthorPermissions


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        AuthorPermissions,
        permissions.IsAuthenticatedOrReadOnly
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        AuthorPermissions,
        permissions.IsAuthenticatedOrReadOnly
    )

    def get_post_id(self):
        return self.kwargs.get("post_id")

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, id=self.get_post_id())
        )

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.get_post_id())


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.folower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
