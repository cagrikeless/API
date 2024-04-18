################  Routing  ##################

from configs import config
from modules import user_module,board_module,board_users_module


@config.app.route("/users", methods=['POST'])
def add_users():
    if config.request.method == 'POST':

        getSubQuery = config.session.query(config.func.max(user_module.app_users.user_id)).subquery()
        query = config.session.query(user_module.app_users).filter(user_module.app_users.user_id.in_(getSubQuery))
        for user_ids in query:
            # print(user_ids.user_id)
            max_value = user_ids.user_id

        user_id = max_value+1
        email = config.request.json['email']
        password = config.request.json['password']
        created_on = config.datetime.today().strftime('%Y-%m-%d')
        last_logged_on = config.datetime.today().strftime('%Y-%m-%d')

        new_user = user_module.app_users(user_id,email,password,created_on,last_logged_on)

        config.db.session.add(new_user)
        config.db.session.commit()

        return user_module.users_s.jsonify(new_user)


@config.app.route('/users/<int:id>', methods=['GET','PUT','DELETE'])
def users(id):

    match config.request.method:
        case 'GET':
            user_list = user_module.app_users.query.filter_by(user_id=id)

            for users in user_list:
                initialize =  user_module.app_users(users.user_id,users.email,users.password,users.created_on,users.last_logged_on)
        
            return user_module.users_s.jsonify(initialize)
    
        case 'DELETE':
            user_module.app_users.query.filter_by(user_id=id).delete()
            config.db.session.commit()
            return 'SUCCESS'
        
        case 'PUT':
            user_edit = user_module.app_users.query.filter_by(user_id=id).first()
            user_edit.password = config.request.json["password"]
            config.db.session.commit()
            return user_module.users_s.jsonify(user_edit)
        



@config.app.route('/boards', methods=['POST'])
def add_boards():
    if config.request.method == 'POST' :

        getSubQuery = config.session.query(config.func.max(board_module.app_boards.board_id)).subquery()
        query = config.session.query(board_module.app_boards).filter(board_module.app_boards.board_id.in_(getSubQuery))
        for board_ids in query:
            # print(user_ids.user_id)
            max_value = board_ids.board_id

        board_id = max_value + 1
        board_name = config.request.json['board_name']

        new_board = board_module.app_boards(board_id,board_name)

        config.db.session.add(new_board)
        config.db.session.commit()

        return board_module.boards_s.jsonify(new_board)
    

@config.app.route('/boards/<int:id>', methods=['GET','DELETE','PUT'])
def get_boards(id):

    match config.request.method:
        case 'GET':
            board_list = board_module.app_boards.query.filter_by(board_id=id)

            for users in board_list:
                initialize =  board_module.app_boards(users.board_id,users.board_name)

            return board_module.boards_s.jsonify(initialize)
        
        case 'DELETE':
            board_module.app_boards.query.filter_by(board_id=id).delete()
            config.db.session.commit()
            return 'SUCCESS'
        
        case 'PUT':
            board = board_module.app_boards.query.filter_by(board_id=id).first()
            board.board_name = config.request.json["board_name"]
            config.db.session.commit()

            return board_module.boards_s.jsonify(board)

@config.app.route('/board_users',methods=['POST'])
def add_board_users():
    if config.request.method == 'POST':
        board_line_id = config.request.json["BOARD_LINE_ID"]
        board_id = config.request.json["BOARD_ID"]
        user_id = config.request.json["USER_ID"]

        new_board_users = board_users_module.app_board_users(board_line_id,board_id,user_id)

        config.db.config.session.add(new_board_users)
        config.db.config.session.commit()
        
        return board_users_module.board_users_s.jsonify(new_board_users)



@config.app.route('/board_users/<int:id>',methods=['GET','DELETE','PUT'])
def board_users(id):

    match config.request.method:
        case 'GET':
            b_user_id = config.request.json["user_id"]
            getboard = board_users_module.app_board_users.query.filter_by(board_id=id,user_id=b_user_id)
            print(getboard)
            for board in getboard:
                initialize =  board_users_module.app_board_users(board.board_line_id,board.board_id,board.user_id)

            return board_users_module.board_users_s.jsonify(initialize)
        case 'DELETE':
            deleteboard = board_users_module.app_board_users.query.filter_by()
            return 'Succesfully deleted'



if __name__ == '__main__':
    config.app.run(debug=True)


