import multiprocessing
import os
import random
from RandomWordGenerator import RandomWord

def main():
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        pool.map(create_file, range(multiprocessing.cpu_count()))

def create_file(x : list):
    file_name : str = f"file{random.randint(100000, 5000000)}_{os.getpid()}.txt"
    with open(file_name, "w", encoding="UTF-8") as fl:
        gen_words = RandomWord(max_word_size=10, constant_word_size=False)
        for _ in range(random.randint(100000, 5000000)):
            fl.write(gen_words .generate() + "\n")
        
    file_analysis(file_name)

def file_analysis(file_name : str):
    sum : int = 0
    max_len : int = 0
    min_len : int = 999999
    vowel : int = 0 #гласные
    consonant : int = 0 #согласные
    len_list : list = []
    with open(file_name, "r", encoding="UTF-8") as fl:
        for word in fl:
            word = word.strip()
            sum += len(word.replace(" ", ""))

            if len(word) > max_len:
                max_len = len(word)
            if len(word) < min_len:
                min_len = len(word)
            
            len_list.append(len(word))
           
            for char in word.lower():
                if char in "aeiouy": vowel += 1
                else: consonant += 1
    result : str = f"""
********************************************************************
  Аналитика для файла {file_name}
********************************************************************
  1. Всего символов --> {sum}
  2. Максимальная длинна слова --> {max_len}
  3. Минимальная длинна слова --> {min_len}
  4. Средняя длинна слова --> {round((max_len+min_len)/2)}
  5. Количество гласных --> {vowel}
  6. Количество согласных --> {consonant}
  7. Количество повторений слов с одинаковой длиной:
""" 
    print(result)
    for i in range(1,11):
        print("\t*"+str(i)+" сим. >> "+str(len_list.count(i)))
    

if __name__ == "__main__":
    main()