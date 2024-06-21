'''from flask import render_template, Blueprint, request
from demo import get_db_connection


admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/')
def admin():
    title = request.form.get('title')
    content = request.form.get('content')
    media = request.form.get('media')
    category = request.form.get('category')
    author = request.form.get('author')
    tags = request.form.get('tags')


    conn = get_db_connection()
    cursor = conn.cursor()

    sql_statement = 'INSERT INTO ARTICLES (title, content) VALUES (%s, %s)'

    cursor.execute(sql_statement, (title, content))



    return render_template('admin.html')
'''