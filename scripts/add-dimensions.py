#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.dom.minidom import parse, parseString, getDOMImplementation

# Opens input BV file, input PWR file, and exports BV file containing rating dimensions

input_feed_bv = open('clean_bv_export_file-2.xml','r')
input_feed_pr = open('clean_pr_export_file.xml','r')
output_feed = open('clean_bv_export_file_plus_dims.xml','w')

bv_feed_parsed = parse(input_feed_bv)
pr_feed_parsed = parse(input_feed_pr)

# You'll need build a dictionary which matches PWR data ids to BV data IDs.  You're looking for the 'key' value of the 'subrating' node in PWR feed, which will correspond to the appropriate ExternalId for the rating taken from the hub.  Use commented code below as example.  

dimensions = {
    "fit" : "Fit",
    "length" : "Length",
    "waist" : "Waist",
    "sleevelength" : "Sleevelength"
}

def append_text_node(parent,child_name,child_value):
    child_node = bv_feed_parsed.createElement(child_name)
    child_node_text = bv_feed_parsed.createTextNode(child_value)
    child_node.appendChild(child_node_text)
    parent.appendChild(child_node)

num_reviews = 0

mapped_subratings = {}

for review in pr_feed_parsed.getElementsByTagName("fullreview"):
    review_id = str(review.getElementsByTagName("id")[0].childNodes[0].nodeValue)
    mapped_subratings[review_id] = {}
    taggroups = review.getElementsByTagName("taggroup")
    for taggroup in taggroups:
        # key = str(taggroup.getAttribute("key"))
        #name = str(taggroup.getAttribute("name"))
        #print "key is "+key+" and name is " + name

        if taggroup.getAttribute("key") == 'fit':
            tag = taggroup.getElementsByTagName("tag")[0]
            value = tag.childNodes[0].nodeValue
            name = str(taggroup.getAttribute("name"))
            
            if value == "Feels too small":
                mapped_subratings[review_id][name] = 1
            if value == "Feels true to size":
                mapped_subratings[review_id][name] = 2
            if value == "Feels too big":
                mapped_subratings[review_id][name] = 3
        
        if taggroup.getAttribute("key") == 'waist':
            tag = taggroup.getElementsByTagName("tag")[0]
            value = tag.childNodes[0].nodeValue
            name = str(taggroup.getAttribute("name"))
            
            if value == "Feels too small":
                mapped_subratings[review_id][name] = 1
            if value == "Feels true to size":
                mapped_subratings[review_id][name] = 2
            if value == "Feels too big":
                mapped_subratings[review_id][name] = 3


        if taggroup.getAttribute("key") == 'length':
            tag = taggroup.getElementsByTagName("tag")[0]
            value = tag.childNodes[0].nodeValue
            name = str(taggroup.getAttribute("name"))

            if value == "Feels too short":
                mapped_subratings[review_id][name] = 1
            if value == "Feels true to length":
                mapped_subratings[review_id][name] = 2
            if value == "Feels too long":
                mapped_subratings[review_id][name] = 3

    #print mapped_subratings[review_id]
    #print mapped_subratings


for review in bv_feed_parsed.getElementsByTagName("Review"):
    review_id = review.getAttribute('id').split('-')[1]
    RatingValues = bv_feed_parsed.createElement('RatingValues')
    if mapped_subratings[review_id]['Fit'] is not None:
        rating_id = 'Fit'
        rating_name = 'Fit'
        rating_value = str(mapped_subratings[review_id]['Fit'])

        RatingValue = bv_feed_parsed.createElement('RatingValue')
        append_text_node(RatingValue,"Rating",rating_value)
        RatingDimension = bv_feed_parsed.createElement('RatingDimension')
        RatingDimension.setAttribute("id",rating_id)
        RatingDimension.setAttribute("displayType","NORMAL")
        RatingDimension.setAttribute("selectedValueInDisplayEnabled","true")
        append_text_node(RatingDimension,"ExternalId",rating_id)
        append_text_node(RatingDimension,"RatingRange","3")
        append_text_node(RatingDimension,"Label",rating_name)
        append_text_node(RatingDimension,"Label1",rating_name)
        RatingValue.appendChild(RatingDimension)
        RatingValues.appendChild(RatingValue)

        review.appendChild(RatingValues)

    if mapped_subratings[review_id]['Waist'] is not None:
        rating_id = 'Waist'
        rating_name = 'Waist'
        rating_value = str(mapped_subratings[review_id]['Waist'])

        RatingValue = bv_feed_parsed.createElement('RatingValue')
        append_text_node(RatingValue,"Rating",rating_value)
        RatingDimension = bv_feed_parsed.createElement('RatingDimension')
        RatingDimension.setAttribute("id",rating_id)
        RatingDimension.setAttribute("displayType","NORMAL")
        RatingDimension.setAttribute("selectedValueInDisplayEnabled","true")
        append_text_node(RatingDimension,"ExternalId",rating_id)
        append_text_node(RatingDimension,"RatingRange","3")
        append_text_node(RatingDimension,"Label",rating_name)
        append_text_node(RatingDimension,"Label1",rating_name)
        RatingValue.appendChild(RatingDimension)
        RatingValues.appendChild(RatingValue)

        review.appendChild(RatingValues)


    if mapped_subratings[review_id]['Length'] is not None:
        rating_id = 'Length'
        rating_name = 'Length'
        rating_value = str(mapped_subratings[review_id]['Length'])

        RatingValue = bv_feed_parsed.createElement('RatingValue')
        append_text_node(RatingValue,"Rating",rating_value)
        RatingDimension = bv_feed_parsed.createElement('RatingDimension')
        RatingDimension.setAttribute("id",rating_id)
        RatingDimension.setAttribute("displayType","NORMAL")
        RatingDimension.setAttribute("selectedValueInDisplayEnabled","true")
        append_text_node(RatingDimension,"ExternalId",rating_id)
        append_text_node(RatingDimension,"RatingRange","3")
        append_text_node(RatingDimension,"Label",rating_name)
        append_text_node(RatingDimension,"Label1",rating_name)
        RatingValue.appendChild(RatingDimension)
        RatingValues.appendChild(RatingValue)

        review.appendChild(RatingValues)


# for location in bv_feed_parsed.getElementsByTagName("ReviewerLocation"):
#     loc_value = location.childNodes[0].nodeValue
#     if "REVIEW_NUMBER_FIELD_PREFIX" in location.childNodes[0].nodeValue:
#         new_loc_value = bv_feed_parsed.createTextNode(loc_value[26:])
#         location.replaceChild(new_loc_value,location.childNodes[0])
#         print loc_value

# print bv_feed_parsed.getElementsByTagName("Review")[0].toprettyxml(encoding="utf-8"),bv_feed_parsed.getElementsByTagName("Review")[0].getAttribute("id")

# print mapped_subratings["48414388"].toxml(encoding="utf-8")

output_feed.write(bv_feed_parsed.toxml(encoding='utf-8'))
