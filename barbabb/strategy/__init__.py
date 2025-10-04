import logging
from typing import List

class SMACrossoverStrategy:
    """Simple SMA crossover signal generator."""
    def __init__(self, short_window: int = 5, long_window: int = 20):
        self.short_window = short_window
        self.long_window = long_window
        self.logger = logging.getLogger("SMACrossoverStrategy")

    def generate_signals(self, prices: List[float]) -> List[int]:
        self.logger.info("Generating SMA crossover signals.")
        # Placeholder logic
        return [0 for _ in prices]
