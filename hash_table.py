class Contact:
    def __init__(self, name, number): #intializes contact
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}" #retruns string of contact

class Node:
    def __init__(self, key, value): #initializes node
        self.key = key
        self.value = value
        self.next= None

class HashTable:

    def __init__(self, size): #initializes the array
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0 
        for char in key:
            total += ord(char) #adds unicode values together
        return total % self.size #returns index 
    
        
    def insert(self, key, value):
        index = self.hash_function(key)#gets index of key

        current = self.data[index]#gets values assigned to index

        if self.data[index] is None: 
            self.data[index] = Node(key, value)
            return
        
        while current: #uses chaining to help with collisions
            if current.key == key:
                current.value = value #handles edge case of same index by updating current value to new data
                return

            if current.next == None: #ends at the last node
                break
            current = current.next #continues loop

        current.next = Node(key, value) #adds new node to chain

    def search(self, key):
        index = self.hash_function(key) #gets index for the key
        current = self.data[index] #gets the node at the index

        while current: #loops through 
            if current.key == key:
                return current.value
            current = current.next #moves to next node
        return None #returns none for edge case of node not existing
    

    def print_table(self):
        for index, node in enumerate(self.data): #index is the variable for index, node is the information
            
            if node is None: #if node is empty
                print(f"Index {index}: Empty")
            else: #if node is not empty prints index and contents.
                current_node = node
                while current_node:
                    print(f"Index {index}: {current_node.key} - {current_node.value}") #prints index, key, and value
                    current_node = current_node.next #moves to next node
        
        


# Test your hash table implementation here.  
contact_1 = Contact("Riley", "123-456-7890")
print(contact_1.name) # Riley
print(contact_1.number) # 123-456-7890 
print(contact_1) # Riley: 123-456-7890 

contact_1 = Contact("Riley", "123-456-7890")
node_1 = Node(contact_1.name, contact_1)
print(node_1.key) # Riley 
print(node_1.value) # Riley: 123-456-7890 
print(node_1.next) # None 

table = HashTable(10)
table.print_table()

table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
# Print the new table structure 
table.print_table()



#edge cases
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")  # May collide with Amy depending on hash function 
table.print_table()

table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number 
table.print_table()

print(table.search("Chris"))