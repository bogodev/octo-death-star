from django.core.management.base import BaseCommand, CommandError
from apps.data.models import SensorData
import requests
import time
from threading import Thread
from optparse import make_option

class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--fake',
            action='store_true',
            dest='fake',
            default=False,
            help=''),
        make_option('--threaded',
            action='store_true',
            dest='threaded',
            default=True,
            help=''),
        make_option('--url',
            action='store',
            dest='url',
            default='http://50.23.68.34:3000/?star=felipe',
            help=''),
        make_option('--clean',
            action='store_true',
            dest='clean',
            default=False,
            help=''),
        )

    def handle(self, *args, **options):

        fake = options['fake']
        threaded = options['threaded']
        url = options['url']
        clean = options['clean']

        if clean:
            SensorData.objects.all().delete()

        def infinite_loop():
            while(True):
                self.do_action(fake, url)
                time.sleep(0.8)

        if threaded:
            infinite_loop()
        else:
            self.do_action(fake, url)


    def do_action(self, fake, url):
        if fake:
            stamp, record = Command.parse_string(Command.get_fake_url())
        else:
            stamp, record = Command.parse_string(Command.get_real_url(url))

        data_object, created = SensorData.objects.get_or_create(stamp=stamp)

        data_object.data_line = record
        data_object.save()

        self.stdout.write('Successfully fetched stamp "%s"' % data_object.stamp)

    @staticmethod
    def get_fake_url():
        return "6564;O,11323,15626,26158;C,-4730,-12648,-9367;O,25899,1710,25899;O,38848,2394,27193;O,2071,3210,2071;O,38848,1881,27193;O,38848,2565,27193;O,38848,1419,33668;O,38848,872,18906;O,37248,2582,18906;O,62157,6002,21496;O,21416,6002,21496;O,14563,6002,21496;O,14563,4963,21496;O,14563,4963,16211;O,7613,-4347,12376;O,-2205,15009,892;O,-25190,11455,141"

    @staticmethod
    def get_real_url(url):
        print "trying : " + url
        r = requests.get(url)
        return r.text.encode('utf-8')

    @staticmethod
    def parse_string(data):
        split = data.split(';', 1)
        index = split[0]
        value = split[1].rstrip("\r\n")

        return index, value
