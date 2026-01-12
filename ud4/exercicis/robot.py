class Robot:
    def __init__(self, x=0.0, y=0.0, speed=0.0):
        self.x = x
        self.y = y
        self.__set_speed(speed)
    
    def __set_speed(self, speed):
        if speed < 0:
            self.speed = 0.0
        elif speed > 10:
            self.speed = 10.0
        else:
            self.speed = speed

    def __str__(self):
        return f'Robot(x={self.x},y={self.y},speed={self.speed})'

    def accelerate(self):
        self.__set_speed(self.speed + 0.5)

    def decelerate(self):
        self.__set_speed(self.speed - 0.5)

    def up(self):
        self.y += self.speed

    def down(self):
        self.y -= self.speed

    def right(self):
        self.x += self.speed

    def left(self):
        self.x -= self.speed


if __name__ == '__main__':
    r = Robot(speed=0)
    print(r)

    r.up()
    print("UP", r)

    r.accelerate()
    print("ACCELERATE", r)

    r.up()
    print("UP", r)

    for i in range(20):
        r.accelerate()
        print("ACCELERATE", r)

    r.left()
    print("LEFT", r)