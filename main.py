from Lib_and_sql.library import *
from application_windows.owner import owner
from application_windows.menu import menu
from application_windows.traffic_police_officer import traffic_police_officer
from application_windows.inspection import inspection
from application_windows.calculation_of_cars import calculation_of_car
from application_windows.list_of_officers import list_of_officer
from application_windows.history import history

Window.size = (600, 600)
Window.clearcolor = '#1c222a'
class PBZApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(menu(name='menu'))
        sm.add_widget(owner(name='owner'))
        sm.add_widget(traffic_police_officer(name='traffic_police_officer'))
        sm.add_widget(inspection(name='inspection'))
        sm.add_widget(calculation_of_car(name='calculation_of_car'))
        sm.add_widget(list_of_officer(name='list_of_officer'))
        sm.add_widget(history(name='history'))
        return sm

if __name__ == '__main__':
    PBZApp().run()