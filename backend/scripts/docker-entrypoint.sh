#!/bin/bash

gunicorn FitnessCentre.wsgi -b 0.0.0.0:8000