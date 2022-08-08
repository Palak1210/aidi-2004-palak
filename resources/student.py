from flask_restful import Resource, reqparse
from models.student import Student


class delete_student(Resource):
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('student_id', type=int)
        data = parser.parse_args()
        response = Student.delete_student(self, data['student_id'])
        return {
            "message": "Data of student no: " + str(data['student_id']) + " isDeleted",
        }, 200


class add_student(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str)
    parser.add_argument('last_name', type=str)
    parser.add_argument('date_of_birth', type=str)
    parser.add_argument('amount_due', type=int)

    def post(self):
        data = add_student.parser.parse_args()
        Student(
                data['first_name'], data['last_name'], data['date_of_birth'],
                data['amount_due']
            ).save_to_db()

        return {
                    "message": "Data of " + data['first_name'] + "is added to Database"
                }, 200


class get_student(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        response = Student.get_student(self)
        return {
            "message" : "All the data of students is retrieved",
            "data": response
        }, 200


class edit_student(Resource):
    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument('student_id', type=int)
        parser.add_argument('first_name', type=str)
        parser.add_argument('last_name', type=str)
        parser.add_argument('date_of_birth', type=str)
        parser.add_argument('amount_due', type=int)
        data = parser.parse_args()
        Student.update_db(self, data['student_id'], data['first_name'], data['last_name'], data['date_of_birth'],
        data['amount_due'])
        return {
            "message": "Data of " + data['first_name'] + " is updated",
        }, 200

