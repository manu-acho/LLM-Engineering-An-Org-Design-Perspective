"""Checks for the shared notebook workspace, using dummy credentials only."""

from unittest.mock import patch

import pytest

from ai_orgdesign import workspace


def test_root_contains_course():
    assert (workspace.project_root() / "examples/01-foundations/foundations_lab.py").is_file()


def test_missing_key_has_actionable_message():
    with (
        patch.object(workspace, "load_local_environment"),
        patch.dict(workspace.os.environ, {}, clear=True),
    ):
        with pytest.raises(RuntimeError, match="Set COURSE_TEST_KEY"):
            workspace.require_api_key("COURSE_TEST_KEY")


def test_key_is_returned_without_output(capsys):
    with (
        patch.object(workspace, "load_local_environment"),
        patch.dict(workspace.os.environ, {"COURSE_TEST_KEY": "dummy-value"}),
    ):
        assert workspace.require_api_key("COURSE_TEST_KEY") == "dummy-value"
    assert capsys.readouterr().out == ""


def test_environment_uses_explicit_path_and_preserves_shell_values():
    with patch.object(workspace, "load_dotenv", return_value=True) as loader:
        assert workspace.load_local_environment()
    loader.assert_called_once_with(workspace.project_root() / ".env", override=False)
