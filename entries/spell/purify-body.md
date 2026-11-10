+++
id = "ref/spell/purify-body"
kind = "spell"
title = "Purify Body"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "purify_body", path = "json/spells15.json" },
]
[[sources]]
publication = "healers-handbook"
page = "9"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous and 1 hour or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Alchemist, Cleric, Medium, Oracle, Paladin, Warpriest\
5: Psychic
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous and 1 hour or until discharged
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
Subschool: Healing
:::

You align the target's chakras and soothe any unwanted imperfections found within its physical form,
leaving its body pristine and without any pain or weakness.

You restore a number of hit points to the creature equal to 3d8 + 1 per caster level (maximum +20).
If the healing would cause the target to exceed its maximum hit points, the target immediately gains
half the excess healing from this spell as temporary hit points that last for 1 hour. These
temporary hit points are lost first when the target takes damage (although some temporary hit points
are lost even before these temporary hit points, such as the temporary hit points from the shell of
succor oracle mystery or the shell of succor hex granted by the restoration spirit specialization).

This spell also ends any pain effects, removes all physical ability score damage (from Strength,
Dexterity, and Constitution), and removes the following conditions: blinded, dazzled, deafened,
nauseated, paralyzed, and sickened.
