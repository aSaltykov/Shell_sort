def shell_sort(obj):

    # Коли я читав про сортування Шела в вікіпедії знайшов емпіричну послідовність Марціна Ціура :
    empirical = [1, 4, 10, 23, 57, 132, 301, 701, 1750]

    while True:
        for inc in empirical:
            for i in range(inc):
                while i < len(obj):
                    el = obj[i]
                    while i >= inc and obj[i - inc] > el:
                        obj[i] = obj[i - inc]
                        i -= inc
                    obj[i] = el
                    i += 1

            return obj  # той самий obj упорядкований за зростанням

print(shell_sort([57, 29, 95, 19, 79, 35, 48, 59, 21]))