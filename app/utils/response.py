from flask import jsonify


def success_response(
    message,
    data=None,
    
):

    response = {
        "success": True,
        "message": message,
        "data": data
    }

    return jsonify(response), 200


def error_response(
    message,
   
):

    response = {
        "success": False,
        "message": message
    }
    return jsonify(response), 400