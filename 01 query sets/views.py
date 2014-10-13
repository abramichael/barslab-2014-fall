from django.db.models import F, Q
from django.http import HttpResponse
from university.models import *

def q(request):
    #h = Lesson.objects.filter(year__gte=1980)
    #h = Lesson.objects.exclude(year__gte=1980)

    #h = Lesson.objects.filter(teacher__school__name='Hogwarts')

    #h = Team.objects.filter(scored__gte=F('missed'))

    #h = Lesson.objects.select_related()

    #query = Q(student__name='Jean') | \
    #            Q(teacher__name='Severus Snape')

    #h = Lesson.objects.filter(query)

    h = Lesson.objects.raw("select * from university_teacher")

    return HttpResponse("<br>".join(
            [str(obj) for obj in h]
        )
    )

