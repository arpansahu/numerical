"""
Shared pytest fixtures for numerical project.
"""
import pytest
import os
from django.test import Client
from django.contrib.auth import get_user_model


@pytest.fixture
def server_url():
    """Server URL for UI tests. Set PLAYWRIGHT_BASE_URL env var or uses default."""
    return os.environ.get('PLAYWRIGHT_BASE_URL', 'http://localhost:8003')


@pytest.fixture
def test_user_credentials():
    """Standard test user credentials."""
    return {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'TestPassword123!'
    }


@pytest.fixture
def django_client():
    """Django test client."""
    return Client()


@pytest.fixture
def create_test_user(db, test_user_credentials):
    """Create a test user in the database."""
    User = get_user_model()
    user = User.objects.create_user(
        username=test_user_credentials['username'],
        email=test_user_credentials['email'],
        password=test_user_credentials['password']
    )
    return user


@pytest.fixture
def authenticated_client(django_client, create_test_user, test_user_credentials):
    """Django test client with authenticated user."""
    django_client.login(
        username=test_user_credentials['username'],
        password=test_user_credentials['password']
    )
    return django_client
