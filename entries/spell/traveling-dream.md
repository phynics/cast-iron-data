+++
id = "ref/spell/traveling-dream"
kind = "spell"
title = "Traveling Dream"
aon = "SpellDisplay.aspx?ItemName=Traveling%20Dream"
source_ids = ["gods-and-magic", "pathfinder-2-the-skinsaw-murders", "inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "traveling_dream", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/arcane-eye" },
]
[[sources]]
publication = "gods-and-magic"
page = "13"
[[sources]]
publication = "pathfinder-2-the-skinsaw-murders"
page = "72"

[fields]
kind = "spell"
school = "divination"
subschools = ["Scrying"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "10 minutes"
components = "V, DF"
range = "unlimited"
effects = [
  { label = "Effect", value = "magical sensor" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Cleric, Druid, Hunter, Oracle, Warpriest
Casting time: 10 minutes
Components: V, DF
Range: unlimited
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Effect: magical sensor
Subschool: Scrying
:::

This spell functions like [arcane eye](ref/spell/arcane-eye), except as noted above. Upon casting
this spell, you fall asleep for its duration, creating an invisible magic sensor (called a
dreamscryer) that is the exact size and shape of your body, is recognizable as you, and cannot pass
through spaces that your body cannot enter. Unlike the invisible sensor created by arcane eye,
children of any race (no older than the human equivalent of 10) and animals can see your
dreamscryer. Sleeping creatures can sense its presence and might incorporate your image into their
dreams. Force effects and abjuration spells that ward out creatures (such as
[magic circle against evil](ref/spell/magic-circle-against-evil)) are effective barriers against a
dreamscryer (regardless of your creature type, alignment, or other specifics). If you dismiss the
spell or the dreamscryer is dispelled or destroyed, you awaken.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
