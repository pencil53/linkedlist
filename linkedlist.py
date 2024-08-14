#python program to implement the queue data structure using
#linked list

#node class representing a single node in the linked list
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

#class to implement queue operations using a linked list
class Queue:
    def __init__(self):

        #pointer to the front and the rear of the linked list
        self.front = None
        self.rear = None

    #function to check if the queue is empty
    def is_empty(self):

        #if the front and rear are null, then the queue is
        #empty, otherwise it's not
        return self.front is None and self.rear is None
    
    #function to add an element to the queue
    def enqueue(self, new_data):

        #create a new linked list node
        new_node = Node(new_data)

        #if queue is empty, the new node is both the front and rear

        if self.rear is None:
            self.front = self.rear = new_node
            return
        
        #add the new node at the end of the queue and change rear

        self.rear.next = new_node
        self.rear = new_node

    #function to remove an element from the queie
    def dequeue(self):

        #if queue is empty, return
        if self.is_empty():
            print("queue underflow")
            return
        
        #store previous front and moce front one node ahead

        temp = self.front
        self.front = self.front.next

        #if front becomes null, then change rear also to null

        if self.front is None:
            self.rear = None

    #function to get the front element of the queue
    def get_front(self):

        #checking if the queue is empty
        if self.is_empty():
            print("queue is empty")
            return float ('-inf')
        return self.front.data
    
    #function to get the rear element of the queue
    def get_rear(self):

        #checking if the queue is empty
        if self.is_empty():
            print("queue is empty")
            return float ('-inf')
        return self.rear.data
    

#Driver code
if __name__ =="__main__":
    q = Queue()

    #enqueue elements into the queue
    q.enqueue(10)
    q.enqueue(20)

    #display the front and rear elements of the queue
    print("queue front:", q.get_front())
    print("queue rear:", q.get_rear())

    #dequeue elements from the queue
    q.dequeue()
    q.enqueue()

    #enqueue more elements into the queue
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)

    #dequeue an element from the queue
    q.enqueue()

    #display the front and rear elements of the queue
    print("queue Front:", q.get_front())
    print("queue Rear:", q.get_rear())