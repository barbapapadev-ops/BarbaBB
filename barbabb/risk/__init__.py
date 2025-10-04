import logging
from typing import List

class RiskManager:
    """Basic stop-loss and exposure control."""
    def __init__(self, stop_loss: float = 0.05, max_exposure: float = 1.0):
        self.stop_loss = stop_loss
        self.max_exposure = max_exposure
        self.logger = logging.getLogger("RiskManager")

    def apply(self, signals: List[int], prices: List[float]) -> List[int]:
        self.logger.info("Applying risk controls.")
        # Placeholder logic
        return signals
