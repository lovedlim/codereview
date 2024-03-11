class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter_and_square_numbers_in_range(self, start, end):
        """
        주어진 범위 내의 숫자를 필터링하고 제곱한 값을 반환하는 메서드
        """
        filtered_numbers = [num for num in self.numbers if start <= num <= end]
        squared_numbers = [num ** 2 for num in filtered_numbers]
        return squared_numbers

# 테스트를 위한 입력 리스트
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# NumberProcessor 클래스 인스턴스 생성
processor = NumberProcessor(input_numbers)

# 특정 범위의 숫자 필터링 및 제곱 계산
start_range = 3
end_range = 8
result = processor.filter_and_square_numbers_in_range(start_range, end_range)

# 결과 출력
print(f"{start_range}와 {end_range} 사이의 숫자를 필터링하고 제곱한 결과:", result)
