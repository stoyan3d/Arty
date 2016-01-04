pip install virtualenv
virtualenv env1
call %~dp0env1\Scripts\activate
cd %~dp0
pip install -r requirements.txt
pause