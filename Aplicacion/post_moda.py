from flask import Flask, render_template, request, redirect, g, session, url_for, Blueprint, flash

from .models import User, Post_Moda

from Aplicacion import db


bp = Blueprint("postmoda", __name__, url_prefix="/post-moda")