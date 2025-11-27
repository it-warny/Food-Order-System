# Lets write a python program to simulate a food orders system where users can create
# orders and the manager can see the current QUEUE and perform actions on it
from collections import deque
# - A way to gather commands/information from the user (done)
# - Collected information should be stored in a data structure (done)
# - Methods to acess or modify the stored information (in progress)
# - Define a status for the current order and inform the user when that status changes
# - The manager should keep track of the current and new orders, perform updates on them in a non finite way.
# - Command list orders
# - Use decapitalize at all and remove blank spaces from the user's input (done)


from enum import StrEnum, Enum

class PROGRAM_INTRUCTIONS(StrEnum):
    EXIT = 'Exit'
    DEQUEUE = 'Completed'

class ORDER_STATUS(Enum):
    PENDING = 1
    ENQUEUED = 2
    COMPLETED = 3

def getTextInput():
    return input("What is your order or your command? ").strip().capitalize()

class Order:
    def __init__(self, data):
        self.data = data
        self.status = ORDER_STATUS.PENDING
        self.next = None

    def setNextOrder(self, order):
        self.next = order


class OrdersQueue:
    def __init__(self):
        self.head = None  # NEVER CHANGE

    def enqueue_order(self, new_order):
        if isinstance(self.head, Order):  # self.head is of the Order type
            current = self.head  # auxiliary pointer
            while current.next:  # traverse all orders to find the last one
                current = current.next  # visit the next node
                print(f"\nThe order {self.head.data} has been created!")
            current.next = new_order  # insert new order at the end of the linked list

        else:  # if self.head is empty, then the orders list are nothing
            self.head = new_order  # then use the new order as the head of the list
        current = self.head


    def dequeue_order(self):
        if isinstance(self.head, Order):
            self.head.status = ORDER_STATUS.COMPLETED
            print(f"\nThe order {self.head.data} has been completed!")
            self.head = self.head.next
            self.print_orders()

    def print_orders(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next


def OpenRestaurant():
    print("Welcome to Rest.PY")
    currentInput = ''
    orders = OrdersQueue()

    while True:
        currentInput = getTextInput()
        if currentInput:
            if currentInput == PROGRAM_INTRUCTIONS.EXIT:
                print("""Foi um prazer ter sua interação no Rest.PY! Até breve.\nRestaurante Fechado!""")
                quit()
            elif currentInput == PROGRAM_INTRUCTIONS.DEQUEUE:
                orders.dequeue_order()
            else:
                new_order = Order(currentInput)
                orders.enqueue_order(new_order)

OpenRestaurant()


            # update previous order to point to the new one