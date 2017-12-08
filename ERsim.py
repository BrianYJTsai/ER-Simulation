#  File: ERsim.py
#  Description: This program simulates an ER. Patients checked in will be treated based on the severity of their injuries
#  Patients will be put on queue and treated based on the conditions of the command. Output is who has been treated and
#  who is left to be treated
#  Student's Name: Brian Tsai
#  Student's UT EID: byt76
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 10/17/17
#  Date Last Modified: 10/19/17


class Queue:
    # Create a new queue
    def __init__(self):
        self.items = []

    # Add a new item to the back of the queue
    def enqueue(self,item):
        self.items.insert(0, item)

    # Remove and return the first element in the queue
    def dequeue(self):
        return self.items.pop()

    # Return whether the queue is empty
    def isEmpty(self):
        return self.items == []

    # Return whether the queue is not empty
    def notEmpty(self):
        return self.items != []

    # Return the number of elements in the queue
    def size(self):
        return len(self.items)

    # Return a copy of the back element in the queue
    def peek(self):
        return self.items[0]

    # Return a string representation of the queue
    def __str__(self):
        return str(self.items)

# Command to add new patient
def addPatient(condition, name):

    # See which queue the patient should be added to
    if (condition == "Critical"):
        CRITICAL.enqueue(name)
    if (condition == "Serious"):
        SERIOUS.enqueue(name)
    if (condition == "Fair"):
        FAIR.enqueue(name)

    # Output the command and current queues
    print("Command: Add patient", name, "to", condition, "queue\n")
    printQueues()

# Command to treat the next patient in order of priority
def treatNext():

    print("Command: Treat next patient\n")

    if (CRITICAL.notEmpty()):
        name = CRITICAL.dequeue()
        queue = "Critical"
    elif (SERIOUS.notEmpty()):
        name = SERIOUS.dequeue()
        queue = "Serious"
    elif (FAIR.notEmpty()):
        name = FAIR.dequeue()
        queue = "Fair"
    else:
        print("     No patients in queues\n")
        return

    # Output who is being treated and current queues
    print("     Treating", name, "from", queue, "queue")
    printQueues()

# Command to treat the next patient based on their condition
def treatCondition(condition):

    print("Command: Treat next patient on", condition, "queue\n")

    if (condition == "Critical" and CRITICAL.notEmpty()):
        name = CRITICAL.dequeue()
    elif (condition == "Serious" and SERIOUS.notEmpty()):
        name = SERIOUS.dequeue()
    elif (condition == "Fair" and FAIR.notEmpty()):
        name = FAIR.dequeue()
    else:
        print("     No patients in queue\n")
        return

    # Output who is being treated and current queues
    print("     Treating", name, "from", condition, "queue")
    printQueues()

# Command to treat all the patients based on priority until their are no more patients
def treatAll():

    print("Command: Treat all patients\n")

    # Keep treating patients in their priority order until there are no more patients
    while(True):
        if (CRITICAL.notEmpty()):
            print("     Treating", CRITICAL.dequeue(), "from Critical queue")
            printQueues()
        elif (SERIOUS.notEmpty()):
            print("     Treating", SERIOUS.dequeue(), "from Serious queue")
            printQueues()
        elif (FAIR.notEmpty()):
            print("     Treating", FAIR.dequeue(), "from Fair queue")
            printQueues()
        else:
            print("     No patients in queues\n")
            break


# Command to exit the program
def exit():

    # Exit the program
    print("Command: Exit")


def printQueues():

    # Output each of the queues
    print("     Queues are:")
    print("     Fair: ", FAIR)
    print("     Serious: ", SERIOUS)
    print("     Critical: ", CRITICAL, "\n")

# The different queues based on priority
SERIOUS = Queue()
FAIR = Queue()
CRITICAL = Queue()

def main():

    # Open the text file for parsing
    input = open("ERsim.txt", "r")

    # Iterate over each line
    for line in input:

        # Get the string tokens
        line = line.strip()
        line = line.split(" ")

        # Execute the command based on the first token
        if (line[0] == "add"):
            addPatient(line[1], line[2])
        elif (line[0] == "treat"):
            if (line[1] == "next"):
                treatNext()
            elif (line[1] == "all"):
                treatAll()
            else:
                treatCondition(line[1])
        else:
            exit()
            break

    # Close the buffer
    input.close()

main()