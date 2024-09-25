import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked=None, expand=1):
        super().__init__(text=text, expand=expand)
        self.on_click = button_clicked
        self.data = text

class DigitButton(CalcButton):
    def __init__(self, text, expand=1):
        super().__init__(text, expand=expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text):
        super().__init__(text)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text):
        super().__init__(text)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

def main(page: ft.Page):
    page.title = "Calc App"
    result = ft.Text(value="0")

    def button_clicked(e):
        if e.control.data == "AC":
            result.value = "0"
        # Aquí puedes añadir más lógica para otros botones

    content = ft.Column(
        controls=[
            ft.Row(controls=[result], alignment="end"),
            ft.Row(
                controls=[
                    ExtraActionButton(text="AC", button_clicked=button_clicked),
                    ExtraActionButton(text="+/-", button_clicked=button_clicked),
                    ExtraActionButton(text="%", button_clicked=button_clicked),
                    ActionButton(text="/", button_clicked=button_clicked),
                ]
            ),
            ft.Row(
                controls=[
                    DigitButton(text="7", button_clicked=button_clicked),
                    DigitButton(text="8", button_clicked=button_clicked),
                    DigitButton(text="9", button_clicked=button_clicked),
                    ActionButton(text="*", button_clicked=button_clicked),
                ]
            ),
            ft.Row(
                controls=[
                    DigitButton(text="4", button_clicked=button_clicked),
                    DigitButton(text="5", button_clicked=button_clicked),
                    DigitButton(text="6", button_clicked=button_clicked),
                    ActionButton(text="-", button_clicked=button_clicked),
                ]
            ),
            ft.Row(
                controls=[
                    DigitButton(text="1", button_clicked=button_clicked),
                    DigitButton(text="2", button_clicked=button_clicked),
                    DigitButton(text="3", button_clicked=button_clicked),
                    ActionButton(text="+", button_clicked=button_clicked),
                ]
            ),
            ft.Row(
                controls=[
                    DigitButton(text="0", expand=2, button_clicked=button_clicked),
                    DigitButton(text=".", button_clicked=button_clicked),
                    ActionButton(text="=", button_clicked=button_clicked),
                ]
            ),
        ]
    )

    page.add(
        ft.Container(
            width=350,
            bgcolor=ft.colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=content
        )
    )

ft.app(main)
