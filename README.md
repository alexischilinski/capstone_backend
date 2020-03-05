# OnTrack

This app was created for runners by a runner. It is meant to help runners keep themselves accountable and track their progress while training for a race.

## Deployment

This app is deployed on Heroku: https://capstone-ontrack.herokuapp.com/

## Getting Started

This is the backend for the project, and it is built in Python/Django. Fork and clone this repo to get started. It also utilizes a PostgreSQL database. It is paired with the frontend repo (https://github.com/alexiscait142/capstone_frontend).

### Prerequisites

In order to successfully run this app, you will need some version of Python 3, and a version of Django that is at least 3.0.3 or higher. Please see **Pipfile.lock** for all versions.
You will also need to have pip3 installed (and pipenv) so you can access the virtual environment.
#### Required packages
Enter the virtual environment within the project director (`pipenv shell`) and run `pip install` for these packages:

```
djangorestframework
```
```
django-cors-headers
```
```
psycopg2
```
```
psycopg2-binary
```
```
django-rest-knox
```
```
gunicorn
```

### Installing

Once you have forked and cloned this repo and installed the proper packages, run `PGGSSENCMODE=disable python manage.py migrate` and `PGGSSENCMODE=disable python manage.py seed` to complete the database.
Assuming everything was successful, you can then run `PGGSSENCMODE=disable python manage.py runserver` to start the server. Check localhost:8000 for success.

## References

* [All About Marathon Training](https://www.all-about-marathon-training.com/half-marathon-training-summer.html) - Half Marathon Training Schedule
* [Shape.com](https://www.shape.com/fitness/training-plans/beginners-guide-running-5k) - 5k Training Schedule
* [How to Run Guide](https://howtorunguide.com/10k-training-schedule-for-beginners/) - 10k Training Schedule
* [Mississippi Gulf Coast Marathon](https://mississippigulfcoastmarathon.com/wp-content/uploads/2018/07/training_full.pdf) - Full Marathon Training Schedule
* [Runner's World](https://www.runnersworld.com/training/a20813186/eight-benefits-of-cross-training/) - Eight Benefits of Crosstraining
* [Runner's World](https://www.runnersworld.com/health-injuries/a20864022/why-rest-days-are-important/) - Why Rest Days are Important
* [OPTP](https://www.optp.com/blog/How-to-Choose-a-Foam-Roller) - How to Choose a Foam Roller
* [Runner's World](https://www.runnersworld.com/training/a24843120/resistance-band-exercises/) - Resistance Band Exercises
* [Business Insider](https://www.businessinsider.com/north-american-healthcare-foot-rocker-2017-2) - Foot Rocker
* [Runner's World](https://www.runnersworld.com/health-injuries/a19578652/plantar-fasciitis/) - Plantar Fasciitis
* [Runner's World](https://www.runnersworld.com/uk/health/injury/a775743/5-things-you-need-to-know-about-your-it-band/) - IT Band
* [Runner's World](https://www.runnersworld.com/uk/health/a760484/the-rw-complete-guide-to-stretching-for-runners/) - Stretching for Runners
* [Active.com](https://www.active.com/running/articles/14-running-specific-strength-training-exercises/) - Strength Training for Runners
* [Runner's World](https://www.runnersworld.com/gear/a20842305/how-to-buy-the-right-running-shoes/) - How to Choose the Right Running Shoes

## Authors

* **Alexis Chilinski** - [GitHub Profile](https://github.com/alexiscait142)

## Acknowledgments

* Flatiron School
* [Traversy Media](https://www.youtube.com/playlist?list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60)
