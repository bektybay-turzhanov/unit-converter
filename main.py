
import tkinter as tk
from tkinter import ttk, messagebox


def convert_value(value, category, source, target):
    if category == "Расстояние":
        factors = {"Километры": 1000, "Метры": 1}
        return value * factors[source] / factors[target]
    elif category == "Масса":
        factors = {"Килограммы": 1000, "Граммы": 1}
        return value * factors[source] / factors[target]
    elif source == target:
        return value
    elif source == "Цельсий":
        return value * 9 / 5 + 32
    elif source == "Фаренгейт":
        return (value - 32) * 5 / 9
    else:
        raise ValueError("Неизвестные единицы измерения")


def convert():
    try:
        value = float(entry.get().replace(",", "."))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите правильное число")
        return

    category = category_box.get()
    source = source_box.get()
    target = target_box.get()

    try:
        result = convert_value(value, category, source, target)
    except (ValueError, KeyError):
        messagebox.showerror("Ошибка", "Проверьте единицы измерения")
        return

    result_label.config(text=f"Результат: {result:.2f} {target}")


def update_units(event=None):
    category = category_box.get()

    if category == "Расстояние":
        units = ["Километры", "Метры"]
    elif category == "Масса":
        units = ["Килограммы", "Граммы"]
    else:
        units = ["Цельсий", "Фаренгейт"]

    source_box["values"] = units
    target_box["values"] = units
    source_box.current(0)
    target_box.current(1)


def main():
    global root, category_box, source_box, target_box, entry, result_label

    root = tk.Tk()
    root.title("Конвертер единиц измерения")
    root.geometry("500x430")
    root.resizable(False, False)

    ttk.Label(
        root,
        text="Конвертер единиц измерения",
        font=("Arial", 17, "bold")
    ).pack(pady=20)

    ttk.Label(root, text="Категория:").pack()

    category_box = ttk.Combobox(
        root,
        values=["Расстояние", "Масса", "Температура"],
        state="readonly",
        width=25
    )
    category_box.pack(pady=5)
    category_box.current(0)
    category_box.bind("<<ComboboxSelected>>", update_units)

    ttk.Label(root, text="Исходная единица:").pack(pady=(10, 0))
    source_box = ttk.Combobox(root, state="readonly", width=25)
    source_box.pack(pady=5)

    ttk.Label(root, text="Единица результата:").pack(pady=(5, 0))
    target_box = ttk.Combobox(root, state="readonly", width=25)
    target_box.pack(pady=5)

    ttk.Label(root, text="Введите значение:").pack(pady=(10, 0))
    entry = ttk.Entry(root, width=28)
    entry.pack(pady=5)

    ttk.Button(
        root,
        text="Конвертировать",
        command=convert
    ).pack(pady=12)

    result_label = ttk.Label(
        root,
        text="Результат:",
        font=("Arial", 12, "bold")
    )
    result_label.pack(pady=5)

    update_units()
    root.mainloop()


if __name__ == "__main__":
    main()