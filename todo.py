import flet as ft

def main(page: ft.Page):

    def add_task(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value=''
        page.update()

    new_task=(ft.TextField(hint_text="Escribe una tarea"))

    page.add(new_task,ft.FloatingActionButton(icon=ft.icons.ADD,on_click=add_task))

ft.app(target=main)
