import pytest

from src.bank_widget.decorators import log


def test_log(capsys):

    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)

    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_err(capsys):

    @log()
    def my_function(x, y):
        return x + y

    my_function('1', 2)

    captured = capsys.readouterr()
    assert captured.out == "my_function error (TypeError: can only concatenate str (not \"int\") to str). Inputs: (\'1\', 2), {}\n"


def test_log_file():
    file_name = "mylog.txt"

    @log(filename=file_name)
    def my_function(x, y):
        return x + y

    my_function(1, 2)

    with open(f'../{file_name}', 'r', encoding="UTF-8") as file:
        assert file.read() == "my_function ok\n"
