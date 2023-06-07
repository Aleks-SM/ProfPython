
def read_json(file_name, engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for record in data:
            model = {
                'publisher': Publisher,
                'shop': Shop,
                'book': Book,
                'stock': Stock,
                'sale': Sale,
            }[record.get('model')]
            session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()
    session.close()
