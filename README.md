Azra Yeniay
2304109037
Management Information Systems
MIS203 Basic Programming

## Week 01
AI Tool Used: ChatGPT
Prompt Used: Create a simple Python program that asks the user for name, department, age, and career goal, then prints a student profile.
What did i change?: I changed the variable names and improved the questions and profile output messages.

## Week 02
AI Tool Used: ChatGPT
Prompt Used: Check my grade calculator code against the assignment instructions and help me with missing or incorrect parts. It should be a Python program named grade_calculator.py that keeps running with while True, stops with break when entering 'q', validates score between 0-100 with continue, assigns letter grades, and calculates the rounded average.
What did you change? I fixed the indentation so the program runs correctly and edited the lines that ChatGPT suggested me to correct and add.
What does break do in your program? Break stops the loop when the user enters q, allowing the program to proceed to the summary and average calculation section.

## Week 03
AI Tool Used: Codex
Prompt Used: Create a cinema ticket program using input, type conversion, f-strings, loops, and conditions. Apply the discounts, validate inputs, and print a sales summary.
What did you change? I used the provided draft as a starting point, then added the missing parts and adjusted the code to match the assignment requirements.
Tests:
Customer name (or q to quit): azra
Age: 22
Day (weekday/weekend): weekend
Student (yes/no): yes
azra: 175.00 TRY (Student)
Customer name (or q to quit): elif
Age: 10
Day (weekday/weekend): weekday
Student (yes/no): yes
elif: 120.00 TRY (Child)
Customer name (or q to quit): musa
Age: 65
Day (weekday/weekend): weekend
Student (yes/no): no
musa: 125.00 TRY (Senior)
Customer name (or q to quit): q
Tickets sold: 3
Total revenue: 420.00 TRY
Average price: 140.00 TRY
Free tickets: 0

Why does the order of the rules matter? A 10 year old student qualifies for both the Child and Student discounts. Checking the Child rule first ensures the child discount is applied.

## Week 03
This code asks the user five questions about their preferred topic, research method, available time, difficulty level and question type. It randomly selects a research topic from the chosen area and displays it as a question. If an answer is invalid, the program asks that question again. Also it uses the "random" and "time" libraries.
Note: The topic is selected randomly based on the chosen category, not based on the filters such as the time, method and difficulty level.
