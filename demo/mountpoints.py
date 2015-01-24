from .views.frontend import frontend
from .views.backend import backend


__author__ = 'xuemingli'


MOUNT_POINTS = (
    (frontend, ''),
    (backend, '/admin')
)