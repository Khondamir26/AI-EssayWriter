##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
