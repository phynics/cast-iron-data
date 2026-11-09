+++
id = "ref/spell/sympathetic-wounds"
kind = "spell"
title = "Sympathetic Wounds"
aon = "SpellDisplay.aspx?ItemName=Sympathetic%20Wounds"
source_ids = ["gods-and-magic", "inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sympathetic_wounds", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shield-other" },
]
[[sources]]
publication = "gods-and-magic"
page = "43"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["evil"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (250 gp of powdered amber)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "will negates"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Cleric, Druid, Hunter, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M (250 gp of powdered amber)
Range: close (25 ft. + 5 ft./2 levels)
Duration: will negates
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: evil
:::

This spell functions like [shield other](ref/spell/shield-other), except some of your wounds
transfer to the targeted creature rather than some of their wounds transferring to you. For example,
you could link yourself to a nearby chained slave so that when you are wounded, some of the damage
is transferred to the slave. You must have at least as many hit dice as the target, otherwise the
spell fails. A creature can only be under the effects of one instance of this spell at a time.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
