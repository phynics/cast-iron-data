+++
id = "ref/arc-fighter/varisian-free-style-fighter"
kind = "archetype"
title = "Varisian Free-Style Fighter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Varisian%20Free-Style%20Fighter"
source_ids = ["weapon-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "varisian_free_style_fighter", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "weapon-masters-handbook"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "martial-flexibility", level = 1 },
  { anchor = "free-fighting-style", level = 3 },
]
trades = [
  { replaces = "Bonus feats gained at 1st level, 6th level, 10th level, and 12th level", feature = "bonus-feats", levels = [1, 6, 10, 12], by = ["martial-flexibility"] },
  { replaces = "weapon training", feature = "weapon-training", by = ["martial-flexibility"] },
  { replaces = "weapon mastery", feature = "weapon-mastery", by = ["martial-flexibility"] },
  { replaces = "Armor training", feature = "armor-training", by = ["free-fighting-style"] },
  { alters = "Class skills" },
]
+++

Free-style fighters are most common in Varisia, where their training—students' traveling study with
multiple teachers, or perhaps instruction in the anything-goes mentality of the Price of Freedom
school in Kaer Maga—allows them to blend fighting styles into a greater whole.

## Class Skills {#class-skills}

A Varisian free-style fighter receives Escape Artist and Knowledge (local) as class skills, but does
not receive Knowledge (dungeoneering) or Ride as class skills. This alters the fighter's class
skills.

## Martial Flexibility (Ex) {#martial-flexibility}

A Varisian free-style fighter gains martial flexibility as per the [brawler](ref/class/brawler)
class feature, treating his fighter level as his brawler level for the purposes of this ability.
This ability replaces the bonus feats gained at 1st level, 6th level, 10th level, and 12th level, as
well as weapon training and weapon mastery.

## Free Fighting Style (Ex) {#free-fighting-style}

At 3rd level, a Varisian free-style fighter can freely mix two of the styles he knows into a more
flexible style. A Varisian free-style fighter can have an additional style feat stance active
simultaneously with his first style feat stance. He can enter all of his allowed stances as a move
action or one stance as a swift action. At 11th level, a Varisian free-style fighter can have the
stances of up to two additional style feats active at the same time. At 15th level, a Varisian
free-style fighter can have the stances of up to three additional style feats active at the same
time. This ability replaces armor training.
