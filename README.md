# Fuzzy Logic Dynamic Pricing System

A modular Python package for dynamic price adjustment based on multiple factors using fuzzy logic.

## Features

- **Multi-factor pricing**: Considers demand, availability, urgency, proximity, weather, time of day, day of week, and season
- **Mock data support**: Can use mock data instead of API calls for testing and development
- **Fuzzy logic decision-making**: Handles uncertainty and combines multiple rules
- **Visualization tools**: Visualize the fuzzy logic output
- **Flexible deployment**: Can be used as a standalone package or integrated into larger systems

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from fuzzy_pricing import FuzzyPricingSystem

pricing = FuzzyPricingSystem(base_price=50)

# Calculate price adjustment with manual inputs
result = pricing.calculate_price_adjustment(
    demand=80,           # High demand (0-100%)
    availability=20,     # Low availability (0-100%)
    urgency=70,          # High urgency (0-100%)
    proximity=30,        # Far distance (0-100%)
)

print(f"Price Adjustment: {result['price_adjustment_percent']:.2f}%")
print(f"Adjusted Price: ${result['adjusted_price']:.2f}/hour")
# Visualize the output
pricing.visualize_output(
    demand=80,
    availability=20,
    urgency=70,
    proximity=30,
    city="Mumbai"
)
```

### Customizing Mock Data

You can customize the mock data by editing the `mock_data.py` file:

```python
# Add or modify city weather data
MOCK_WEATHER_DATA = {
    "Your City": {
        "temperature": 22.5,
        "condition": "Clear",
        "wind_speed": 3.0
    },
    # ... other cities
}
```

## Architecture

The package is organized into the following components:

- `fuzzy_pricing.py`: Main class that integrates all components
- `models.py`: Fuzzy logic variables and membership functions
- `rules.py`: Fuzzy logic rules for price adjustment
- `data_providers.py`: Real-time data providers for weather and time
- `mock_data.py`: Mock data for testing without API calls

## Example Rules

The system includes 32 rules, such as:

- If demand is high AND availability is scarce AND urgency is high → increase price
- If demand is low AND availability is plentiful → decrease price
- If it's a weekend AND season is summer AND weather is good → increase price (premium leisure time)
- If it's night AND weather is poor AND proximity is far → increase price
- If it's a weekday during business hours AND weather is good → decrease price