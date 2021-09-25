import secrets



def check_credentials(username, password):
    """Dummy function to hande credentials.
    Right now only a hard coded username - password pair is allowed.

    Parameters
    ----------
    username : str
        Description of parameter `username`.
    password : str
        Description of parameter `password`.

    Returns
    -------
    bool
        True if given username password pair is valid.

    """
    username_ok = secrets.compare_digest(username, "please")
    password_ok = secrets.compare_digest(password, "open")
    return password_ok and username_ok
