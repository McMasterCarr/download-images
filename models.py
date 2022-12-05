from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alpaca_id = db.Column(db.String(50))
    alpaca_class = db.Column(db.String(50))
    exchange = db.Column(db.String(50))
    symbol = db.Column(db.String(10))
    name = db.Column(db.String(150))
    status = db.Column(db.String(20))
    tradable = db.Column(db.Integer)
    marginable = db.Column(db.Integer)
    maintenance_margin_requirement = db.Column(db.Integer)
    shortable = db.Column(db.Integer)
    easy_to_borrow = db.Column(db.Integer)
    fractionable = db.Column(db.Integer)
    '''address1 = 
    address2 = 
    city = 
    state = 
    country = 
    postal_code = 
    icon_url = '''


class Social(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True)

    friend_1 = db.Column(db.Integer)
    friend_2 = db.Column(db.Integer)
    friend_3 = db.Column(db.Integer)
    friend_4 = db.Column(db.Integer)
    friend_5 = db.Column(db.Integer)
    friend_6 = db.Column(db.Integer)
    friend_7 = db.Column(db.Integer)
    friend_8 = db.Column(db.Integer)
    friend_9 = db.Column(db.Integer)
    friend_10 = db.Column(db.Integer)
    friend_11 = db.Column(db.Integer)
    friend_12 = db.Column(db.Integer)
    friend_13 = db.Column(db.Integer)
    friend_14 = db.Column(db.Integer)
    friend_15 = db.Column(db.Integer)
    friend_16 = db.Column(db.Integer)
    friend_17 = db.Column(db.Integer)
    friend_18 = db.Column(db.Integer)
    friend_19 = db.Column(db.Integer)
    friend_20 = db.Column(db.Integer)
    
    aboutMe= db.Column(db.String(50))
    biography = db.Column(db.String(150))
    location = db.Column(db.String(50))
    alpaca_id = db.Column(db.String(50))

    group_1 = db.Column(db.Integer)
    group_2 = db.Column(db.Integer)
    group_3 = db.Column(db.Integer)
    group_4 = db.Column(db.Integer)
    group_5 = db.Column(db.Integer)

    number_of_followers = db.Column(db.Integer)
    number_of_following = db.Column(db.Integer)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))

    public_or_private = db.Column(db.Integer)
    is_brokerage_account = db.Column(db.Integer)
    has_brokerage_account_info = db.Column(db.Integer)
    has_identity_info = db.Column(db.Integer)
    has_disclosure_info = db.Column(db.Integer)
    has_agreement_info = db.Column(db.Integer)

    phone_number=db.Column(db.String(150))
    street_address=db.Column(db.String(150))
    city=db.Column(db.String(150))
    state=db.Column(db.String(150))
    postal_code=db.Column(db.String(150))
    country=db.Column(db.String(150))

    given_name=db.Column(db.String(150))
    middle_name=db.Column(db.String(150))
    family_name=db.Column(db.String(150))
    date_of_birth=db.Column(db.String(150))
    tax_id=db.Column(db.String(150))
    tax_id_type=db.Column(db.String(150))
    country_of_citizenship=db.Column(db.String(150))
    country_of_birth=db.Column(db.String(150))
    country_of_tax_residence=db.Column(db.String(150))
    funding_source=db.Column(db.String(150))

    is_control_person=db.Column(db.Integer)
    is_affiliated_exchange=db.Column(db.Integer)
    is_politically_exposed=db.Column(db.Integer)
    immediate_family_exposed=db.Column(db.Integer)

    margin_signed_at=db.Column(db.String(150))
    margin_ip_address=db.Column(db.String(150))

    account_signed_at=db.Column(db.String(150))
    account_ip_address=db.Column(db.String(150))

    customer_signed_at=db.Column(db.String(150))
    customer_ip_address=db.Column(db.String(150))

    crypto_signed_at=db.Column(db.String(150))
    crypto_ip_address=db.Column(db.String(150))

    brokerage_id=db.Column(db.String(150))
    brokerage_account_number=db.Column(db.String(150))
    brokerage_currency=db.Column(db.String(150))
    
    ach_relationship_id=db.Column(db.String(150))
    username=db.Column(db.String(150))
    mini_bio = db.Column(db.String(250))

