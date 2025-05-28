from django.urls import path
from .views import PageListView, PageDetailView, PageCreate, PageUpdateView,PageDeleteView

pages_patterns = ([
    path('', PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>', PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PageDeleteView.as_view(), name='delete')
], 'pages') #esto nos permitira trabajar mejor la reversa