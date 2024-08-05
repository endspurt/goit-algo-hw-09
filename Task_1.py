import time

# Функція жадібного алгоритму для розбивки суми на монети
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount = amount % coin
    
    return result

# Функція динамічного програмування для розбивки суми на монети
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for x in range(coin, amount + 1):
            if min_coins[x - coin] + 1 < min_coins[x]:
                min_coins[x] = min_coins[x - coin] + 1
                coin_used[x] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

# Функція для вимірювання часу виконання алгоритмів
def measure_time(function, amount):
    start_time = time.time()
    result = function(amount)
    end_time = time.time()
    return result, end_time - start_time

# Вимірювання часу виконання для великих сум
amounts = [100, 500, 1000, 5000, 10000]
greedy_times = []
dp_times = []

for amount in amounts:
    _, greedy_time = measure_time(find_coins_greedy, amount)
    _, dp_time = measure_time(find_min_coins, amount)
    
    greedy_times.append(greedy_time)
    dp_times.append(dp_time)

# Виведення результатів
print("Суми:", amounts)
print("Час виконання жадібного алгоритму:", greedy_times)
print("Час виконання динамічного програмування:", dp_times)

# Написання висновків до файлу readme.md
with open("readme.md", "w", encoding="utf-8") as file:
    file.write("# Висновки\n")
    file.write("Порівняння ефективності жадібного алгоритму та алгоритму динамічного програмування.\n\n")
    file.write("## Результати вимірювання часу виконання\n")
    file.write("Суми: {}\n".format(amounts))
    file.write("Час виконання жадібного алгоритму: {}\n".format(greedy_times))
    file.write("Час виконання динамічного програмування: {}\n\n".format(dp_times))
    file.write("## Висновки\n")
    file.write("Жадібний алгоритм виконується швидше для всіх тестованих сум, оскільки він використовує простий підхід з вибором найбільшого номіналу. "
               "Проте він не завжди дає оптимальне рішення, особливо для великих сум.\n")
    file.write("Алгоритм динамічного програмування знаходить оптимальне рішення, але потребує більше часу для виконання, особливо для великих сум. "
               "Це відбувається через те, що він обчислює мінімальну кількість монет для кожної проміжної суми.\n")
    file.write("Таким чином, жадібний алгоритм може бути ефективнішим, коли важлива швидкість виконання, а алгоритм динамічного програмування є кращим вибором, коли важлива оптимальність рішення.\n")
