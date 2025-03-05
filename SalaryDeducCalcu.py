def compute_deductions(salary):
    Calculate_SSS = 1200
    Calculate_Philhealth = (salary * 0.05) / 2
    Calculate_pagibig = 100
    Calculate_tax = 1875 # Assuming fixed value for simplicity
    Computed_Deductions = Calculate_SSS + Calculate_Philhealth + Calculate_pagibig + Calculate_tax
    Net_Salary = salary - Computed_Deductions
    
    print("Gross Salary:", salary)
    print("SSS Deduction:", Calculate_SSS)
    print("PhilHealth Deduction:", Calculate_Philhealth)
    print("Pag-IBIG Deduction:", Calculate_pagibig)
    print("Tax Deduction:", Calculate_tax)
    print("Total Deductions:", Computed_Deductions)
    print("Net Salary:", Net_Salary)

salary = float(input("Enter your monthly salary: "))
compute_deductions(salary)