import cv2
import numpy as np
import dlib
import time
from datetime import datetime

class ExamEnvironment:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.exam_duration = 0
        self.cheating_detected = False
        self.exam_started = False
        self.exam_ended = False
        self.face_detector = dlib.get_frontal_face_detector()
        self.camera = cv2.VideoCapture(0)

    def start_exam(self):
        self.start_time = time.time()
        self.exam_started = True
        print("Exam Started: ", datetime.now())

    def end_exam(self):
        self.end_time = time.time()
        self.exam_duration = self.end_time - self.start_time
        self.exam_ended = True
        print("Exam Ended: ", datetime.now())

    def check_cheating(self):
        if self.exam_started and self.exam_ended:
            if self.exam_duration < 600:
                print("Suspicious! Exam completed too quickly.")
                self.cheating_detected = True
            else:
                print("Exam duration seems normal.")
        else:
            print("Exam not yet started or ended.")
        return self.cheating_detected

    def detect_face(self):
        ret, frame = self.camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector(gray)

        if len(faces) > 0:
            print("Face Detected!")
            self.cheating_detected = True
        else:
            print("No face detected.")
        return self.cheating_detected

    def release_camera(self):
        self.camera.release()
        cv2.destroyAllWindows()

def main():
    exam = ExamEnvironment()
    exam.start_exam()

    # Simulate some exam activity
    time.sleep(10)  # Simulating 10 seconds of exam activity
    exam.detect_face()

    exam.end_exam()
    if exam.check_cheating():
        print("Cheating Detected!")
    else:
        print("No Cheating Detected.")

if __name__ == "__main__":
    main()
import random

class ExamSubmission:
    def __init__(self):
        self.submissions = []

    def submit_answer(self, answer):
        submission_time = time.time()
        self.submissions.append({"answer": answer, "time": submission_time})
        print(f"Answer submitted at {datetime.now()}.")

    def check_multiple_submissions(self):
        if len(self.submissions) > 1:
            print("Multiple submissions detected!")
            return True
        return False

    def check_answer_variation(self):
        if len(self.submissions) > 1:
            first_answer = self.submissions[0]["answer"]
            for submission in self.submissions[1:]:
                if submission["answer"] != first_answer:
                    print("Answer variation detected!")
                    return True
        return False

class Exam:
    def __init__(self):
        self.exam_started = False
        self.exam_ended = False
        self.exam_duration = 0
        self.submission_checker = ExamSubmission()

    def start_exam(self):
        self.exam_started = True
        print("Exam started.")

    def end_exam(self):
        self.exam_ended = True
        self.exam_duration = random.randint(600, 1800)  # Random duration between 10-30 minutes
        print("Exam ended.")

    def submit_answer(self, answer):
        if self.exam_started and not self.exam_ended:
            self.submission_checker.submit_answer(answer)
        else:
            print("Exam not started or already ended.")

    def check_for_cheating(self):
        if self.submission_checker.check_multiple_submissions():
            print("Cheating detected: Multiple submissions.")
        if self.submission_checker.check_answer_variation():
            print("Cheating detected: Answer variation.")

def main():
    exam = Exam()
    exam.start_exam()

    # Simulating user answer submissions
    exam.submit_answer("A")
    time.sleep(2)  # Simulate delay
    exam.submit_answer("B")
    time.sleep(3)
    exam.submit_answer("A")

    exam.end_exam()
    exam.check_for_cheating()

if __name__ == "__main__":
    main()
class CheatingDetectionSystem:
    def __init__(self):
        self.exam_environment = ExamEnvironment()
        self.exam_submission = ExamSubmission()

    def start_exam(self):
        self.exam_environment.start_exam()

    def end_exam(self):
        self.exam_environment.end_exam()
        self.exam_submission.check_multiple_submissions()
        self.exam_submission.check_answer_variation()

    def submit_answer(self, answer):
        self.exam_submission.submit_answer(answer)

    def check_cheating(self):
        if self.exam_environment.check_cheating():
            print("Cheating Detected in Environment!")
        self.exam_submission.check_for_cheating()

    def run(self):
        self.start_exam()

        # Simulate some exam activity and answer submissions
        time.sleep(5)  # Simulate 5 seconds of exam activity
        self.exam_submission.submit_answer("A")

        # Detect cheating based on answers and environment
        self.exam_environment.detect_face()

        self.submit_answer("B")
        self.submit_answer("A")

        self.end_exam()
        self.check_cheating()

if __name__ == "__main__":
    system = CheatingDetectionSystem()
    system.run()
