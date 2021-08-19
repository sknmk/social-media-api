from model_mommy import mommy

from django.db import transaction, IntegrityError
from django.test import TestCase as BaseTestCase


class TestCase(BaseTestCase):
    def make(self, class_name, **kwargs):
        return mommy.make(class_name, **kwargs)

    def prepare(self, class_name, **kwargs):
        return mommy.prepare(class_name, **kwargs)


def model_instance(ModelClass):
    def wrapper(func):
        def wraps(*args, **kwargs):
            _persisted = kwargs.pop('_persisted', True)

            data = func(args[0])
            data.update(kwargs)

            if not _persisted:
                return mommy.prepare(ModelClass, **data)

            try:

                with transaction.atomic():
                    return mommy.make(ModelClass, **data)

            except IntegrityError:
                filters = []
                unique_together = ModelClass._meta.unique_together

                unique_field_names = [
                    field.name for field in ModelClass._meta.fields
                    if field.name in data.keys()
                ]

                for field_name in unique_field_names:
                    filters = {
                        field_name: data[field_name]
                    }
                    instances = ModelClass.objects.filter(**filters)
                    if instances.exists():
                        return instances.first()

                if unique_together:
                    if set(unique_together).issubset(data.keys()):
                        filters.append({
                            field_name: data[field_name]
                            for field_name in ModelClass._meta.unique_together
                        })

                raise

        return wraps

    return wrapper
