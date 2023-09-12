class MyIterator:
    def __init__(self, value):
        self.value = value
        self.current = 0

    def __str__(self):
        return "My name is Iterator"

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.value:
            self.current += 1
            return self.current
        else:
            raise StopIteration

my_iter = MyIterator(15)
for num in my_iter:
    print(num)



my_list = [1,2,3,4,56]
my_list.append(2)
my_list.remove(5)
my_list.reverse()



my_dict = {"a": 1,"b": 2, "c": 3}
my_dict["d"] = 2
my_dict["b"] = 5
