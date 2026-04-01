from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from model import TipCalculatorModel

class TipCalculatorView(BoxLayout):
    # Properties for data binding
    bill_amount = StringProperty("0.00")
    num_people_input = StringProperty("1")  # NEW: for number of people
    split_output = StringProperty("Total per person: $0.00")  # NEW: for split result
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = TipCalculatorModel()
        # Initialize with default values
        self.update_tip_display()
    
    def btn_click_calc_tip(self, tip_percentage):
        """Handle tip calculation button clicks"""
        try:
            # Get and validate bill amount
            bill = float(self.bill_amount)
            if bill < 0:
                raise ValueError("Bill amount cannot be negative")
            
            # Update model
            self.model.bill_amount = bill
            self.model.tip_percentage = tip_percentage
            
            # NEW: Update model with number of people
            if self.num_people_input and self.num_people_input.strip():
                self.model.num_people = self.num_people_input
            
            # Calculate and display results
            self.update_tip_display()
            
            # Clear any previous error messages
            self.ids.error_label.text = ""
            
        except ValueError as e:
            # Display error to user
            self.ids.error_label.text = f"Error: {str(e)}"
            # Reset display to default values
            self.ids.tip_result.text = "Tip: $0.00"
            self.ids.total_result.text = "Total: $0.00"
            self.split_output = "Total per person: $0.00"
    
    def update_tip_display(self):
        """Update UI with calculated values"""
        tip = self.model.calculate_tip_amount()
        total = self.model.calculate_total_bill()
        total_per_person = self.model.total_per_person
        
        # Update labels
        self.ids.tip_result.text = f"Tip: ${tip:.2f}"
        self.ids.total_result.text = f"Total: ${total:.2f}"
        self.split_output = f"Total per person: ${total_per_person:.2f}"

class TipCalculatorApp(App):
    def build(self):
        return TipCalculatorView()

if __name__ == '__main__':
    TipCalculatorApp().run()
