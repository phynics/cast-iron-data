+++
id = "ref/rule/control-devices"
kind = "rule"
title = "Control Devices"
source_ids = ["skull-and-shackles-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "control_devices", path = "json/rules_campaign_types10.json" },
]
[[sources]]
publication = "skull-and-shackles-players-guide"
page = "10"

[fields]
kind = "none"
+++

Every vehicle has a control device for steering. A control device is typically an object with object
immunities and resistances and with its own statistics. The following are some of the typical
control devices for ships, plus their usual Armor Class, hit points, and
[hardness](ref/umr/hardness). When a control device gains the broken condition, all sailing checks
take a -10 penalty. When a control device is destroyed, a ship cannot be piloted until the control
device is repaired.

|Control Device|AC|Hit Points|Hardness|
| --- | --- | --- | --- |
|Oars^[1](ref/rule/control-devices#footnote-o)^|12|10 per oar|5|
|Steering|wheel 10|25|5|
|Tiller|10|25|5|
|Magically treated^[2](ref/rule/control-devices#footnote-m)^|—|×2|×2|

###### ^1^ {#footnote-o}

Oars gain the broken condition if at least half the oars on a ship are destroyed.

###### ^2^ {#footnote-m}

More information on magically treated control devices can be found in
[Ship Modifications](ref/rule/ship-modifications).
