
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

There is a use case to group together mentions of same entity in different 
ways, for example: Alex, the Chemistry teacher, the son, the man etc.

## Schema design and Database
The raw input, the metadata, the constituent results (symbols, associations, 
images etc) need to be recorded at least for future analysis. Database would
make sense. 

## What to record
For parsed dreams:
- link to original dream
- how dream was parsed
  - parser and configurations
- results of parsing
  - symbols extracted, associations made, images generated etc

## What to parse
- Does the number of mentions of an entity have an impact on its importance in 
the dream?
- Would it be useful to create a hierarchy of entities? 
Ex: school > building 1 > clasroom 54 > chair
- how should conjuecture about an entity be handled? Should we consider both, or 
try and find importance of one or the other? Probably need to help someone figure
out which symbol makes more sense? But need to detect conjecture first. 
Ex: I can't tell what it was, could be a dog or a deer. 
- What is the importance of detecting emotion? *I feel lonely*, *I feel misunderstood*
seem to have important consequences for the message, no?

## Ideas
Archetypes
Remalize needs a way to lookup archetypes (there a finite amount of different
ones) and, if the dreamer is 'stuck', suggest associations between their 
symbols to archetypal symbols. 
the output would be a classification into one of the archetypes
the input would be a symbol and its context. 
there are a finite number of archetypes, but not small. Will need to review
arhcetypal lit to see whether this makes sense. 