create a login and A PLAIN DASHBOARD usign email and password , already created migratiions and tables

create 2 tables syllabuses - name created at and updatd at, standards - name,syllabus_id pls cont do over testing
i want user_profiles table - id, user_id, name,address,mobile,remark,type default-1,school,designation
i want teacher_standards table - user_id,standard_id
add an admin user in users and user_profiles table wiht type=2

for admin user that is type=2 dashboard only there should be provision to add users wiht form with all the possible
fields in users and user_profiles table wiht name ,adress , mobile ,email mandatory and vildation for them also to avoid
bad insertion type not needed it will inserted as default 1 dont do ever testing and unit testing and listing with
mainimal fields and edit

the validation error should come in form modal itseft

while add teacher and edit teacher there should be a provision to add multiple standards to thenm and the entries should
go to teacher_standards
in listing type 1 = teacher, type2 =Administrator
add status to users table default active =1

create a table questions - name,description,standard_id,type (1-single option,2-multiple option,3 Text Entry),
created_by- user_id of logged user,marks
add a status to questions table 1 -active ,2 inactive
create table answers -name,question_id,is_correct - correct 1 or not correct 0,
status 1 -active ,2 inactive defualt active,

teacher and admin can be able to add questions with anwers
question name reguiered , type single select box (1-single option,2-multiple option,3 Text Entry),
if type is single option or multiple then user can enter 4 answers max
descrition optional, standard single select box wiht all standards , created will automaticall save id of logged user ,
then marks fields wiht mandatory and no char
status automatically goto active no need to enter
for answers name required , is_correct 1 for yes and 0 for no, stauts no need to enter
i want an option for editing questions also

can u add 15 single options question

in question add and edit there should be validation for single option and multiple option to enter atleast 2 answers and
single option
there sohuld be only one is correct and for multiple option there should be alleast one is correct

while editing single , multiple option if if uncheck all is correct and click on update then validation comes
like Single Option questions must have exactly ONE correct answer selected. but the thing is the options text box
becomes blank
-not showing entered options it should come there with validation errors

I want back button from question bank to dashboard
i want pagination for question listing

create table exams - name,created_by - logged in user id , type - (1 - timed 2 - non timed),
status (1-active 2 inactive),total_mark

create table exam_questions exam_id,question_id,status{1- active ,2 inactive}

i want teachers to create/edit exams . create or edit exams with name , add questions from question bank
to exams remove questions from exam
the details sohuld be updated in already created Table: exam_questions

In Add Questions from Question Bank the height should be minimal and this should be scrollable downwards
height should be 500px and it should be scrollable downwards

height should be 500px and it should be scrollable downwards i mean the section showing questions with select check box
this section only
In Add Questions from Question Bank i want a search option with searching questions by
created by ,name ,class and question type
same as edit exam i want a view exam also
create a table exam_assign - id -exam_id , standard_id,status-1 for -active, 2 for inactive
create a table students - id , name,standard_id,
i dint see students table in db
in Add New User / Teacher form add a select box -with options Teacher , Student if we select teacher then
table user_profiles type = 1 , and all all existing othwer codes are same
for students dont insert data to teacher_standards i want type =2 in user_profiles
and entries to table
students - id = users table id , name users table name,standard_id measn selected class id,
User Type can t be edited
if a student logins he should see blank dashboard as of now
just add a change password section only to admin
need only teachers to assign exam to standard through table exam_assign
i want assign exam option to teachers
students should see their exams on dashboard i mean exams are
assigned to standards , the students of respective standards should see them
for admin also give full permission to exam management that is admin can assign exam to classes
create a table student_exam_details
fields , id , student_id,exam_id,question_id,student_written_ans_id
students have to write exam like this -
click on start exam
then first question come with answer options and student will be having apportunity to select his
answer option once selected he can click next button and he can see next question with answer options
thre also he can select his answer option ans click on next button and the next question
with answer options will be coming ...like that ...at the last question there will be
a submit buttom named submit exam button when student clicks on it all student exam detials will be stored
on table
table student_exam_details
fields , id , student_id,exam_id,question_id,student_written_ans_id



only on last submit exam button clicked then only saving is done on table student_exam_details
dont save on clicking next ,next button

in view submission can you show question with student submitted answers if the submitter answr is correct
then show tick mark and marks he got ,if the answer is wrong pls show wrong sympol
and no marks
on heading please show like this 30/40 here 30 is the total marks got by student
40 is the total marks for the exam

Questions & Answers Management also full screen




can you make exam management ad all full screen


can you make white baCKGROUD all project means theme white background

