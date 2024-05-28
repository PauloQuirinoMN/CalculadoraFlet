import flet as ft
from flet import colors
 
botoes = [
    {'Operador': 'AC', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'Operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'Operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'Operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'Operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'Operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'Operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'Operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'Operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE}
]


def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 270
    page.window_height = 390
    page.title = 'Calculadora'
    page.window_always_on_top = True
 

    resultado = ft.Text(value="0", color=colors.WHITE, size=20,)

    def calculate(operador, value_at):
        try:
            value = eval(value_at)

            if operador == '%':
                value/= 100
            elif operador == '±':
                value = -value
        except:
            return 'Ta Doido'
        
        return str(value)

    def select(e):
        value_at = resultado.value if resultado.value not in ('0', 'Ta Doido') else ''
        value = e.control.content.value

        if value.isdigit(): 
            value = value_at + value
        elif value == 'AC':
            value='0'
        else:
            if value_at and value_at[-1] in ('/','*','-','+','.'):
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ('=', '%', '±'):
                value = calculate(operador=value[-1], value_at=value_at)
        
        resultado.value= value
        resultado.update()

    display = ft.Row(
        width=270,
        controls=[resultado],
        alignment='end'
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['Operador'], color=btn['fonte']),
        width=50,
        height=50,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select
 
    )for btn in botoes]

    keyboard = ft.Row(
        width=270,
        wrap=True,
        controls=btn,
        alignment='end'
    )


    page.add(display, keyboard)



ft.app(target = main)    