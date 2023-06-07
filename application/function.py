from application.db.models.employee import Employee
from application.db.models.department import Department
from application.db.models.department import EmployeeDepartments

def read_json(file_name, engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for record in data:
            model = {
                'empoyees': Employee,
                'departments': Department,
                'empoyee_departments': EmployeeDepartments
            }[record.get('model')]
            session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()
    session.close()
