
## Raw Dream File Format
Each file has dreams for one day. Filename has <datestamp_timestamp>. 
The dream could have a title in it. 
Dreams in one file are new line separated. 

Timestamp is difficult to record, exact time is usually unknown. What we can
decide though, is whether it's morning (4am-12pm), afternoon (12-5pm) evening (5pm to 10pm), night(10pm-4am)
Woudl be tough to record and not sure if it'll be helpful. 

## Entity Extraction

Tried to use nltk chunker for entity extraction. 
It was able to extract some entities, but missed important ones. 

## Ideas
Archetypes
Remalize needs a way to lookup archetypes (there a finite amount of different
ones) and, if the dreamer is 'stuck', suggest associations between their 
symbols to archetypal symbols. 
the output would be a classification into one of the archetypes
the input would be a symbol and its context. 
there are a finite number of archetypes, but not small. Will need to review
arhcetypal lit to see whether this makes sense. 