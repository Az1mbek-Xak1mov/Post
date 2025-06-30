from django.db.models import Model, CharField, URLField, DecimalField, TextChoices, TextField


class Comment(Model):
    class RatingChoices(TextChoices):
        YAXSHI = 'yaxshi', 'Yaxshi'
        ALO = 'alo', 'Alo'
        QONIQARLI = 'qoniqarli', 'Qoniqarli'

    book_name = CharField(max_length=255)
    rating = CharField(choices=RatingChoices, default=RatingChoices.YAXSHI)
    comment = TextField()
    name = CharField(max_length=255)
