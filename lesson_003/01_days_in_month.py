
import simple_draw as sd

# Налаштування розміру екрану
sd.resolution = (800, 600)

# Запуск малювання
sd.start_drawing()

# Малюємо лінію
start_point = sd.get_point(100, 100)
end_point = sd.get_point(300, 100)
sd.line(start_point, end_point, color=sd.COLOR_RED, width=3)

# Малюємо коло
center_point = sd.get_point(400, 300)
sd.circle(center_position=center_point, radius=50, color=sd.COLOR_YELLOW, width=2)

# Малюємо прямокутник
left_bottom = sd.get_point(500, 400)
right_top = sd.get_point(700, 500)
sd.rectangle(left_bottom, right_top, color=sd.COLOR_GREEN, width=4)

# Завершуємо малювання та показуємо результат
sd.finish_drawing()

# Чекаємо, поки користувач закриє вікно
sd.sleep(5)  # Показуємо результат 5 секунд
sd.quit()