PWR-JDW-Migration
=================

1. New script to allow dupe nicknames
2. rating dimensions
3. Run command line tool
4. String replace with RegEx (to remove duplicate DescribeYourselfs)
```
<ContextDataDimension id="DescribeYourself"><ExternalId>DescribeYourself</ExternalId><Label>Describe Yourself</Label></ContextDataDimension></ContextDataValue><ContextDataValue id=".*"><ExternalId>.*</ExternalId><Label>.*</Label><ContextDataDimension id="DescribeYourself"><ExternalId>DescribeYourself</ExternalId><Label>Describe Yourself</Label></ContextDataDimension></ContextDataValue>
```
Replaced by:
```
<ContextDataDimension id="DescribeYourself"><ExternalId>DescribeYourself</ExternalId><Label>Describe Yourself</Label></ContextDataDimension></ContextDataValue>
```
5. string replace
    DescribeYourself - Describeyoursel
    BestUse - Bestuse

6. hide questions in display... BestUse, DescribeYourself
