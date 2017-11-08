exp: generate
	cp *.html  ../Web-Site/recursionWonderland/

generate: 
	jupyter nbconvert --config config.py *.ipynb
