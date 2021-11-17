# Freebase Relation Searching

[readline.py](https://github.com/zecoo/mini_tools/blob/master/readline.py)   
Usage: Extract few lines from an extremely big file.   
[txt2sql.py](https://github.com/zecoo/mini_tools/blob/master/txt2sql.py)    
Usage: Store .txt to mysql   
[get_relations_by_keyword.py](https://github.com/zecoo/freebase_structure/blob/master/get_relations_by_keyword.py)   
Usage: Literaly   

Freebase has marked relations between 2 entities in dataset like FB15K, which you can download from [THU OpenKE](https://github.com/thunlp/OpenKE).   
Mid2name mapping can be downloaded from [CSDN](https://download.csdn.net/download/guotong1988/9865898).

## New to freebase
The RDF triples in Freebase look like:    
> <m.01jzhl>  <people.person.education>   <m.0n1k91v> .  
> <m.01jzhl>  <people.person.profession>  <m.02h664x> .  
   
The `mid2name.txt` is extremely big that Sublime Text would open it for several minutes.    
1. I store the `mid2name.txt` into mysql using `txt2sql.py`.
2. Searching from FB15K for relations intuitionaly via `get_relations_by_keyword,py`
   
Terminaly the demo looks like:   
```
Keyword to search: Wuhan
<Wuhan> administrative_division <Hubei>
<Wuhan> time_zones      <Time in China>
<Wuhan> containedby     <China>
<Wuhan> containedby     <Hubei>
<Wuhan> country <China>
```   
```
Keyword to search: Steve Jobs
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
  
Enjoy your study on Freebase!
