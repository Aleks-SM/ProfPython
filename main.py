from application.salary import calculate_salary
from application.db.models.department import Department



if __name__ == '__main__':
    bd_test = Department

    print(round(calculate_salary(), 2))