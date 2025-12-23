import tkinter as tk
from sudoku import resolver_sudoku
from tkinter import messagebox

def validar_entrada(nueva_entrada):
    if nueva_entrada == "":
        return True
    if nueva_entrada.isdigit() and 1 <= int(nueva_entrada) <= 9:
        return True
    return False

def crear_gui_con_tablero(tablero):
    ventana = tk.Tk()
    ventana.title("Sudoku")

    vcmd = ventana.register(validar_entrada), "%P"

    entries = []

    for fila in range(9):
        fila_entries = []
        for col in range(9):

            borde_izq = 4 if col in [0, 3, 6] else 1
            borde_arriba = 4 if fila in [0, 3, 6] else 1

            entrada = tk.Entry(
                ventana,
                width=2,
                font=("Arial", 18),
                justify="center",
                validate="key",
                validatecommand=vcmd,
                highlightthickness=1,
                highlightbackground="black"
            )
            entrada.grid(
                row=fila,
                column=col,
                padx=(borde_izq, 1),
                pady=(borde_arriba, 1)
            )

            if tablero[fila][col] != 0:
                entrada.insert(0, str(tablero[fila][col]))
                entrada.config(state="disabled", disabledbackground="#ddd")

            fila_entries.append(entrada)
        entries.append(fila_entries)

    def resolver():
        tablero_usuario = []
        for fila in range(9):
            fila_tablero = []
            for col in range(9):
                valor = entries[fila][col].get()
                if valor == "":
                    fila_tablero.append(0)
                else:
                    fila_tablero.append(int(valor))
            tablero_usuario.append(fila_tablero)

        if resolver_sudoku(tablero_usuario):
            for fila in range(9):
                for col in range(9):
                    if  entries[fila][col]["state"] != "disabled":
                        entries[fila][col].delete(0, tk.END)
                        entries[fila][col].insert(0, str(tablero_usuario[fila][col]))
            messagebox.showinfo("Sudoku resuelto", "¡Enhorabuena, has resuelto el Sudoku!")
        else:
            messagebox.showinfo("Error", "No se pudo resolver el Sudoku.")

    boton_resolver = tk.Button(ventana, text="Resolver", command=resolver)
    boton_resolver.grid(row=9, column=0, columnspan=9, sticky="we")

    def limpiar_campos():
        for fila in range(9):
            for col in range(9):
                if entries[fila][col]["state"] != "disabled":
                    entries[fila][col].delete(0, tk.END)

    boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
    boton_limpiar.grid(row=10, column=0, columnspan=9, sticky="we")

    ventana.mainloop()

if __name__ == "__main__":
    tablero_ejemplo = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    crear_gui_con_tablero(tablero_ejemplo)
