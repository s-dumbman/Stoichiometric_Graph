import json

class ban:
    def __init__(self, mass, f_weight):
        self.mass = mass
        self.f_weight = f_weight

    def volume(self):
        return self.mass / self.f_weight

b1 = ban(2, 1)
b2 = ban(2, 1)

class fomula:
    global b1, b2
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number
        if first_number <= 0 or second_number <= 0:
            raise ValueError("계수 오류")
        if int(first_number) != first_number or int(second_number) != second_number:
            raise ValueError("계수는 정수여야 합니다")
        self.sdf = second_number / first_number
        self.fds = first_number / second_number
    def determineFomula(self):
        if b2.volume() - self.sdf*b1.volume() > 0:
            return "Case_b1"
        elif b1.volume() - self.fds*b2.volume() > 0:
            return "Case_b2"
        elif b2.volume() - self.sdf*b1.volume() <= 0 and b1.volume() - self.fds*b2.volume() <= 0:
            return "Case_all"
        else:
            raise SyntaxError("경우 오류")

f_1 = 2
f_2 = 1
f = fomula(f_1, f_2)
f_d = f.determineFomula()
        
def save_fomula(first_number, second_number):
    global f, f_d
    fomula_data = {
        "first_number": first_number,
        "second_number": second_number,
        "fomula_determine" : f_d
    }
    with open("fomulaclip.json", "w") as f:
        json.dump(fomula_data, f, indent=4)
    print("fomula saved")
    
def save_banclip(b1, b2):
    banclip_data = {
        "b1": {
            "mass": b1.mass,
            "f_weight": b1.f_weight,
            "volume": b1.volume()
        },
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
    save_banclip(b1, b2)
    save_fomula(f_1, f_2)

datafold()

