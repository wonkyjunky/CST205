class MyNote:
    def __init__(self, name, frequency, duration):
        self.name = name
        self.frequency = frequency
        self.duration = duration

    # redefine greater than operator (>)
    def __gt__(self, note2):
        return self.frequency > note2.frequency

first_note = MyNote('A', 440.0, 2)

second_note = MyNote('C', 246.9, 3)

print(second_note > first_note)