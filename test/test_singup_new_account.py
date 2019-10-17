


def test_singup_new_account(app):
    username = "user"
    password = "test"
    app.james.ensure_user_exists(username, password)
