# Full-stack web app

[![Feliciano](https://colorlib.com/wp/wp-content/uploads/sites/2/feliciano-free-template.jpg "Feliciano")](https://colorlib.com/wp/template/feliciano/ "Feliciano")


### Крок 1.

	git clone https://ole9@bitbucket.org/ole9/full-stack-web-app.git

Відкрийте в браузері [Get started with Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/ "Get started with Bootstrap").

Додайте необхідні компоненти:

[https://getbootstrap.com/docs/4.3/components/navbar/](https://getbootstrap.com/docs/4.3/components/navbar/ "https://getbootstrap.com/docs/4.3/components/navbar/")

[https://getbootstrap.com/docs/4.3/components/carousel/](https://getbootstrap.com/docs/4.3/components/carousel/ "https://getbootstrap.com/docs/4.3/components/carousel/")


### Крок 2.

	git checkout step-2

Розпакуйте архів `feliciano.zip`

### Крок 3.

	git checkout step-3

Створіть віртуальне середовище з ім'ям `myvenv`:

	python3 -m venv myvenv

> Більше деталей [https://tutorial.djangogirls.org/uk/django_installation/](https://tutorial.djangogirls.org/uk/django_installation/ "https://tutorial.djangogirls.org/uk/django_installation/")

Запустіть своє віртуальне середовище

	source myvenv/bin/activate

Встановіть потрібні залежності

	pip install -r requirements.txt

Створіть Django проект

	django-admin startproject mysite .

> не забудьте скопіювати крапку . в кінці

За необхідності налаштуйте базу даних у файлі `mysite/settings.py`

```python
	DATABASES = {
		'default': {
        	'ENGINE': 'django.db.backends.sqlite3',
        	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    	}
	}
```

Створіть базу даних

	python manage.py migrate

Запустіть проект

	python manage.py runserver

### Крок 4.

> Якщо у вас виникли труднощі на попередньому кроці виконайте в терміналі 
> 
> `git reset HEAD --hard && git clean -f -d && git checkout step-4`

Розпакуйте архів `feliciano.zip` якщо ви цього ще не зробили. Перегляньте розпакований вміст.

Створіть новий додаток у проекті Django:

	python manage.py startapp cafe

Відредагуйте файл `mysite/settings.py`. Знайдіть `INSTALLED_APPS` та додайте рядок `'cafe',`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cafe',
]
```

Відкрийте файл `mysite/urls.py` та додайте вгорі сторінки:

	from cafe import views as cafe_views

та до `urlpatterns`:

	path('', cafe_views.home, name='home'),

Тобто файл має виглядати:

```python
from django.contrib import admin
from django.urls import path
from cafe import views as cafe_views

urlpatterns = [
    path('', cafe_views.home, name='home'),
    path('admin/', admin.site.urls),
]
```

Далі відредагуйте файл `cafe/views.py` наступним чином:

```python
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<p>This is Home view</p>")
```

Запустіть проект `python manage.py runserver` та перевірте результат.

Змініть функцію `home` у файлі `cafe/views.py` до:

```python
def home(request):
    return render(request, 'cafe/home.html', {})  
```

Створфть у папці `cafe` нову папку `templates` і в цій папці знову папку `cafe` (це не помилка).

Скопіюйте у папку `cafe/templates/cafe`  файл `index.html` (з архіву) та переназвіть його на `home.html`

Створіть директорію `static` всередині додатку `cafe`:

	full-stack-web-app
	├─ cafe
	│   ├── migrations
	│   ├── static
	│   └── templates
	└── mysite

Скопіюйте в папку `static` з архіву папки `css`, `js`, `images`, `fonts`.

У файлі `home.html` поміняйте `url` для всіх статичних файлів:

	css/style.css   ->  static/css/style.css
	js/main.js   ->   /static/js/main.js
	images/bg_1.jpg   ->    /static/images/bg_1.jpg

Перезавантажте сервер (`Ctrl + C` а потім `python manage.py runserver`)"# full-stack-web-app" 
