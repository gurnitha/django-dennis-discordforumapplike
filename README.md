## BUILDING DISCORD APP, A FORUM LIKE APP, USING DJANGO V3.2

This is my exercise base on the tutorials made by Dennis on Youtube.

## Links to sources:
* [Youtube](https://www.youtube.com/watch?v=PtQiiknWUcI&t=3930s)
* [My repository](https://github.com/gurnitha/django-dennis-discordforumapplike)


### 1. COMPLETE SETUP


#### 1.1 Create: project, app, db using django-environ

        new file:   .gitignore
        new file:   README.md
        new file:   apps/base/__init__.py
        new file:   apps/base/admin.py
        new file:   apps/base/apps.py
        new file:   apps/base/migrations/__init__.py
        new file:   apps/base/models.py
        new file:   apps/base/templates/base/index.html
        new file:   apps/base/tests.py
        new file:   apps/base/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        new file:   templates/base.html


#### 1.2 Finished app

![Algorithm schema](./config/images/fns-app.jpg)


### 2. TEMPLATES, VIEWS AND URLS


#### 2.1 Create a home page

        modified:   README.md
        modified:   apps/base/templates/base/index.html
        new file:   apps/base/urls.py
        modified:   apps/base/views.py
        modified:   config/urls.py


#### 2.2 Template inheritance

        modified:   README.md
        modified:   apps/base/templates/base/index.html
        modified:   config/settings.py
        modified:   templates/base.html


#### 2.3 Add theme for home page

        modified:   README.md
        modified:   apps/base/templates/base/index.html
        new file:   apps/base/templates/inc/activities.html
        new file:   apps/base/templates/inc/room.html
        new file:   apps/base/templates/inc/topics.html
        modified:   templates/base.html
        new file:   templates/inc/head.html
        new file:   templates/inc/header.html
        new file:   templates/inc/scripts.html


#### 2.4 Create room page - Templates, Views and Urls


### 3. ROOM APP


#### 3.1 Create room app and room page

        modified:   README.md
        new file:   apps/base/templates/base/room.html
        new file:   apps/room/__init__.py
        new file:   apps/room/admin.py
        new file:   apps/room/apps.py
        new file:   apps/room/migrations/__init__.py
        new file:   apps/room/models.py
        new file:   apps/room/templates/room/room.html
        new file:   apps/room/tests.py
        new file:   apps/room/urls.py
        new file:   apps/room/views.py
        modified:   config/settings.py
        modified:   config/urls.py


#### 3.2 Template inheritance

        modified:   README.md
        new file:   apps/room/templates/inc/participants.html
        renamed:    apps/base/templates/base/room.html -> apps/room/templates/inc/room-content.html
        modified:   apps/room/templates/room/room.html





























































































































































































