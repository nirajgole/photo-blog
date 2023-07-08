"""created base class for creating sql tables"""
# from typing import Any
# from sqlalchemy.ext.declarative import as_declarative, declared_attr

# @as_declarative()
# class Base:
#     """base class"""
#     id: Any
#     __name__: str

#     @declared_attr
#     def __tablename__(self) -> str:
#         """to generate tablename from classname"""
#         return self.__name__.lower()


from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()