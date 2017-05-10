#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Assignment: Hospital
You're going to build a hospital with patients in it! Create a hospital class.

Before looking at the requirements below, think about what you might want each patient and hospital to be able to do.

Patient:
Attributes:

Id: an id number

Name

Allergies

Bed number: should be none by default

Hospital
Attributes:

Patients: an empty array

Name: hospital name

Capacity: an integer indicating the maximum number of patients the hospital can hold.

Methods:

Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the
capacity do not admit the patient. Return a message either confirming that admission is complete or saying the
hospital is full.

Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.

This is a challenging assignment. Ask yourself what input each method requires and what output you will need.
"""

import random
import math


def random_id():
    """
    Generate a new UNIQUE ID for the caller.
    :return:
    """
    return int(math.floor(random.random() * 500001))


class Hospital(object):
    def __init__(self, hospital_name, capacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.counter = 0

    def admit_patient(self, patient):
        if self.counter >= self.capacity:
            print("We are at our limit! Cannot accept more patients.")
            return self
        if isinstance(patient, basestring) or isinstance(patient, int):
            raise("Please only pass me a patient from the Patient class!")
        else:
            self.counter += 1
            patient.bed_number = self.counter
        print("Patient accepted...")
        self.patients.append(patient)
        return self

    def discharge_patient(self):
        if len(self.patients) > 0:
            self.patients[0].bed_number = None
            self.patients.remove(self.patients[0])


class Patient(object):
    def __init__(self, patient_name, allergies, bed_number=None):
        self.unique_id = random_id()
        self.patient_name = patient_name
        self.allergies = allergies
        self.bed_number = bed_number


new_patient = Patient("Turd", "Water")
patient_two = Patient("SecondPatient", "Drugs")
patient_three = Patient("ThirdPatient", "Poop")
patient_four = Patient("FourthPatient", "Paper")
patient_five = Patient("FifthPatient", "Metal")
patient_six = Patient("SixPatient", "Plastic")

best_hospital = Hospital("Best Hospital", 5)
best_hospital.admit_patient(new_patient).admit_patient(patient_two).admit_patient(patient_three).\
    admit_patient(patient_four).admit_patient(patient_five).admit_patient(patient_six)

#print(new_patient.bed_number)
best_hospital.discharge_patient()

#print(new_patient.bed_number)
print("Hello %s world" % 5)