from typing import AsyncIterator, Awaitable, Callable, Generic, List, TypeVar, Union


T = TypeVar("T")
R = TypeVar("R")

class ConnectionIterator(AsyncIterator[T]):
    def filter(self, func: Callable[[T], Union[bool, Awaitable[bool]]]) -> ConnectionIterator[T]: ...
    def map(self, func: Callable[[T], Union[R, Awaitable[R]]]) -> ConnectionIterator[R]: ...
    async def flatten(self) -> List[T]: ...
