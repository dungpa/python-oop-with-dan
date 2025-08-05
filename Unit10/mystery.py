from random import randint

class MysteryBox:
    def __init__(self, list):
        self.list = list

    def choice(self):
        i=randint(0, len(self.list))
        reward = self.list[i]
        return reward


mysterybox = MysteryBox(["custom_teddy", "model_train", "action_figure", "diecast_car", "lego_set"])
print(mysterybox.choice())
