generate: 
	jupyter nbconvert --config config.py *.ipynb

site: generate
	cp HTML/*.html  ../Web-Site/recursionWonderland/

