from queue_module import Queue

def test_queue():
    q = Queue()

    assert q.is_empty() == True, "Queue should be empty initially"

    q.enqueue("Alice")
    q.enqueue("Bob")
    q.enqueue("Charlie")

    assert q.peek() == "Alice", "Peek should return the first item"

    assert q.dequeue() == "Alice", "Dequeue should remove and return the first item"
    assert q.peek() == "Bob", "Peek should now return Bob"

    assert q.is_empty() == False, "Queue should not be empty"

    winner = q.select_and_announce_winner()
    assert winner in ["Bob", "Charlie"], "Winner should be one of the remaining names"

    assert q.is_empty() == True, "Queue should be empty after selecting a winner"

    print("All tests passed!")

if __name__ == "__main__":
    test_queue()
