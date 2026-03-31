# Celsius temperature data
cel = [37.1, 36.8, 37.0, 37.4, 36.5]

# Convert and display Fahrenheit temperature
for celsius in cel:
    fahrenheit = (celsius * 9/5) + 32
    print(f"Celsius {celsius}°C converted to Fahrenheit {fahrenheit:.1f}°F")
