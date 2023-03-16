from random import randint, uniform


# **Шовкопляс Богдан Вікторович **

# Реалізуйте програму для сортування списку кандидатів на роботу на основі їхньої кваліфікації за допомогою алгоритму швидкого сортування (quick sort). Відсортувати за ідентифікатором рекрутера (за зростанням) та кваліфікацією (від найбільшої до найменшої).
# Приклад рядку (ідентифікатор кандидата,ідентифікатор рекрутера,індекс кваліфікації від 0.1 до 1.0): "10,0.75"
 
def quick_sort(array: list):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = list(filter(lambda x: x < pivot, array))
    center = list(filter(lambda x: x == pivot, array))
    right = list(filter(lambda x: x > pivot, array))

    return quick_sort(left) + center + quick_sort(right)


class Employee:
    def __init__(self, id: int, skill: int(0 | 100)):
        self.id = id
        self.skill = skill/10

    def __gt__(self, other):
        if self.skill > other.skill:
            return True
        elif self.skill == other.skill:
            return self.id > other.id

    def __lt__(self, other):
        if self.skill < other.skill:
            return True
        elif self.skill == other.skill:
            return self.id < other.id

    def __eq__(self, other):
        return self.id == other.id and self.skill == other.skill

    def __repr__(self):
        return f"Employee №{self.id}, skill: {self.skill:.1f}"

    # @staticmethod
    # def sort_stuff(array: list):
    #     pass


if __name__ == '__main__':
    x = int(input("Enter array's length:\n"))
    arr = [Employee(randint(0, x*10), randint(0,100)) for i in range(x)]
    print(*quick_sort(arr), sep="\n")
    print("---" * 20)







    # manual tests
    # #test_1
    # print("test №1")
    # arr  = [Employee(23, 0.5),Employee(2, 0.5),Employee(6, 3.5),Employee(6, 4),Employee(18, 3.5),Employee(21, 3.5)]
    # print(*quick_sort(arr), sep = "\n")
    # print("---"* 20)
    # #test_2
    # print("test №1")
    # arr = [Employee(randint(0,100), randint(0,100)) for i in range(10)]
    # print(*quick_sort(arr), sep="\n")
    # print("---" * 20)
    # # test_3
    # print("test №3")
    # arr = [Employee(randint(0, 1_000), randint(0,100)) for i in range(100)]
    # print(*quick_sort(arr), sep="\n")
    # print("---" * 20)
    # # test_4
    # print("test №4")
    # arr = [Employee(randint(0, 100_000), randint(0,100)) for i in range(10_000)]
    # print(*quick_sort(arr), sep="\n")
    # print("---" * 20)
