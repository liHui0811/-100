import os

class Config:
    # APP_NAME = 'OAUTH'
    # if os.environ.get('SECRET_KEY'):
    #     SECRET_KEY = os.environ.get('SECRET_KEY')
    # else:
    #     SECRET_KEY = 'SECRET_KEY_ENV_VAR_NOT_SET'
    #     print('SECRET KEY ENV VAR NOT SET! SHOULD NOT SEE IN PRODUCTION')

    DEBUG = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    print('THIS APP IS IN DEBUG MODE. YOU SHOULD NOT SEE THIS IN PRODUCTION.')


config = {
    'dev': DevelopmentConfig
}
