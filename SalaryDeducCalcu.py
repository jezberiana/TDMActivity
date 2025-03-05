class SalaryDeductionCalculator:
    def __init__(self, salary):
      
        self.salary = salary
        self.sss_rate = 0.05  # 5% of salary
        self.philhealth_rate = 0.05  # 5% of salary
        self.pagibig_deduction = 100  # Fixed Pag-IBIG deduction
        self.tax_deduction = 1875  # Fixed tax deduction

    def calculate_sss_deduction(self):
        """Calculate the SSS deduction."""
        return self.salary * self.sss_rate  # **Lead Developer (Modular Function)**

    def calculate_philhealth_deduction(self):
        """Calculate the PhilHealth deduction."""
        return (self.salary * self.philhealth_rate) / 2  # **Lead Developer (Modular Function)**

    def calculate_pagibig_deduction(self):
        """Return the fixed Pag-IBIG deduction."""
        return self.pagibig_deduction  # **Lead Developer (Modular Function)**

    def calculate_tax_deduction(self):
        """Return the fixed tax deduction."""
        return self.tax_deduction  # **Lead Developer (Modular Function)**

    def compute_deductions(self):
        # Calls modular functions to calculate deductions
        sss_deduction = self.calculate_sss_deduction()
        philhealth_deduction = self.calculate_philhealth_deduction()
        pagibig_deduction = self.calculate_pagibig_deduction()
        tax_deduction = self.calculate_tax_deduction()

        # Total deductions and net salary calculation
        total_deductions = sss_deduction + philhealth_deduction + pagibig_deduction + tax_deduction
        net_salary = self.salary - total_deductions

        # Return all deductions and net salary
        return {
            "gross_salary": self.salary,
            "sss_deduction": sss_deduction,
            "philhealth_deduction": philhealth_deduction,
            "pagibig_deduction": pagibig_deduction,
            "tax_deduction": tax_deduction,
            "total_deductions": total_deductions,
            "net_salary": net_salary
        }


def main():
    
    print("Welcome to the Salary Deduction Calculator!")

    # Get valid salary input using the InputValidator class
    salary = InputValidator.get_valid_salary_input()  # **Tester & Documenter (Input Validation)**

    # Instantiate the SalaryDeductionCalculator with the user input salary
    calculator = SalaryDeductionCalculator(salary)  # **Lead Developer (OOP)**

    # Compute deductions and net salary using the calculator
    results = calculator.compute_deductions()  # **Lead Developer (OOP, Modular Function)**

    # Display the results of the deductions and net salary
    calculator.display_results(results)  # **Refactoring Specialist (Improved Readability)**


if __name__ == "__main__":
    main()  # **Lead Developer (Program Execution)**