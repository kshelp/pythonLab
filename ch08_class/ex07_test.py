# @staticmethod, @classmethod 차이
class foo(object):
    name = 'foo'

    @staticmethod
    def get_name_static():
        print(foo.name)

    @classmethod
    def get_name_class(cls):
        print(cls.name)

foo.get_name_static()  # foo
foo.get_name_class()   # foo


# 상속인 경우
class bar(foo):
    name = 'bar'

bar.get_name_static()  # foo
bar.get_name_class()   # bar

