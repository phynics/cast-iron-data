+++
id = "ref/spell/dahaks-release"
kind = "spell"
title = "Dahak's Release"
aon = "SpellDisplay.aspx?ItemName=Dahak%27s%20Release"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dahaks_release", path = "json/spells3.json" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "28"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["draconic", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a dried drop of blood)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Arcanist, Mesmerist, Occultist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a dried drop of blood)
Range: touch
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Subschool: Compulsion
Descriptors: draconic, mind-affecting
:::

You unleash all the target's anger and destructive urges, causing it to fly into a violent
bloodlust. The target attacks creatures as determined by the following table. If a creature is
killed or the target is for some reason unable to effectively attack it, roll on the table again to
select a new action for the target.

|d%|Behavior|
| --- | --- |
|01-25|Target attacks the creature nearest to it.|
|26-75|Target attacks its nearest ally.|
|76-100|Target always attacks the last creature to attack it.|

Beginning on its next turn, the target attacks the subject determined by the chart with a melee
weapon, natural weapon, or supernatural ability that deals damage. If necessary, it moves to or
charges to the subject in order to make this attack. If it is unable to reach its subject on its
next turn, the target uses its turn to get as close as possible to the subject of its bloodlust. The
target gains a +2 morale bonus on attack and damage rolls, and cannot use any Charisma-, Dexterity-,
or Intelligence-based skills (except Acrobatics, Fly, Intimidate, and Ride) or any abilities that
require patience or concentration. This spell is otherwise treated as confusion and rage-any
creature immune to confusion or rage is immune to this spell, and any ability or effect that ends
confusion or rage (such as calm emotions) can end this spell.

Antipaladins, bloodragers, clerics, and inquisitors who worship Dahak add Dahak's release to their
spell lists as a 4th-level spell.
