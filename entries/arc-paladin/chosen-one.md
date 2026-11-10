+++
id = "ref/arc-paladin/chosen-one"
kind = "archetype"
title = "Chosen One"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Chosen%20One"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chosen_one", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "familiar-folio"
page = "6"

[fields]
kind = "archetype"
alters = ["Divine grace", "smite evil", "Lay on hands", "channel positive energy"]
+++

Most paladins train for years at a temple to attain a holy status, but rarely, an emissary of the
divine appears to one of humble origins and calls her directly to the charge. These chosen ones may
lack experience, but their teamwork with their emissaries allows them to defeat any evil.

**Bondless**

**Info:** A chosen one does not gain the _divine bond_ class feature.

**Divine Emissary (Ex)**

**Ability:** A chosen one gains an [emissary](ref/arc-familiar/emissary)
[familiar](ref/ability/familiars), treating her paladin level as her [wizard](ref/class/wizard)
level for the purpose of this ability.

**Gained:** At 1st Level

**Religious Mentor (Ex)**

**Flavor:** The [familiar's](ref/sidekick/familiar) sworn duty is to help train the chosen one for
her future glory.

**Passive:** The familiar is treated as having a number of ranks in Knowledge (religion) equal to
the chosen one's paladin level.

**Special:** The chosen one doesn't gain Knowledge (religion) as a class skill.

**Delayed Grace (Su)**

**Alters:** Divine grace, smite evil

**Flavor:** A chosen one begins her adventuring career without fully understanding her true
potential.

**Info:** She receives the _smite evil_ ability at 2nd level and the _divine grace_ ability at 4th
level. This does not affect the rate at which she gains additional uses per day of _smite evil,_ so
she still gains her second use at 4th level, her third at 7th level, and so on.

**Passive:** The chosen one uses the Intuitive column to calculate her typical starting
[age](ref/rule/age).

**Lay on Paws (Su)**

**Ability:** The familiar can use the chosen one's _lay on hands_ ability, including all of her
mercies, but each such use consumes two uses of the paladin's _lay on hands_ ability.

**Alters:** Lay on hands, channel positive energy

**Flavor:** A chosen one's familiar is able to borrow some of her divine energy to heal itself and
others.

**At 4th Level:** The familiar can also _channel positive energy,_ but each such use consumes four
uses of the paladin's _lay on hands_ ability.

**Gained:** At 2nd Level

**True Form (Ex)**

**Ability:** A chosen one's familiar reveals its true form, transforming into an outsider
[improved familiar](ref/ability/improved-familiars) that matches the chosen one's patron's alignment
(typically an [arbiter](ref/monster/inevitable-arbiter), a [cassisian](ref/monster/angel-cassisian),
a [harbinger](ref/monster/archon-harbinger-archon), or a
[silvanshee](ref/monster/agathion-silvanshee), but potentially any lawful neutral, lawful good, or
neutral good outsider familiar depending on the patron). The familiar gains the
[change shape](ref/umr/change-shape) universal monster ability if it doesn't already have it, which
it can use at will to transform into its original form or back to its true form.

**Gained:** At 7th Level

**Emissary's Smite (Su)**

**Gained:** At 11th Level

**Passive:** A chosen one's familiar also benefits from the paladin's _smite evil_ ability whenever
the chosen one uses _smite evil._
