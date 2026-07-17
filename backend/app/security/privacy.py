PUBLIC = "public"
SINGLE = "single"
BROKEN = "broken"
LOVER = "lover"
FAMILY = "family"
HIDDEN = "hidden"


def can_message(
    me,
    target,
    is_friend=False,
):

    if target.status == PUBLIC:
        return True

    if target.status == SINGLE:
        return me.gender != target.gender

    if target.status == BROKEN:
        return is_friend

    if target.status == LOVER:

        if is_friend:
            return True

        return me.gender == target.gender

    if target.status == FAMILY:

        if not is_friend:
            return False

        return me.status == FAMILY

    return False