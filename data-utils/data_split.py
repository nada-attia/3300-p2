import csv

playerID, birthYear, birthMonth, birthDay, birthCountry, birthState, birthCity, deathYear, deathMonth, deathDay, deathCountry, deathState, deathCity, nameFirst, nameLast, nameGiven, weight, height, bats, throws, debut, finalGame, retroID, bbrefID, birth_date, debut_date, finalgame_date, death_date, ID, yearID, teamID, team_ID, lgID, playerID: 1, salary, ID: 1, yearID: 1, teamID: 1, team_ID: 1, lgID: 1, playerID: 2, G_all, GS, G_batting, G_defense, G_p, G_c, G_1b, G_2b, G_3b, G_ss, G_lf, G_cf, G_rf, G_of, G_dh, G_ph, G_pr
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


f = open('data-utils/joined_data.csv')
csv_f = csv.reader(f)

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

col = 'playerID,birthYear,birthMonth,birthDay,birthCountry,birthState,birthCity,deathYear,deathMonth,deathDay,deathCountry,deathState,deathCity,nameFirst,nameLast,nameGiven,weight,height,bats,throws,debut,finalGame,retroID,bbrefID,birth_date,debut_date,finalgame_date,death_date,ID,yearID,teamID,team_ID,lgID,playerID:1,salary,ID:1,yearID:1,teamID:1,team_ID:1,lgID:1,playerID:2,G_all,GS,G_batting,G_defense,G_p,G_c,G_1b,G_2b,G_3b,G_ss,G_lf,G_cf,G_rf,G_of,G_dh,G_ph,G_pr'
f_1985.write(col)
f_1986.write(col)
f_1987.write(col)
f_1988.write(col)
f_1989.write(col)
f_1990.write(col)
f_1991.write(col)
f_1992.write(col)
f_1993.write(col)
f_1994.write(col)
f_1995.write(col)
f_1996.write(col)
f_1997.write(col)
f_1998.write(col)
f_1999.write(col)
f_2000.write(col)
f_2001.write(col)
f_2002.write(col)
f_2003.write(col)
f_2004.write(col)
f_2005.write(col)
f_2006.write(col)
f_2007.write(col)
f_2008.write(col)
f_2009.write(col)
f_2010.write(col)
f_2011.write(col)
f_2012.write(col)
f_2013.write(col)
f_2014.write(col)
f_2015.write(col)
f_2016.write(col)

print(csv_f)
for (csv_row, row) in zip(csv_f, f):
    year = csv_row[30]

    if year == '1985':
        f_1985.write(row)
    elif year == '1986':
        f_1986.write(row)
    elif year == '1987':
        f_1987.write(row)
    elif year == '1988':
        f_1988.write(row)
    elif year == '1989':
        f_1989.write(row)
    elif year == '1990':
        f_1990.write(row)
    elif year == '1991':
        f_1991.write(row)
    elif year == '1992':
        f_1992.write(row)
    elif year == '1993':
        f_1993.write(row)
    elif year == '1994':
        f_1994.write(row)
    elif year == '1995':
        f_1995.write(row)
    elif year == '1996':
        f_1996.write(row)
    elif year == '1997':
        f_1997.write(row)
    elif year == '1998':
        f_1998.write(row)
    elif year == '1999':
        f_1999.write(row)
    elif year == '2000':
        f_2000.write(row)
    elif year == '2001':
        f_2001.write(row)
    elif year == '2002':
        f_2002.write(row)
    elif year == '2003':
        f_2003.write(row)
    elif year == '2004':
        f_2004.write(row)
    elif year == '2005':
        f_2005.write(row)
    elif year == '2006':
        f_2006.write(row)
    elif year == '2007':
        f_2007.write(row)
    elif year == '2008':
        f_2008.write(row)
    elif year == '2009':
        f_2009.write(row)
    elif year == '2010':
        f_2010.write(row)
    elif year == '2011':
        f_2011.write(row)
    elif year == '2012':
        f_2012.write(row)
    elif year == '2013':
        f_2013.write(row)
    elif year == '2014':
        f_2014.write(row)
    elif year == '2015':
        f_2015.write(row)
    elif year == '2016':
        f_2016.write(row)
