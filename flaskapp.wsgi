  GNU nano 7.2                                                          flaskapp.wsgi
import sys
sys.path.insert(0,'/var/www/html/flaskapp')

from flaskapp import app as application

