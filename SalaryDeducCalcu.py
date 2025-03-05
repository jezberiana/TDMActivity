def display_results(self, results):
        """
        Display the deductions and net salary in a readable format.
        - Assigned to: Refactoring Specialist (Readability Improvement)
        """
        # Display the result in a clear and readable format
        print("\nSalary Breakdown:")
        print(f"Gross Salary: {results['gross_salary']:.2f}")
        print(f"SSS Deduction: {results['sss_deduction']:.2f}")
        print(f"PhilHealth Deduction: {results['philhealth_deduction']:.2f}")
        print(f"Pag-IBIG Deduction: {results['pagibig_deduction']:.2f}")
        print(f"Tax Deduction: {results['tax_deduction']:.2f}")
        print(f"Total Deductions: {results['total_deductions']:.2f}")
        print(f"Net Salary: {results['net_salary']:.2f}")