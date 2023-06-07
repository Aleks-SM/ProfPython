
def read_json(file_name, engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for record in data:
            model = {
                'empoyees': Empoyees,
                'departments': Departments,
                'empoyee_departments': Empoyee_Departments
            }[record.get('model')]
            session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()
    session.close()
