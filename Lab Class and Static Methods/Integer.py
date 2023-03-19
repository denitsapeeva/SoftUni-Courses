class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        int_value = int(float_value)
        return cls(int_value)

    @classmethod
    def from_roman(cls, value: str):
        room_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_value = 0
        for i in range(len(value)):
            if i != 0 and room_value[value[i]] > room_value[value[i - 1]]:
                int_value += room_value[value[i]] - 2 * room_value[value[i - 1]]
            else:
                int_value += room_value[value[i]]

        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))
