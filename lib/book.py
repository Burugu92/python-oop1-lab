
# Step 1: Book Class Definition

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Initialize private attribute
        self.page_count = page_count  # Use property setter for validation

    # Property for page_count
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Method to simulate turning a page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# Example usage
book1 = Book("power mechanics", 250)
print(book1.title)        # Output: power mechanics
print(book1.page_count)   # Output: 250

book1.turn_page()         # Output: Flipping the page...wow, you read fast!

book2 = Book("Interesting Read", "three hundred")  # Output: page_count must be an integer
        