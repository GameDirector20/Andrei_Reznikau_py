
# with open('c:/Users/81236312/Documents/GitHub/Andrei_Reznikau_py/Tasks/Task3/test-test.txt', 'r') as f:
    
#     print(f.read())
#     f.seek(0)
    
#     x = f.read(5)
#     print(x, f'position - {f.tell()}')

#     # f.seek(4)
#     x = f.read(5)
#     print(x, f'position - {f.tell()}')

    # f.seek(0)

    # for i in range(15):
    #     x = f.readline(3)
    #     print(x,  f'position - {f.tell()}')

    # else:
    #     x = '10'

    # print(x, len(x),  f'position - {f.tell()}')

    # xl = []

    # xl.append(x)
    # print(xl)

    # xl.append('x')

    # print(xl)

# s = ' 0123456789 \n '

# s_w = '0123456789'

# l = []

# l.append(s)

# l_w = []

# l_w.append(s_w)

# b = '\n' in s

# bs = "\n" in s_w

# print(f" leng of str with N - {len(s)}, {b}")

# print(f' leng of str without N - {len(s_w)}, {bs}')

# print(f' leng of lst with N - {len(l)}')

# print(f' leng of lst without N - {len(l_w)}')

# print(s)

# print('------------------------------------')

# for i in range(len(s_w)):
#     print(s_w[i], f'the position number - {i}')

# for i in range(1, len(s_w)+1):
#     print(s_w[i*(-1)], f'the position number - {i*(-1)}')



t = """
The  February  TIOBE Index of the most popular programming languages is out, and
while  the  work  going  on  in  the  background  of  TIOBE’s calculations has
changed, not much has shifted in the way of rankings.
Python  continues  to sit atop the index, with C and Java directly behind it. In
Feb.  2021,  those  three  also  occupied  the  top spot, but with Python in the
number three position, C at top, and Java in second place.
Beyond  the  top  three,  there  hasn’t  been much movement in the index, with
positions  four  through  eight  unchanged  from  the same time last year. Those
slots  are  occupied,  respectively,  by  C++,  C#, Visual Basic, JavaScript and
PHP.  Positions  nine and 10 swapped from Feb. 21 to now, with Assembly Language
and SQL now occupying each other’s positions.
The  one  big  move  of note between Feb. 2021 and Feb. 2022 was with the Groovy
programming  language,  an object-oriented language for Java. Over the course of
the  year,  Groovy  fell  from  12th  position  all  the way to 20th, putting it
perilously close to the “other programming languages” list.
TIOBE  CEO  Paul Jansen attributes Groovy’s decline to the growth in the CI/CD
space.  Groovy  was the only language used for writing scripts on Jenkins, which
Jansen  describes  as having been “the only real player in the CI/CD domain”
early  on.  Now,  with platforms that don’t require Groovy, like GitHub, Azure
DevOps and GitLab, Groovy is losing its place at the table.
“Groovy  could  have  grown  further  because  it  was  the major script-based
alternative  for  Java  running  on the same JVM. However, Kotlin is taking over
that  position  right  now,  so  I think Groovy will have a hard time,” Jensen
said.
The  TIOBE  index may not be full of surprises this month, but Jansen did have a
lot  to  say about the index itself this month, as this is the first time it has
been compiled using Similarweb’s traffic analysis platform instead of Alexa.
“We  have  used  Similarweb  for  the  first  time this month to select search
engines  and  fortunately,  there  are  no  big changes in the index due to this
swap.  The  only striking difference is that the top 3 languages, Python, C, and
Java, all gained more than 1 percent in the rankings,” Jansen said.
TIOBE  decided  to  make  the switch this month after Amazon’s announcement in
December  2021  that  it  was  shutting  the  Alexa  web  ranking  service down,
effective May 1, 2022, ending 25 years of the program.
Jansen  noted  that not every website has been onboarded, but that the switch to
Similarweb  included  a  switch  to  using  HtmlUnit, a non-GUI web browser with
APIs  that  let  Java  apps  invoke  pages, fill forms and do other standard web
browsing  activity.  This switch will eventually allow TIOBE to include websites
it  was  unable  to  crawl  before,  like Stackoverflfow and Github, which could
have                a               larger               impact               on
scores."""



print('TIOBE CEO Paul Jansen attributes Groovy’s decline to the growth in the CI/CD space. Groovy was the only language used for writing scripts on Jenkins, which Jansen describes as having been “the only real player in the CI/CD domain” early on. Now, with platforms that don’t require Groovy, like GitHub, Azure DevOps and GitLab, Groovy is losing its place at the table.'.encode('utf-8'))
print(b'\xe2\x80\x9c'.decode('utf-8'), len (b'\xe2\x80\x9c'.decode('utf-8')), len(b'\xe2\x80\x9c'))