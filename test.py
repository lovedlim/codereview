def select_and_square_even_numbers(numbers):
    """
    주어진 리스트에서 짝수를 선택하여 제곱한 값들을 새로운 리스트에 저장하는 함수
    """
    squared_even_numbers = []  # 짝수를 제곱한 값들을 저장할 리스트

    for num in numbers:
        if num % 2 == 0:  # 짝수인 경우에만 제곱하여 리스트에 추가
            squared_even_numbers.append(num ** 2)

    return squared_even_numbers

# 테스트를 위한 입력 리스트
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 주어진 리스트에서 짝수를 선택하여 제곱한 값들을 가져옴
result = select_and_square_even_numbers(input_numbers)

# 결과 출력
print("주어진 리스트에서 짝수를 선택하여 제곱한 값들:", result)
