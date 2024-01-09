from django.urls import path
# ournalCreateView, JournalUpdateView, JournalDeleteView
from .views import JournalListView, active_members, contact, about, file_list, home, nominate_member, projects, trustees_list, upload_journal, view_trustee


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
    path('nominate/', nominate_member, name='nominate_member'),
    path('upload_journal/', upload_journal, name='upload_journal'),
    path('file_list/', file_list, name='file_list')
    # path('journals/create/', JournalCreateView.as_view(), name='journal-create'),
    # path('journals/<slug:slug>/update/', JournalUpdateView.as_view(), name='journal-update'),
    # path('journals/<slug:slug>/delete/', JournalDeleteView.as_view(), name='journal-delete'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
