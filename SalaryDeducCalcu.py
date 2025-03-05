class SalaryDeductionCalculator:
    def __init__(self, salary):
        self.salary = salary
        self.sss_rate = 0.05  # 5% of salary
        self.philhealth_rate = 0.05  # 5% of salary
        self.pagibig_deduction = 100  # Fixed Pag-IBIG deduction
        self.tax_deduction = 0  # Tax deduction will be calculated dynamically

    def calculate_sss_deduction(self):
        """Calculate the SSS deduction (5% of salary)."""
        return self.salary * self.sss_rate  

    def calculate_philhealth_deduction(self):
        """Calculate the PhilHealth deduction (50% of 5% of salary)."""
        return (self.salary * self.philhealth_rate) / 2  

    def calculate_pagibig_deduction(self):
        """Return the fixed Pag-IBIG deduction (100)."""
        return self.pagibig_deduction 

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

    def compute_deductions(self):
        """Compute all salary deductions and net salary."""
        sss_deduction = self.calculate_sss_deduction()
        philhealth_deduction = self.calculate_philhealth_deduction()
        pagibig_deduction = self.calculate_pagibig_deduction()
        tax_deduction = self.calculate_tax_deduction()

        total_deductions = sss_deduction + philhealth_deduction + pagibig_deduction + tax_deduction
        net_salary = self.salary - total_deductions

        return {
            "gross_salary": self.salary,
            "sss_deduction": sss_deduction,
            "philhealth_deduction": philhealth_deduction,
            "pagibig_deduction": pagibig_deduction,
            "tax_deduction": tax_deduction,
            "total_deductions": total_deductions,
            "net_salary": net_salary
        }

    def display_results(self, results):
        """
        Display the deductions and net salary in a readable format.
        - Assigned to: Refactoring Specialist (Readability Improvement)
        """
        print("\nSalary Breakdown:")
        print(f"Gross Salary: {results['gross_salary']:.2f}")
        print(f"SSS Deduction: {results['sss_deduction']:.2f}")
        print(f"PhilHealth Deduction: {results['philhealth_deduction']:.2f}")
        print(f"Pag-IBIG Deduction: {results['pagibig_deduction']:.2f}")
        print(f"Tax Deduction: {results['tax_deduction']:.2f}")
        print(f"Total Deductions: {results['total_deductions']:.2f}")
        print(f"Net Salary: {results['net_salary']:.2f}")

class InputValidator:
    @staticmethod
    def get_valid_salary_input():
        while True:
            try:
                salary_input = float(input("Enter your monthly salary: "))
                if salary_input <= 0:
                    raise ValueError("Salary must be a positive value greater than zero.")
                return salary_input
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.") 

def main():
    print("Welcome to the Salary Deduction Calculator!") 
    salary = InputValidator.get_valid_salary_input()
    calculator = SalaryDeductionCalculator(salary)
    results = calculator.compute_deductions()
    calculator.display_results(results)

if __name__ == "__main__":
    main()