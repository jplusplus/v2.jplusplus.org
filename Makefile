# Project : Journalism++ v2
# -----------------------------------------------------------------------------
# Author : Edouard Richard                                  <edou4rd@gmail.com>
# -----------------------------------------------------------------------------
# License : GNU General Public License
# -----------------------------------------------------------------------------

PYC        = $(wildcard *.pyc */*.pyc sources/*/*.pyc sources/*/*/*.pyc sources/*/*/*/*.pyc sources/*/*/*/*/*.pyc)
CACHE      = $(wildcard staticfiles/CACHE)
RM         = rm -fr
VENV       = `pwd`/.env
VIRTUALENV = virtualenv
PIP        = pip
PYTHON     = python

run: clean
	. `pwd`/.env ; $(PYTHON) manage.py runserver

clean:
	$(RM) $(PYC)
	$(RM) $(CACHE)

install: install_dependances init_db

install_dependances:
	$(VIRTUALENV) venv --no-site-packages --distribute --prompt=jppv2
	. $(VENV) ; $(PIP) install -r requirements_core.txt

dump_data:
	. $(VENV) ; $(PYTHON) manage.py dumpdata cms djangocms_style taggit djangocms_column djangocms_text_ckeditor djangocms_file djangocms_flash djangocms_googlemap djangocms_inherit djangocms_link djangocms_picture djangocms_teaser djangocms_video jplusplus --indent 4 --natural > sources/jplusplus/fixtures/initial_data.json

init_db:
	. $(VENV) ; $(PYTHON) manage.py syncdb
	. $(VENV) ; $(PYTHON) manage.py migrate

update_i18n:
	. $(VENV) ; django-admin.py makemessages -a -i "venv/*"

compile_i18n:
	. $(VENV) ; django-admin.py compilemessages

clone_db:
	heroku run python manage.py dumpdata --indent=2 --format=json --app jplusplus2 > /tmp/jpp_initial_data.json.tmp
	sed '1d' /tmp/jpp_initial_data.json.tmp > /tmp/jpp_initial_data.json
	make init_db
	. $(VENV) ; $(PYTHON) manage.py loaddata /tmp/jpp_initial_data.json

# EOF
