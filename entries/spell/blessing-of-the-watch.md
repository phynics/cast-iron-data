+++
id = "ref/spell/blessing-of-the-watch"
kind = "spell"
title = "Blessing of the Watch"
source_ids = ["inner-sea-gods", "pathfinder-8-seven-days-to-the-grave", "gods-and-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blessing_of_the_watch", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bless" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "50 ft."
effects = [
  { label = "Area", value = "The caster and all allies within a 50-ft. burst, centered on the caster" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: 50 ft.
Duration: 1 hour/level
Saving throw: none
Spell resistance: yes
Area: The caster and all allies within a 50-ft. burst, centered on the caster
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Inner Sea Gods pg 230, Pathfinder \#8: Seven Days to the Grave pg 71, Gods and Magic pg
5

This spell functions like [bless](ref/spell/bless), except as noted. It works only in the caster's
home city, and in areas under the jurisdiction of the city watch. For example, if the watch patrols
a shantytown outside the city walls but not the ruined subterranean tunnels that lie beneath the
city, the spell works in the former area but not the latter.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
