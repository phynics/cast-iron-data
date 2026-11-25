+++
id = "ref/arc-skald/bold-schemer"
kind = "archetype"
title = "Bold Schemer"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Bold%20Schemer"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bold_schemer", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "48"

[fields]
kind = "archetype"
features = [
  { anchor = "skald-of-twists-and-turns", level = 4 },
  { anchor = "bold-strategy", level = 10 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["skald-of-twists-and-turns"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["skald-of-twists-and-turns"] },
  { replaces = "damage reduction", feature = "damage-reduction", by = ["skald-of-twists-and-turns"] },
  { replaces = "Dirge of doom", feature = "dirge-of-doom", by = ["bold-strategy"] },
  { alters = "Class skills and bardic knowledge", feature = "bardic-knowledge" },
]
+++

The bold schemer combines wrath, wits, and daring to win battles and wars in unconventional ways,
often through infiltration and deception. If raw force of arms is insufficient, she improvises ways
to pull victory from the jaws of defeat.

## Skills {#skills}

A bold schemer gains Disable Device, Sleight of Hand, and Stealth as class skills, instead of
Knowledge (arcana), Knowledge (dungeoneering), and Knowledge (planes).

Her bardic knowledge does not apply to those skills.

This ability alters the skald's class skills and bardic knowledge.

## Skald of Twists and Turns (Su) {#skald-of-twists-and-turns}

At 4th level, a bold schemer becomes increasingly adept at infiltration and devising cunning
strategies to overcome enemy fortifications.

A bold schemer can spend 8 hours observing a physical location (such as a fortress, a walled city,
or perhaps even a section of an underground dungeon or cavern complex), contemplating methods to
infiltrate the location and engage its defenders in battle in ways that subvert their defensive
advantages.

At the end of the 8 hours, the bold schemer gains a +2 insight bonus on her Bluff, Disable Device,
Disguise, Sleight of Hand, and Stealth checks while in that same physical location. This bonus
increases by 2 at 8th level and every 4 skald levels thereafter, to a maximum of +10 at 20th level.
The bonus lasts until the bold schemer observes a new location. While observing a location, the bold
schemer must fully focus her attention; any distractions, such as engaging in combat, immediately
ends the observation and the bold schemer must start a new period of observing a physical location
to receive the bonus.

This ability replaces uncanny dodge, improved uncanny dodge, and
[damage reduction](ref/rule/damage-reduction).

## Bold Strategy (Su) {#bold-strategy}

At 10th level, a bold schemer can tailor her plans and observations so they are able to assist her
allies as well. As long as they can see or hear the bold schemer while inside the observed location,
all of her allies gain half the insight bonus she gains from the skald of twists and turns ability.

This ability replaces dirge of doom.
