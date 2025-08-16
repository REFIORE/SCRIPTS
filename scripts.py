from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
import random

schoolkid = Schoolkid.objects.filter(full_name__contains='Фролов Иван').first()
praise_for_kid = [
    'Молодец!'
    'Отлично!'
    'Хорошо!'
    'Гораздо лучше, чем я ожидал!'
    'Ты меня приятно удивил!'
    'Великолепно!'
    'Прекрасно!'
    'Ты меня очень обрадовал!'
    'Именно этого я давно ждал от тебя!'
    'Сказано здорово – просто и ясно!'
    'Ты, как всегда, точен!'
    'Очень хороший ответ!'
    'Талантливо!'
    'Ты сегодня прыгнул выше головы!'
    'Я поражен!'
    'Уже существенно лучше!'
    'Потрясающе!'
    'Замечательно!'
    'Прекрасное начало!'
    'Так держать!'
    'Ты на верном пути!'
    'Здорово!'
    'Это как раз то, что нужно!'
    'Я тобой горжусь!'
    'С каждым разом у тебя получается всё лучше!'
    'Мы с тобой не зря поработали!'
    'Я вижу, как ты стараешься!'
    'Ты растешь над собой!'
    'Ты многое сделал, я это вижу!'
    'Теперь у тебя точно все получится!'
]


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid):
    praise = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title__contains='Музыка').order_by('-date')
    laud = praise.first()
    Commendation.objects.create(text=random.choice(praise_for_kid), created=laud.date, schoolkid=schoolkid, subject=laud.subject, teacher=laud.teacher)
