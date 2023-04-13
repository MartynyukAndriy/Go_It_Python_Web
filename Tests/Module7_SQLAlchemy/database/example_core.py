# from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, create_engine
# from sqlalchemy.sql import select


# engine = create_engine("sqlite:///:memory:", echo=True)
# metadata = MetaData()


# users = Table("users", metadata,
#               Column("id", Integer, primary_key=True),
#               Column("fullname", String)
#               )

# addresses = Table("address", metadata,
#                   Column("id", Integer, primary_key=True),
#                   Column("user_id", Integer, ForeignKey("users.id")),
#                   Column("email", String(150), nullable=False)
#                   )


# metadata.create_all(engine)


# if __name__ == "__main__":
#     with engine.connect() as  .values(fullname="Andriy Martynyukprint(user)")
#         res = conn.execute(user)
#         all_users = conn.execute(select(users)).fetchall()
#         print(all_users)

#         address = addresses.insert().values(
#             email="Andriy@gmail.com", user_id=res.lastrowid)
#         res_email = conn.execute(address)
#         all_emails = conn.execute(select(addresses)).fetchall()
#         print(all_emails)

#         r = select(users.c.fullname, addresses.c.email).join(
#             users).group_by(users.c.id)
#         res2 = conn.execute(r).fetchall()
#         print(r)
#         print(res2)


# MYSELF
from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey, create_engine, select


metadata = MetaData()

engine = create_engine("sqlite:///:memory:", echo=True)


users = Table("users", metadata,
              Column("id", Integer, primary_key=True),
              Column("fullname", String)
              )

addresses = Table("addresses", metadata,
                  Column("id", Integer, primary_key=True),
                  Column("user_id", Integer, ForeignKey("users.id")),
                  Column("email", String(150), nullable=False)
                  )


metadata.create_all(engine)


if __name__ == "__main__":
    with engine.connect() as conn:
        user = users.insert().values(fullname="Andriy Martynyuk")
        res = conn.execute(user)
        print(conn.execute(select(users)).fetchall())

        new_address = addresses.insert().values(
            email="Andriy Martynyuk", user_id=res.lastrowid)
        address_res = conn.execute(new_address)
        print(conn.execute(select(addresses)).fetchall())
