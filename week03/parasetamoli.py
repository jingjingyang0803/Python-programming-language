"""
COMP.CS.100 Programming 1.
Jingjing Yang, jingjing.yang@tuni.fi, student id 154016843.
Solution of task 3.8.3 - Paracetamol Dosage:
 Parasetamol (also known as Panadol® or Tylenol®), a drug for pain and
  fever, can be administered to an adult patient in doses of 15 mg per
  kilogram of weight, once every six hours. The daily dose cannot be over
  4000 mg.
 Implement a function calculate_dose, which calculates and returns a
  correct dose when the following initial values are given as parameters
  in the following order: patient's weight, the time from receiving the
  previous dose, the previous daily ratio. The function processes all
  information (including the weight) as integers.

Example output:
    Patient's weight (kg): 50
    How much time has passed from the previous dose (full hours): 6
    The total dose for the last 24 hours (mg): 750
    The amount of Parasetamol to give to the patient: 750

Learning Goals:
 Practising implementing functions in further detail.
"""

def calculate_dose(patient_weight, time_from_receiving_dose,
                    dose_in_last_24_hours):
    """
    Calculates the correct dose of Parasetamol to give to the patient
    based on the patient's weight, the time from receiving the previous
    dose, and the previous daily ratio.
    Parameters:
        patient_weight (int): The weight of the patient in kilograms.
        time_from_receiving_dose (int): The time in hours since the patient
         received the previous dose.
        dose_in_last_24_hours (int): The total dose of Parasetamol the patient
         has received in the last 24 hours in milligrams.
    Returns:
        int: The correct dose of Parasetamol to give to the patient in
         milligrams.
    """
    # calculate the dose based on the patient's weight(kg)
    dose = patient_weight * 15

    # check if the time from receiving the previous dose is less than 6
    # hours, if so, return 0
    if time_from_receiving_dose < 6:
        return 0

    # return the correct dose to give to ensure the total dose for the last
    # 24 hours is not over 4000 mg
    if 4000 - dose_in_last_24_hours > dose:
        return dose
    elif 4000 - dose_in_last_24_hours > 0:
        return 4000 - dose_in_last_24_hours
    else:
        return 0

def main():
    weight = int(input("Patient's weight (kg): "))
    time_from_receiving_dose = int(input("How much time has passed from the "
                                         "previous dose (full hours): "))
    dose_in_last_24_hours = int(input("The total dose for the last 24 hours "
                                      "(mg): "))

    dose_to_give = calculate_dose(weight, time_from_receiving_dose,
                                 dose_in_last_24_hours)
    print(f"The amount of Parasetamol to give to the patient: {dose_to_give}")


if __name__ == "__main__":
  main()
