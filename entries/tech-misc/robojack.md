+++
id = "ref/tech-misc/robojack"
kind = "item"
title = "Robojack"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "robojack", path = "json/equipment_tech_misc.json" },
]

[fields]
kind = "item"
category = "Technological Gear"
price = "30,000 gp"
weight = "3 lbs."
slot = "none"
+++

**Sources:** Technology Guide pg 51\
**Price** 30,000 gp\
**Slot** none; **Weight** 3 lbs.\
**Capacity** 10; **Usage** 1 charge

### Construction

**Craft DC** 29; **Cost** 15,000 gp\
[Craft Technological Item](ref/feat/craft-technological-item),
[military lab](ref/rule/crafting-laboratories)

A robojack is a strange, rod-like device that can be used to usurp control of an otherwise
functional robot. In order to gain control of a robot, the wielder must first make a ranged touch
attack against a target robot within a range of 60 feet. If the attack is successful, the robot must
succeed at a DC 14 Will saving throw to prevent the robojack from linking to the robot's command
processor. On a subsequent turn after a link is established, the wielder can issue a command to the
robot as a standard action - each attempt to do so consumes 1 charge from the robojack, and the
robot gets a new DC 14 Will saving throw to resist following each command. The wielder must be
within 60 feet of the robot and must issue the command in a language understood by the robot. The
types of commands he can issue are similar to those allowed by a [suggestion](ref/spell/suggestion)
spell - once a command is successfully issued, the robot does its best to carry out the orders over
the course of the next hour. This does not drain further charges from the robojack.
