# Lets write a python program to simulate a food orders system where users can create
# orders and the manager can see the current QUEUE and perform actions on it
from collections import deque
# - A way to gather commands/information from the user (done)
# - Collected information should be stored in a data structure (done)
# - Methods to acess or modify the stored information (done)
# - Define a status for the current order and inform the user when that status changes (done)
# - The manager should keep track of the current and new orders, perform updates on them in a non finite way. (done)
# - Command list orders
# - Use decapitalize at all and remove blank spaces from the user's input (done)


from enum import StrEnum, Enum


class PROGRAM_INTRUCTIONS(StrEnum):
    EXIT = 'Exit'
    DEQUEUE = 'Completed'
    LIST = "List"


class ORDER_STATUS(Enum):
    PENDING = 1
    ENQUEUED = 2
    COMPLETED = 3


def getTextInput():
    return input("\nWhat is your order or your command? ").strip().capitalize()


class Order:
    def __init__(self, data):
        self.data = data
        self.status = ORDER_STATUS.PENDING
        self.next = None

    def setNextOrder(self, order):
        self.next = Order


class OrdersQueue:
    def __init__(self):
        self.head = None  # NEVER CHANGE

    def enqueue_order(self, new_order):
        if isinstance(self.head, Order):  # self.head is of the Order type
            current = self.head  # auxiliary pointer
            while current.next:  # traverse all orders to find the last one
                current = current.next  # visit the next node
            current.next = new_order  # insert new order at the end of the linked list

        else:  # if self.head is empty, then the orders list are nothing
            self.head = new_order  # then use the new order as the head of the list
        print(f"\nThe order {new_order.data} has been created!")
        new_order.status = ORDER_STATUS.ENQUEUED
        current = self.head

    def dequeue_order(self):
        if isinstance(self.head, Order):
            self.head.status = ORDER_STATUS.COMPLETED
            print(f"\nThe order {self.head.data} has been completed!")
            self.head = self.head.next

    def print_list(self):
        if isinstance(self.head, Order):
            self.head.status = PROGRAM_INTRUCTIONS.LIST
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next

    def can_i_close(self):
        return not self.head

def OpenRestaurant():
    print("Welcome to Rest.PY!")
    currentInput = ''
    orders = OrdersQueue()

    while True:
        currentInput = getTextInput()
        if currentInput:
            if currentInput == PROGRAM_INTRUCTIONS.EXIT:
                if orders.can_i_close():
                    print("""\nIt was a pleasure to have you at our restaurant.
                    Rest.PY closed!""")
                    quit()
                else:
                    print("""\nThe restaurant order's list is not empty.""") # Let the manager the name of the orders that need to be done before close the restaurant.
            elif currentInput == PROGRAM_INTRUCTIONS.DEQUEUE: # If there are no orders to be completed, let the manager know.
                orders.dequeue_order()
            elif currentInput == PROGRAM_INTRUCTIONS.LIST:
                print("\nWe still have the following order(s):")
                orders.print_list()
            else:
                new_order = Order(currentInput)
                orders.enqueue_order(new_order)

OpenRestaurant()