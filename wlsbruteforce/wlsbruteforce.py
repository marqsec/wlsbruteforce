import itertools
import string
from typing import Generator, Optional

DEFAULT_CHARSET = string.ascii_lowercase + string.ascii_uppercase + string.digits

class WlsBruteforce:
    def __init__(self, charset: Optional[str] = DEFAULT_CHARSET):
        self._charset = charset
        self.total_combinations_estimate: int = 0
        
    def _calculate_combinations(self, min_length: int, max_length: int) -> int:
        total = 0
        charset_size = len(self._charset)
        for length in range(min_length, max_length + 1):
            total += charset_size ** length
        return total

    def brute(self, min_length: int, max_length: int) -> Generator[str, None, None]:
        if min_length <= 0:
            raise ValueError("min_length harus berupa bilangan bulat positif (> 0).")
        if max_length < min_length:
            raise ValueError("max_length tidak boleh kurang dari min_length.")
        
        self.total_combinations_estimate = self._calculate_combinations(min_length, max_length)

        for length in range(min_length, max_length + 1):
            combinations = itertools.product(self._charset, repeat=length)
            
            for attempt in combinations:
                yield ''.join(attempt)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
