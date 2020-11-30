class bike():
    specious='Vehicle'
    def __init__(self,company_name,model,fuel_type,top_speed,gears):
        self.company_name=company_name
        self.model=model
        self.fuel_type=fuel_type
        self.top_speed=top_speed
        self.gears=gears
        self.Vehicle_type='Two Wheeler'

    def change_gear(self,val):
        if self.gears<val:
            self.gears=val
            return('gear is incremented in:',val)
        elif self.gears==val:
            return ('Gear value remains same')
        else:
            self.gears = self.gears - 1
            return('gear is decremented in:',val)
    def change_model(self,name):
        self.model=name
        print('model name is changed into',name)
def remote(bikes):
    bikes.change_model('Bullet')


bike1=bike('yamaha','FZ','petrol',114,5)
bike2=bike('hero honda','passion plus','petrol',88,4)

remote(bike1)

