import random

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # Add an item to the end of the queue
        self.items.append(item)

    def dequeue(self):
        # Remove and return the item from the front of the queue
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        # Return the item at the front of the queue without removing it
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        # Return True if the queue is empty
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            return None

        # Randomly pick an index of the winner
        winner_index = random.randint(0, len(self.items) - 1)
        winner = self.items[winner_index]

        # Dequeue up to and including the winner
        for _ in range(winner_index + 1):
            self.dequeue()

        return winner


def is_valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    def test_queue():
        q = Queue()
        print("Is empty initially?", q.is_empty())  # True

        q.enqueue("Alice")
        q.enqueue("Bob")
        q.enqueue("Charlie")

        print("Peek:", q.peek())  # Alice
        print("Is empty after enqueue?", q.is_empty())  # False

        winner = q.select_and_announce_winner()
        print("Winner:", winner)
        print("Queue after winner selection:", q.items)

        while not q.is_empty():
            print("Dequeue:", q.dequeue())

        print("Is empty after dequeues?", q.is_empty())  # True

    test_queue()
