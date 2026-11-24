+++
id = "ref/arc-hunter/divine-hunter"
kind = "archetype"
title = "Divine Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Divine%20Hunter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_hunter", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "advanced-class-guide"
page = "95"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "domain", level = 3 },
  { anchor = "otherworldly-companion", level = 3 },
]
trades = [
  { replaces = "Teamwork feats", feature = "teamwork-feat", by = ["domain"] },
  { replaces = "Hunter tactics", feature = "hunter-tactics", by = ["otherworldly-companion"] },
]
+++

While most hunters heed the call of nature and fight to protect its bounty, some are inspired to
serve a higher power. These divine hunters use faith to aid them in their struggles, and their faith
infuses their animal companions, making these companions champions of their deities.

**Prerequisites:** A divine hunter's alignment must be within one step of her deity's, along either
the law/chaos axis or the good/evil axis. A divine hunter can otherwise be of any alignment.

**Gained class skills:** kr

**Lost class skills:** kd

## Alignment {#alignment}

A divine hunter's alignment must be within one step of her deity's, along either the law/chaos axis
or the good/evil axis. A divine hunter can otherwise be of any alignment.

## Class Skills {#class-skills}

A divine hunter gains Knowledge (religion) as a class skill, but she does not gain Knowledge
(dungeoneering) as a class skill.

## Domain {#domain}

At 3rd level, a divine hunter learns to call upon the power of her deity. The divine hunter must
select one [domain](ref/ability/domains) from those available to her deity. She gains the granted
powers of this domain, using her hunter level - 2 as her cleric level for determining when the
powers are gained and what effects they have. Once she chooses this domain, it cannot be changed.

If the divine hunter selects the [animal](ref/domain/animal) domain, she does not gain a second
animal companion upon reaching an effective cleric level of 4th. When the divine hunter would gain
that ability, her animal companion instead gains two ability score increases (gaining +1 to two
different ability scores or +2 to one ability score). If her animal companion dies or is released,
when she gains a new one, it benefits from this ability score increase.

In addition, the divine hunter adds the 1st-level domain spell from her domain to her list of spells
known. She adds the 2nd-level domain spell at 6th level, the 3rd-level domain spell at 9th level,
the 4th-level domain spell at 12th level, the 5th-level domain spell at 15th level, and the
6th-level domain spell at 18th level.

This ability replaces teamwork feats.

## Otherworldly Companion (Su) {#otherworldly-companion}

At 3rd level, a hunter's companion takes on otherworldly features. If the divine hunter is good (or
worships a good deity), the animal companion gains the [celestial template](ref/template/celestial).
If the hunter is evil (or worships an evil deity), the animal companion gains the
[fiendish template](ref/template/fiendish). If the hunter is neutral and worships a neutral deity,
she must choose either the celestial or fiendish template; once this choice is made, it cannot be
changed. The companion's CR is considered to be equal to its Hit Dice for the purpose of the
celestial or fiendish template. This ability replaces hunter tactics.
