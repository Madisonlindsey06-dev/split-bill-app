from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from model import TipModel

Builder.load_file('view.kv')

class TipCalculator(BoxLayout):
    bill_input = StringProperty()
    tip_output = StringProperty()
    
    __model: TipModel

    def __init__(self, model):
        super().__init__()    
        self.__model = model

    def btn_click_calc_tip(self, tip_percent):
        try:
            self.__model.bill_amount = float(self.bill_input)
            self.__model.tip_percent = float(tip_percent)
            
            self.tip_output = f"Tip Amount: ${self.__model.tip_amount:.2f}"

        except ValueError as ex:
            print("error")
        
