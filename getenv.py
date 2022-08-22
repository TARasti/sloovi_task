from dotenv import load_dotenv
import os

# getURL function
def getURL():
    """
        This function is used get mongodb connection url from env
    """
    ENV = os.getenv("ENV", "")
    dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__name__)), "configs",
                               "{env}.env".format(env=ENV))
    load_dotenv(verbose=True, dotenv_path=dotenv_path)
    URL = os.environ.get("URL")
    print(URL)
    return URL

# getKey function
def getKEY():
    """
        This function is used get Key from env
    """
    ENV = os.getenv("ENV", "")
    dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__name__)), "configs",
                               "{env}.env".format(env=ENV))
    load_dotenv(verbose=True, dotenv_path=dotenv_path)
    KEY = os.environ.get("SECRET_KEY")
    print(KEY)
    return KEY
