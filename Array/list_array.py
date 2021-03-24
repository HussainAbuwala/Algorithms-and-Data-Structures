
class List:

    def __init__(self, size):
        assert size > 0, "Size should be positive"
        self.array = size * [None]
        self.count = 0

    def length(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count >= len(self.array)

    def add(self, item):
        has_space_left = not self.is_full()
        if has_space_left:
            self.array[self.count] = item
            self.count += 1
        return has_space_left

    def pretty_print(self):
        print("[", end="")
        for i in range(0, self.count):
            print(self.array[i], end=", ")
        print("]")

    def delete(self, index):
        is_valid_index = 0 <= index < self.count
        if is_valid_index:
            for i in range(index, self.count-1):
                self.array[i] = self.array[i+1]
            self.count -=1
        return is_valid_index

    def get_element(self, index):
        assert 0 <= index < self.count, "No valid index"
        return self.array[index]


if __name__ == "__main__":
    a_list = List(5)
    for i in range(10):
        a_list.add(i)
    a_list.pretty_print()
    print(a_list.length())
    a_list.delete(1)
    a_list.pretty_print()
    a_list.add("A string")
    a_list.pretty_print()



