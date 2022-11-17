from Lib_and_sql.library import *
#окно сотрудника гаи
class traffic_police_officer(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gl_name_officer = TextInput(hint_text='Введите ФИО сотрудника', text='', height=30)
        self.gl_row_name_officer = TextInput(hint_text='Введите названия столбца', text='', height=30)
        self.gl_data_officer = TextInput(hint_text='Введите содержимое', text='', height=30)

        bl = BoxLayout(orientation='vertical', spacing=1)
        gl = GridLayout(cols=2, spacing=1, size_hint=(1, 2))

        gl.add_widget(self.gl_name_officer)
        gl.add_widget(Button(text='В меню', background_color='#825b00', background_normal='', on_press=self.click_for_move))
        gl.add_widget(self.gl_row_name_officer)
        gl.add_widget(Label(text = 'name, job_title, rank', font_size=10))
        gl.add_widget(self.gl_data_officer)
        gl.add_widget(Label(text = 'Добавить - создает новую запись \nРедактировать - осуществяет замену данных в одной из ячеек \nУдалить - удаляет запись', font_size = 10))
        bl.add_widget(gl)
        gl = GridLayout(cols=3, rows=2, spacing=1)
        gl.add_widget(Button(text='Добавить', background_color='#edb021', background_normal='', on_press=self.add))
        gl.add_widget(Button(text='Редактировать', background_color='#edb021', background_normal='', on_press=self.update))
        gl.add_widget(Button(text='Удалить', background_color='#edb021', background_normal='', on_press=self.delete))

        bl.add_widget(gl)
        self.add_widget(bl)

    def click_for_move(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

    def delete(self, instance):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM police WHERE name = '{self.gl_name_officer.text}'")
            connection.commit()
        except Exception as e:
            Error.error(e)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed")

    def update(self, instance):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            cursor = connection.cursor()
            cursor.execute(f"UPDATE police SET {self.gl_row_name_officer.text} = '{self.gl_data_officer.text}' Where name = '{self.gl_name_officer.text}'") #ошибка
            connection.commit()
        except Exception as e:
            Error.error(e)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed")

    def add(self, instance):
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            cursor = connection.cursor()
            cursor.execute(f"INSERT INTO police(name, job_title, rank) VALUES ('{self.gl_name_officer.text}', Null, Null)")
            connection.commit()
        except Exception as e:
            Error.error(e)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed")