# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.db.utils import OperationalError
import sqlite3


class ProgramMethodTests(TestCase):

    def test_connect_to_bd(self):
        try:
            conn = sqlite3.connect('programa.db')
            c = conn.cursor()
        except OperationalError:
            connected = False
        else:
            connected = True

        self.assertEqual(connected, True)

    def test_dia_from_program_notNone(self):
        conn = sqlite3.connect('programa.db')
        c = conn.cursor()

        for row in c.execute('SELECT DIA FROM PROGRAMA'):
            self.assertIsNotNone(row)

    def test_fecha_from_program_notNone(self):
        conn = sqlite3.connect('programa.db')
        c = conn.cursor()

        for row in c.execute('SELECT FECHA FROM PROGRAMA'):
            self.assertIsNotNone(row)

    def test_horaFin_from_program_notNone(self):
        conn = sqlite3.connect('programa.db')
        c = conn.cursor()

        for row in c.execute('SELECT HORA_FIN FROM PROGRAMA'):
            self.assertIsNotNone(row)

    def test_sessionCode_from_charla_notNone(self):
        conn = sqlite3.connect('programa.db')
        c = conn.cursor()

        for row in c.execute('SELECT SESSIONCODE FROM CHARLAS'):
            self.assertIsNotNone(row)

    def test_evento_from_charla_notNone(self):
        conn = sqlite3.connect('programa.db')
        c = conn.cursor()

        for row in c.execute('SELECT EVENTO FROM CHARLAS'):
            self.assertIsNotNone(row)

    def test_titulo_from_charla_notNone(self):
        conn = sqlite3.connect('programa.db')
        c = conn.cursor()

        for row in c.execute('SELECT TITULO FROM CHARLAS'):
            self.assertIsNotNone(row)

    def test_ponentes_from_charla_notNone(self):
        conn = sqlite3.connect('programa.db')
        c = conn.cursor()

        for row in c.execute('SELECT PONENTES FROM CHARLAS'):
            self.assertIsNotNone(row)
