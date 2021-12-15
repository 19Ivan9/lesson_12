class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open('logs.txt', 'w') as file:
            file.write(self.msg)

