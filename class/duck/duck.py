class Duck:
    def quack(self):
        print("这鸭子正在嘎嘎叫")

    def feathers(self):
        print("这鸭子拥有白色和灰色的羽毛")


class Person:
    def quack(self):
        print("这人正在模仿鸭子")

    def feathers(self):
        print("这人在地上拿起1根羽毛然后给其他人看")


def in_the_forest(duck):
    duck.quack()
    duck.feathers()


def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)


game()
