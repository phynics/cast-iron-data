+++
id = "ref/arc-cleric/cardinal"
kind = "archetype"
title = "Cardinal"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Cardinal"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cardinal", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "64"

[fields]
kind = "archetype"
features = [
  { anchor = "political-skill", level = 1 },
]
trades = [
  { replaces = "Armor proficiencies", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { replaces = "Spontaneous casting ability", feature = "spontaneous-casting", by = ["political-skill"] },
  { alters = "Domains", feature = "domains", by = ["political-skill"] },
  { alters = "class skills", by = ["political-skill"] },
  { alters = "skill ranks per level", by = ["political-skill"] },
  { alters = "base attack bonus", by = ["political-skill"] },
]
+++

While a cleric's faith is her highest priority, her church may wield significant political power in
some regions. In these cases, cardinals arise from the ranks of the clergy, engaging in the game of
intrigue on behalf of their churches. While some cardinals manage to join the world of politics and
retain the purity of their faith, many cardinals find that they must compromise some part of their
beliefs in pursuit of their church's political power, and some cardinals even fall prey to the
corrupting influence of their power.

## Armor Proficiency {#armor-proficiency}

A cardinal is proficient in light armor, but not shields.

This ability replaces the cleric's armor proficiencies.

## Political Skill {#political-skill}

A cardinal adds [Bluff](ref/skill/bluff), [Intimidate](ref/skill/intimidate),
[Knowledge (geography)](ref/skill/knowledge-geography), and
[Knowledge (local)](ref/skill/knowledge-local) to her list of class skills. She gains a number of
skill ranks equal to 6 + her Intelligence modifier at each level, instead of the normal 2 + her
Intelligence modifier. However, she gains only one domain, and her base attack bonus from cleric
levels is equal to [half](ref/misc/fractions-and-rounding) her class level (which is the same as for
a sorcerer or wizard).

This ability replaces the cleric's spontaneous casting ability. It alters the cleric's domains, as
well as her class skills, skill ranks per level, and base attack bonus.
