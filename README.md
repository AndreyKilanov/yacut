# Сервис сокращения ссылок  YaCut

---

<span style="font-weight:700; font-size:18px">
Сервис создает короткие ссылки из длинных и нечитабельных.
</span>

Вы можете придумать своё название короткой ссылки(по умолчанию стоит ограничение в 16 символов).  
Если оставить поле пустым сервис создаст короткую ссылку(по умолчнию 6 символов) по клику по которой
происходит редирект на нужную ссылку.  

---

### Так же реализован API ([ Документация](https://github.com/AndyFebruary74/yacut/blob/master/openapi.yml))

### _Examples_:


######  _Request POST_

```json
{
  "url": "https://github.com/AndyFebruary74/yacut/",
  "custom_id": "777777"
}
```
###### *Response*

```json
{
  "url": "https://github.com/AndyFebruary74/yacut/",
  "short_link": "http://127.0.0.1:5000/777777"
}
```
###### *Request GET*

```json
{
  "url": "http://127.0.0.1:5000/777777"
}
```

---

### Как пользоваться:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AndyFebruary74/yacut
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Запуск:

```
flask run
```

---

### .env

`/yacut/.env` - месторасположение

#### Example:

```python
FLASK_DEBUG=True
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=SECRET_KEY
```

---

### Используемые технологии([requirements](https://github.com/AndyFebruary74/yacut/blob/master/requirements.txt)):
1. [x] Python 3.10
2. [x] Flask 2.0.2
3. [x] SQLAlchemy 1.4.29
4. [x] Alembic 1.7.5
5. [x] Jinja 3.0.3

---

**_Author: [Andrey Kilanov](https://github.com/AndyFebruary74/) [telegram](https://t.me/AndyFebruary)_**