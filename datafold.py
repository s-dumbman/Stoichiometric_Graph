import json

class ban:
    def __init__(self, mass, f_weight):
        self.mass = mass
        self.f_weight = f_weight

    def volume(self):
        return self.mass / self.f_weight
    
b2 = ban(16, 1)

class fomula:
    global b1, b2
    def __init__(self, first_number, second_number, third_number):
        self.first_number = first_number
        self.second_number = second_number
        self.third_number = third_number
        if first_number <= 0 or second_number <= 0:
            raise ValueError("계수 오류")
        if int(first_number) != first_number or int(second_number) != second_number:
            raise ValueError("계수는 정수여야 합니다")
        self.sdf = second_number / first_number
        self.fds = first_number / second_number

f_1 = 20
f_2 = 21
f_3 = 23
f = fomula(f_1, f_2, f_3)
        
def save_fomula(first_number, second_number, third_number):
    global f, f_d
    fomula_data = {
        "first_number": first_number,
        "second_number": second_number,
        "third_number": third_number
    }
    with open("fomulaclip.json", "w") as f:
        json.dump(fomula_data, f, indent=4)
    print("fomula saved")
    
def save_banclip(b2):
    banclip_data = {
        "b2": {
            "mass": b2.mass,
            "f_weight": b2.f_weight,
            "volume": b2.volume()
        }
    }
    with open("banclip.json", "w") as f:
        json.dump(banclip_data, f, indent=4)
    print("banclip saved")

def datafold():
    save_banclip(b2)
    save_fomula(f_1, f_2, f_3)

datafold()

