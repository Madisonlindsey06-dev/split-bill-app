from kivy.app import App
from kivy.core.window import Window
from model import TipModel
from controller import TipCalculator

scale = 50
Window.size = (9*scale, 20*scale)

class TipCalculatorApp(App):
    def build(self):
        model = TipModel()
        controller = TipCalculator(model)
        # the view is created automatically when the controller is created.

        return controller
    
if __name__ == "__main__":
    app = TipCalculatorApp()
    app.run()
