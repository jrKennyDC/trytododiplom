import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Функция для обновления кадров с камеры
def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(image=Image.fromarray(frame))
        panel.img = img
        panel.config(image=img)
    panel.after(10, update_frame)

# Функция для открытия или скрытия комбобокса
def toggle_combobox():
    if combobox.winfo_viewable():
        combobox.pack_forget()
    else:
        combobox.pack()

# Создание окна Tkinter
root = tk.Tk()
root.title("Отображение видеопотока с камеры")

# Использование камеры с индексом 0 (обычно это встроенная камера)
cap = cv2.VideoCapture(0)

# Создание панели для отображения видеопотока
panel = tk.Label(root)
panel.pack(padx=10, pady=10)

# Создание кнопки для открытия/скрытия комбобокса
toggle_button = ttk.Button(root, text="Показать/Скрыть Комбобокс", command=toggle_combobox)
toggle_button.pack(pady=5)

# Создание комбобокса
combobox = ttk.Combobox(root, values=["СТАС МАФИЯ", "СТАС МАФИЯ", "СТАС МАФИЯ"])

# Обновление кадров
update_frame()

# Запуск основного цикла обработки событий
root.mainloop()

# Остановка захвата видео и закрытие окон
cap.release()
cv2.destroyAllWindows()