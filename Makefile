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
	. `pwd`/.env ; pip install -r requirements_core.txt

dump_data:
	. `pwd`/.env ; python manage.py dumpdata cms djangocms_style taggit djangocms_column djangocms_text_ckeditor djangocms_file djangocms_flash djangocms_googlemap djangocms_inherit djangocms_link djangocms_picture djangocms_teaser djangocms_video jplusplus --indent 4 --natural > sources/jplusplus/fixtures/initial_data.json

init_db:
	. `pwd`/.env ; python manage.py syncdb
	. `pwd`/.env ; python manage.py migrate

# EOF
