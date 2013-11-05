#!/bin/zsh

rm src/leap/mail/_version.py
python setup.py freeze_debianver
sed -i 's/-dirty//g' src/leap/mail/_version.py 
git add src/leap/mail/_version.py
git ci -m "freeze debian version"	
