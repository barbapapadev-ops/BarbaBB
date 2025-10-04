# BarbaBB

BarbaBB is a friendly, modular algorithmic trading platform inspired by the Barbapapa universe and powered by OpenBB. It helps you build, test, and visualize trading strategies for Forex markets with a clean, professional codebase.

## Features
- Loads Forex data using OpenBB SDK
- Generates trading signals with a simple SMA crossover strategy
- Applies basic risk management (stop-loss, exposure)
- Simulates order execution
- Visualizes results with matplotlib

## Structure
- `barbabb/core`: Orchestrator
- `barbabb/data`: Data loading
- `barbabb/strategy`: Signal generation
- `barbabb/risk`: Risk management
- `barbabb/oms`: Order management simulation
- `barbabb/viz`: Visualization
- `barbabb/utils`: Utilities
- `barbabb/tests`: Tests

## Getting Started
1. Install dependencies: `pip install -r requirements.txt`
2. Run: `python main.py`

BarbaBB is your smart, helpful trading assistant. Happy trading!
