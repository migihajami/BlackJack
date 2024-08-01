import json


class Statistics:
    filename: str
    stats: dict

    def __init__(self):
        self.filename = "stats.json"
        self.load()

    def load(self):
        try:
            file = open(self.filename, "r")
        except OSError:
            self.stats = {"wins": 0, "looses": 0, "pushes": 0}
            return

        with file:
            data = file.read()
            self.stats = json.loads(data)

    def save(self):
        with open(self.filename, "w") as file:
            data = json.dumps(self.stats)
            file.write(data)

    def win(self):
        self.stats["wins"] += 1
        self.save()

    def loose(self):
        self.stats["looses"] += 1
        self.save()

    def push(self):
        self.stats["pushes"] += 1
        self.save()

    def __str__(self):
        return f"{self.stats["wins"]} wins, {self.stats["looses"]} looses, {self.stats["pushes"]} pushes."
