class CarsModel():
    mode = 'petrol'
    def __init__(self,engine,model):
        self.eng = engine
        self.model = model
    def report(self):
        print(f'This is an {self.industry}')
Mercedes_ = CarsModel(engine = 'V6',model = '4matic')
Toyota_ = CarsModel(engine = 'V4',model = 'camry')
Mercedes_.eng
Toyota_.model
Mercedes_.mode
