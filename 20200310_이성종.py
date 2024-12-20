import random
import string

# SW알고리즘개발 001분반 이성종

def generate_random_students(num_students=30):  # 랜덤 학생 데이터를 생성하는 함수
    students = []
    for i in range(num_students):
        name = ''.join(random.choices(string.ascii_uppercase, k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    return students


def save_file(students, filename="students.txt"):  # 생성된 학생 정보를 .txt 파일로 저장
    with open(filename, "w", encoding="utf-8") as file:
        file.write("생성된 학생 정보:\n")
        for student_list in students:
            student_line = f"이름: {student_list['이름']}, 나이: {student_list['나이']}, 성적: {student_list['성적']}\n"
            file.write(student_line)


def selection_sort(students, field):  # 선택 정렬
    n = len(students)
    for i in range(0, n - 1, 1):
        least = i
        for j in range(i + 1, n):
            if students[j][field] > students[least][field]:
                least = j
        if i != least:
            students[i], students[least] = students[least], students[i]
        # 단계별 리스트 상태 출력
        print(f"Step {i + 1}: {students}")
    return students


def insertion_sort(students, field):  # 삽입 정렬
    comparison_count = 0
    move_count = 0
    for i in range(1, len(students)):
        key = students[i]
        j = i - 1
        while j >= 0 and students[j][field] < key[field]:
            comparison_count += 1
            students[j + 1] = students[j]
            j -= 1
            move_count += 1
        students[j + 1] = key
        if j >= 0:
            comparison_count += 1
        # 과정 출력
        print(f"Step {i}: {students}, Comparisons: {comparison_count}, Moves: {move_count}")
    return students


def quick_sort(students, field):  # 퀵 정렬
    step = 1  # 단계 추적용 변수

    def partition(array, left, right): # 배열을 피벗 기준으로 분할
        pivot_value = array[right][field]
        store_index = left
        for i in range(left, right):
            if array[i][field] > pivot_value: # 현재 값이 피벗보다 크다면, store_index에 위치시켜야 하므로 두 요소를 교환함
                array[i], array[store_index] = array[store_index], array[i]
                store_index += 1
        array[store_index], array[right] = array[right], array[store_index]
        return store_index # 피벗 값의 최종 위치를 반환함

    def quick_sort_recursive(array, left, right):
        nonlocal step
        if left < right:
            print(f"Step {step}: Sorting range array[{left}:{right + 1}] -> {array[left:right + 1]}")
            step += 1
            new_pivot = partition(array, left, right)
            print(f"Partitioned at index {new_pivot}, pivot placed at array[{new_pivot}] -> {array[new_pivot]}")
            print("현재 리스트:", array)
            print("\n")
            quick_sort_recursive(array, left, new_pivot - 1)
            quick_sort_recursive(array, new_pivot + 1, right)

    quick_sort_recursive(students, 0, len(students) - 1)
    return students

# 기수 정렬 알고리즘과 함께 구현하는 계수 정렬 알고리즘
def counting_sort(arr, exp, field): #계수 정렬
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 빈도 카운트 배열 생성
    for student in arr:
        index = (student[field] // exp) % 10
        count[index] += 1

    # 누적 합 배열 생성
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 출력 배열 생성 (역순으로 처리)
    for student in reversed(arr):
        index = (student[field] // exp) % 10
        output[count[index] - 1] = student
        count[index] -= 1

    # 원래 배열로 복사
    for i in range(n):
        arr[i] = output[i]

    return arr


def radix_sort(students): # 기수 정렬
    max_score = max(student['성적'] for student in students)
    exp = 1
    while max_score // exp > 0:
        print(f"\nSorting by digit at place {exp}:")
        students = counting_sort(students, exp, '성적')
        print(f"After sorting by place {exp}: {students}")
        exp *= 10
    return students


# 선택 정렬, 삽입 정렬, 퀵 정렬은 내림차순으로 정렬
# 기수 정렬(성적 기준으로 정렬)은 오름차순으로 정렬
def main():
    student_records = generate_random_students()
    save_file(student_records)

    print("랜덤 생성된 학생 정보가 .txt 파일로 저장되었습니다.")
    print("랜덤 생성된 학생 데이터 원본:")
    for student in student_records:
        print(student)

    while True:
        print("\n메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")
        choice_1 = input("정렬 기준을 선택하세요 (1, 2, 3, 4) : ")

        if choice_1 == '4':
            print("프로그램을 종료합니다.")
            break

        if choice_1 == '1':
            field = '이름'
        elif choice_1 == '2':
            field = '나이'
        elif choice_1 == '3':
            field = '성적'
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")
            continue

        print("\n1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        print("4. 기수 정렬")
        choice_2 = input("정렬 알고리즘을 선택하세요 (1, 2, 3, 4) : ")

        if choice_2 == '1':
            sorted_students = selection_sort(student_records.copy(), field)
            sort_type = '선택 정렬'
        elif choice_2 == '2':
            sorted_students = insertion_sort(student_records.copy(), field)
            sort_type = '삽입 정렬'
        elif choice_2 == '3':
            sorted_students = quick_sort(student_records.copy(), field)
            sort_type = '퀵 정렬'
        elif choice_2 == '4':
            if field != '성적':
                print("기수 정렬은 성적 기준으로만 가능합니다. 다시 선택하세요.")
                continue
            sorted_students = radix_sort(student_records.copy())
            sort_type = '기수 정렬'
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")
            continue

        print(f"\n'{field}'을 기준으로 '{sort_type}' 수행 결과:")
        for student in sorted_students:
            print(student)


if __name__ == "__main__":
    main()
