# Add docstrings for the class and its defined instance functions
# Each one should describe the instance function and any required parameters/returned values
class Domino:
    def __init__(self, side_1_num: int, side_2_num: int):
        self.side_1_num = side_1_num
        self.side_2_num = side_2_num

    def can_connect(self, other_domino: "Domino") -> bool:
        return (
            self.side_1_num == other_domino.side_1_num
            or self.side_1_num == other_domino.side_2_num
            or self.side_2_num == other_domino.side_1_num
            or self.side_2_num == other_domino.side_2_num
        )


first_domino = Domino(2, 6)
second_domino = Domino(1, 2)
print(first_domino.can_connect(second_domino))
