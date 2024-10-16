from Aplicacion import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __reprt__(self):
        return f"<User: {self.username}>"
    

class Post_Moda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text)
    photo = db.Column(db.String(100))

    def __init__(self, created_by, title,url,desc,photo):
        self.created_by = created_by
        self.title = title
        self.url = url
        self.desc = desc
        self.photo = photo

    def __reprt__(self):
        return f"<Moda: {self.title}>"
    

class Post_Cortes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text)
    photo = db.Column(db.String(100))

    def __init__(self, created_by, title,url,desc,photo):
        self.created_by = created_by
        self.title = title
        self.url = url
        self.desc = desc
        self.photo = photo

    def __reprt__(self):
        return f"<Cortes: {self.title}>"
    

class Post_Temporadas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text)
    photo = db.Column(db.String(100))

    def __init__(self, created_by, title,url,desc,photo):
        self.created_by = created_by
        self.title = title
        self.url = url
        self.desc = desc
        self.photo = photo

    def __reprt__(self):
        return f"<Temporadas: {self.title}>"