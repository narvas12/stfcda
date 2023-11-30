from django.urls import path
# ournalCreateView, JournalUpdateView, JournalDeleteView
from .views import JournalListView, active_members, contact, about, home, projects, trustees_list, view_trustee


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('about_us/', about, name='about_us'),
    path('contat_us/', contact, name='contact_us'),
    path('projects/', projects, name='projects'),
    path('members/', active_members, name='members'),
    path('journals/', JournalListView.as_view(), name='journal_list'),
    path('trustees/', trustees_list, name='trustees_list'),
    path('trustees/<slug:slug>/', view_trustee, name='view-trustee'),

    # path('journals/create/', JournalCreateView.as_view(), name='journal-create'),
    # path('journals/<slug:slug>/update/', JournalUpdateView.as_view(), name='journal-update'),
    # path('journals/<slug:slug>/delete/', JournalDeleteView.as_view(), name='journal-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
