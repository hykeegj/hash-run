import hashlib
import os

program_version = '1.0.0'

os.system('cls')

path_dir = './'
files = os.listdir(path_dir)

while True:
    try:
        print(f'<프로그램 버전: {program_version}>\n')
        file_dictionary = {}
        index = 1

        for file in files:
            file_dictionary[index] = file
            print(f'[{index}] {file}')
            index += 1

        print('검사할 파일 번호-> ', end='')
        input_number = input()
        input_number = int(input_number)

        print(f'\n선택된 파일: {file_dictionary[input_number]}')
        f = open(f'{file_dictionary[input_number]}', 'rb')
        data = f.read()
        f.close()

        print('해시값 검사 중...')
        md5_hash = hashlib.md5(data).hexdigest()
        sha1_hash = hashlib.sha1(data).hexdigest()
        sha256_hash = hashlib.sha256(data).hexdigest()
        print(f'\033[96mMD5: {md5_hash}\033[0m')
        print(f'\033[96mSHA1: {sha1_hash}\033[0m')
        print(f'\033[96mSHA256: {sha256_hash}\033[0m')

        break
    except:
        print('')
        print('\033[91m잘못된 입력값이거나 폴더입니다! 다시 입력해 주세요!\033[0m')
        os.system('pause')
        os.system('cls')

print('비교할 해시값 입력-> ', end='')
input_hash_value = input()
input_hash_value = input_hash_value.lower()


def HashCheck(input_hash_value):
    if md5_hash == input_hash_value:
        print('\033[92mMD5 해시값과 동일합니다!\033[0m')
    elif sha1_hash == input_hash_value:
        print('\033[92mSHA1 해시값과 동일합니다!\033[0m')
    elif sha256_hash == input_hash_value:
        print('\033[92mSHA256 해시값과 동일합니다!\033[0m')
    else:
        print('\033[91m일치하는 해시값이 없습니다!\033[0m')


print('')
HashCheck(input_hash_value)
print('프로그램을 종료합니다')
os.system('pause')
