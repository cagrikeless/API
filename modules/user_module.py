from configs import config


class app_users(config.db.Model):
    user_id= config.db.Column(config.db.Integer, primary_key=True)
    email = config.db.Column(config.db.String(100))
    password = config.db.Column(config.db.String(40))
    created_on = config.db.Column(config.db.DateTime())
    last_logged_on = config.db.Column(config.db.DateTime())


    def __init__(self, user_id, email,password,created_on,last_logged_on):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.created_on = created_on
        self.last_logged_on = last_logged_on


class app_users_schema(config.ma.Schema):
    class Meta:
        fields = ('user_id', 'email','password', 'created_on','last_logged_on')


users_s = app_users_schema()