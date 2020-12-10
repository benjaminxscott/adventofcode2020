#!/usr/bin/env python3
# https://adventofcode.com/2020/day/4

'''
You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789
Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

Count the number of valid passports - those that have all required fields and valid values.
Continue to treat cid as optional. In your batch file, how many passports are valid?
'''

from jsonschema import validate

def main():
    with open ('day4input.txt') as fp:
        # parse input into passport objects, delimited by blank line (e.g. len(line) = 0)
        lines = fp.read().splitlines()
        passports = []
        passport = {}
        for line_index, line in enumerate(lines):
            # a blank line (or end of file, jankily measured with line_index) delimits the end of each passport object
            # we assume the first line is not blank
            if len(line) == 0 or line_index == len(lines) -1:
                # convert strings to ints
                for key in ['iyr', 'eyr', 'byr']:
                    if passport.get(key):
                        passport[key] = int(passport.get(key))

                passports.append(passport)
                passport = {}
                continue

            # if we don't have a blank line, parse out the fields for our passport
            passport.update(dict(x.split(":") for x in line.split(" ")))

    schema = {
         "type" : "object",
         "properties" : {
             "byr" : {"type" : "integer", "minimum": 1920, "maximum": 2002},
             "iyr" : {"type" : "integer", "minimum": 2010, "maximum": 2020},
             "eyr" : {"type" : "integer", "minimum": 2020, "maximum": 2030},
             "hgt" : {"type" : "string"}, # we handle validation later since it's wonky
             "hcl" : {"type" : "string", "pattern": "#[a-f0-9]{6}"},
             "ecl" : {"type" : "string", "enum": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]},
             "pid" : {"type" : "string", "pattern": "[0-9]{9}"},
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
            # custom handling for height, this probably can be handled via json-schema but I couldn't be arsed
            # https://json-schema.org/understanding-json-schema/reference/object.html#pattern-properties
            height = passport.get('hgt')
            if "cm" in height:
                height = int(height.split('cm')[0])
                if height < 150 or height > 193:
                    raise Exception
            elif "in" in height:
                height = int(height.split('in')[0])
                if height < 59 or height > 76:
                    raise Exception
            else:
                raise Exception
            # hooray it's valid
            valid_passports +=1

        except Exception as e:
            #print(e)
            pass


    print(f"Valid passports:{valid_passports}")

if __name__ == '__main__':
    main()
