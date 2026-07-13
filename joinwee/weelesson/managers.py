from django.db.models import Manager
from django.db.models.query import QuerySet

class LessonQuerySet(QuerySet):
    def draft(self):
        return self.filter(is_draft=True)

    def fine(self):
        return self.filter(is_fine=True)

    def published(self):
        return self.filter(is_draft=False)

class LessonManager(Manager):
    def get_query_set(self):
        return LessonQuerySet(self.model, using=self._db)

    def draft(self):
        return self.get_query_set().draft()

    def published(self):
        return self.get_query_set().published()

    def fine(self):
        return self.get_query_set().fine()
    
