import pytest
from src.decorators.log import log


@log()
def test_func_success(x, y):
    return x + y


@log()
def test_func_error(x, y):
    raise ValueError("Test error")


def test_log_to_console(capsys):
    result = test_func_success(1, 2)
    captured = capsys.readouterr()
    assert "test_func_success ok" in captured.out
    assert result == 3


def test_log_to_console_error(capsys):
    with pytest.raises(ValueError, match="Test error"):
        test_func_error(1, 2)
    captured = capsys.readouterr()
    assert "test_func_error error: Test error. Inputs: (1, 2), {}" in captured.out


def test_log_to_file(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def test_func(x, y):
        return x + y

    test_func(1, 2)
    with open(log_file, 'r') as file:
        log_content = file.read()
    assert "test_func ok" in log_content


def test_log_to_file_error(tmp_path):
    log_file = tmp_path / "test_log_error.txt"

    @log(filename=str(log_file))
    def test_func(x, y):
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        test_func(1, 2)
    with open(log_file, 'r') as file:
        log_content = file.read()
    assert "test_func error: Test error. Inputs: (1, 2), {}" in log_content
