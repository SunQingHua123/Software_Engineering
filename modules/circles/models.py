from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from modules.users.models import User

Base = declarative_base()


class Circle(Base):
    __tablename__ = 'circles'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP)
    user_id = Column(Integer, ForeignKey('users.id'))

    creator = relationship("User", back_populates="circles")


class CircleMember(Base):
    __tablename__ = 'circle_members'

    circle_id = Column(Integer, ForeignKey('circles.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    role = Column(String(50), default='member')
    joined_at = Column(TIMESTAMP)

    circle = relationship("Circle", back_populates="members")
    user = relationship("User", back_populates="membership")


class Discussion(Base):
    __tablename__ = 'discussions'

    id = Column(Integer, primary_key=True)
    circle_id = Column(Integer, ForeignKey('circles.id'))
    creator_id = Column(Integer, ForeignKey('users.id'))
    topic = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP)

    circle = relationship("Circle", back_populates="discussions")
    creator = relationship("User", back_populates="discussions")


User.circles = relationship("Circle", back_populates="creator", order_by=Circle.id)
User.discussions = relationship("Discussion", back_populates="creator", order_by=Discussion.id)
User.membership = relationship("CircleMember", back_populates="user", order_by=CircleMember.joined_at)
Circle.members = relationship("CircleMember", back_populates="circle", order_by=CircleMember.user_id)
Circle.discussions = relationship("Discussion", back_populates="circle", order_by=Discussion.created_at)

# 数据库连接和会话创建
engine = create_engine('mysql+pymysql://root:@localhost/moyun?charset=utf8mb4')
Session = sessionmaker(bind=engine)


def create_all_tables():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_all_tables()
