import urllib2
import json


def num_active_mesos_tasks():
    """
    An example metric used by the relay.mesos demo to query mesos master
    for the number of currently running tasks.
    """
    while True:
        data = json.load(urllib2.urlopen(
            'http://localdocker:5050/master/state.json'))
        yield data['started_tasks'] + data['staged_tasks'] - (
            data['failed_tasks'] + data['killed_tasks']
            + data['lost_tasks'] + data['finished_tasks'])
