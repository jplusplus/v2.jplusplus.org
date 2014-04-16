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

dump_data:
	. `pwd`/.env ; python manage.py dumpdata cms auth djangocms_style djangocms_column djangocms_file djangocms_flash djangocms_googlemap djangocms_inherit djangocms_link djangocms_picture djangocms_teaser djangocms_video jplusplus --indent 4 > sources/jplusplus/fixtures/initial_data.json

init_db:
	. `pwd`/.env ; python manage.py syncdb
	. `pwd`/.env ; python manage.py migrate

# EOF
