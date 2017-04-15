# python-general-template
The structure template of general project which can provide some userfull files and quickly build

How to use the general template (skeleton) for your project:
============

0. Make copy of the project, the rename it as your new project, for example "project1".
1. Rename the "project" dir to the name of yor project or others as your root moudle.
2. Now, edit your setup.py to what your want to modifing or adding more infomations for your project.
3. Rename the tests/project_tests.py to your root module again, for example "project1_tests.py"
4. Then you should check if you have make it right , so you will use "nosetests " at the root dir;
   if it ouput as "Ran 1 test in xxx.s", so it's all right,others you should fix it again.
5. Okay, you can start coding for new project now.

Details:
============

0. If you modify the setup.py file, you can visit the website" http://docs.python.org/distutils/setupscript.html".
1. The general template is the The most simplified, so you can adding more rules as you can do.
2. Before you install the project, you should install some python packages, as "pip","distribute","nose","virtualenv". pip: install the python packages from PyPI, virtualenv or venv is used to isolate application specific dependencies from a shared Python installation, and nose can be as unit test tools, in fact, the distribute as the standard of Python disutils extension, but it can be replaced by "setuptools".
3. SomeHow, those tools will not usefull in future, the web site "https://packaging.python.org/current/" can be most useful.

Usefull web sites:
==============

Python Packaging User Guide: https://packaging.python.org/ 

Distributing Python Modules: https://docs.python.org/3/distributing/index.html

Packaging and Distributing Projects: https://packaging.python.org/distributing/

Python Packaging Authority: https://www.pypa.io/en/latest/

Tool Recommendations: https://packaging.python.org/current/

