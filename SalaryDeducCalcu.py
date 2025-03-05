class SalaryDeductionCalculator:
    def __init__(self, salary):
        
        self.salary = salary
        self.sss_rate = 0.05  # 5% of salary
        self.philhealth_rate = 0.05  # 5% of salary
        self.pagibig_deduction = 100  # Fixed Pag-IBIG deduction
        self.tax_deduction = 1875  # Fixed tax deduction

print("Gross Salary:", salary)
print("SSS Deduction:", sss)
print("PhilHealth Deduction:", philhealth)
print("Pag-IBIG Deduction:", pagibig)
print("Tax Deduction:", tax)
print("Total Deductions:", deductions)
print("Net Salary:", net_salary)

def main():
    
    print("Welcome to the Salary Deduction Calculator!")

    # Get valid salary input using the InputValidator class
    salary = InputValidator.get_valid_salary_input()  # 

    # Instantiate the SalaryDeductionCalculator with the user input salary
    calculator = SalaryDeductionCalculator(salary)  

    # Compute deductions and net salary using the calculator
    results = calculator.compute_deductions()  

    # Display the results of the deductions and net salary
    calculator.display_results(results)  


if __name__ == "__main__":
    main() 