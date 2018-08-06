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
<St. Louis, Missouri>   time_zones      <Central Time Zone (North America)>
<Jay Kogen>     award_winner    <Peter Casey>
<Miami Hurricanes football>     position_s      <Kickoff returner>
<Nino Rota>     film    <Death on the Nile (1978 film)>
<Comedian>      people_with_this_profession     <Richard Dreyfuss>
<Satellite Award for Best Original Song>        award_nominee   <Emmylou Harris>
<Ron Silver>    major_field_of_study    <Spanish language>
<George Burns>  type_of_union   <Marriage>
<Sound editor>  film    <Star Trek: Insurrection>
```

```
Keyword to search: Apple
Searching for Apple ing...
Apple   /m/014j1m
<Apple> seasonal_months <October>
<Apple> nutrient        <Alpha-Tocopherol>
<Apple> location        <Marin County, California>
<Apple> nutrient        <Vitamin C>
<Apple> compatible_with_dietary_restrictions    <Vegetarian cuisine>
<Apple> seasonal_months <July>
<Apple> nutrient        <Ash (analytical chemistry)>
<Apple> location        <San Francisco Bay Area>
<Apple> nutrient        <Myristic acid>
<Apple> compatible_with_dietary_restrictions    <Gluten-free diet>
<Apple> nutrient        <Zinc>
<Apple> seasonal_months <November>
<Apple> nutrient        <Oleic acid>
<Apple> seasonal_months <December>
<Apple> nutrient        <Vitamin B6>
<Apple> rank    <Species>
<Apple> seasonal_months <August>
<Apple> seasonal_months <September>
<Apple> location        <Southern California>
<Apple> compatible_with_dietary_restrictions    <Veganism>
<Apple> nutrient        <Water>
<Apple> nutrient        <Vitamin A>
```

```
Keyword to search: Steve Jobs
Searching for Steve Jobs ing...
Steve Jobs      /m/06y3r
<Steve Jobs>    condition       <Pancreatic cancer>
<Steve Jobs>    organizations_founded   <Apple Inc.>
<Steve Jobs>    award_winner    <John Lasseter>
<Steve Jobs>    institution     <Reed College>
<Steve Jobs>    ethnicity       <German American>
<Steve Jobs>    profession      <Inventor (patent)>
<Steve Jobs>    organization    <Apple Inc.>
<Steve Jobs>    ethnicity       <Caucasian race>
<Steve Jobs>    profession      <Designer>
<Steve Jobs>    gender  <Male>
<Steve Jobs>    organization    <Pixar>
<Steve Jobs>    place_of_birth  <San Francisco>
<Steve Jobs>    currency        <United States dollar>
<Steve Jobs>    nationality     <United States>
<Steve Jobs>    company <Hewlett-Packard>
<Steve Jobs>    currency        <United States dollar>
<Steve Jobs>    religion        <Lutheranism>
<Steve Jobs>    place_of_death  <Palo Alto, California>
<Steve Jobs>    list    <Time 100>
<Steve Jobs>    company <Apple Inc.>
<Steve Jobs>    cause_of_death  <Pancreatic cancer>
<Steve Jobs>    religion        <Atheism>
<Steve Jobs>    profession      <Businessperson>
<Steve Jobs>    type_of_union   <Marriage>
<Steve Jobs>    religion        <Buddhism>
<Steve Jobs>    type_of_union   <Domestic partnership>
<Steve Jobs>    profession      <Entrepreneur>
```
