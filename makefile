generate: 
	jupyter nbconvert --config config.py *.ipynb

site: generate
	cp docs/*.html  ../Web-Site/recursionWonderland/

