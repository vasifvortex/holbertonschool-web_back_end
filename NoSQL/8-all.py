#!/usr/bin/env python3
"""Listing all documents in a collection"""


def list_all(mongo_collection):
    """Listing all documents in a collection"""
    all = mongo_collection.find()
    
    if (len(list(all)) > 0):
        return all
    return []
