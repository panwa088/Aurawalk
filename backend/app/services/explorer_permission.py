def map_visibility(distance: float):

    if distance <= 200:

        return {
            "level": "clear",
            "avatar": True,
            "profile": True,
            "message": True,
        }

    if distance <= 500:

        return {
            "level": "blur",
            "avatar": False,
            "profile": False,
            "message": False,
        }

    return {
        "level": "dot",
        "avatar": False,
        "profile": False,
        "message": False,
    }