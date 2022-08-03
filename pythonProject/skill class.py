# list = ['abcd', 1921, 2.23, 'kowshik', 99.9]
# print(list)  # print complete list
# print(list[0])  # print 1st element
# print(list[1:3])  # print 2 to 3
# print(list[2:])  # print from 2
# print(list * 2)  # print 2 times
#
# print('tuple starts here')
# tuple = ('abcd', 1921, 2.23, 'kowshik', 99.9)
# print(tuple)  # print complete list
# print(tuple[0])  # print 1st element
# print(tuple[1:3])  # print 2 to 3
# print(tuple[2:])  # print from 2
# print(tuple * 2)  # print 2 times
#
# str = 'pfsd'
# print(len(str))


# code to split and join 2 strings
# s = 'kowshik is cse student'
# # print string after split method
# print(s.split(" "))
# # print the string after join method
# print('-'.join(s.split()))
#
# # max in list
# list1 = [10, 20, 30, 40]
# print('largest element is :', max(list1))

import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output