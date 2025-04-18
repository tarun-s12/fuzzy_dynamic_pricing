from fuzzy_pricing import FuzzyPricingSystem
from config import BASE_PRICE, SHOW_GRAPHS, CURRENCY_SYMBOL

def main():
    print("="*80)
    print("DYNAMIC PRICING SYSTEM DEMO")
    print("="*80)
    
    # PART 1: Demo with manual inputs
    print("\n1. TESTING WITH MANUAL INPUTS:")
    print("-"*50)
    
    # Create a pricing system instance with standard settings
    pricing_system = FuzzyPricingSystem(base_price=BASE_PRICE)
    
    # Example 1: High demand, scarce availability
    result1 = pricing_system.calculate_price_adjustment(
        demand=80, 
        availability=20, 
        urgency=70, 
        proximity=30,
        weather=80
    )
    print_result("High demand scenario", result1)
    
    # Show graph for Example 1
    if SHOW_GRAPHS:
        pricing_system.visualize_output(
            demand=80, 
            availability=20, 
            urgency=70, 
            proximity=30,
            weather=80
        )
    
    # Example 2: Moderate values
    result2 = pricing_system.calculate_price_adjustment(
        demand=50, 
        availability=50, 
        urgency=50, 
        proximity=50,
        weather=50
    )
    print_result("Moderate scenario", result2)
    
    # Show graph for Example 2
    if SHOW_GRAPHS:
        pricing_system.visualize_output(
            demand=50, 
            availability=50, 
            urgency=50, 
            proximity=50,
            weather=50
        )
    
    # Example 3: Low demand, high availability
    result3 = pricing_system.calculate_price_adjustment(
        demand=30, 
        availability=70, 
        urgency=20, 
        proximity=80,
        weather=90
    )
    print_result("Low demand scenario", result3)
    
    # Show graph for Example 3
    if SHOW_GRAPHS:
        pricing_system.visualize_output(
            demand=30, 
            availability=70, 
            urgency=20, 
            proximity=80,
            weather=90
        )

def print_result(title, result, show_real_data=False):

    print(f"\n--- {title} ---")
    inputs = result['inputs']
    print(f"Inputs: Demand={inputs['demand']}%, Availability={inputs['availability']}%, "
          f"Urgency={inputs['urgency']}%, Proximity={inputs['proximity']}%")
    
    if show_real_data and 'real_time_data' in result:
        real_data = result['real_time_data']
        data_source = real_data.get('data_source', 'unknown')
        print(f"Time: {real_data['time']}, Day: {real_data['day']}, Season: {real_data['season']} (Source: {data_source})")
        
        if 'weather' in real_data:
            weather = real_data['weather']
            print(f"Weather: {weather['condition']}, {weather['temperature']}°C (Score: {inputs['weather']}%)")
        else:
            print(f"Weather: {inputs['weather']}%")
    else:
        print(f"Weather: {inputs['weather']}%")
        print(f"Time: {inputs['time_of_day']}h, Day: {inputs['day_of_week']}, Season: {inputs['season']}")
    
    # Use the currency symbol from the result
    currency_symbol = result.get('currency_symbol', '₹')
    
    print(f"Price Adjustment: {result['price_adjustment_percent']:.2f}%")
    print(f"Base Price: {currency_symbol}{result['base_price']:.2f}/hour")
    print(f"Adjusted Price: {currency_symbol}{result['adjusted_price']:.2f}/hour")

if __name__ == "__main__":
    main()