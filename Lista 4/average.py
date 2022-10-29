import statistics
from typing import Any, SupportsFloat, TypeVar, Union

T = TypeVar('T', bound=SupportsFloat)

def average_scores(dictionary: dict[Any, T]) -> Union[float, T]:
    """Calculates the average of the values of dict

    :param dictionary: The dictionary whose values will be used in the calculation
    :type dictionary: dict[Any, T]
    :raises TypeError: When the parameter is not of the indicated type
    :return: The calculated average
    :rtype: Union[float, T]
    """
    if not isinstance(dictionary, dict):
        raise TypeError("Parameter must be a dictionary")

    return statistics.mean(dictionary.values())