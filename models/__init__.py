#!/usr/bin/python3
"""Here, is for __init__ magic method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
