from flask import Blueprint, request
from flask import render_template, flash, redirect, url_for

from db import db
from forms import NewUserForm, UpdateUserForm
from models import User

users = Blueprint('users', __name__)

title = "Users page"


@users.route('/')
def user_page():
    page = request.args.get('page', 1, type=int)
    all_users = User.query.order_by(User.id).paginate(page=page, per_page=4)
    return render_template('users.html', user_list=all_users)


@users.route('/add_user', methods=['GET', 'POST'])
def add_new_user():
    form = NewUserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    group_id=form.group.data.id,
                    group=form.group.data.name,
                    )
        db.session.add(user)
        db.session.commit()
        flash('User created successfully', 'success')
        return redirect(url_for('users.user_page'))
    return render_template('add_user.html', form=form, title=title)


@users.route('/change_user/<int:user_id>', methods=['GET', 'POST'])
def change_user(user_id):
    changed_user = User.query.get_or_404(user_id)
    form = UpdateUserForm()
    if form.validate_on_submit():
        changed_user.username = form.username.data
        changed_user.group_id = form.group.data.id
        changed_user.group = form.group.data.name
        db.session.commit()
        flash('User updated successfully', 'success')
        return redirect(url_for('users.user_page'))
    elif request.method == "GET":
        form.username.data = changed_user.username
        form.group.data = changed_user.group_id
    return render_template('chage_user.html', form=form, title=title)


@users.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user_to_delete = User.query.get_or_404(user_id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect(url_for('users.user_page'))
