
gp:
	git status;./gp.sh;git status

dump:
	echo "####### scrapy genspider -t basic basic example.com ######################"
	scrapy genspider -d basic basic example.com
	echo "##### scrapy genspider -t crawl crawl example.com ####################################"
	scrapy genspider -d crawl crawl example.com
	echo "#### scrapy genspider -t csvfeed csvfeed example.com ##############"
	scrapy genspider -d csvfeed csvfeed example.com
	echo "######### scrapy genspider -t xmlfeed xmlfeed example.com ##############"
	scrapy genspider -d xmlfeed xmlfeed example.com
	
venv:
	python3.9 -m venv .venv;
	.venv/bin/python -m pip install --upgrade pip setuptools wheel pip-tools robotframework bpython
	.venv/bin/python -m pip install --upgrade pip yapf autoflake isort coverage scrapy newspaper3k requests bs4 
	.venv/bin/python -m pip install --upgrade -r requirements.txt