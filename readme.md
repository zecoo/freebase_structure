# Mini Tools

The repositoty is bulid for simple text processing.

[readline.py](https://github.com/zecoo/mini_tools/blob/master/readline.py)   
Usage: Extract few lines from an extremely big file.

[txt2sql.py](https://github.com/zecoo/mini_tools/blob/master/txt2sql.py)  
Usage: store .txt to mysql

## Freebase

Freebase has marked relation between 2 entities.
You can [download](https://download.csdn.net/download/guotong1988/9865898) the mid2name.txt on csdn.

While I am learning I found that the id `"/m/0jrcc"` type is helpless to know more about the relation like:  

> <m.01jzhl>  <people.person.education>   <m.0n1k91v> .  
> <m.01jzhl>  <people.person.profession>  <m.02h664x> .  

As the mid2name.txt is extremely big that Sublime Text would open it for several minutes. I want to store the mid2name.txt into mysql for better searching and later learning.

txt2sql.py is suitable for case like this.

```
<St. Louis, Missouri>   /location/location/time_zones   <Central Time Zone (North America)>
<Jay Kogen>     /award/award_winner/awards_won./award/award_honor/award_winner  <Peter Casey>
<Miami Hurricanes football>     /american_football/football_team/historical_roster./american_football/football_historical_roster_position/position_s    <Kickoff returner>
<Nino Rota>     /film/music_contributor/film    <Death on the Nile (1978 film)>
<Comedian>      /people/profession/people_with_this_profession  <Richard Dreyfuss>
<Satellite Award for Best Original Song>        /award/award_category/nominees./award/award_nomination/award_nominee
<Emmylou Harris>
<Ron Silver>    /people/person/education./education/education/major_field_of_study      <Spanish language>
<George Burns>  /people/person/spouse_s./people/marriage/type_of_union  <Marriage>
<Sound editor>  /film/film_job/films_with_this_crew_job./film/film_crew_gig/film        <Star Trek: Insurrection>
```
