**PROJECT OVERVIEW:**


This activity involves a collaborative effort to refactor a Salary Deduction Calculator, focusing on managing technical debt and improving code quality. The members utilized GitHub for version control and teamwork. Further, the goal is to simulate a real-world software development scenario and provide hands-on experience in refactoring and collaboration.


**ORIGINAL CODE UNDER REVIEW**



The team began with the following code:



def compute_deductions(salary):
    sss = 1200
    philhealth = (salary * 0.05) / 2
    pagibig = 100
    tax = 1875  # Assuming fixed value for simplicity

    deductions = sss + philhealth + pagibig + tax
    net_salary = salary - deductions

    print("Gross Salary:", salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", deductions)
    print("Net Salary:", net_salary)

salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)




**REFACTORED CODE:**


The team refactored the code into the following structure:

class SalaryDeductionCalculator:
    # ... (class definition)

class InputValidator:
    # ... (class definition)

def main():
    # ... (main function)

if __name__ == "__main__":
    main()




**ROLES PER MEMBER**

- Project Manager: Jezrelle Cris Beriana
- Lead Developer 1: Shan Chai Manlunas
- Lead Developer 2: Casey Jan Saguing
- Tester: Jayza Joy Castillo
- Refactoring Specialist: Emmanuel Sonquipal
- Documentor: Zynnah Marie Ortiz



**ROLE ASSIGNMENTS**

Specific tasks were assigned as follows:

- Project Manager: Oversees progress and ensures timely completion of the activity.
- Lead Developer (OOP Implementation): Initialized the SalaryDeductionCalculator class with salary and default deduction rates.
- Lead Developer (Modular Function): Implemented modular functions to calculate each deduction (SSS, PhilHealth, Pag-IBIG, Tax).
- Lead Developer (OOP, Modular Function): Implemented the compute_deductions method, calling modular functions and calculating total deductions and net salary.
- Lead Developer (OOP): Instantiated the SalaryDeductionCalculator with user input salary.
- Lead Developer (Program Execution): Implemented the main function to drive the salary deduction process.
- Refactoring Specialist (Readability Improvement): Implemented the display_results method to present deductions and net salary in a readable format.
- Tester (Input Validation & Error Handling): Implemented the InputValidator class to get and validate user salary input and added error handling for invalid input in the InputValidator class.
- Documenter: Writes and updates the project documentation.







