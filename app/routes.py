# app/routes.py
from datetime import datetime
import json
from sqlalchemy import or_, and_
from flask import render_template, request, flash, redirect, url_for
from app import  app,db
from app.models import LogEntry
from sqlalchemy.exc import SQLAlchemyError
from elasticsearch import Elasticsearch

def parse_log(log_data):
    # Parse the JSON log data and return a dictionary
    try:
        log_dict = json.loads(log_data)
        return log_dict
    except json.JSONDecodeError:
        flash('Invalid log format', 'error')
        return None
    
@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    logs : list[LogEntry]  = LogEntry.query.paginate(page=page, per_page=per_page, error_out=False)
   
    return render_template('index.html', logs=logs)

@app.route('/add_log', methods=['POST'])
def add_log():
    log_data = request.form.get('log_data')
    print(log_data)
    log_dict = parse_log(log_data)
   
    if log_dict:
        # Create a LogEntry object and add it to the database
        log_entry = LogEntry(
            level=log_dict['level'],
            message=log_dict['message'],
            resourceId=log_dict['resourceId'],
            timestamp=datetime.strptime(log_dict['timestamp'], '%Y-%m-%dT%H:%M:%SZ'),
            traceId=log_dict.get('traceId'),
            spanId=log_dict.get('spanId'),
            commit=log_dict.get('commit'),
            parentResourceId=log_dict['metadata'].get('parentResourceId')
        )
        try:
            db.session.add(log_entry)
            db.session.commit()
            flash('Log entry added successfully', 'success')
            return "success"
        except SQLAlchemyError as e:
            error = str(e.__dict__.get('orig') or e)
            return f"Error: {error}"
    return "Error: Invalid log format"

@app.route('/search', methods=['GET', 'POST'])
def search():
    page = request.args.get('page', 1, type=int)
    per_page = 30
    if request.method == 'POST':
        # Full-text search
        query = request.form.get('query')
        full_text_results = LogEntry.query.filter(or_(
            LogEntry.level.ilike(f"%{query}%"),
            LogEntry.message.ilike(f"%{query}%"),
            LogEntry.resourceId.ilike(f"%{query}%"),
            LogEntry.traceId.ilike(f"%{query}%"),
            LogEntry.spanId.ilike(f"%{query}%"),
            LogEntry.commit.ilike(f"%{query}%"),
            LogEntry.parentResourceId.ilike(f"%{query}%")
        )).paginate(page=page, per_page=per_page, error_out=False)

        # Additional filters
        level = request.form.get('level')
        message = request.form.get('message')
        resourceId = request.form.get('resourceId')
        timestamp_start = request.form.get('timestamp_start')
        timestamp_end = request.form.get('timestamp_end')
        traceId = request.form.get('traceId')
        spanId = request.form.get('spanId')
        commit = request.form.get('commit')
        parentResourceId = request.form.get('parentResourceId')

        # Build the filter conditions
        filters = []
        if level and level != '':
            filters.append(LogEntry.level == level)
        if message and message != '':
            filters.append(LogEntry.message == message)
        if resourceId and resourceId != '':
            filters.append(LogEntry.resourceId == resourceId)
        if traceId and traceId != '':
            filters.append(LogEntry.traceId == traceId)
        if spanId and spanId != '':
            filters.append(LogEntry.spanId == spanId)
        if commit and commit != '':
            filters.append(LogEntry.commit == commit)
        if parentResourceId and parentResourceId != '':
            filters.append(LogEntry.parentResourceId == parentResourceId)

        # Date range filter
        if timestamp_start and timestamp_end:
            filters.append(LogEntry.timestamp.between(timestamp_start, timestamp_end))
           
        # Combine multiple filters
        if filters:
            query_result = LogEntry.query.filter(and_(*filters)).paginate(page=page, per_page=per_page, error_out=False)
            full_text_results=None
        else:
            query_result = []
        

        return render_template('search.html', query_result=query_result, full_text_results=full_text_results,postFilters=request.form)

    return render_template('search.html',postFilters=request.form)