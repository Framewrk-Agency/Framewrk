import os


class BaseConfig(object):
    """Config variables."""

    SECRET_KEY = b'_5#y2L"F4fghfghfghdfhdfgQ8z\n\xec]/'
    COMPRESSOR_DEBUG = True
    # FLASK_ENV = development
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
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
    #MONGO_URI = 'mongodb+srv://framewrk_user:OjwLpzWvyCt4cFtg@hackerdata-gktww.gcp.mongodb.net/framewrk?retryWrites=true'
