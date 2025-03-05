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

    calculator = SalaryDeductionCalculator(salary)
    results = calculator.compute_deductions() 
    


if __name__ == "__main__":
    main()  
