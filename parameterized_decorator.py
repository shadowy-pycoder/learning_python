#!/usr/bin/env python3
# Simple parameterized decorator for re-executing the decorated function after a while.
# Uses a naive exponential growth of the repeat time (factor)
# to the boundary timeout (border_sleep_time).
from functools import wraps
from time import sleep
from typing import Callable, TypeVar, Optional, Protocol, Any


class SupportsMul(Protocol):
    def __mul__(self, other: Any) -> Any: ...


ML = TypeVar('ML', bound=SupportsMul)


def slower(
    *,
    call_count: int = 1,
    start_sleep_time: int = 0,
    factor: int = 0,
    border_sleep_time: int = 0
) -> Callable:
    def decorate(func: Callable[[ML], ML | None]) -> Callable:
        @wraps(func)
        def slow(num: ML) -> None:
            nonlocal start_sleep_time
            print('Number of calls', call_count)
            print('Start')
            for call in range(1, call_count+1):
                t = start_sleep_time * 2**factor
                if t >= border_sleep_time:
                    t = border_sleep_time
                start_sleep_time = t
                print(f'Function call {call}. Waiting {t} seconds... ', end='')
                sleep(t)
                print('Result: ', func(num))
            print('End')
        return slow
    return decorate


@slower(call_count=3, start_sleep_time=1, factor=1, border_sleep_time=100)
def multiplier(param: Optional[ML] = None) -> ML | None:
    return param * 2 if param is not None else param


multiplier(5)
