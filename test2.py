def add_numbers(a, b):
    """
    두 숫자를 더하는 함수
    """
    return a + b

# 사용자로부터 두 숫자를 입력 받음
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 두 숫자를 더하고 결과 출력
result = add_numbers(num1, num2)
print("두 숫자의 합은:", result)
