from model import TipModel

tip_model = TipModel(52.49, 0.25)

print(f"Current Tip: {tip_model}")

tip_model.bill_amount = 109.45
tip_model.tip_percent = 0.15
print(f"Current Tip: {tip_model}")

try:
    tip_model.bill_amount = -20.00
except ValueError as ex:
    print(ex)

try:
    tip_model.tip_percent = -0.03

except ValueError as ex:
    print(ex)