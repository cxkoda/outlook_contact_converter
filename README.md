# outlook_contact_converter
quick python-script i wrote to solve an issue when i wanted to sync outlook.com contacts to an android smartphone or to gmail.

the problem was caused by outlook.com using some strange field-names, i.e. Car Phone, which are not recognized by gmail or android (even if sync through the offical microsoft outlook app).
my workaround was to
- export all contacts from outlook.com as csv
- move all car-phone-numbers to a different label (using the script)
- delete all contacts and reimport the contacts from the modified csv

the contacts can now be sync to the android or gmail directly from outlook.com
