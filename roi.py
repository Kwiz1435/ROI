class RentalProperty:
    def __init__(self, purchase_price, closing_costs, renovation_costs, annual_rent, mortgage_payment, property_tax, insurance, maintenance):
        self.purchase_price = purchase_price
        self.closing_costs = closing_costs
        self.renovation_costs = renovation_costs
        self.annual_rent = annual_rent
        self.mortgage_payment = mortgage_payment
        self.property_tax = property_tax
        self.insurance = insurance
        self.maintenance = maintenance

    def calculate_roi(self):
        total_cost = self.purchase_price + self.closing_costs + self.renovation_costs
        annual_expenses = (self.mortgage_payment * 12) + self.property_tax + self.insurance + self.maintenance
        roi = (self.annual_rent - annual_expenses) / total_cost
        return roi

# create a rental property object
property1 = RentalProperty(200000, 10000, 5000, 24000, 1000, 3000, 1000, 2000)

# calculate the ROI for the property
roi = property1.calculate_roi()

print(f"ROI: {roi}")
