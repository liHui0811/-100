from flask_restful import Resource, reqparse

class TestView(Resource):

    def get(self):

        print('hello, testview')
        dic = {'code': '200', 'message': 'welcome testview'}
        return dic