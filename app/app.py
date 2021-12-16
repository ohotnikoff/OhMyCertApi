from flask import Flask, send_from_directory, url_for
from flask_restful import Resource, Api, reqparse

from pdf2cert import create_cert
import config


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'files'

api = Api(app)


@app.route('/files/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


class Cert(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('contact_id')
        parser.add_argument('user_fio')
        parser.add_argument('template_pdf')

        args = parser.parse_args()

        # на вход
        contact_id = args['contact_id']
        user_fio = args['user_fio']
        template_pdf = args['template_pdf']

        if (len(user_fio) > 10) & (len(user_fio) < 40):

            # создание сертификата
            cert_pdf = create_cert(user_fio, contact_id, template_pdf)
            if cert_pdf is not False:
                return {
                    'status': 'success',
                    'cert_url': url_for("download_file", name=cert_pdf, _external=True)
                }

        return {
            'status': 'error',
            'cert_url': ''
        }


api.add_resource(Cert, '/api/create_cert')
app.add_url_rule(
    "/files/<name>", endpoint="download_file", build_only=True
)


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
