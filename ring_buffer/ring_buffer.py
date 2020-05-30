class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.index = 0 

    def append(self, item):
        # Adds the given element to the buffer
        # Handle if list is full
        """ Append an element overwriting the oldest one. """
        if len(self.data) == self.capacity:
            self.data[self.index] = item
        else:
            self.data.append(item)
        self.index = (self.index + 1) % self.capacity
        

    def get(self):
        # Returns all of the elements in the buffer in a list in their given order
        # Should not return any None values
        if len(self.data) != self.capacity:
            new_data = [d for d in self.data if d is not None]
            return new_data
        else:
            return self.data

        