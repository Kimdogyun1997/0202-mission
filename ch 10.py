# 1 아무 내용이 없는 Thing 클래스를 만들어서 출력한다. 이 클래스의 example 객체를 생성하여 출력한다.
# 이 때 두 출력값은 같은가?

class Thing():
    pass

example = Thing()

print(example)  # <__main__.Thing object at 0x000001FCDC3D7FD0>
print(Thing())  # <__main__.Thing object at 0x000001FCDC3D7F10>

# 다르다.


# 2 Thing2 클래스를 만들고 이 클래스의 letters 속성에 값 'abc'를 할당한 후 letters를 출력해보자.

# class 클래스이름():
#     속성 = 값

class Thing2():
    letters = "abc"

print(Thing2().letters)  # abc


# 3 Thing3 클래스를 만든다. 이번에는 인스턴스의 letters 속성에 값 'xyz'를 할당한 후 'letters'를  출력한다.
# letters를 출력하기 위해 객체를 생성해야 하는가?

class Thing3():
    pass

# Thing3 = Thing3()  # 객체 생성 : 객체이름 = 클래스이름()

Thing3.letters = "xyz"  # 객체의 letters 속성에 값 할당  ->  객체이름.속성이름 = " "
print(Thing3.letters)  # xyz

# 답 : 아니다. 객체 생성 없이도 letters 출력됨.



# 4 name, symbol, number 인스턴스 속성을 가진 Element 클래스를 만들어보자.. 이 클래스에서 'Hydrogen', 'H', 1
#값을 가진 객체를 생성한다.

class Element():
    def __init__(self,name,symbol,number):  # 객체를 생성할 때 속성(attribute)을 할당하기 위해 __init__ 메서드
        self.name = name
        self.symbol = symbol
        self.number = number                  # __init_ 메서드: 객체 초기화 메서드, self는 관례적으로 첫번째에 씀
                                              # self는 개별 객체 자신을 참조
Suso=Element("Hydrogen","H",1)  # Suso라는 객체를 생성하고 파라미터인 name, symbol, number에 각각 값 할당.
print(Suso.name,Suso.symbol,Suso.number)


# 5
# 'name':'Hydrogen', 'symbol':'H', 'number':1과 같이 키와 값으로 이루어진 el_dict 딕셔너리를 만들어보자.
# 그리고 el_dict 딕셔너리로부터 Element 클래스의 hydrogen 객체를 생성한다.

el_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}

class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number

hydrogen = Element(el_dict.get("name"), el_dict.get("symbol"),el_dict.get("number"))
#  딕셔너리.get()을 이용하여 딕셔너리의 각 값을 파라미터로 할당하여 hydrogen 객체  생성

print(hydrogen.name, hydrogen.symbol, hydrogen.number)  # Hydrogen H 1




# 6
# Element 클래스에서 객체의 속성(name, symbol, number) 값을 출력하는 dump() 메서드를 정의한다.
# 이 클래스의 hydrogen 객체를 생성하고, dump() 메서드로 이 속성을 출력한다.

# class Element():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#
#     def dump(self):
#         print(self.name, self.symbol, self.number)
#
# hydrogen = Element("Hydrogen" ,"H", 1)
# hydrogen.dump()  # Hydrogen H 1



# 7
# print(hydrogen)을 호출한다. Element 클래스의 정의에서 dump 메서드를 __str__() 메서드로 바꿔서
# 새로운 hydrogen 객체를 생성한다.
# 그리고 print(hydrogen)을 다시 호출한다.

print(hydrogen)
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):  # __이름__ -> 내장된 특수한 함수와 변수를 나타낸다.
# __str__ 함수 : 어떤 값 또는 객체를 문자열로 변화하는데 사용. print로 출력하는 일반 문자열을 표기하는 방식
        return f"{self.name} {self.symbol} {self.number}"

hydrogen = Element("Hydrogen", "H", 1)
print(hydrogen)  # Hydrogen H 1



# 8
# Element 클래스를 수정해서 name, symbol, number의 속성을 private으로 만든다.
#      각 속성값을 반환하기 위해 getter 프로퍼티를 정의한다.

# 데이터를 읽어주는 메서드를 getter(게터), 데이터를 변경(저장)해주는 메서드를 setter(세터)

# 기존의 getter 메서드 위에 @property 데코레이터를 선언하고, 메서드 이름으로부터 get_을 삭제

# setter 메서드의 경우에는 @<필드명>.setter 데코레이터를 선언하고, 메서드 이름으로부터 set_을 삭제

class Element:
    def __init__(self,name,symbol,number):
        self.hidden_name=name
        self.hidden_symbol = symbol
        self.hidden_number = number

    @property
    def name(self):
        return self.hidden_name

    @property
    def symbol(self):
        return self.hidden_symbol

    @property
    def number(self):
        return self.hidden_number

    def __str__(self):
        return f"{self.get_name} {self.get_symbol} {self.get_number}"

hydrogen = Element("Hydrogen", "H", 1)
print(hydrogen)