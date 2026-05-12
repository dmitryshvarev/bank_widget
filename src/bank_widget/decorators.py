from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable], Callable]:
    """
    Фабрика декораторов. Принимает параметр декоратора и возвращает сам декоратор.

    :param filename: Название файла, куда будет записываться вывод работы декоратора.
                     Если не передаётся, информация выводится в консоль.
    :return: Декоратор, который оборачивает исходную функцию.
    """

    def decorator(func: Callable) -> Callable:

        @wraps(func)  # Сохраняет docstring и __name__ оригинальной функции
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """
            Обертка для декорируемой функции.
            Логирует выполнение функции, ее результаты или возникшие ошибки.
            """
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
            except Exception as error:
                result = None
                log_message = f"{func.__name__} error ({type(error).__name__}: {error}). Inputs: {args}, {kwargs}"

            if filename:
                with open(f"../{filename}", "a", encoding="UTF-8") as file:
                    file.write(f"{log_message}\n")
            else:
                print(log_message)

            return result

        return wrapper

    return decorator
