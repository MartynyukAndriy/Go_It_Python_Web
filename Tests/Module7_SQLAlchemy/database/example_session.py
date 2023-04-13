# from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
# from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# engine = create_engine("sqlite:///:memory:", echo=True)

# DBSession = sessionmaker(bind=engine)

# Base = declarative_base()


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     fullname = Column(String)


# class Address(Base):
#     __tablename__ = "addresses"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     email = Column(String(150), nullable=False)
#     user = relationship('User')


# Base.metadata.create_all(engine)


# if __name__ == "__main__":
#     session = DBSession()
#     andriy = User(fullname="Andriy")
#     igor = User(fullname="Igor")
#     andriy_address = Address(email="Andriy@gmail.com", user=andriy)
#     igor_address = Address(email="Igor@gmail.com", user=igor)
#     session.add(igor)
#     session.add(andriy)
#     session.add(andriy_address)
#     session.add(igor_address)
#     session.commit()

#     u = session.query(User).all()
#     for us in u:
#         print(us.id, us.fullname)

#     addr = session.query(Address).join(Address.user).all()

#     for ad in addr:
#         print(ad.id, ad.user.fullname, ad.email)

#     session.close()


# from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
# from sqlalchemy.orm import relationship, declarative_base, sessionmaker

# engine = create_engine("sqlite:///:memory:", echo=True)

# DBSession = sessionmaker(bind=engine)

# Base = declarative_base()


# class User(Base):
#     __tablename__ = "users"
#     id = Column("id", Integer, primary_key=True)
#     fullname = Column("fullname", String)


# class Address(Base):
#     __tablename__ = "addresses"
#     id = Column("id", Integer, primary_key=True)
#     user_id = Column("user_id", Integer, ForeignKey("users.id"))
#     email = Column("email", String(150))
#     user = relationship("User")


# Base.metadata.create_all(engine)


# if __name__ == "__main__":
#     session = DBSession()
#     andriy = User(fullname="Andriy")
#     andriy_address = Address(email="Andriy@gmail.com")
#     session.add(andriy)
#     session.add(andriy_address)
#     session.commit()

#     user1 = session.query(Address).first()
#     print(user1.id, user1.email, user1.user_id)

#     user2 = session.query(Address).join(Address.user).all()
#     print(user2)
#     for u in user2:
#         print(u.id, u.user.fullname, u.email)
#     print("Oh")


# from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
# from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# engine = create_engine("sqlite:///:memory:", echo=True)

# DBSession = sessionmaker(bind=engine)

# Base = declarative_base()


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     fullname = Column(String)


# class Address(Base):
#     __tablename__ = "addresses"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     email = Column(String)
#     user = relationship("User")


# Base.metadata.create_all(engine)


# if __name__ == "__main__":
#     session = DBSession()
#     andriy = User(fullname="Andriy")
#     andriy_address = Address(email="Andriy@gmail.com", user=andriy)
#     session.add(andriy)
#     session.add(andriy_address)
#     session.commit()

#     address = session.query(Address).all()
#     for ad in address:
#         print(ad.id, ad.user_id, ad.email)

#     join_ = session.query(Address).join(Address.user).all()
#     for ad in join_:
#         print(ad.id, ad.user.fullname, ad.email)
