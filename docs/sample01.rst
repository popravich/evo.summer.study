Пример #1. Структура проекта
============================

Простая структура
-----------------

Пример структурирования проекта:

.. code-block:: bash

   /requirements.txt # основные зависимости проекта
   /requirements-dev.txt # инструменты разработки
   /setup.py         # если ваш проект необходимо устанавливать в виде модуля.

   /sample01         # директория исходников проекта.
      /templates     # html-шаблоны проекта
      /__init__.py
      /__main__.py
      /main.py
      /db.py
      /config.py
      /views.py
   /frontend         # исходный код браузерной части проекта
                     # js/coffee/sass/less/etc
      /\*.sass / \*.less \.css ....
   /static           # статика проекта.

Когда проект начинает расти
---------------------------

1. Структурирование зависимостей проекта.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Когда все просто в ``requirements.txt`` описываются зависимости проекта
без версий, но для продакшена такой вариант не подходит.
В продакшен окружении необходимо точно знать с какими версиями
пакетов (зависимостей) установлен ваш проект, поэтому
для продакшена необходимо писать ``requirements.txt`` с указанием конкретных
версий каждой из зависимостей, например::

   # requirements.txt
   Flask=0.11.1
   SQLAlchemy=1.0.0


2. Когда проект выростает из одного приложения.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Когда проект разростается до такого, что возникает необходимость
выделить в нем функцонально разные части (приложения), то есть несколько
путей это сделать:

I. Обычно в проекте можно выделить публичную часть (назовем ``site``) --
   то чем пользуются все пользователи системы
   и административную (назовем ``admin``) -- то где другие пользователи
   управляют тем, чем пользуются первые)

   В таком случае лучше всего делать эти части отдельными приложениями --
   с отдельными точками входа. Структура проекта в этом случае может измениться
   следующим образом::

      /sample01
         /templates
         /__init__.py
         /config.py
         /db.py
         /admin
            /__init__.py
            /__main__.py
            /main.py       # создается свое Flask-приложение
            /views.py
            /db.py         # методы для работы с БД, только для админки.
         /site
            /__init__.py
            /__main__.py
            /main.py       # создается свое Flask-приложение
            /views.py
         /lib  # или /common или /core или т.п.
               # содержит общий для обоих приложений код.
            /__init__.py
            /utils.py
            /...

   И запускаться такой проект будет следующим образом::

      $ python -m sample01.admin
      $ python -m sample02.site

   Т.е. необходимо будет запустить два отдельных процесса.

II. Также в рамках одного приложения возможно деление на логические части,
    например приложение ``site`` может содержать основной функционал
    (назовем ``public``) и функционал кабинета (профиля) пользователя
    (назовем ``cabinet``)::

      /sample01
         /site
            /__init__.py
            /__main__.py
            /main.py          # вызывает setup_public_routes()
                              # и setup_cabinet_routes()
            /public
               /__init__.py
               /views.py      # содержит setup_public_routes()
            /cabinet
               /__init__.py
               /views.py      # содержит setup_cabinet_routes()
