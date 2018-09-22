class ProductionConfig(object):
    """Config variables."""

    HEROKU_FLASK_KEY = '\xc3\xc1\xf2\xe9\xd8\x14\\\x16\x9a\xbf\xee\x07'
    COMPRESSOR_DEBUG = True
    COMPRESSOR_STATIC_PREFIX = 'static'
    COMPRESSOR_OUTPUT_DIR = 'build'
    CORS_HEADERS = 'Content-Type'
    Access_Control_Allow_Origin = '*'
    STATIC_FOLDER = 'static'
    DEBUG = True
    ASSETS_DEBUG = True
    FILEUPLOAD_S3_BUCKET = 'sample-bucket-name'                         # name of the S3 bucket
    FILEUPLOAD_S3_ACL = 'public-read'                                   # S3 permission
