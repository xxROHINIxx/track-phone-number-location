#open terminal and install the packages "pip install phonenumbers"
from test import number

import phonenumbers
from phonenumbers import \
    geocoder  # geocoder is a built-in function from phonenumbers that provides geographical information about phonenumbers.

ch_num=phonenumbers.parse(number,"CH") #ch indicates the country code.
print(geocoder.description_for_number(ch_num,"en"))

from phonenumbers import \
    carrier  # carrier indicates the carrier service of phone numbers

service_number=phonenumbers.parse(number,"RO") #parse is used because it is easier convert string into an object and easier to manipulate as well as analyze it
print(carrier.name_for_number(service_number,"en"))

