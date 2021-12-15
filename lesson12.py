from tack1 import Student, Teacher
from tack2 import Mathematician
from tack3 import Product, ProductStore
from tack4 import CustomException

if __name__ == '__main__':
    print('tack1:')
    teacher = Teacher('Mari', 'Ivanna', 55)
    teacher.hello()
    teacher.home_works()
    student = Student('Piotr', 'Petrov', 12)
    student.hello()
    student.home_works()

    print('tack2:')
    m = Mathematician()
    print(m.square_nums([7, 11, 5, 4]))
    print(m.remove_positives([26, -11, -8, 13, -90]))
    print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))
    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

    print('tack3:')
    p = Product('Sport', 'Football T-Shirt', 100)
    p2 = Product('Food', 'Ramen', 1.5)
    s = ProductStore()
    s.add(p, 10)
    s.add(p2, 300)
    s.sell_product('Ramen', 10)
    assert s.get_product_info('Ramen') == ('Ramen', 290)

    print('tack4:')
    try:
        a = -1
        if a < 0:
            raise CustomException("You give negative!")
    except CustomException as ms:
        print(ms)
