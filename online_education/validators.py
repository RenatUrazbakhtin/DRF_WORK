import re

from rest_framework.exceptions import ValidationError


class URLValidator:
    youtube = "youtube.com"
    def __call__(self, value):
        if self.youtube not in value:
            raise ValidationError('You cant use such url')