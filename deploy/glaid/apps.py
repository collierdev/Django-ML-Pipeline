from django.apps import AppConfig
import html
import pathlib
import os

from fast_bert.prediction import BertClassificationPredictor

class GlaidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'glaid'
