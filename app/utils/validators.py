def validate_required_fields(
    data,
    required_fields
):

    missing_fields = []

    for field in required_fields:

        if field not in data or not data[field]:

            missing_fields.append(field)

    if missing_fields:

        return False, {
            "missing_fields": missing_fields
        }

    return True, None