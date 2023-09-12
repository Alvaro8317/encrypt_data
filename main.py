from read_info import read_data_from_file
from get_nicknames import return_only_nicknames
from encrypt_with_kms import encrypt_list_data_with_kms
import time

def test1(filename: str):
    people = read_data_from_file(filename)
    nicknames = return_only_nicknames(people)
    start_reading = time.time()
    cipher_nicknames = encrypt_list_data_with_kms(list_to_encrypt=nicknames)
    end_reading = time.time()
    print(f'Time with encrypt: {end_reading - start_reading}')
    # print(cipher_nicknames)


if __name__ == '__main__':
    print('Test 1: With 10 records')
    start = time.time()
    test1('raw_data_2.txt')
    end = time.time()
    print(f'Test 1 took: {end - start} seconds')
    print('Test 2: With all records')
    start = time.time()
    # It can take more than one hour, it has 30733 users
    # test1('raw_data.txt')
    end = time.time()
    print(f'Test 2 took: {end - start} seconds')