
import os
from behave import *

CURRENT_FOLDER = os.getcwd()

def after_scenario(context, scenario):
    os.chdir(CURRENT_FOLDER)
