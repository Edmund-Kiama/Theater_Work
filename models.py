from sqlalchemy.ext.declarative import declarative_base #type:ignore
from sqlalchemy.orm import relationship, sessionmaker #type:ignore
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, create_engine #type:ignore

Base = declarative_base()

class Role(Base):
    
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False)

    auditions = relationship('Audition', back_populates='role', cascade='all, delete')
    
    def __repr__(self) -> str:
        return f"Role(id={self.id}, character_name={self.character_name})"
    
    def actors(self) -> list:
        return [audition.actor for audition in self.auditions]
    
    def locations(self) -> list:
        return [audition.location for audition in self.auditions]
    
    def lead(self):
        for audition in self.auditions:
            if audition.hired:
                return audition
        return "no actor has been hired for this role"
    
    def understudy(self):
        hired_actors = [audition.actor for audition in self.auditions if audition.hired]
        return hired_actors[1] if len(hired_actors) > 1 else "no actor has been hired for understudy for this role"

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)
    
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    role = relationship('Role', back_populates='auditions')
    
    def __repr__(self) -> str:
        return f"Audition(id={self.id}, actor={self.actor}, location={self.location}, phone={self.phone}, hired={self.hired}, role={self.role})"

    def call_back(self) -> None:
        self.hired = True

engine = create_engine('sqlite:///theater.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()