#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Views.'''
from flask import render_template, request, send_from_directory

from . import app


@app.route('/')
def root():
    '''Main.'''
    return render_template('index.html')

@app.route('/robots.txt')
def static_from_root():
    '''Serve robots.txt file.'''
    return send_from_directory(app.static_folder, request.path[1:])


@app.errorhandler(404)
def error_404(error):
    '''404 error handling.'''
    return render_template('404.html', error=error)
