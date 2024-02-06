import numbers

from pandas.core import frame


def calculate_percentage(input_value):
    """
    Function to calculate the percentage of a list.
    @param input_value: List of True and False value.
    @return: percentage of True / Total.
    """
    if len(input_value) == 0:
        return None
    elif isinstance(input_value, list):
        count_true = 0
        count_total = 0
        for i in input_value:
            if isinstance(i, bool):
                count_total += 1
                if i:
                    count_true += 1
            else:
                return ValueError("Invalid input - The input value must be the list of bool values")
        return count_true / count_total


def calculate_numbers(input_value):
    """
    Function return min, max, average of list of integer
    This function will be mainly used in interface
    For non GUI, not plan to develop
    @input_value : List of numbers (int / float / double)
    @return : Dict that contains min, max, average
    """
    if len(input_value) == 0:
        return {'min': None, 'max': None, 'average': None}
    elif isinstance(input_value, list):
        min_value = input_value[0]
        max_value = input_value[0]
        average = 0
        for i in input_value:
            if isinstance(i, numbers.Number):
                if i < min_value:
                    min_value = i
                if i > max_value:
                    max_value = i
                average += i
        average = round(average / len(input_value), 2)
        res = {'min': min_value, 'max': max_value, 'average': average}
        return res


def calculate_true_false(input_value):
    """
    Function return the number of True and False in the list
    This function will be mainly used in interface
    For non GUI, not plan to develop
    @input_value : List of boolean
    @return : Dict that contains counter of True, False and percentage of True
    """
    if len(input_value) == 0:
        return {'True': 0, 'False': 0}
    elif isinstance(input_value, list):
        count_true = 0
        count_false = 0
        for i in input_value:
            if isinstance(i, bool):
                if i:
                    count_true += 1
                else:
                    count_false += 1
            else:
                return ValueError("Invalid input - The input value must be the list of bool values")
        return {'True': count_true, 'False': count_false, 'True %': round(count_true * 100 / len(input_value), 2)}


def calculate_list(input_value):
    """
    Function return length of the list and stats if all the value is number
    This function will be mainly used in interface
    For non GUI, using pandas to select field and only give it the data (metadata not included)
    @input_value : List
    @return : Dict that contains length of list.
    @return : Dict that contains stats and length of list if only list contains number
    """
    if len(input_value) == 0:
        return {'length': 0}
    elif isinstance(input_value, list):
        if_only_number = True
        if_only_boolean = True
        for i in input_value:
            if not isinstance(i, numbers.Number) and if_only_number:
                if_only_number = False
            if not isinstance(i, bool) and if_only_boolean:
                if_only_boolean = False
        if if_only_boolean:
            stats_value = calculate_true_false(input_value)
            return {'True': stats_value['True'], 'False': stats_value['False'], 'True %': stats_value['True %'],
                    'length': len(input_value)}
        if if_only_number:
            stats_value = calculate_numbers(input_value)
            return {'min': stats_value['min'], 'max': stats_value['max'], 'average': stats_value['average'],
                    'length': len(input_value)}
        else:
            return {'length': len(input_value)}


def get_columns_from_dataframe(data):
    if isinstance(data, frame.DataFrame):
        return data.columns.tolist()
    else:
        return None
