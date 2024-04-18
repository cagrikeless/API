from configs import config


class app_board_users(config.db.Model):
    board_line_id = config.db.Column(config.db.Integer,primary_key=True)
    board_id = config.db.Column(config.db.Integer)
    user_id = config.db.Column(config.db.Integer)

    def __init__(self,board_line_id,board_id,user_id):
        self.board_line_id = board_line_id
        self.board_id = board_id
        self.user_id = user_id


class app_board_users_schema(config.ma.Schema):
    class Meta:
        fields = ('board_line_id','board_id','user_id')


board_users_s = app_board_users_schema()