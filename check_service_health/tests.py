"""Tests for check_service_health application."""
import pytest
from django.test import TestCase
from django.core.management import call_command
from django.core.cache import cache
from io import StringIO


class TestHealthCheckBasic(TestCase):
    """Basic tests for health check."""

    def test_check_service_health_app_exists(self):
        """Test that check_service_health app is properly configured."""
        from django.apps import apps
        app = apps.get_app_config('check_service_health')
        self.assertIsNotNone(app)


class TestCacheManagementCommand(TestCase):
    """Tests for test_cache management command."""

    def test_test_cache_command_exists(self):
        """Test that test_cache command exists."""
        try:
            call_command('test_cache', stdout=StringIO())
        except Exception as e:
            self.fail(f"test_cache command failed: {e}")

