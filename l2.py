import abc

class Team_name():
    def __init__(self):
        print("Your team has been created")

    def method(self):
        print("Team_name: 'Savage'")



class Team_member(abc.ABC):
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


    @abc.abstractmethod
    def position(self):
        pass

    def get_name(self):
        print("Имя: ", self.name, "Фамилия: ", self.surname)

class Team(Team_name):
    def __init__(self) -> str:
        Team_name.__init__(self)

    def method(self):
        super().method()





class Member_name():
    def __init__(self, nickname: str):
        self._nickname = nickname



    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, nickname: str):
         self._nickname = nickname



class Member(Team_member):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def position(self):
        return ' '





class Role:
    @staticmethod
    def print_role():
        print("Стрелок")

Captain = Team()
Player = Member_name("Moonlight")
Name_of_member = Member("Андрей", "Заец")
Name_of_member.get_name()
Captain.method()


print(Player.nickname)
Role.print_role()



