import logging
import os
from typing import Any

try:
    from openbb import obb
except ImportError:
    obb = None

class DataLoader:
    """Loads Forex data using OpenBB SDK."""
    def __init__(self):
        self.logger = logging.getLogger("DataLoader")

    def load(self, symbol: str) -> Any:
        self.logger.info(f"Loading data for {symbol} using OpenBB SDK.")
        if obb is None:
            self.logger.error("OpenBB SDK is not installed.")
            return []
        fmp_api_key = os.getenv("FMP_API_KEY") or "RcFy1G4m06mV2C70nzhqbVU0okTYCTRu"
        try:
            obb.account.set_credential("fmp_api_key", fmp_api_key)
        except Exception as e:
            self.logger.error(f"Failed to set FMP API key: {e}")
            return []
        try:
            # Use 'fmp' provider and default dates for demo
            data = obb.currency.price.historical(symbol=symbol, provider='fmp')
            self.logger.info(f"Loaded {len(data.results)} records for {symbol}.")
            return data.results
        except Exception as e:
            self.logger.error(f"Failed to load data: {e}")
            return []
