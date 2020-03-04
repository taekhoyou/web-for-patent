# index.py

from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
import pandas as pd
import networkx as nx

main = Blueprint('main',__name__,url_prefix='/')

@main.route('/main',methods=['GET'])
def index():
	testdata = 'testdata array'

	return render_template('/main/index.html', testDataHtml = testdata)
