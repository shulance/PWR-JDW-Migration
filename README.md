PWR-JDW-Migration
=================

1. Run `unique-reviews-TC-allowDuplicateNicknames-4.py` to allow dupe nicknames ()
2. Run command line tool in WRB
2. rating dimensions
4. Search for duplicate DescribeYourselfs
```
<ContextDataDimension id="DescribeYourself"><ExternalId>DescribeYourself</ExternalId><Label>Describe Yourself</Label></ContextDataDimension></ContextDataValue><ContextDataValue
```
remove them with RegEx
```
<ContextDataDimension id="DescribeYourself"><ExternalId>DescribeYourself</ExternalId><Label>Describe Yourself</Label></ContextDataDimension></ContextDataValue><ContextDataValue id=".*"><ExternalId>.*</ExternalId><Label>.*</Label><ContextDataDimension id="DescribeYourself"><ExternalId>DescribeYourself</ExternalId><Label>Describe Yourself</Label></ContextDataDimension></ContextDataValue>
```
Replaced by:
```
<ContextDataDimension id="DescribeYourself"><ExternalId>DescribeYourself</ExternalId><Label>Describe Yourself</Label></ContextDataDimension></ContextDataValue>
```
5. string replace
    DescribeYourself - Describeyourspr
    BestUse - Bestusepr

6. hide questions in display... BestUse, DescribeYourself

