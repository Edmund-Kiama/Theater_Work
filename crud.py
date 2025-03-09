from models import session, Audition, Role

# CREATE
role1= Role(
    id= 1,
    character_name = "Eren Yeager"
)

audition1 = Audition(
    id = 1,
    actor = "Scott",
    location = "Nairobi",
    phone = 25472210,
    hired = False,
    role_id = 1
)

audition2 = Audition(
    id = 2,
    actor = "Mary",
    location = "Rongai",
    phone = 2548149,
    hired = False,
    role_id = 1
)

session.add_all([role1, audition1, audition2])
session.commit

# READ
actress = select(Audition).where(Audition.actor == "Mary")
print(actress)

audition1.call_back()
lead = select(Audition).where(Audition.hired == True)
print(lead)
print(role1.lead())

# UPDATE
stmt = select(Role).where(Role.character_name == "Eren Yeager")
main_character = session.scalars(stmt)
main_character.character_name = "Monkey D Luffy"
session.commit()
print(role1.character_name)

# DELETE
session.delete(role1)
session.delete(audition1)
session.delete(audition2)
session.commit()