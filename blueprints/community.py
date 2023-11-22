from flask import Blueprint, render_template, request, redirect, session

from static import styles

@app.route('/create_community')
def create_community():
    return render_template('create_community.html')