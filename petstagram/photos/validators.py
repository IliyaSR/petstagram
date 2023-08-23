from django.core.exceptions import ValidationError


def image_max_size(value):
    if value.size <= 5 * 1024 * 1024:
        pass
    else:
        raise ValidationError('The maximum file size that can be uploaded is 5MB')
