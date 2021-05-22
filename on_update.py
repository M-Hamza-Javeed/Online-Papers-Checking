import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="",database="papers")
mycursor = mydb.cursor()


print("Run this code after performing migrations")
print("python manage.py makemigrations")
print("python manage.py migrate")
print("Django by default not support CASCADE do we add manually on update and on_delete")





'''//TODO@Kashif'''
query = "ALTER TABLE `exam` DROP FOREIGN KEY `exam_Email_b632a88d_fk_teacher_Email`; ALTER TABLE `exam` ADD CONSTRAINT `exam_Email_b632a88d_fk_teacher_Email` FOREIGN KEY (`Email`) REFERENCES `teacher`(`Email`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)


query = "ALTER TABLE `exam__mcqs_choice` DROP FOREIGN KEY `exam__mcqs_choice_MQuestion_0caf9602_fk_exam_mcqs_MQuestion`; ALTER TABLE `exam__mcqs_choice` ADD CONSTRAINT `exam__mcqs_choice_MQuestion_0caf9602_fk_exam_mcqs_MQuestion` FOREIGN KEY (`MQuestion`) REFERENCES `exam_mcqs`(`MQuestion`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `exam_mcqs` DROP FOREIGN KEY `exam_mcqs_Examid_5b922c02_fk_exam_Examid`; ALTER TABLE `exam_mcqs` ADD CONSTRAINT `exam_mcqs_Examid_5b922c02_fk_exam_Examid` FOREIGN KEY (`Examid`) REFERENCES `exam`(`Examid`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `exam_questions` DROP FOREIGN KEY `exam_questions_Examid_5f835bae_fk_exam_Examid`; ALTER TABLE `exam_questions` ADD CONSTRAINT `exam_questions_Examid_5f835bae_fk_exam_Examid` FOREIGN KEY (`Examid`) REFERENCES `exam`(`Examid`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `exam_scan_paper` DROP FOREIGN KEY `exam_scan_paper_Examid_66228bd7_fk_exam_Examid`; ALTER TABLE `exam_scan_paper` ADD CONSTRAINT `exam_scan_paper_Examid_66228bd7_fk_exam_Examid` FOREIGN KEY (`Examid`) REFERENCES `exam`(`Examid`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `exam_scan_paper` DROP FOREIGN KEY `exam_scan_paper_Question_7fa215a5_fk_exam_questions_Question`; ALTER TABLE `exam_scan_paper` ADD CONSTRAINT `exam_scan_paper_Question_7fa215a5_fk_exam_questions_Question` FOREIGN KEY (`Question`) REFERENCES `exam_questions`(`Question`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `exam_scan_paper` DROP FOREIGN KEY `exam_scan_paper_RegNo_b0dacfe4_fk_student_RegNo`;ALTER TABLE `exam_scan_paper` ADD CONSTRAINT `exam_scan_paper_RegNo_b0dacfe4_fk_student_RegNo` FOREIGN KEY (`RegNo`) REFERENCES `student`(`RegNo`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `exam_student_answer` DROP FOREIGN KEY `exam_student_answer_Examid_704d5db4_fk_exam_Examid`; ALTER TABLE `exam_student_answer` ADD CONSTRAINT `exam_student_answer_Examid_704d5db4_fk_exam_Examid` FOREIGN KEY (`Examid`) REFERENCES `exam`(`Examid`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `exam_student_answer` DROP FOREIGN KEY `exam_student_answer_Question_1eab46af_fk_exam_questions_Question`; ALTER TABLE `exam_student_answer` ADD CONSTRAINT `exam_student_answer_Question_1eab46af_fk_exam_questions_Question` FOREIGN KEY (`Question`) REFERENCES `exam_questions`(`Question`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `exam_student_answer` DROP FOREIGN KEY `exam_student_answer_RegNo_a988ce28_fk_student_RegNo`; ALTER TABLE `exam_student_answer` ADD CONSTRAINT `exam_student_answer_RegNo_a988ce28_fk_student_RegNo` FOREIGN KEY (`RegNo`) REFERENCES `student`(`RegNo`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `exam_student_mcqs` DROP FOREIGN KEY `exam_student_mcqs_Examid_163bc36d_fk_exam_Examid`; ALTER TABLE `exam_student_mcqs` ADD CONSTRAINT `exam_student_mcqs_Examid_163bc36d_fk_exam_Examid` FOREIGN KEY (`Examid`) REFERENCES `exam`(`Examid`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `exam_student_mcqs` DROP FOREIGN KEY `exam_student_mcqs_MQuestion_3ed29753_fk_exam_mcqs_MQuestion`; ALTER TABLE `exam_student_mcqs` ADD CONSTRAINT `exam_student_mcqs_MQuestion_3ed29753_fk_exam_mcqs_MQuestion` FOREIGN KEY (`MQuestion`) REFERENCES `exam_mcqs`(`MQuestion`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `exam_student_mcqs` DROP FOREIGN KEY `exam_student_mcqs_RegNo_41ab464a_fk_student_RegNo`; ALTER TABLE `exam_student_mcqs` ADD CONSTRAINT `exam_student_mcqs_RegNo_41ab464a_fk_student_RegNo` FOREIGN KEY (`RegNo`) REFERENCES `student`(`RegNo`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `mcqs` DROP FOREIGN KEY `mcqs_Uniqueid_8ef510bc_fk_quiz_assignment_id_Uniqueid`; ALTER TABLE `mcqs` ADD CONSTRAINT `mcqs_Uniqueid_8ef510bc_fk_quiz_assignment_id_Uniqueid` FOREIGN KEY (`Uniqueid`) REFERENCES `quiz_assignment_id`(`Uniqueid`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `questions` DROP FOREIGN KEY `questions_Uniqueid_11e5071e_fk_quiz_assignment_id_Uniqueid`; ALTER TABLE `questions` ADD CONSTRAINT `questions_Uniqueid_11e5071e_fk_quiz_assignment_id_Uniqueid` FOREIGN KEY (`Uniqueid`) REFERENCES `quiz_assignment_id`(`Uniqueid`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `quiz_assignment_id` DROP FOREIGN KEY `quiz_assignment_id_Email_c48b5814_fk_teacher_Email`; ALTER TABLE `quiz_assignment_id` ADD CONSTRAINT `quiz_assignment_id_Email_c48b5814_fk_teacher_Email` FOREIGN KEY (`Email`) REFERENCES `teacher`(`Email`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `result_stubject` DROP FOREIGN KEY `result_stubject_Examid_fe363c95_fk_exam_Examid`; ALTER TABLE `result_stubject` ADD CONSTRAINT `result_stubject_Examid_fe363c95_fk_exam_Examid` FOREIGN KEY (`Examid`) REFERENCES `exam`(`Examid`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `result_stubject` DROP FOREIGN KEY `result_stubject_RegNo_805774c3_fk_student_RegNo`; ALTER TABLE `result_stubject` ADD CONSTRAINT `result_stubject_RegNo_805774c3_fk_student_RegNo` FOREIGN KEY (`RegNo`) REFERENCES `student`(`RegNo`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `result_stubject` DROP FOREIGN KEY `result_stubject_Subject_95c8189b_fk_courses_Subject`; ALTER TABLE `result_stubject` ADD CONSTRAINT `result_stubject_Subject_95c8189b_fk_courses_Subject` FOREIGN KEY (`Subject`) REFERENCES `courses`(`Subject`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `result_stubject` DROP FOREIGN KEY `result_stubject_Uniqueid_99b92f12_fk_quiz_assignment_id_Uniqueid`; ALTER TABLE `result_stubject` ADD CONSTRAINT `result_stubject_Uniqueid_99b92f12_fk_quiz_assignment_id_Uniqueid` FOREIGN KEY (`Uniqueid`) REFERENCES `quiz_assignment_id`(`Uniqueid`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `student_answer` DROP FOREIGN KEY `student_answer_Question_1e56e443_fk_questions_Question`; ALTER TABLE `student_answer` ADD CONSTRAINT `student_answer_Question_1e56e443_fk_questions_Question` FOREIGN KEY (`Question`) REFERENCES `questions`(`Question`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `student_answer` DROP FOREIGN KEY `student_answer_RegNo_fb9e5223_fk_student_RegNo`; ALTER TABLE `student_answer` ADD CONSTRAINT `student_answer_RegNo_fb9e5223_fk_student_RegNo` FOREIGN KEY (`RegNo`) REFERENCES `student`(`RegNo`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `student_answer` DROP FOREIGN KEY `student_answer_Uniqueid_1fe85c7e_fk_quiz_assignment_id_Uniqueid`; ALTER TABLE `student_answer` ADD CONSTRAINT `student_answer_Uniqueid_1fe85c7e_fk_quiz_assignment_id_Uniqueid` FOREIGN KEY (`Uniqueid`) REFERENCES `quiz_assignment_id`(`Uniqueid`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `student_mcqs` DROP FOREIGN KEY `student_mcqs_MQuestion_4c936b9a_fk_mcqs_MQuestion`; ALTER TABLE `student_mcqs` ADD CONSTRAINT `student_mcqs_MQuestion_4c936b9a_fk_mcqs_MQuestion` FOREIGN KEY (`MQuestion`) REFERENCES `mcqs`(`MQuestion`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `student_mcqs` DROP FOREIGN KEY `student_mcqs_RegNo_bc06bff4_fk_student_RegNo`; ALTER TABLE `student_mcqs` ADD CONSTRAINT `student_mcqs_RegNo_bc06bff4_fk_student_RegNo` FOREIGN KEY (`RegNo`) REFERENCES `student`(`RegNo`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `student_mcqs` DROP FOREIGN KEY `student_mcqs_Uniqueid_9ed491a5_fk_quiz_assignment_id_Uniqueid`; ALTER TABLE `student_mcqs` ADD CONSTRAINT `student_mcqs_Uniqueid_9ed491a5_fk_quiz_assignment_id_Uniqueid` FOREIGN KEY (`Uniqueid`) REFERENCES `quiz_assignment_id`(`Uniqueid`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `student_subject` DROP FOREIGN KEY `student_subject_RegNo_71d5df2a_fk_student_RegNo`; ALTER TABLE `student_subject` ADD CONSTRAINT `student_subject_RegNo_71d5df2a_fk_student_RegNo` FOREIGN KEY (`RegNo`) REFERENCES `student`(`RegNo`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `student_subject` DROP FOREIGN KEY `student_subject_Subject_f0411093_fk_courses_Subject`; ALTER TABLE `student_subject` ADD CONSTRAINT `student_subject_Subject_f0411093_fk_courses_Subject` FOREIGN KEY (`Subject`) REFERENCES `courses`(`Subject`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `teacher_subject` DROP FOREIGN KEY `teacher_subject_Email_7fa577a9_fk_teacher_Email`; ALTER TABLE `teacher_subject` ADD CONSTRAINT `teacher_subject_Email_7fa577a9_fk_teacher_Email` FOREIGN KEY (`Email`) REFERENCES `teacher`(`Email`) ON DELETE CASCADE ON UPDATE CASCADE; ALTER TABLE `teacher_subject` DROP FOREIGN KEY `teacher_subject_Subject_f8e1bbe1_fk_courses_Subject`; ALTER TABLE `teacher_subject` ADD CONSTRAINT `teacher_subject_Subject_f8e1bbe1_fk_courses_Subject` FOREIGN KEY (`Subject`) REFERENCES `courses`(`Subject`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

query = "ALTER TABLE `mcqs_choice` DROP FOREIGN KEY `mcqs_choice_MQuestion_4c2cba94_fk_mcqs_MQuestion`; ALTER TABLE `mcqs_choice` ADD CONSTRAINT `mcqs_choice_MQuestion_4c2cba94_fk_mcqs_MQuestion` FOREIGN KEY (`MQuestion`) REFERENCES `mcqs`(`MQuestion`) ON DELETE CASCADE ON UPDATE CASCADE;"
for i in query.split(';'):
    mycursor.execute(i)

