#### Implementation using collections.deque

Queue in Python can be implemented using deque class from the collections module. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. Instead of enqueue and deque, append() and popleft() functions are used.

#### Implementation using queue.Queue

Queue is built-in module of Python which is used to implement a queue. queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule.
There are various functions available in this module:

* **maxsize ** – Number of items allowed in the queue.
* **empty()** – Return True if the queue is empty, False otherwise.
* **full()** – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
* **get()** – Remove and return an item from the queue. If queue is empty, wait until an item is available.
* **get_nowait()** – Return an item if one is immediately available, else raise QueueEmpty.
* **put(item)** – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
* **put_nowait(item)** – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
* **qsize()** – Return the number of items in the queue.
