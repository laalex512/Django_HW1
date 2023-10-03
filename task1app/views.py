import logging
from django.shortcuts import render
from django.http import HttpResponse

from task1app.functions import import_count


logger_main = logging.getLogger('visits_main')
logger_about = logging.getLogger('visits_about')
visits_main = import_count('./task1app/log/visits_main.log')
visits_about = import_count('./task1app/log/visits_about.log')



def main(request):
    global visits_main
    response = '<h1>Main</h1><img src="./task1app/img/main.jpg" alt="image_main"><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eos voluptatum cumque, delectus molestiae voluptatibus debitis sit quod distinctio deleniti nemo doloremque repellendus quasi aspernatur esse commodi beatae sint neque deserunt?</p>'
    visits_main += 1
    logger_main.info(f'visits to main - {visits_main}')
    return HttpResponse(response)


def about(request):
    global visits_about
    response = '<h1>About</h1><img src="./task1app/img/about.jpg" alt="image_about"><p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eos voluptatum cumque, delectus molestiae voluptatibus debitis sit quod distinctio deleniti nemo doloremque repellendus quasi aspernatur esse commodi beatae sint neque deserunt?</p>'
    visits_about += 1
    logger_about.info(f'visits to about - {visits_about}')
    return HttpResponse(response)