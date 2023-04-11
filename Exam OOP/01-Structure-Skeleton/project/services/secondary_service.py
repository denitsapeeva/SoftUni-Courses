from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def details(self):
        if not self.robots:
            return f"{self.name} Main Service:\nRobots: none"
        robots_name = []
        for robot in self.robots:
            robots_name.append(robot.name)
        return f"{self.name} Main Service:\nRobots: {' '.join(robots_name)}"