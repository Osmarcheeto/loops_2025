# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    if subject == "history":
        break
    print(subject)
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
list1000 = list(range(1, 1001))
for list1000 in list1000:
    if list1000 > 600:
        break
    print(list1000)
list101 = list(range(1,10000))
for list101 in list101:
    if 300 <= number <= 500:
        continue
    print(list101)
# Given:



# Challenge:
# Use a for loop to add all the numbers and print the total.
applicants_for_credit= ["alice", "Bob", "Charlie", "David", "Eve"]
Credit_scores = [720, 680,520,670,750]
Zipped_data = zip(Credit_scores, applicants_for_credit)
list_of_tuples = list(Zipped_data)
print(list_of_tuples)
for applicant, score in zip(applicants_for_credit, Credit_scores):
    if score < 600:
        continue
    print(applicant + " approved credit score" + str(score))




for index in range(len(class)-1):
    print("subject " + str(index) + ": " + class[index])



numbers = [5, 10, 15, 20]
total = 0
for numbers in numbers:
    total += numbers
    #short hand for total = total + number
print("total" ,total)

new_numbers = list(range(1, 261))
# This creates a list of number from 1 to 20
# Challege: sum up all the numbers from 1 to 260
# and print the total
total = 0
for number in new_numbers:
    total += number
print
