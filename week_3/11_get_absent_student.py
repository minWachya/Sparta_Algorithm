all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


# O(N)
# 해시 테이블 사용하면 시간은 줄지만 공간은 늘어나는구나
def get_absent_student(all_array, present_array):
    # 모든 학생 딕셔너리 만들기
    student_dict = {}
    for key in all_array:
        student_dict[key] = True    # 공강 복잡도도 O(N)
    # 출석한 학생 삭제하기
    for key in present_array:
        del student_dict[key]

    # 남은 학생 출력
    for key in student_dict.keys():
        return key


print(get_absent_student(all_students, present_students))