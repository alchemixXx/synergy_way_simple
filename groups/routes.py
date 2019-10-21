from flask import Blueprint, flash, redirect, render_template, url_for, request

from db import db
from groups.forms import NewGroupForm, UpdateGroupForm
from models import Group, User

groups = Blueprint('groups', __name__)
title = "Groups page"


@groups.route('/groups')
def all_groups():
    page = request.args.get('page', 1, type=int)
    groups_list = Group.query.order_by(Group.id).paginate(page=page, per_page=4)
    return render_template('groups.html', title=title, groups_list=groups_list)


@groups.route('/add_group', methods=['GET', 'POST'])
def add_new_group():
    form = NewGroupForm()
    if form.validate_on_submit():
        user = Group(name=form.name.data,
                     description=form.description.data,
                     )
        flash('Group created successfully', 'success')
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('groups.all_groups'))
    return render_template('add_group.html', form=form, title=title)


@groups.route('/change_group/<int:group_id>', methods=['GET', 'POST'])
def change_group(group_id):
    changed_group = Group.query.get_or_404(group_id)
    form = UpdateGroupForm()
    if form.validate_on_submit():
        changed_group.name = form.name.data
        changed_group.description = form.description.data
        db.session.commit()
        flash('Group updated successfully', 'success')
        return redirect(url_for('groups.all_groups'))
    elif request.method == "GET":
        form.name.data = changed_group.name
        form.description.data = changed_group.description
    return render_template('change_group.html', form=form, title=title)


@groups.route('/delete_group/<int:group_id>')
def delete_group(group_id):
    group_to_delete = Group.query.get_or_404(group_id)
    users_in_group = User.query.filter(User.group_id == group_id).first()
    if not users_in_group:
        db.session.delete(group_to_delete)
        db.session.commit()
    else:
        flash('Group can not be deleted while some user still there', 'warning')
    return redirect(url_for('groups.all_groups'))
