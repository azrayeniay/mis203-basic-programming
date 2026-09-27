total_score = 0
student_count = 0

while True:
    name = input("Enter student name (or q to quit): ")

    # Kullanıcı 'q' girerse döngüden çık
    if name == "q":
        break

    score = float(input("Enter score: "))

    # Geçersiz notta döngünün başına dön
    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    # Harf notunu belirle
    if score >= 90:
        letter_grade = "A"
    elif score >= 80:
        letter_grade = "B"
    elif score >= 70:
        letter_grade = "C"
    elif score >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    formatted_score = int(score) if score.is_integer() else score
    print(f"{name}: {formatted_score} -> {letter_grade}")

    total_score += score
    student_count += 1

# Döngü bittikten sonra sonuçları yazdır
if student_count == 0:
    print("No students entered.")
else:
    average_score = total_score / student_count
    print(f"Total students: {student_count}")
    print(f"Average score: {average_score:.2f}")
