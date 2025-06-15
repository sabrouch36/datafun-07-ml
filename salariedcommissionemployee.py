
# salariedcommissionemployee.py
"""SalariedCommissionEmployee class inherits from CommissionEmployee."""

from commissionemployee import CommissionEmployee

class SalariedCommissionEmployee(CommissionEmployee):
    """An employee with a base salary + commission."""

    def __init__(self, first_name, last_name, gross_sales, commission_rate, base_salary):
        """Initialize inherited and new attributes."""
        super().__init__(first_name, last_name, gross_sales, commission_rate)
        self.base_salary = base_salary

    def earnings(self):
        """Calculate total earnings including base salary."""
        return self.base_salary + super().earnings()

    def __repr__(self):
        return (f"Salaried {super().__repr__()}\n"
                f"Base Salary: {self.base_salary:.2f}")


if __name__ == "__main__":
    employee = SalariedCommissionEmployee("Sabri", "Hamdaoui", 10000, 0.06, 500)
    print(employee)
    print(f"Total Earnings: ${employee.earnings():.2f}")

##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
