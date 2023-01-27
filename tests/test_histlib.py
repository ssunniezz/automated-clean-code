from automated_clean_code.exercise_20_histlib import fill_up_histogram_from_list, find_max_key


def test_fill_up_histogram_from_list():
    lst = ["1", "2", "3", "1"]
    result = {"1": 2, "2": 1, "3": 1}
    assert fill_up_histogram_from_list(lst) == result


def test_find_max_key():
    counter = {"1": 2, "2": 1, "3": 3, "4": 1}
    max_key, max_counter, min_key, min_counter = find_max_key(counter)
    assert max_key == "3"
    assert max_counter == 3
    assert min_key == "2"
    assert min_counter == 1
