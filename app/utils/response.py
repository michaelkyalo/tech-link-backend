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

    return jsonify(response), 


def error_response(
    message,
   
):

    response = {
        "success": False,
        "message": message
    }