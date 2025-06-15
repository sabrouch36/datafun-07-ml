# commissionemployee.py
"""CommissionEmployee class."""

class CommissionEmployee:
    """An employee who gets paid based on commission."""

    def __init__(self, first_name, last_name, gross_sales, commission_rate):
        """Initialize CommissionEmployee attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate

    def earnings(self):
        """Calculate earnings."""
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        return (f"CommissionEmployee: {self.first_name} {self.last_name}\n"
                f"Gross Sales: {self.gross_sales:.2f}\n"
                f"Commission Rate: {self.commission_rate:.2%}")
if __name__ == "__main__":
    employee = CommissionEmployee("Sabri", "Hamdaoui", 10000, 0.06)
    print(employee)
    print(f"Earnings: ${employee.earnings():.2f}")
