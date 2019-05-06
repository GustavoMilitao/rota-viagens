# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestFindRoute::test_with_required_parameter 1'] = {
    'price': 40.0,
    'route': [
        'GRU',
        'BRC',
        'SCL',
        'ORL',
        'CDG'
    ]
}

snapshots['TestFindRoute::test_with_all_parameter 1'] = {
    'price': 40.0,
    'route': [
        'GRU',
        'BRC',
        'SCL',
        'ORL',
        'CDG'
    ]
}
