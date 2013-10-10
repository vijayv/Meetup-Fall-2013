zipcodes = {}
zipcodes['80403'] = 'Boulder, CO, Boulder County'
zipcodes['80123'] = 'Monument, CO El Paso County'
zipcodes['80919'] = 'Colorado Springs, CO El Paso County'

# Solution with lists
names = {}
names['Pat'] = '80403'
names['Bob'] = '80919'
names['Jane'] = '80132'

name = 'Pat'
print name, 'lives in', zipcodes[names[name]]
