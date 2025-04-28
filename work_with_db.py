from sqlalchemy import create_engine, Column, Integer, String, insert, select, update, delete
from sqlalchemy.orm import declarative_base, declared_attr, Session

Base = declarative_base()


class PreBase:

    @declared_attr
    def __tablename__(cls):
        # В моделях-наследниках свойство __tablename__ будет создано
        # из имени модели, переведённого в нижний регистр.
        # Возвращаем это значение.
        return cls.__name__.lower()

    # В моделях-наследниках будет создана колонка id типа Integer
    id = Column(Integer, primary_key=True)


# Декларативная база включит в себя атрибуты,
# описанные в классе PreBase.
Base = declarative_base(cls=PreBase)


# Наследники класса Base теперь автоматически получат
# приватный атрибут __tablename__ и атрибут id.

class Pep(Base):
    # __tablename__ = 'pep'  # Задали имя таблицы в БД.

    # Описываем свойства модели/колонки таблицы:
    # id = Column(Integer, primary_key=True)
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    def __repr__(self):
        # При представлении объекта класса Pep
        # будут выводиться значения полей pep_number и name.
        return f'PEP {self.pep_number} {self.name}'


if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db', echo=False)
    # Сессия создаётся на основе движка.
    session = Session(engine)

    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    # pep8 = Pep(
    #     pep_number=8,
    #     name='Style Guide for Python Code',
    #     status='Active'
    # )
    # pep20 = Pep(
    #     pep_number=20,
    #     name='The Zen of Python',
    #     status='Active'
    # )
    # pep216 = Pep(
    #     pep_number=216,
    #     name='Docstring Format',
    #     status='Rejected'
    # )

    # session.add(pep8)
    # session.add(pep20)
    # session.add(pep216)
    # session.commit()
    # Замените код: уберите создание и добавление объектов в сессию
    # и запросите информацию из БД.
    # results = session.query(Pep).filter(Pep.status == 'Active').all()
    # print(results)
    # print(type(results))
    # Получаем объект из базы:
    # pep8 = session.query(Pep).filter(Pep.pep_number == 8).first()
    # # Заменяем свойство объекта:
    # pep8.status = 'Closed'
    # Коммитим:

    # session.query(Pep).update(
    #     {'status': 'Active'}
    # )
    # session.commit()

    # pep8 = session.query(Pep).filter(Pep.pep_number == 8).first()
    # session.delete(pep8)

    # session.query(Pep).filter(Pep.pep_number > 20).delete()

    # session.commit()

    # results = session.query(Pep).first()
    # print(results)

    # results = session.query(Pep).filter(Pep.status == 'Active')
    # # Переменная results хранит объект Query...
    # print(type(results))
    # # ...который содержит только те объекты модели Pep, у которых поле status == 'Active'
    # print(results.all())

    # session.execute(
    #     insert(Pep).values(
    #         pep_number='8',
    #         name='Style Guide for Python Code',
    #         status='Proposal'
    #     )
    # )
    # session.commit()

    # result = session.execute(
    #     select(Pep).where(Pep.status == 'Active')
    # )

    # session.execute(
    #     update(Pep).where(Pep.pep_number == 8).values(status='Active')
    # )
    # session.commit()

    session.execute(
        delete(Pep).where(Pep.status == 'Active')
    )
    session.commit()
