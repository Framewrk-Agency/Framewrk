import os


class BaseConfig(object):
    """Config variables."""

    SECRET_KEY = b'_5#y2L"F4fghfghfghdfhdfgQ8z\n\xec]/'
    COMPRESSOR_DEBUG = True
    COMPRESSOR_STATIC_PREFIX = os.path.realpath('static')
    COMPRESSOR_OUTPUT_DIR = os.path.realpath('build')
    CORS_HEADERS = 'Content-Type'
    Access_Control_Allow_Origin = '*'
    STATIC_FOLDER = 'static'
    DEBUG = True
    ENV = 'development'
    ASSETS_DEBUG = True
    FILEUPLOAD_S3_BUCKET = 'sample-bucket-name'                         # name of the S3 bucket
    FILEUPLOAD_S3_ACL = 'public-read'
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))                                 # S3 permission
    # DB Creds
    # mongo = MongoClient('mongodb+srv://todd:a9tw3rjw@hackerdata-gktww.gcp.mongodb.net/admin?retryWrites=true', maxPoolSize=50, connect=False)
    # db = database.Database(mongo, 'framewrk')


URI = 'mongodb://toddbirchard%40gmail.com:a9tw3rjw@stitch.mongodb.com:27020/?authMechanism=PLAIN&authSource=%24external&ssl=true&appName=framewrk-iroeq:mongodb-atlas:local-userpass'
