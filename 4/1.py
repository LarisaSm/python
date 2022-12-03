from sys import argv

script_name, production_in_hours, rate_per_hour, premium = argv


def employee_payroll_calculation(production_hours, rate_hour, bonus):
    return (production_hours / rate_hour) + bonus


print(
    employee_payroll_calculation(
        int(production_in_hours), int(rate_per_hour), int(premium)
    )
)
