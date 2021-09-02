# Networking - Computer Networking Assignment 1
CS-GY6843 - Fall 2021 NYU

The goal of this assignment is to bring you up to speed with basic programming skills and tools that you will be using throughout the semester to complete course assignments. At the end of this assignment, you should be able to write conditional statements in Python and be familiar with tools like GitHub, GradeScope, and PyCharm. 

GitHub
GitHub provides hosting for software development and version control using Git. It offers the distributed version control and source code management (SCM) functionality of Git, plus its own features. It provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.

Please use your NYU account to open a new GitHub account (it is not necessary to open a new account if you already have one). Assignments will be submitted to GradeScope using GitHub. Please follow the quickstart guide to set up a new repository. Please also create and attach the SSH key to your GitHub account using the following guide (make sure to select the right operating system in the guide).

GradeScope
GradeScope automatically grades the course assignments. Most of the assignments will be sent to GradeScope for grading. 

PyCharm
PyCharm is a recommended Python IDE. JetBrains offers a free professional license for students. https://www.jetbrains.com/community/education/#students

Please note: Course instructors may ask to review students’ GitHub repositories and use the repositories for grading for all assignments. 






Welcome Assignment
Steps required in order to complete the assignment:
Create a GitHub account and follow the instructions to attach a SSH key to your account.
Create a GradeScope account.
Download and install PyCharm (recommended, not required).
Import the Python skeleton code to your Python environment.
Complete the skeleton code.
Push the code to GitHub.
Name the solution file “solution.py” and use GitHub to upload the code to GradeScope.

Skeleton Code - https://drive.google.com/file/d/1qh763hUUn3kEdJZfT2AYlVaQMUFeQgwh/view?usp=sharing

```
### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
   # The student doesn't have to follow the skeleton for this assignment.
   # Another way to implement it is using "case" statements similar to C.
   if question == "Are encoding and encryption the same? - Yes/No":
       answer = "The student should type the answer here"
   elif question == "Is it possible to decrypt a message without a key? - Yes/No":
       answer = "The student should type the answer here"
   return (answer)


# Complete all the questions.


if __name__ == "__main__":
   # use this space to debug and verify that the program works
   debug_question = "Are encoding and encryption the same? - Yes/No"
   print(welcome_assignment_answers(debug_question))

```

As you can see, the first two questions are already in the skeleton code. Please follow the first two questions and add the rest of the questions to the code. Questions should be copied exactly the same as shown below. 

Students should write the right answer in the source code/script. For example, the answer for "Are encoding and encryption the same? - Yes/No" is “No”. Therefore, the code should be:
   if question == "Are encoding and encryption the same? - Yes/No":
       answer = "No"
   elif question....

Returning variable:
“Yes”, “no”, and MD5 hash should be string type.
Numbers should be int type.

Students may submit the assignment to GradeScope unlimited times until they receive full credit.

Questions:
 • "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?", "you have to hunt for this one in slack"
 
 • "Are encoding and encryption the same? - Yes/No"
 
 • "Is it possible to decrypt a message without a key? - Yes/No"
 
 • "Is it possible to decode a message without a key? - Yes/No"
 
 • "Is a hashed message supposed to be un-hashed? - Yes/No"
 
 • "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code"
 
 • "Is MD5 a secured hashing algorithm? - Yes/No"
 
 • "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number"
 
 • "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"




FAQ
Q: Why is the autograder saying I have questions wrong?
A: The autograder randomly selects a question to validate the answer. So the sequence which a question is regarded as wrong, may not directly align with how your function sequenced questions. (i.e. question 1 on your first submission, may be question 5 on your subsequent submission)

Q: I am getting the following error in gradescope: 
“cp: cannot stat '/autograder/submission/solution.py': No such file or directory”
A: If you are submitting a python solution, all python submissions must have the filename titled “solution.py” (minus the quotation marks). Make sure your file meets this naming requirement.

Q: I am getting a different error than above in gradescope.
A: Follow these steps. 
Confirm your code is working locally
Working locally DOES NOT just mean that your application runs with no errors.
Working locally is defined as the program runs and produces the expected output set forth by the assignment. Output expectations may require you to design test cases to validate your code operates as expected.
If your application is producing an error, google what the error means and attempt to debug your code. (If you do not understand what your code is doing, it is unlikely that others will understand)
Search through the respective assignment Slack channel to see if anyone else has shared a question on the same problem. If the question does not exist, share the question in the assignment Slack channel so students and TAs may help where available. Collaboration is encouraged through Slack. This DOES NOT mean sharing or copying assignment submissions and code. 

