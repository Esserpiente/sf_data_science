import numpy as np
def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем среднее число (50) от диапазона (1, 100), а потом уменьшаем или
       или увеличиваем среднее число (50) в 2 раза (т.е 25, 12, 6 и т.д) в зависимости от того, больше оно или меньше нужного.
          Функция принимает загаданное число и возвращает число попыток

       Args:
           number (int, optional): Загаданное число. Defaults to 1.

       Returns:
           int: Число попыток
       """
    count = 0
    predict = 50
    predict_1 = 50
    while number != predict:
        count += 1
        if number > predict:
            if predict_1 == 0:
                predict = 100
            predict = predict + round (predict_1/2)
            predict_1 = round (predict_1/2)

        elif number < predict:
            predict = predict - round (predict_1/2)
            predict_1 = round(predict_1 / 2)
    return count
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")



print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)