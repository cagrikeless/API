from configs import config

class app_boards(config.db.Model):
    board_id = config.db.Column(config.db.Integer, primary_key=True)
    board_name = config.db.Column(config.db.String(4000))

    def __init__(self,board_id,board_name):
        self.board_id = board_id
        self.board_name = board_name


class app_boards_schema(config.ma.Schema):
    class Meta:
        fields = ('board_id','board_name')

boards_s = app_boards_schema()