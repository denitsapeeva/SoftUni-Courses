from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type == "MainService":
            service = MainService(name)
            self.services.append(service)
            return f"{service_type} is successfully added."
        elif service_type == "SecondaryService":
            service = SecondaryService(name)
            self.services.append(service)
            return f"{service_type} is successfully added."
        raise Exception("Invalid service type!")

    def add_robot(self, robot_type, name, kind, price):
        if robot_type == "MaleRobot":
            robot = MaleRobot(name, kind, price)
            self.robots.append(robot)
            return f"{robot_type} is successfully added."
        elif robot_type == "FemaleRobot":
            robot = FemaleRobot(name, kind, price)
            self.robots.append(robot)
            return f"{robot_type} is successfully added."
        raise Exception("Invalid robot type!")

    def add_robot_to_service(self, robot_name, service_name):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]
        if robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "SecondaryService":
            if len(service.robots) == service.capacity:
                raise Exception("Not enough capacity for this robot!")
            else:
                self.robots.remove(robot)
                service.robots.append(robot)
                return f"Successfully added {robot_name} to {service_name}."
        elif robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "MainService":
            if len(service.robots) == service.capacity:
                raise Exception("Not enough capacity for this robot!")
            else:
                self.robots.remove(robot)
                service.robots.append(robot)
                return f"Successfully added {robot_name} to {service_name}."
        else:
            return "Unsuitable service."

    def remove_robot_from_service(self, robot_name, service_name):
        service = [s for s in self.services if s.name == service_name][0]
        try:
            robot = next(filter(lambda r: r.name == robot_name, service.robots))
        except StopIteration:
            raise Exception("No such robot in this service!")
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name):
        service = [s for s in self.services if s.name == service_name][0]
        robots_fed = 0
        for robot in service.robots:
            robot.eating()
            robots_fed += 1
        return f"Robots fed: {robots_fed}."

    def service_price(self, service_name):
        service = [s for s in self.services if s.name == service_name][0]
        price = 0
        for robot in service.robots:
            price += robot.price
        return f"The value of service {service_name} is {price:.2f}."

    def __str__(self):
        if self.services:
            return "\n".join(s.details() for s in self.services)
        else:
            return None
