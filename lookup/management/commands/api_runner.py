# -*- coding: utf-8 -*-
import json
import requests


from django.core.management.base import BaseCommand, CommandError

from lookup.models import Office


class Command(BaseCommand):
    # First page of Setting json url
    url = 'https://setting.io/api/spaces/?format=json'

    def handle(self, *args, **options):
        self.get_data()

    def get_data(self):
        response = requests.get(url)
        data = json.loads(response.text)

        """ I'm looking for data["results"][i]["title"] key to get title,
                            data["results"][i]["expose_url"] key to get url,
                            data["results"][i]["longtitude"] key to get longtitude,
                            data["results"][i]["latitude"] key to get latitude,
        """
