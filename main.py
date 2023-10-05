
class ABACStudent:
    def __init__(self, student_id, student_name, previous_institute):
        self.student_id = student_id
        self.student_name = student_name
        self.previous_institute = previous_institute

    def display_gpa(self):
        return 2.79

    def display_credits_earned(self):
        return 136

class MSMEStudent(ABACStudent):
    def __init__(self, student_id, student_name, previous_institute, major, specialization, certificate):
        super().__init__(student_id, student_name, previous_institute)
        self.major = major
        self.specialization = specialization
        self.certificate = certificate

    def display_major(self):
        return self.major

    def display_certification(self):
        return self.certificate

# Abac Student Info
abac_student = ABACStudent(6118301, "Trevor Chingosho", "WaterShed College")

# MSME student Info
msme_student = MSMEStudent(6118302, "Trae Chingz", "Asia Pacific University", "M.I.S", "Cyber-Security", "None")

print("ABAC Student Information:")
print("Student ID:", abac_student.student_id)
print("Student Name:", abac_student.student_name)
print("Previous Institute:", abac_student.previous_institute)
print("GPA:", abac_student.display_gpa())
print("Credits Earned:", abac_student.display_credits_earned())

print("\nMSME Student Information:")
print("Student ID:", msme_student.student_id)
print("Student Name:", msme_student.student_name)
print("Previous Institute:", msme_student.previous_institute)
print("Major:", msme_student.display_major())
print("Specialization:", msme_student.specialization)
print("Certification:", msme_student.display_certification())