class SalaryDeductionCalculator:
    def __init__(self, salary):

        self.salary = salary
        self.sss_rate = 0.05  # 5% of salary
        self.philhealth_rate = 0.05  # 5% of salary
        self.pagibig_deduction = 100  # Fixed Pag-IBIG deduction
        self.tax_deduction = 0  # Tax deduction will be calculated dynamically

     def calculate_tax_deduction(self):
        """Calculate the tax deduction based on salary income brackets."""
        salary = self.salary
        if salary <= 250000:
            return 0  # No tax for income <= 250,000
        elif salary <= 400000:
            return (salary - 250000) * 0.20  # 20% for income between 250,001 to 400,000
        elif salary <= 800000:
            return (salary - 400000) * 0.25 + 30000  # 25% for income between 400,001 to 800,000
        else:
            return (salary - 800000) * 0.30 + 125000  # 30% for income above 800,000

    print("Gross Salary:", salary)
    print("SSS Deduction:", Calculate_SSS)
    print("PhilHealth Deduction:", Calculate_Philhealth)
    print("Pag-IBIG Deduction:", Calculate_pagibig)
    print("Tax Deduction:", Calculate_tax)
    print("Total Deductions:", Computed_Deductions)
    print("Net Salary:", Net_Salary)

def main():
   
    print("Welcome to the Salary Deduction Calculator!")

    # Get valid salary input using the InputValidator class
    salary = InputValidator.get_valid_salary_input()  

    # Instantiate the SalaryDeductionCalculator with the user input salary
    calculator = SalaryDeductionCalculator(salary)  

    # Compute deductions and net salary using the calculator
    results = calculator.compute_deductions() 

    # Display the results of the deductions and net salary
    calculator.display_results(results)  


if __name__ == "__main__":
    main()  
