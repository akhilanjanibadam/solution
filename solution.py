

#problem 1

class MultiDimentionalArray:
    def _init_(self, *dimentions):
        self.array = self.create_array(list(dimensions))

    def create_array(self, dimensions):
        if len(dimensions) ==1:
            return [0] * dimensions[0]
        else:
            return [self.create_array(dimensions[1:]) for _ in range(dimensions[0])]

    def add_element(self, index, value):
        self.get_element(index, set_value=value)

    def remove_element(self, index):
        self.get_element(index, remove=True)

    def get_element(self, index, set_value=None, remove=False):
        array = self.array
        for i in index[:-1]:
            array=aqrray[i]
        if set_value is not None:
            array[index[-1]] = set_value
        elif remove:
            del array[index[-1]]
        else:
            return array[index[-1]]

    def get_size(self):
        return self.get_size_recursive(self.array)
    def get_size_recursive(self, array):
        if isinstance(array[0], list):
            return len(array) * self.get_size_recursive(array[0])
        else:
            return len(array)
    def get_index(self, value):
        return self.get_index_recursive(self.array, value)

    def get_index_recursive(self, array, value, prefix=[]):
        for i, x in enumerate(array):
            if isinstance(x, list):
                result = self.get_index_recursive(x, value, prefix+[i])
                if result is not None:
                    return result
            elif x== value:
                return prefix + [i]
        return None

def main():
    dimensions = input("Enter the dimensions of the array (separated by spaces): ")
    dimensions = list(map(int, dimensions.split()))
    array = MultiDimensionalArray(*dimensions)

    print("Array created successfully!")

    while True:
        print("\n1. Add element")
        print("2. Remove element")
        print("3. Get element")
        print("4. Get size")
        print("5. Get index")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            index = input("Enter the index of the element (separated by spaces): ")
            index = list(map(int, index.split()))
            value = input("Enter the value to add: ")
            array.add_element(index, value)
            print("Element added successfully!")
        elif choice == "2":
            index = input("Enter the index of the element to remove (separated by spaces): ")
            index = list(map(int, index.split()))
            array.remove_element(index)
            print("Element removed successfully!")
        elif choice == "3":
            index = input("Enter the indexd of the element to get (separated by spaces): ")
            index = list(map(int, index.split()))
            element = array.get_element(index)
            print("Element:", element)
        elif choice == "4":
            size = array.get_size()
            print("Size of the array:", size)
        elif choice == "5":
            value = input("Enter the value to get the index of: ")
            index = array.get_index(value)
            print("Index:", index)
        elif choice =="6":
            break
        else:
            print("Invalid choice. Please try again.")
    
        
