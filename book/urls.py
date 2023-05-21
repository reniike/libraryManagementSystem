from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

urlpatterns = router.urls

# views.AuthorView.as_view()
# django debug toolbar
# path('', include(router.urls)),
# path('authors/', views.AuthorList.as_view()),
# path('__debug__/', include('debug_toolbar.urls')),
# path('author/<int:pk>/' , views.AuthorDetails.as_view(), name='author-detail'),
# path('book/', views.list_of_books),
# path('book/<int:pk>/', views.book_details)
# ]
