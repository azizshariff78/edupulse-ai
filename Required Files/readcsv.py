#this is the fist module : reads a csv file containing student names , class names and marks 
import csv

student_data=[{"student name":"Bobby Firmino","class name":"Form 1 Alpha","subject":"Math","marks":85}, {"student name":"Mohamed Salah","class name":"Form 1 Alpha","subject":"Math","marks":90}, {"student name":"Sadio Mane","class name":"Form 2 Beta","subject":"Chemistry","marks":80}, {"student name":"Marcus Rashford","class name":"Form 1 Alpha","subject":"Math","marks":80}, {"student name":"Virgil van Dijk","class name":"Form 1 Alpha","subject":"Chemistry","marks":85}, {"student name":"Bruno Fernandes","class name":"Form 2 Beta","subject":"Chemistry","marks":75}]
#writes the student data to a csv file named student_data.csv
with open('student_data.csv', mode='w', newline='') as the_file:
    column_names = student_data[0].keys()
    writer = csv.DictWriter(the_file,fieldnames=column_names)
    writer.writeheader()
    writer.writerows(student_data)

#: reads the csv file created by the first module and prints the student names , class names and marks in a formatted way    
with open('student_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['student name']} scored {row['marks']} marks in {row['class name']}")

#THIS IS THE SECOND MODULE : reads the csv file created by the first module and calculates class averages from the CSV file for two subjects
with open('student_data.csv', mode='r') as file :
     reader = csv.DictReader(file)
     for rows in reader:
        try:
            score = int(row['marks'])
        except ValueError:
            score = 0  # Default to 0 if the data is broken or empty

      #putting the two parameters class and subject into a tupple and cleaning the data by using .strip() to remove any white spaces and .lower() to format into lower case       
     class_subject = (row['class name'].strip().lower(), row['subject'].strip().lower())
     student_count={}
     total_sum={}  
     if class_subject in total_sum: #checks if the class,subject tuple is in the tolal_sum dictionary 
          total_sum[class_subject] += score #updates the marks based on the tupple 
          student_count[class_subject] += 1 
     else:
          total_sum[class_subject] = score #marks and new tuple are created and saved
          student_count[class_subject] = 1

     def cal_avg() :
        for key, value  in student_count.items():
          average = value / student_count[key] #calculates the average by dividing the total marks by the number of students in that class and subject
          return (f"The average marks for {key[0].title()} in {key[1].title()} is {average:.2f}") #formats the output to 2 decimal places and returns the average marks for each class and subject

     print(cal_avg())