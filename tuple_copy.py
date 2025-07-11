"""
Делая поверхностную копию кортежа - мы не создаем новый объект в памяти,
а просто создаем ссылку на уже существующий объект.
А делая поверхностную копию списка - мы создаем новый объект в памяти,
даже если элементы списка одинаковы.
"""

tpl = (1, 2, "str")
print(id(tpl))
copy_tpl = tuple(tpl)
print(id(copy_tpl))

lst = [1, 2, "str"]
print(id(lst))
copy_lst = list(lst)
print(id(copy_lst))
