from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'usuario'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    nome_usuario = Column(String(20), unique=True, nullable=False)
    email = Column(String(20), unique=True, nullable=False)
    senha = Column(String(100), nullable=False) 
    data_criacao = Column(DateTime(timezone=True))
    todo_list = relationship('TodoList', backref='usuario', lazy='subquery')

class TodoList(Base):
    __tablename__ = "todo_list"

    todo_list_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("usuario.user_id"), nullable=False)
    titulo = Column(String(50), nullable=False)
    data_criacao = Column(DateTime(timezone=True))
    item = relationship('Item', backref='item', lazy='subquery')
    user_id = Column(Integer, ForeignKey('usuario.user_id'))

class Item(Base):
    __tablename__ = "item"

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    todo_list_id = Column(Integer, ForeignKey("todo_list.todo_list_id"), nullable=False)
    titulo = Column(String(55))
    descricao = Column(String(255))
    concluido = Column(Boolean, default=False)
    todo_list_id = Column(Integer, ForeignKey('todo_list.todo_list_id'))
