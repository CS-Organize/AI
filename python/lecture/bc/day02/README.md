# Python string formatting

## Percent Formatting
- C 스타일의 문자열 포매팅을 파이썬에서 사용할 수 있게 합니다. 
- 문자열에 % 연산자를 사용하여 변수를 삽입할 수 있습니다. 
- 이 방식은 파이썬 3에서도 여전히 사용할 수 있지만, 더 현대적인 방식들에 비해 권장되지는 않습니다.
```python
name = 'John'
age = 25
print('My name is %s and I am %d years old' % (name, age))
```

네, 파이썬에서는 f-string과 따옴표 3개 문자열 외에도 여러 가지 다른 문자열 포맷 방식을 제공합니다. 다음은 그 중 일부입니다:

## `str.format()`
- `str.format()` 메소드는 파이썬 2.6 이상에서 사용할 수 있는 문자열 포매팅 방식입니다. 
- 중괄호 `{}`를 사용하여 문자열 내에서 변수의 위치를 지정하고, `format()` 메소드에 전달된 인자를 해당 위치에 삽입합니다.
```python
name = '홍길동'
age = 20
print("제 이름은 {0}이고, 나이는 {1}살입니다.".format(name, age))
```

또는 키워드 인자를 사용할 수도 있습니다:
```python
print("제 이름은 {name}이고, 나이는 {age}살입니다.".format(name='홍길동', age=20))
```

## Template Strings

- `string` 모듈의 `Template` 클래스를 사용하는 방법입니다. 
- 이 방식은 보안이 중요한 애플리케이션에서 사용자 입력을 포함하는 문자열을 처리할 때 유용할 수 있습니다. 
- `$` 기호를 사용하여 변수를 표시합니다.

```python
from string import Template

name = '홍길동'
age = 20
t = Template('제 이름은 $name이고, 나이는 $age살입니다.')
print(t.substitute(name=name, age=age))
```

파이썬에서 문자열을 다루는 방법은 다양하며, 여기서는 f-string과 따옴표 3개를 사용한 문자열에 대해 자세히 설명하겠습니다.

## f-string (Formatted String Literals)

- f-string은 Python 3.6 버전에서 도입된 문자열 포매팅 방법입니다. 
- 문자열 앞에 `f` 혹은 `F`를 붙여 사용하며, 중괄호 `{}` 안에 변수 이름이나 표현식을 직접 삽입하여 사용할 수 있습니다. 
- 이를 통해 코드의 가독성을 높이고, 문자열 내에서 변수의 값을 쉽게 조합하거나 변환할 수 있습니다.
```python
name = '홍길동'
age = 20

# f-string 사용 예제
message = f"제 이름은 {name}이고, 나이는 {age}살입니다."
print(message)
```

## Triple-quoted Strings

- 따옴표 3개(`""" """` 또는 `''' '''`)로 둘러싸인 문자열은 여러 줄에 걸친 문자열을 표현할 때 사용합니다. 
- 이 방식을 사용하면 문자열 내에서 엔터키를 눌러 줄바꿈을 직접 입력할 수 있으며, 문자열 내에 따옴표를 추가로 사용할 때 이스케이프 시퀀스를 사용하지 않아도 됩니다. 
- 이는 코드의 가독성을 높이는 데 유용합니다.

```python
# 따옴표 3개 사용 예제
multi_line_string = """이것은 여러 줄에 걸쳐 있는
문자열입니다.
따옴표(')나 큰따옴표(")를
이스케이프 없이 직접 사용할 수 있습니다."""
print(multi_line_string)
```
