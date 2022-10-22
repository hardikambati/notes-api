from django.urls import path
from . import views

# uses Viewset Architecture

get_single_view = views.NoteView.as_view({
    'get': 'get_single'
})

get_all_view = views.NoteView.as_view({
    'get': 'get_all'
})

create_view = views.NoteView.as_view({
    'post': 'create'
})

update_view = views.NoteView.as_view({
    'put': 'update'
})

delete_view = views.NoteView.as_view({
    'delete': 'delete'
})

urlpatterns = [
    path('get-single/<int:id>/', get_single_view),
    path('get-all/', get_all_view),
    path('create/', create_view),
    path('update/<int:id>/', update_view),
    path('delete/<int:id>/', delete_view),
]