class user_follower(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    sourceID = db.Column(db.BigInteger)
    targetID = db.Column(db.BigInteger)
    message = db.Column(db.SmallInteger)
    createdAt = db.Column(db.String(150))
    updatedAt = db.Column(db.String(150))
    #createdAt = db.Column(db.DateTime(timezone=True), default=func.now())
    #updatedAt = db.Column(db.DateTime(timezone=True), default=func.now())
    
class user_message(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    sourceID = db.Column(db.BigInteger)
    targetID = db.Column(db.BigInteger)
    message = db.Column(db.String(150))
    createdAt = db.Column(db.String(150))
    updatedAt = db.Column(db.String(150))
    #createdAt = db.Column(db.DateTime(timezone=True), default=func.now())
    #updatedAt = db.Column(db.DateTime(timezone=True), default=func.now())

class user_friend(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    sourceID = db.Column(db.BigInteger)
    targetID = db.Column(db.BigInteger)
    type = db.Column(db.SmallInteger)
    status = db.Column(db.SmallInteger)
    createdAt = db.Column(db.String(150))
    updatedAt = db.Column(db.String(150))
    #createdAt = db.Column(db.DateTime(timezone=True), default=func.now())
    #updatedAt = db.Column(db.DateTime(timezone=True), default=func.now())

class user_post(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    userID = db.Column(db.BigInteger)
    senderID = db.Column(db.BigInteger)
    message = db.Column(db.String(150))
    status = db.Column(db.SmallInteger)
    createdAt = db.Column(db.DateTime(timezone=True), default=func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), default=func.now())

class group(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    createdByID = db.Column(db.BigInteger)
    updatedByID = db.Column(db.BigInteger)
    title = db.Column(db.String(150))
    metaTitle = db.Column(db.String(150))
    slug = db.Column(db.String(150))
    summary = db.Column(db.String(150))
    status = db.Column(db.String(150))
    createdAt = db.Column(db.DateTime(timezone=True), default=func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), default=func.now())
    profile = db.Column(db.String(150))
    content = db.Column(db.String(150))

class group_message(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    groupID = db.Column(db.BigInteger)
    userID = db.Column(db.BigInteger)
    message = db.Column(db.String(150))
    status = db.Column(db.SmallInteger)
    createdAt = db.Column(db.DateTime(timezone=True), default=func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), default=func.now())

class group_member(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    groupID = db.Column(db.BigInteger)
    userID = db.Column(db.BigInteger)
    roleID = db.Column(db.SmallInteger)
    status = db.Column(db.SmallInteger)
    createdAt = db.Column(db.DateTime(timezone=True), default=func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), default=func.now())

class group_post(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    groupID = db.Column(db.BigInteger)
    userID = db.Column(db.BigInteger)
    message = db.Column(db.String(150))
    status = db.Column(db.SmallInteger)
    createdAt = db.Column(db.DateTime(timezone=True), default=func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), default=func.now())

class group_follower(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    groupID = db.Column(db.BigInteger)
    userID = db.Column(db.BigInteger)
    type = db.Column(db.SmallInteger)
    createdAt = db.Column(db.DateTime(timezone=True), default=func.now())
    updatedAt = db.Column(db.DateTime(timezone=True), default=func.now())

class group_meta(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    groupID = db.Column(db.BigInteger)
    key = db.Column(db.String(150))
    content = db.Column(db.String(150))

class stock_data(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    groupID = db.Column(db.BigInteger)
    key = db.Column(db.String(150))
    content = db.Column(db.String(150))