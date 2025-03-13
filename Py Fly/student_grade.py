# organizing student grades
marks = [85, 92, 78, 90, 88]

#adding a new grade
marks.append(95)

# average marks
average_mark = sum(marks)/len(marks)
print(f"Average marks: {average_mark:.2f}")

# Finding highest and lowest marks
highest_mark = max(marks)
lowest_mark = min(marks)

print(f"Highest mark: {highest_mark}")
print(f"Lowest mark: {lowest_mark}")
