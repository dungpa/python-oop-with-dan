# Fix the errors in this program
# - It defines a class called 'GPU'
#   = It contains a constructor with three parameters and declares instance variables for all three parameters
#   = It also defines an instance function called 'has_required_vram'
#       == It returns True if the vram instance variable is greater than or equal to the parameter, otherwise it returns False
#   = It also contains a docstring for the 'has_required_vram' instance function
# - It then instantiates a GPU object and calls its 'has_required_vram' instance function
class GPU:
    def __init__(self, manufacturer: str, model: str, vram: int):
        self.manufacturer = manufacturer
        self.model = model
        self.vram = vram

    def has_required_vram(self, check_vram: int) -> bool:
        ""
        Checks if the GPU has the required VRAM
        :p check_vram: the amount of VRAM to check for
        :r: True if the GPU has the required VRAM, False otherwise
        """
        self.vram >= check_vram


my_gpu = GPU("MSI", "Slipstream", 8)
print(my_gpu.has_required_vram(4))
