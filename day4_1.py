#!/usr/bin/env python3
# https://adventofcode.com/2020/day/4

'''
The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value pairs separated by spaces or newlines.
Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, not a passport at all!
Surely, nobody would mind if you made the system temporarily ignore missing cid fields. Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the string of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
'''

from jsonschema import validate

def main():
    with open ('day4input.txt') as fp:
        # parse input into passport objects, delimited by blank line (e.g. len(line) = 0)
        lines = fp.read().splitlines()
        passports = []
        passport = {}
        for line in lines:
            # a blank line delimits the end of each passport object
            # we assume the first line is not blank
            if len(line) == 0:
                passports.append(passport)
                passport = {}
                continue

            passport.update(dict(x.split(":") for x in line.split(" ")))


    '''
    # overkill
            schema = {
                 "type" : "object",
                 "properties" : {
                     "byr" : {"type" : "string"},
                     "iyr" : {"type" : "string"},
                     "eyr" : {"type" : "string"},
                     "hgt" : {"type" : "string"},
                     "hcl" : {"type" : "string"},
                     "ecl" : {"type" : "string"},
                     "pid" : {"type" : "string"},
                     "cid" : {"type" : "string"},
                 },
                 "required": [ "byr","iyr","eyr","hgt","hcl","ecl","pid" ] # cid is optional
             }
            # validate passports based on schema
            valid_passports = 0
            for passport in passports:
                try:
                    #print(passport)
                    validate(instance=passport, schema=schema)
                    valid_passports +=1
                except Exception as e:
                    print(e)
    '''
    
    valid_passports = 0
    print(f"Total passports:{len(passports)}")
    for passport in passports:
        if passport.get('byr') and passport.get('iyr') and passport.get('eyr') and passport.get('hgt') and passport.get('hcl') and passport.get('ecl') and passport.get('pid'):
            valid_passports +=1

    print(f"Valid passports:{valid_passports}")

if __name__ == '__main__':
    main()
