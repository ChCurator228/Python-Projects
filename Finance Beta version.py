def kredit():
    # Ввод данных от пользователя
    amount = int(input("Сумма кредита: "))
    percent = float(input("Процентная ставка: "))
    years = int(input("Срок кредитования (в годах): "))
    
    # Преобразование процентной ставки
    monthly_rate = percent / 100 / 12  # Месячная процентная ставка
    number_of_payments = years * 12  # Общее количество платежей
    
    # Расчет ежемесячного платежа по формуле аннуитета
    if monthly_rate > 0:
        monthly_payment = (amount * monthly_rate) / (1 - (1 + monthly_rate) ** -number_of_payments)
    else:
        monthly_payment = amount / number_of_payments  # Если процент 0, просто делим сумму на количество месяцев
    
    total_payment = monthly_payment * number_of_payments  # Общая сумма выплат
    total_interest = total_payment - amount  # Общая переплата по кредиту
    
    # Вывод результатов
    print(f"Вы переплачиваете: {total_interest:.2f} \nВ месяц платите: {monthly_payment:.2f}")
    
def razdelit_money():
     # Ввод данных от пользователя
     salary = int(input("Ваш доход за месяц: "))
     # Разделение на проценты
     food = salary * 0.5 #Еда и одежда
     expenses = salary * 0.3 #Развлечения
     pillow = salary * 0.1 #На черный день
     invest = salary * 0.1 #Облигации и прочее
     
     # Вывод результатов
     print("Советуем разделить ваши деньги таким образом!", "\n 1. На еду и одежду: ", food, "\n 2. На развлечение: ", expenses, "\n 3. Ваша подушка безопасности: ", pillow, "\n 4. На инвестиции и облигации: ", invest)
     print("Таким образом вы не сдохните раньше времени :)", "\n Удачного вам дня!")
# Основное меню
print("1. Рассчитать процент кредита.")
print("2. Разделить средства по уму.")
vopros = int(input("Выберите пункт: "))

if vopros == 1:
    kredit() 
elif vopros == 2:
    razdelit_money()
else:
    print("Такого пункта не существует")
    
# Код написал ChCurator 
# instagram: ahennso
# Студент университета Turan Astana:)