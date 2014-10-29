#!/usr/bin/python

import ephem
from datetime import date, time, datetime

def main():

    sun = ephem.Sun()
    moon = ephem.Moon()

    # define observer
    home = ephem.Observer()
    home.date = ephem.date(datetime.utcnow())
    home.lat, home.lon = '50.46', '9.61'

    sun.compute(home)
    sunrise, sunset = (home.next_rising(sun),
                       home.next_setting(sun))
    moon.compute(home)
    moonrise, moonset = (home.next_rising(moon),
                       home.next_setting(moon))
    home.horizon = '-6'
    m6_start, m6_end = (home.next_rising(sun, use_center=True),
                        home.next_setting(sun, use_center=True))
    home.horizon = '-12'
    m12_start, m12_end = (home.next_rising(sun, use_center=True),
                          home.next_setting(sun, use_center=True))
    home.horizon = '-18'
    m18_start, m18_end = (home.next_rising(sun, use_center=True),
                          home.next_setting(sun, use_center=True))

    print home.date

    e = {}
    e[sunrise] =   " Sunrise:                      "
    e[sunset] =    " Sunset:                       "
    e[moonrise] =  " Moonrise:                     "
    e[moonset] =   " Moonset:                      "
    e[m6_start] =  " Civil twilight starts:        "
    e[m6_end] =    " Civil twilight ends:          "
    e[m12_start] = " Nautical twilight starts:     "
    e[m12_end] =   " Nautical twilight ends:       "
    e[m18_start] = " Astronomical twilight starts: "
    e[m18_end] =   " Astronomical twilight ends:   "

    for time in sorted(e.keys()):
        print e[time], ephem.localtime(time).ctime()

    # Here start the moon specific data

    print " ---"
    print " Moon phase: %d%% " % moon.phase

    e = {}
    e1 = ephem.previous_new_moon(home.date)
    e[e1] = " Previous new moon:            "
    e1 = ephem.previous_first_quarter_moon(home.date)
    e[e1] = " Previous first quarter moon:  "
    e1 = ephem.previous_full_moon(home.date)
    e[e1] = " Previous full moon:           "
    e1 = ephem.previous_last_quarter_moon(home.date)
    e[e1] = " Previous last quarter moon:   "

    e1 = ephem.next_new_moon(home.date)
    e[e1] = " Next new moon:                "
    e1 = ephem.next_first_quarter_moon(home.date)
    e[e1] = " Next first quarter moon:      "
    e1 = ephem.next_full_moon(home.date)
    e[e1] = " Next full moon:               "
    e1 = ephem.next_last_quarter_moon(home.date)
    e[e1] = " Next last quarter moon:       "

    for time in sorted(e.keys()):
        print e[time], ephem.localtime(time).ctime()

if __name__ == "__main__":
    main()

