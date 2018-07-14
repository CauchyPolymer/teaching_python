class Sedan():
    no_of_doors = 4
    def __init__(self, owner='Unknown', plate_no = '', mileage=0):
        self.owner = owner
        self.plate_no = plate_no
        self.mileage = mileage

    def __str__(self):    #이 클래스를 통해서 만들어진 instance obj를 str으로 만들어줄 일이 있을때 사용.
        return('Sedan owned by {}'
                'plate no. {}'
                'mileage {}'.format(self.owner,
                                    self.plate_no,
                                    self.mileage))
    def set_owner(self, owner):
        self.owner = owner

    def set_plate_no(self, plate_no):
        self.plate_no = plate_no

    def set_mileage(self, mileage):
        self.mileage = mileage

alice_sedan = Sedan('Alice ', 'ABCED ', 10000)
print(alice_sedan)
