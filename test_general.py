import pytest
import sys
sys.path.append('..')
from day1 import top_N_total_calories

@pytest.mark.parametrize('N, expected_value', ((1, 24000), (3, 45000)))
def test_top_N_total_calories_valid(N, expected_value):
    filepath = "test_data/testdata_day1_1.txt"
    total_calories = top_N_total_calories(filepath, N)
    assert total_calories == expected_value

@pytest.mark.parametrize('N', (-1, 0, 'nothing'))
def test_top_N_total_calories_invalid(N):
    filepath = "test_data/testdata_day1_1.txt"
    with pytest.raises(Exception):
        total_calories = top_N_total_calories(filepath, N)




# def test_number_of_food_per_elf():
#     filepath = "test_data/testdata_day1_1.txt"
    
#     elf_calories = get_food_per_elf(filepath)

#     assert len(elf_calories[0]) == 3
#     assert len(elf_calories[1]) == 1
#     assert len(elf_calories[4]) == 1

# def test_sum_of_calories_per_elf():
#     filepath = "test_data/testdata_day1_1.txt"
    
#     elf_calories = get_food_per_elf(filepath)

    