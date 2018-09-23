class ProductionConfig(object):
    """Config variables."""

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
    # DB Creds
    # mongo = MongoClient('mongodb+srv://todd:a9tw3rjw@hackerdata-gktww.gcp.mongodb.net/admin?retryWrites=true', maxPoolSize=50, connect=False)
    # db = database.Database(mongo, 'framewrk')

URI = 'mongodb://toddbirchard%40gmail.com:a9tw3rjw@stitch.mongodb.com:27020/?authMechanism=PLAIN&authSource=%24external&ssl=true&appName=framewrk-iroeq:mongodb-atlas:local-userpass'
