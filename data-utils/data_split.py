import csv

PLAYERID = 0
NAMEFIRST = 1
NAMELAST = 2
NAMEGIVEN = 3
BBREFID = 4
YEARID = 6
TEAMID = 7
LEAGUEID = 8
SALARY = 10
GAMES_PLAYED = 11
GAMES_PITCHER = 16
GAMES_CATCHER = 17
GAMES_1BASE = 18
GAMES_2BASE = 19
GAMES_3BASE = 20
GAMES_SHORTSTOP = 21
GAMES_LEFTFIELD = 22
GAMES_CENTERFIELD = 23
GAMES_RIGHTFIELD = 24


f = open('joined_data1.csv')
f_1985 = open('1985.csv', 'w')
f_1986 = open('1986.csv', 'w')
f_1987 = open('1987.csv', 'w')
f_1988 = open('1988.csv', 'w')
f_1989 = open('1989.csv', 'w')
f_1990 = open('1990.csv', 'w')
f_1991 = open('1991.csv', 'w')
f_1992 = open('1992.csv', 'w')
f_1993 = open('1993.csv', 'w')
f_1994 = open('1994.csv', 'w')
f_1995 = open('1995.csv', 'w')
f_1996 = open('1996.csv', 'w')
f_1997 = open('1997.csv', 'w')
f_1998 = open('1998.csv', 'w')
f_1999 = open('1999.csv', 'w')
f_2000 = open('2000.csv', 'w')
f_2001 = open('2001.csv', 'w')
f_2002 = open('2002.csv', 'w')
f_2003 = open('2003.csv', 'w')
f_2004 = open('2004.csv', 'w')
f_2005 = open('2005.csv', 'w')
f_2006 = open('2006.csv', 'w')
f_2007 = open('2007.csv', 'w')
f_2008 = open('2008.csv', 'w')
f_2009 = open('2009.csv', 'w')
f_2010 = open('2010.csv', 'w')
f_2011 = open('2011.csv', 'w')
f_2012 = open('2012.csv', 'w')
f_2013 = open('2013.csv', 'w')
f_2014 = open('2014.csv', 'w')
f_2015 = open('2015.csv', 'w')
f_2016 = open('2016.csv', 'w')


csv_f = csv.reader(f)
csv_1985 = csv.writer(f_1985)
csv_1986 = csv.writer(f_1986)
csv_1987 = csv.writer(f_1987)
csv_1988 = csv.writer(f_1988)
csv_1989 = csv.writer(f_1989)
csv_1990 = csv.writer(f_1990)
csv_1991 = csv.writer(f_1991)
csv_1992 = csv.writer(f_1992)
csv_1993 = csv.writer(f_1993)
csv_1994 = csv.writer(f_1994)
csv_1995 = csv.writer(f_1995)
csv_1996 = csv.writer(f_1996)
csv_1997 = csv.writer(f_1997)
csv_1998 = csv.writer(f_1998)
csv_1999 = csv.writer(f_1999)
csv_2000 = csv.writer(f_2000)
csv_2001 = csv.writer(f_2001)
csv_2002 = csv.writer(f_2002)
csv_2003 = csv.writer(f_2003)
csv_2004 = csv.writer(f_2004)
csv_2005 = csv.writer(f_2005)
csv_2006 = csv.writer(f_2006)
csv_2007 = csv.writer(f_2007)
csv_2008 = csv.writer(f_2008)
csv_2009 = csv.writer(f_2009)
csv_2010 = csv.writer(f_2010)
csv_2011 = csv.writer(f_2011)
csv_2012 = csv.writer(f_2012)
csv_2013 = csv.writer(f_2013)
csv_2014 = csv.writer(f_2014)
csv_2015 = csv.writer(f_2015)
csv_2016 = csv.writer(f_2016)

for row in csv_f:
    year = row[YEARID]
    if year == '1985':
        csv_1985.writerow(row)
    elif year == '1986':
        csv_1986.writerow(row)
    elif year == '1987':
        csv_1987.writerow(row)
    elif year == '1988':
        csv_1988.writerow(row)
    elif year == '1989':
        csv_1989.writerow(row)
    elif year == '1990':
        csv_1990.writerow(row)
    elif year == '1991':
        csv_1991.writerow(row)
    elif year == '1992':
        csv_1992.writerow(row)
    elif year == '1993':
        csv_1993.writerow(row)
    elif year == '1994':
        csv_1994.writerow(row)
    elif year == '1995':
        csv_1995.writerow(row)
    elif year == '1996':
        csv_1996.writerow(row)
    elif year == '1997':
        csv_1997.writerow(row)
    elif year == '1998':
        csv_1998.writerow(row)
    elif year == '1999':
        csv_1999.writerow(row)
    elif year == '2000':
        csv_2000.writerow(row)
    elif year == '2001':
        csv_2001.writerow(row)
    elif year == '2002':
        csv_2002.writerow(row)
    elif year == '2003':
        csv_2003.writerow(row)
    elif year == '2004':
        csv_2004.writerow(row)
    elif year == '2005':
        csv_2005.writerow(row)
    elif year == '2006':
        csv_2006.writerow(row)
    elif year == '2007':
        csv_2007.writerow(row)
    elif year == '2008':
        csv_2008.writerow(row)
    elif year == '2009':
        csv_2009.writerow(row)
    elif year == '2010':
        csv_2010.writerow(row)
    elif year == '2011':
        csv_2011.writerow(row)
    elif year == '2012':
        csv_2012.writerow(row)
    elif year == '2013':
        csv_2013.writerow(row)
    elif year == '2014':
        csv_2014.writerow(row)
    elif year == '2015':
        csv_2015.writerow(row)
    elif year == '2016':
        csv_2016.writerow(row)
