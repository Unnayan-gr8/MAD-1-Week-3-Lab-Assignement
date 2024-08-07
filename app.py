import sys
import pyhtml as h
import matplotlib.pyplot as plt

def tablehtml(data):
  return (h.tr(h.td(cell) for cell in row)for row in data)

def studentid(a,A,B,C):
  l = len(A)
  data = []
  total = 0
  for i in range(l):
    if(A[i] == a):
      data.append([a,B[i],C[i]])
      total += C[i]
  t1 = tablehtml(data)
  t = h.html(h.body(h.h1("Student Details"),h.table(h.tr(h.th('Student id'),h.th('Course id'),h.th('Marks')),t1,h.tr(h.td('Total Marks'),h.td(total)))))
  return t

def display_histogram(numbers):
  plt.hist(numbers)
  plt.xlabel("Marks")
  plt.ylabel("Frequency")
  plt.savefig('histogram.png')
  I = h.img(src='histogram.png')
  return I

def courseid(a,A,B):
  avg = 0
  high = 0
  c = 0
  Marks = []
  for i in range(len(A)):
    if(a == A[i]):
      avg += B[i]
      c += 1
      Marks.append(B[i])
      if(B[i] > high):
        high = B[i]
  avg = avg / c
  H = display_histogram(Marks)
  table = h.table(h.tr(h.th("Average Marks"), h.th("Highest Marks")),h.tr(h.td(avg),h.td(high)))
  t = h.html(h.body(h.div(h.h1("Course Details")),h.div(table),h.div(H)))
  return t

def wronginput():
  t = h.html(h.body(h.div(h.h1('Wrong Inputs')),h.div(h.p("Something went wrong"))))
  return t
  

a = sys.argv[1]
b = int(sys.argv[2])
print("h")
student_ids = []
course_ids = []
marks = []
with open("data.csv", "r") as file:
    next(file)
    for line in file:
        student_id, course_id, mark = line.strip().split(",")
        student_ids.append(int(student_id))
        course_ids.append(int(course_id))
        marks.append(int(mark))
print (type(b))
if(a == "-s" and b in student_ids):
  HTMLDOC = studentid(b,student_ids,course_ids,marks)
elif(a == "-c" and b in course_ids):
  HTMLDOC = courseid(b,course_ids,marks)
else:
  HTMLDOC = wronginput()
f = open("output.html","w")
f.write(str(HTMLDOC))

