# Повышенное задание 2. CRUD через ORM (SQLAlchemy)
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)


engine = create_engine("sqlite:///library.db")
Base.metadata.create_all(engine)

with Session(engine) as session:
    # Create
    session.add(Book(title="Мастер и Маргарита", author="Булгаков"))
    session.add(Book(title="Война и мир", author="Толстой"))
    session.commit()

    # Read
    print("Все книги:")
    for book in session.query(Book).all():
        print(book.id, book.title, book.author)

    # Update
    book = session.query(Book).filter_by(title="Война и мир").first()
    book.title = "Анна Каренина"
    session.commit()
    print("После изменения:", book.title)

    # Delete
    session.delete(book)
    session.commit()
    print("Осталось книг:", session.query(Book).count())
