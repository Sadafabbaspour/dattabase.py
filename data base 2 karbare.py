
from  sqlalchemy import Column, create_engine , column ,Integer , String
from sqlalchemy .ext . declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker
from sqlalchemy .orm import declarative_base
Base=declarative_base()



class USER(Base):



    __tablename__="user"
    id = Column(Integer, primary_key=True)

    name=Column(String)
    user=relationship("USER",backref)





class POST(Base):
    __tablename__="Post"


    text=Column(String)
    id_user=Column(Integer)
    post=relationship("USER",backref="POST")


engine=create_engine("sqlite link database")
Base.metadata.create_all(engine)


ses=sessionmaker(bind=engine)
ses=ses()
ses.add(USER)

post1=POST(text="its a new post",user=USER)
post2=POST(text="its a secend post",user=USER)
ses.add(post1)
ses.add(post2)
ses.commit()