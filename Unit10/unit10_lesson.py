class Time:
    def __init__(self, seconds):
        """
        It helps create the connections and variable values.
        :param seconds: the amount of seconds mentioned
        """
        self.seconds = seconds

    def minutes(self):
        """
        the function prints out the number of minutes and sends it to a different print function which
        phrases it correctly
        :return: the number of minutes0
        """
        return self.seconds // 60



time = Time(300)
print(f"{time.minutes()} minutes")

