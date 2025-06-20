# simple_interest.py

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Example usage
p = 1000  # Principal amount
r = 5     # Interest rate
t = 2     # Time in years

print("Simple Interest:", calculate_simple_interest(p, r, t))
