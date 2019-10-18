from flask import Blueprint, request
from flask import render_template, flash, redirect, url_for
from flask_paginate import Pagination, get_page_args

from forms import NewUserForm, UpdateUserForm, SearchAndSortForm
from utils import get_all_courses, get_filtered_by_id_users, get_all_users, get_users, add_user, delete_user_by_id, \
    get_filtered_by_name_users

users = Blueprint('users', __name__)

title = "Users page"