in submitted exam performance Submitted Answer: is showing inside text box remove the textbox
change the background to white
in submitted exam performance make all texts to black or in color it fits in white background
in Add Questions from Question Bank i see questions where i can select ie checkbox
i want to view the questions when i click on that like a pop up
go to questions card is not needed in dashboard
in Exam Overview also i need view questions while i click - like a popup
i want Submitted Exam Performance view a proffessional look
now its look is ok but i am not able see heasder
view submission shoulde be little more small in my screen i am not able to see header and also ✕
Submitted Answer and correct answer color is also not black
make the pop up not full screen little small
make this scrollable
in view submission
now Total Questions,✓
Correct Answer
Wrong Answers
Question Evaluation Details make all this blaick font
can you add 100 questions in db
in manage questions in exam in add questions section can you make a pagination

in My Assigned Exams only exam name should see first on clicking exam name all other things
should see

do same this in Exams Management
can you add 30 student to class 3

user_profiles type=1 for teacher, 2for Student, 3 for administrator ok make changes

you have create 30 students but the entries are there in students table olny i want their entries in users and
user_profiles
table also so that they can login

can you add all this students to class 6
some student is having no classes assigned please assign them to class 5
in admin dashboard there should be pagination in Users Directory
admin should see no of students in dashboard
teacher dashboard should see all the students linked wiht teacher linked classes
Students in My Classes in teacher dashboard can you include search by class and search by name
style is broken can youy make student list width full cscreen
just show the name of student and class on searching then a view button click -
will show all the detials of the students
now i can t see see student list in my computer i can only see in mobile view

in mobile view make it compact and avoid scrol vertical

in student My Assigned Exams with exam name student need to see the teacher name who assigned exam

the assigned teacher should see the no of students who completed each exam and each student
name who completed the exam and each question marks like in students view

in teacher dashboard against each student view question marks not working

can you make limit for students in classes upto 100 that is in a class user can t enter students more than 100 nos dont
unit test

in teacher dashboard initially dont load all the students in Students in My Classes
just make them to search

in teacher dashboard Exam Performance & Submissions Report exams lising one by one -
give a pagination there for 10 nos

in table standards add a column created_by
in manage exams if a student done that exam then dont show option edit ,delete and manage questions
teachers can also create/edit standard with created_by their user id
in admin Users Directory create a search by teacehr,student,admin and word search
admin part add standard is ok but in teacher part when i click add standard the modal
popup not coming

add standard is not opening
teacher should able to see his created and admin created standards only
teacher should be able to edit her/her standdards only not admin standards
Standards / Classes Directory on teacher dashboard should be seen with pagination only by clicking on standards
button for teachers and admin admin can edit all standards
admin cant open standard directory
teacher can assign students mean his standard students to he created standards
assign class is not opening , pls dont do unit testing
teacher can assign students to he created standards only
in teacher dashboard Standards / Classes Directory there is assign students
if i click on assign students a pop up coming and all the studnts list there with checkbox
i want 30 students pagination there
in Standards / Classes Directory botton assign Students in that modal i want pagination for students 50 nos


I have updated the Assign Students popup modal
in the Standards / Classes Directory to use 50 students per page pagination not working
in teacher dashboard student listing remove assign class
can you integrate speech recognition say if a student do an exam
if he says option b then option b is selected

if teachers assigns an exam to Standards / Classes (Table: exam_assign), he can only assign to
standards created by him only
if an exam is timed can you make entry to give time in minutes in create exam and
edit exam
can you integrate timer in student side also show a clock runs in second
and lock the text after duration min completed
and save results to the database
There should be a chat option where teacher can chat to students which will come as notification -
student can also give reply
There should be a chat option where teacher can chat to students which will come as notification -
student can also give reply
create tables for this if you are doing migrations dont remove any of existing datas
teacher side chat message is not ok
Students only see and send his standard got teachers chats only
only show his teacher in chat to students

i want leader board for each exams submitted
Can you create chapter master table named chapters-id,name,subject,syllabus
and subject master tables named subjects id,name,syllabus
and topic master table table name topics - id,name,chapter
and enter some chapters and topics under cbse
pls dont remove my existing data

can you change question table with stadard_id,
subject,chapter, topic and give existing questions all of this
pls dont remove my existing data


can you integrate this in design while creating and editing questions also
in question management search also i need search wiht ,subject,standard,chapter,topic


in adding questions to exam create and edit also i need also i need search with ,
subject,standard,chapter,topic

kkskkskkskks

napmkkkvs








flowboard
is an project mangement software,
it can assign projects to users
it can assign users tasks
flowboard have options to create project story -description about project
flowbard has employee login checkin and checkout facility login time and logout time
we can do meeting details in it
it has worklog and release log
user can create task with time estimation after done user can change status from doing to done