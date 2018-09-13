class ProductionConfig(object):
    """Config variables."""

    heroku_flask_key = '\xc3\xc1\xf2\xe9\xd8\x14\\\x16\x9a\xbf\xee\x07'
    COMPRESSOR_DEBUG = True
    COMPRESSOR_STATIC_PREFIX = 'static'
    COMPRESSOR_OUTPUT_DIR = 'build'
    CORS_HEADERS = 'Content-Type'
    Access_Control_Allow_Origin = '*'
    static_folder = 'static'
    debug = True
    ASSETS_DEBUG = True
