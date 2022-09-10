# seamstresses
1) git clone https://github.com/alisher1989/seamstresses.git
2) cd seamstresses/
3) virtualenv -p python3.8 venv
4) source venv/bin/activate
5) pip install --upgrade pip
6) pip install -r req.txt 
7) ./manage.py migrate
8) ./manage.py loaddata db.json
9) ./manage.py loaddata user.json 
10) ./manage.py runserver
