from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    user_favorite = db.relationship("Favorite_People", backref="user")

    # de manera automática, el nombre de la tabla es el nombre de la clase en minúscula
    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "descripcion": self.description
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mass = db.Column(db.Float)
    people_favorite = db.relationship("Favorite_People", backref="people")
    heigth = db.Column(db.Float)
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.Date)
    gender = db.Column(db.String(50))
    created = db.Column(db.Date)
    edited = db.Column(db.Date)
    homeworld = db.Column(db.String(250))
    url = db.Column(db.String(250))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "mass": self.mass,
            "heigth": self.heigth,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "created": self.created,
            "edited": self.edited,
            "homeworld": self.homeworld,
            "url": self.url
        }


class Favorite_People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # con el nombre de la tabla user y atributo id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    starShip_id = db.Column(db.Integer, db.ForeignKey('starShip.id'))
    # Esta es una tabla pivote para relacionar User y People, relación muchos a muchos

    def serialize(self):
        return {
            "id": self.id,
            "user_email": User.query.get(self.user_id).serialize()['email'],
            "character_name": People.query.get(self.people_id).serialize()['name']
            
        }


class Planet(db.Base):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    diameter = db.Column(db.Float)
    rotation_period = db.Column(db.Float)
    rotation_period = db.Column(db.Float)
    gravity = db.Column(db.String(50))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.Integer)
    created = db.Column(db.Date)
    edited = db.Column(db.Date)
    url = db.Column(db.String(250))

    def serialize(self):
        return {

            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited,
            "url": self.url
        }


class Starship(db.Base):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250))
    starship_class = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    hyperdrive_rating = db.Column(db.Float)
    mglt = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(100))
    pilots = db.Column(db.ARRAY(String))
    created = db.Column(db.Date)
    edited = db.Column(db.Date)
    url = db.Column(db.String(250))

    def serialize(self):
        return {
            "id": self.id,
            "model": self.model,
            "starship_class": self.starship_class,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "mglt": self.mglt,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "pilots": self.pilots,
            "created": self.created,
            "edited": self.edited,
            "url": self.url
        }
