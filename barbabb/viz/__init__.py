import logging
from typing import List
import matplotlib.pyplot as plt

class Visualizer:
    """Visualizes results using matplotlib."""
    def __init__(self):
        self.logger = logging.getLogger("Visualizer")

    def plot(self, prices: List[float], signals: List[int], trades: List[float]) -> None:
        self.logger.info("Plotting results.")
        plt.figure(figsize=(10, 5))
        plt.plot(prices, label="Prices")
        plt.plot(signals, label="Signals")
        plt.plot(trades, label="Trades")
        plt.legend()
        plt.title("BarbaBB Trading Results")
        plt.show()
