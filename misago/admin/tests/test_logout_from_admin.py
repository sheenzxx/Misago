from django.contrib.messages import get_messages
from django.urls import reverse

from ...test import assert_contains
from ..auth import is_admin_authorized

admin_logout_link = reverse("misago:admin:logout")
site_logout_link = reverse("misago:logout")
site_link = reverse("misago:index")


def test_admin_can_logout_from_admin_site_but_stay_logged(admin_client, superuser):
    response = admin_client.post(admin_logout_link)
    assert response.wsgi_request.user == superuser
    assert not is_admin_authorized(response.wsgi_request)


def test_admin_is_redirected_to_site_on_logout(admin_client, superuser):
    response = admin_client.post(admin_logout_link)
    assert response.status_code == 302
    assert response["location"] == site_link


def test_admin_is_displayed_a_message_after_logout(admin_client, superuser):
    response = admin_client.post(admin_logout_link)
    message = list(get_messages(response.wsgi_request))[0]
    assert str(message) == "Your admin session has been closed."


def test_admin_can_logout_from_entire_site(admin_client):
    response = admin_client.post(site_logout_link)
    assert response.wsgi_request.user.is_anonymous
    assert not is_admin_authorized(response.wsgi_request)


def test_admin_is_redirected_to_site_on_logout(admin_client, superuser):
    response = admin_client.post(admin_logout_link)
    assert response.status_code == 302
    assert response["location"] == site_link
