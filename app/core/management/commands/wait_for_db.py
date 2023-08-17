"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as Pyscopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for the db to start"""

    def handle(self, *args, **kwargs):
        """Entry point for command"""
        self.stdout.write('[wait_for_db] Waiting'
                          'for database to start...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Pyscopg2Error, OperationalError):
                self.stdout.write('[wait_for_db] Database unavailable'
                                  ', waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('[wait_for_db]'
                                             ' Database available!'))
