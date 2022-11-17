from Lib_and_sql.library import *
#окно меню

class menu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text_inf = 'Владелец - Добавление/редактирование/удаление информации \n о владельцах автомобилей и их транспортных средствах \n\n' \
                   'Сотрудник Гаи - Добавление/редактирование/удаление информации \n сотрудниках ГАИ \n\n' \
                   'Осмотр - Добавление/редактирование/удаление информации \n об проведенном осмотре \n\n' \
                   'Рассчет по дням - Расчет количество автомобилей, прошедших \n техосмотр за заданный промежуток времени с разбивкой по дням. \n\n' \
                   'Список сотрудников ГАИ - Просмотр списка сотрудников ГАИ, проводивших \n осмотр  на заданную дату: ФИО, звание сотрудника, госномера \n автомобилей, которые он осматривал \n\n' \
                   'История - Просмотр истории прохождения осмотров заданным автомобилем \n (номер двигателя) – дата прохождения, результат'
        bl = BoxLayout(orientation='vertical', spacing=1)
        bl.add_widget(Label(text=text_inf, font_size = 12))
        gl = GridLayout(cols=3, rows=2, spacing=1)
        gl.add_widget(Button(text='Владелец', background_color='#edb021', background_normal='', on_press=self.click_for_move_to_owner))
        gl.add_widget(Button(text='Сотрудник Гаи', background_color='#edb021', background_normal='', on_press=self.click_for_move_to_traffic_police_officer))
        gl.add_widget(Button(text='Осмотр', background_color='#edb021', background_normal='', on_press=self.click_for_move_to_inspection))
        gl.add_widget(Button(text='Рассчет по дням', background_color='#edb021', background_normal='', on_press=self.click_for_move_to_calculation_of_car))
        gl.add_widget(Button(text='Список сотрудников ГАИ', background_color='#edb021', background_normal='', on_press=self.click_for_move_to_list_of_officer))
        gl.add_widget(Button(text='История', background_color='#edb021', background_normal='', on_press=self.click_for_move_to_history))
        bl.add_widget(gl)
        self.add_widget(bl)

    def click_for_move_to_owner(self, *args): #переход на окно владельца
        self.manager.transition.direction = 'left'
        self.manager.current = 'owner'

    def click_for_move_to_traffic_police_officer(self, *args): #переход на окно сотрудника ГАИ
        self.manager.transition.direction = 'left'
        self.manager.current = 'traffic_police_officer'

    def click_for_move_to_inspection(self, *args):  # переход на окно просмотра
        self.manager.transition.direction = 'left'
        self.manager.current = 'inspection'

    def click_for_move_to_calculation_of_car(self, *args):  # переход на окно список машин
        self.manager.transition.direction = 'left'
        self.manager.current = 'calculation_of_car'

    def click_for_move_to_list_of_officer(self, *args):  # переход на окно список сотрудника ГАИ
        self.manager.transition.direction = 'left'
        self.manager.current = 'list_of_officer'

    def click_for_move_to_history(self, *args):  # переход на окно истории
        self.manager.transition.direction = 'left'
        self.manager.current = 'history'