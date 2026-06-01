from app.people.customer import Customer
from app.people.cinema_staff import Cleaner
from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall


def cinema_visit(movie, customers, hall_number, cleaner):
    customer_objects = []
    for customer_dict in customers:
        c = Customer(customer_dict["name"], customer_dict["food"])
        customer_objects.append(c)

    for c in customer_objects:
        CinemaBar.sell_product(c, c.food)

    hall = CinemaHall(hall_number)

    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(movie, customer_objects, cleaner_obj)


