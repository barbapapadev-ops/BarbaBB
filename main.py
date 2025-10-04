"""
BarbaBB Main Entrypoint
Runs the full workflow: data → signal → risk → execution → visualization.
"""
import logging
from barbabb.core import BarbaCore
from barbabb.data import DataLoader
from barbabb.strategy import SMACrossoverStrategy
from barbabb.risk import RiskManager
from barbabb.oms import OMSimulator
from barbabb.viz import Visualizer

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("BarbaBB")
    logger.info("Welcome to BarbaBB — your friendly trading assistant!")

    # Step 1: Load data
    data_loader = DataLoader()
    prices = data_loader.load("EURUSD")

    # Step 2: Generate signals
    strategy = SMACrossoverStrategy()
    signals = strategy.generate_signals(prices)

    # Step 3: Apply risk controls
    risk_manager = RiskManager()
    safe_signals = risk_manager.apply(signals, prices)

    # Step 4: Simulate execution
    oms = OMSimulator()
    trades = oms.execute(safe_signals, prices)

    # Step 5: Visualize results
    viz = Visualizer()
    viz.plot(prices, safe_signals, trades)

if __name__ == "__main__":
    main()
