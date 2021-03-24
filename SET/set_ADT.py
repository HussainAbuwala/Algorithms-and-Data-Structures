class Set:
    def __init__(self,size):
        assert size > 0, "Size should be positive"
        self.array = size * [None]
        self.count = 0

    def length(self):
        return self.count

    def is_empty(self):
        if self.count == 0:
            return True
        else:
            return False

    def is_full(self):

        if self.count >= len(self.array):
            return True
        else:
            return False

    def add(self, item):
        has_space_left = self.is_full()
        check = self.check_duplicate(item)
        if has_space_left == False and check ==True:
            self.array[self.count] = item
            self.count += 1

        return has_space_left

    def check_duplicate(self,item):
        for i in range(self.count):
            if self.array[i] == item:
                return False
        return True

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

    def set_intersection(self,the_list):
        common = []
        for i in range (len(self.array)):
            for j in range(len(the_list)):
                if self.array[i] == the_list[j]:
                    common.append(the_list[j])

        return common

if __name__ == "__main__":
    set = Set(5)

    set.add(1)
    set.add(2)
    set.add(3)
    set.add(1)
    set.add(2)

    set.pretty_print()




