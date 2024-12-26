from django.urls import include, path

from blog import views

app_name = 'blog'


posts_urls = [
    path(
        '<int:post_pk>/',  # Изменено с <int:pk> на <int:post_pk>
        views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path(
        'create/',
        views.PostCreateView.as_view(),
        name='create_post'
    ),
    path(
        '<int:post_pk>/edit/',  # Изменено с <int:post_id> на <int:post_pk>
        views.PostUpdateView.as_view(),
        name='edit_post'
    ),
    path(
        '<int:post_pk>/delete/',  # Изменено с <int:post_id> на <int:post_pk>
        views.PostDeleteView.as_view(),
        name='delete_post'
    ),
    path(
        '<int:post_pk>/comment/',  # Изменено с <int:post_id> на <int:post_pk>
        views.CommentCreateView.as_view(),
        name='add_comment'
    ),
    path(
        '<int:post_pk>/edit_comment/<int:comment_id>/',  # Изменено с <int:post_id> на <int:post_pk>
        views.CommentUpdateView.as_view(),
        name='edit_comment'
    ),
    path(
        '<int:post_pk>/delete_comment/<int:comment_id>/',  # Изменено с <int:post_id> на <int:post_pk>
        views.CommentDeleteView.as_view(),
        name='delete_comment',
    ),
]

profile_urls = [
    path(
        'edit/',
        views.ProfileUpdateView.as_view(),
        name='edit_profile'
    ),
    path(
        '<str:username>/',
        views.ProfileView.as_view(),
        name='profile'
    ),
]

urlpatterns = [
    path(
        '',
        views.IndexHome.as_view(),
        name='index'
    ),
    path('posts/', include(posts_urls)),
    path('profile/', include(profile_urls)),
    path(
        'category/<slug:category_slug>/',
        views.CategoryListView.as_view(),
        name='category_posts'
    )
]
