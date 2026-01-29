from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie, customers, hall_number, cleaner):
    # Create Customer instances
    customer_objects = [
        Customer(name=customer["name"], food=customer["food"])
        for customer in customers
    ]

    # Sell food to customers
    for customer in customer_objects:
        CinemaBar.sell_product(product=customer.food, customer=customer)

    # Create cinema hall and cleaner
    hall = CinemaHall(hall_number=hall_number)
    cleaning_staff = Cleaner(name=cleaner)

    # Start movie session
    hall.movie_session(
        movie_name=movie,
        customers=customer_objects,
        cleaning_staff=cleaning_staff
    )
