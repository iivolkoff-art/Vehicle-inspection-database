from Lib_and_sql.library import *
#окно хозяина

class owner(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gl_government_number = TextInput(hint_text='Введите госномер автомобиля', text ='', height=30)
        self.gl_row_name = TextInput(hint_text='Введите названия столбца', text='', height=30)
        self.gl_data = TextInput(hint_text='Введите содержимое', text = '', height=30)

        bl = BoxLayout(orientation='vertical', spacing=1)
        gl = GridLayout(cols=2, spacing=1, size_hint = (1, 2))

        gl.add_widget(self.gl_government_number)
        gl.add_widget(Button(text='В меню',background_color='#825b00', background_normal='', on_press=self.click_for_move))
        gl.add_widget(self.gl_row_name)
        gl.add_widget(Label(text = 'government_number, engine_number, color, brand, \ntechnical_passport_number, driver_license_number , owner_name, \nplace_of_residence, year_of_birth, sex ', font_size = 10))
        gl.add_widget(self.gl_data)
        gl.add_widget(Label(text = 'Добавить - создает новую запись \nРедактировать - осуществяет замену данных в одной из ячеек \nУдалить - удаляет запись', font_size = 10))
        bl.add_widget(gl)
        gl1 = GridLayout(cols=3, rows=2, spacing=1)
        gl1.add_widget(Button(text='Добавить', background_color='#edb021', background_normal='', on_press=self.add))
        gl1.add_widget(Button(text='Редактировать', background_color='#edb021', background_normal='', on_press=self.update))
        gl1.add_widget(Button(text='Удалить', background_color='#edb021', background_normal='', on_press=self.delete))

        bl.add_widget(gl1)
        self.add_widget(bl)

    def click_for_move(self, *args): #переход в меню
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
            cursor.execute(f"DELETE FROM owner WHERE government_number = '{self.gl_government_number.text}'")
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
            cursor.execute(f"UPDATE owner SET {self.gl_row_name.text} = '{self.gl_data.text}' Where owner.government_number = '{self.gl_government_number.text}'") #ошибка
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
            cursor.execute(f"INSERT INTO owner(government_number, engine_number, color, brand, technical_passport_number, driver_license_number, owner_name, place_of_residence, year_of_birth, sex ) VALUES ('{self.gl_government_number.text}', Null, Null, Null, Null, Null,Null,Null,Null,Null)")
            connection.commit()
        except Exception as e:
            Error.error(e)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Connection closed")

