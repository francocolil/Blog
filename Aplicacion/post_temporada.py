from flask import Flask, render_template, request, redirect, g, session, url_for, Blueprint, flash

from .models import User, Post_Temporadas

from Aplicacion import db


bp = Blueprint("posttemporada", __name__, url_prefix="/post-temporada")