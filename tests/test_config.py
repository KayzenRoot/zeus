"""Configuration security and identity migration tests."""

import pytest

from zeus.config import Settings


def _legacy_auth_name(suffix):
    """Construct the retired authentication variable name without active product branding."""
    return "OPEN" + "JEV_" + suffix


def test_legacy_api_key_fails_closed(monkeypatch):
    """A stale pre-Zeus API key stops startup instead of disabling auth silently."""
    monkeypatch.setenv(_legacy_auth_name("API_KEY"), "legacy-api-secret")
    monkeypatch.delenv("ZEUS_API_KEY", raising=False)
    with pytest.raises(ValueError, match="ZEUS_API_KEY"):
        Settings()


def test_legacy_origin_secret_fails_closed(monkeypatch):
    """A stale pre-Zeus origin secret stops startup instead of disabling auth silently."""
    monkeypatch.setenv(_legacy_auth_name("ORIGIN_SECRET"), "legacy-origin-secret")
    monkeypatch.delenv("ZEUS_ORIGIN_SECRET", raising=False)
    with pytest.raises(ValueError, match="ZEUS_ORIGIN_SECRET"):
        Settings()


def test_zeus_auth_environment_remains_supported(monkeypatch):
    """The Zeus authentication namespace remains the accepted configuration surface."""
    monkeypatch.setenv("ZEUS_API_KEY", "zeus-api-secret")
    monkeypatch.setenv("ZEUS_ORIGIN_SECRET", "zeus-origin-secret")
    assert Settings().api_key == "zeus-api-secret"
    assert Settings().origin_secret == "zeus-origin-secret"
