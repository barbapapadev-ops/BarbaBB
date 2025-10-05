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

### Installation

#### Option 1: Quick Install (Recommended)
```bash
pip install -r requirements.txt
```

#### Option 2: Local Development with OpenBB Fork
If you need to modify OpenBB alongside BarbaBB:

```bash
# Clone the OpenBB fork (if not already cloned)
git clone https://github.com/barbapapadev-ops/OpenBB.git
cd OpenBB
git checkout develop

# Install OpenBB in editable mode
pip install -e .

# Return to BarbaBB and install other dependencies
cd ../BarbaBB
pip install matplotlib
```

### Running BarbaBB
```bash
python main.py
```

## Dependencies

- **OpenBB**: We use our own fork at [barbapapadev-ops/OpenBB](https://github.com/barbapapadev-ops/OpenBB) (branch: `develop`)
  - This fork includes custom modifications for BarbaBB
- **matplotlib**: For visualization

BarbaBB is your smart, helpful trading assistant. Happy trading!
