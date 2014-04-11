# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : GNU General Public License
# -----------------------------------------------------------------------------

run:
	. `pwd`/.env ; python manage.py runserver

install: install_dependances init_db

install_dependances:
	virtualenv venv --no-site-packages --distribute --prompt=jppv2
	. `pwd`/.env ; pip install -r requirements.txt

init_db:
	. `pwd`/.env ; python manage.py syncdb
	. `pwd`/.env ; python manage.py migrate

# EOF
