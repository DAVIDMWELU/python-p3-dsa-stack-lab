class Stack:
    def __init__(self, items=None, max_size=None):
        """Initialize the stack with optional items and an optional max size."""
        self.items = items if items is not None else []  # Initialize with a list
        self.max_size = max_size  # Optional max size for the stack

    def push(self, value):
        """Push a value onto the stack. Raise an error if the stack is full."""
        if self.max_size is not None and len(self.items) >= self.max_size:
            raise IndexError("Stack is full")
        self.items.append(value)

    def pop(self):
        """Pop a value from the stack. Raise an error if the stack is empty."""
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def size(self):
        """Return the size of the stack."""
        return len(self.items)

    def empty(self):
        """Return True if the stack is empty, otherwise False."""
        return len(self.items) == 0

    def full(self):
        """Return True if the stack is full, otherwise False."""
        if self.max_size is None:
            return False  # No max size means the stack can never be full
        return len(self.items) >= self.max_size

    def search(self, value):
        """Search for the value in the stack. Returns the distance from the top of the stack."""
        try:
            # The index from the bottom of the stack
            index_from_bottom = self.items.index(value)
            # Distance from the top of the stack
            return len(self.items) - 1 - index_from_bottom
        except ValueError:
            return -1  # If the value is not found, return -1
