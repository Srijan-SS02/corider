db = db.getSiblingDB("user");
db.user.drop()

db.user.insertOne(
    {
        name: "Kanishk",
        email: "itsKanishkp.py@gmail.com",
        password: "Kanishk123@",
    }
)