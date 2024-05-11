#!/usr/bin/env python3
"""Documentation"""


def schools_by_topic(mongo_collection, topic):
    """Documentation"""
    return mongo_collection.find(
        {"topics": topic}
        )
