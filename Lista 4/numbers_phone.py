import re
from typing import Union


def number_phone_br(obj: Union[int, str]) -> int:
    """Converts brazilian phone numbers to int, adding DDD 21 if unspecified

    :param obj: String or int containing the phone number
    :type obj: Union[int, str]
    :return: The digits of the phone number as an int
    :rtype: int
    """
    if isinstance(obj, str):
        # Removes preceding "+55" if present and any "(", ")", " " or "-"
        num_str = re.sub(r"\A\+55|[ \-\(\)]", "", obj)
    else:
        num_str = str(obj)

    # Adds DDD 21 at the start if no DDD is specified
    if len(num_str) <= 9:
        num_str = "21" + num_str

    return int(num_str)
