from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('',views.NotesListView.as_view(), name="notes.list"),
    path('<int:pk>', views.NotesDetailView.as_view(),name="notes.detail"),
    path('new',views.NotesCreateView.as_view(), name="notes.new"),
    
]

