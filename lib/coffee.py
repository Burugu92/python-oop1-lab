
# Step 2: Coffee Class Definition

class Coffee:
    def __init__(self, size, price):
        self._size = None  # private attribute
        self.size = size   # use setter for validation
        self.price = price

    # Property for size with validation
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ["Small", "Medium", "Large"]
        if value in valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    # Method to give a tip
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1  # increase price by 1

# Example usage
coffee1 = Coffee("Medium", 3.5)
print(coffee1.size)   # Output: Medium
print(coffee1.price)  # Output: 3.5

coffee1.tip()         # Output: This coffee is great, here’s a tip!
print(coffee1.price)  # Output: 4.5

coffee2 = Coffee("Medium Small", 5)  # Output: size must be Small, Medium, or Large