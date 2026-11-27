+++
id = "ref/arc-occultist/ancestral-aspirant"
kind = "archetype"
title = "Ancestral Aspirant"
aon = "ArchetypeDisplay.aspx?FixedName=Occultist%20Ancestral%20Aspirant"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ancestral_aspirant", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "67"

[fields]
kind = "archetype"
features = [
  { anchor = "family-jewels", level = 1 },
  { anchor = "emotional-reading", level = 2 },
  { anchor = "courtly-contacts", level = 8 },
]
trades = [
  { replaces = "Object reading", feature = "object-reading", by = ["emotional-reading"] },
  { replaces = "Outside contact", feature = "outside-contact", by = ["courtly-contacts"] },
  { alters = "Implements", feature = "implements", by = ["family-jewels"] },
  { alters = "Class skills" },
]
+++

It is common for a noble to possess a deep pride for his family's past, but when such
self-importance gives way to obsession, an ancestral aspirant is born. Ancestral aspirants perform
all the typical social functions of a noble, but they fill their conversations with stories of the
great deeds of their family forebears, and they spend their nights researching old histories and
primary sources, hungry for more.

## Class Skills {#class-skills}

An ancestral aspirant adds Bluff and Knowledge (nobility) to his list of class skills, instead of
Knowledge (planes) and Profession.

This alters the occultist's class skills.

## Family Jewels {#family-jewels}

An ancestral aspirant's implements are always objects connected to his family history. One of his
starting implements must be an implement from the [enchantment](ref/implement/enchantment) school.

This ability alters implements.

## Emotional Reading (Su) {#emotional-reading}

An ancestral aspirant doesn't care much about objects that didn't belong to his ancestors, but he is
keenly attuned to his relatives and fellow nobles, allowing him to read the emotions of others. If
he spends 1 minute examining a creature, he learns one fact, chosen by the GM, about the creature's
current emotions. Since emotional auras are complex, this ability is unlikely to reveal the secret
feelings of a professional spy; instead, it only touches upon surface emotions.

This ability replaces object reading.

## Courtly Contacts (Su) {#courtly-contacts}

Ancestral aspirants have contacts among courtly circles rather than otherworldly circles. This works
similarly to outside contact except for the following differences: First, he doesn't need to use a
[magic circle](ref/spell/magic-circle) or make a payment (though he still expends 1 point of mental
focus from his enchantment implement). Second, he can use those contacts to gather information for
him (as per the Diplomacy skill to gather information) without spending the time himself, rather
than asking a question and receiving a result similar to a _divination_. He can ask more questions
over the same time period at 12th level and every 4 levels thereafter, as normal with outside
contact. At 16th level, instead of delivering messages and objects, the courtly contacts can spread
vicious rumors and gossip about a target throughout a settlement, causing any creatures in the
settlement whose attitude toward the target wasn't helpful to have its attitude toward the target
worsened by one step. These baseless rumors last 1 week or until the target spends 8 hours refuting
them and succeeds at a Diplomacy check (DC = 10 + the ancestral aspirant's occultist level + his
Intelligence modifier).

This ability replaces outside contact.
