from django.urls import path
from .views import (
    client_list_create,
    client_retrieve_update_destroy,
    mailing_list_create,
    mailing_retrieve_update_destroy,
    message_list_create,
    message_retrieve_update_destroy,
)

urlpatterns = [
    # Client URLs
    path('clients/', client_list_create, name='client-list-create'),
    path('clients/<int:pk>/', client_retrieve_update_destroy, name='client-retrieve-update-destroy'),

    # Mailing URLs
    path('mailings/', mailing_list_create, name='mailing-list-create'),
    path('mailings/<int:pk>/', mailing_retrieve_update_destroy, name='mailing-retrieve-update-destroy'),

    # Message URLs
    path('messages/', message_list_create, name='message-list-create'),
    path('messages/<int:pk>/', message_retrieve_update_destroy, name='message-retrieve-update-destroy'),
]
