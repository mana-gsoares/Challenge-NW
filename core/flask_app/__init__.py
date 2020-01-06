#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Inicio app.'''
import os

from flask import Flask

app = Flask(__name__)
# Carregando config das classes.
configurations = {
    'development': 'flask_app.config.DefaultConfig',
    'production': 'flask_app.config.ProductionConfig',
}
app.config.from_object(configurations[os.getenv('FLASK_ENV')])

import flask_app.views
