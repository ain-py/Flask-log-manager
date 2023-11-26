from app import db
from sqlalchemy import Index, text
class LogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    resourceId = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    traceId = db.Column(db.String(50), nullable=True)
    spanId = db.Column(db.String(50), nullable=True)
    commit = db.Column(db.String(20), nullable=True)
    parentResourceId = db.Column(db.String(50), nullable=True)
    message_index = Index('idx_message_gin_trgm', 'message', postgresql_ops={'message': 'gin_trgm_ops'})
    level_index = Index('idx_level_gin_trgm', 'level', postgresql_ops={'level': 'gin_trgm_ops'})
    resourceId_index = Index('idx_resourceId_gin_trgm', 'resourceId', postgresql_ops={'resourceId': 'gin_trgm_ops'})
    traceId_index = Index('idx_traceId_gin_trgm', 'traceId', postgresql_ops={'traceId': 'gin_trgm_ops'})
    spanId_index = Index('idx_spanId_gin_trgm', 'spanId', postgresql_ops={'spanId': 'gin_trgm_ops'})
    commit_index = Index('idx_commit_gin_trgm', 'commit', postgresql_ops={'commit': 'gin_trgm_ops'})
    parentResourceId_index = Index('idx_parentResourceId_gin_trgm', 'parentResourceId', postgresql_ops={'parentResourceId': 'gin_trgm_ops'})
    
