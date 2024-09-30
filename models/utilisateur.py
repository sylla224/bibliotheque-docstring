class User:
    """Classe pour les utilisateurs

    Raises:
        ValueError: Le nom d'utilisateur {username} existe déjà.

    Returns:
        _type_: User
    """
    _usernames = set()
    def __init__(self, username, password, type_utilisateur:int):
        if User.username_exists(username):
            raise ValueError(f'Le nom d''utilisateur {username} existe déjà.')
        self.username = username
        self.password = password
        self.type_utilisateur = type_utilisateur
        User._usernames.add(username)

    def __str__(self):
        return f'User: {self.username}'
    @classmethod
    def username_exists(cls, username):
        return username in cls._usernames