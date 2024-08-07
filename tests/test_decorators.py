import pytest

from src.decorators import log


def test_log_to_console(capsys):
    @log()
    def test_func_success(x: int, y: int) -> int:
        return x + y

    captured = capsys.readouterr()
    assert "test_func_success ok" in captured.out


def test_log_to_console_error(capsys):
    @log()
    def test_func_error(x: int, y: int) -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        test_func_error(1, 2)
    captured = capsys.readouterr()
    assert "test_func_error error: Test error. Inputs: (1, 2), {}" in captured.out
