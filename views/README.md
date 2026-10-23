---
title: views
tags: cyber, cyberia, views
alias: views, the bridge, dashboard, the views of cyberia
crystal-type: measure
crystal-domain: cyberia
---

# views

the queries of [[dev]] § the views, run by the graph itself on every render; nothing here is maintained by hand. what the graph cannot see from its pages — pull requests, the requirement counters, receipt ages, the train — a sensor writes to [[cyberia/views/sensors|sensors]] once an hour.

## verdicts waiting for the father

review tasks owned by the father and still open; the rule is fewer than five.

{{query (and (page-property :kind "review") (page-property :owner "master") (page-property :status "open"))}}

## tasks in flight

{{query (and (page-tags [[task]]) (page-property :status "doing"))}}

## tasks open

{{query (and (page-tags [[task]]) (page-property :status "open") (not (page-property :kind "review")))}}

## projects

{{query (page-tags [[project]])}}

## processes

{{query (page-tags [[process]])}}

## decisions rendered

{{query (and (page-property :kind "review") (page-property :status "done"))}}

## receipts

every audit page of the graph, newest first where the renderer sorts; the ages per product are on [[cyberia/views/sensors|sensors]].

{{query (page-tags [[audit]])}}
