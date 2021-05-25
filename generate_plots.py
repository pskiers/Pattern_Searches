from timeit import timeit
from matplotlib import pyplot as plt


def read_from_file(filename, count):
    words_list = list()
    with open(filename) as file_handle:
        i = 1
        for line in file_handle:
            splitted_line = line.split()
            for word in splitted_line:
                words_list.append(word)
                if i == count:
                    return words_list
                i += 1


if __name__ == "__main__":
    n_words = [100, 200, 500, 1000]
    navie_times = []
    kmp_times = []
    rk_times = []
    file_content = read_from_file('pan-tadeusz.txt', 68346)
    text = str()
    for word in file_content:
        text += word
        text += ' '
    for n in n_words:
        words_to_find = read_from_file('pan-tadeusz.txt', n)
        navie_times.append(timeit(f'for word in words: find_N(word, "{text}")', number=1, setup=f'from algorithms import find_N; words = {words_to_find}'))
        kmp_times.append(timeit(f'for word in words: find_KMP(word, "{text}")', number=1, setup=f'from algorithms import find_KMP; words = {words_to_find}'))
        rk_times.append(timeit(f'for word in words: find_KR(word, "{text}")', number=1, setup=f'from algorithms import find_KR; words = {words_to_find}'))
    plt.plot(n_words, navie_times, label="Algoytm naiwny")
    plt.plot(n_words, kmp_times, label="Algrytm Knuths-Morrisa-Pratta")
    plt.plot(n_words, rk_times, label="Algorytm Karpa-Rabina")
    plt.legend()
    plt.title('Search for n words in text')
    plt.savefig('search_plot.png')
    plt.clf()
