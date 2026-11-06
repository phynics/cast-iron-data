+++
id = "ref/spell/curse-of-befouled-fortune"
kind = "spell"
title = "Curse of Befouled Fortune"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_of_befouled_fortune", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Antipaladin, Cleric, Oracle, Shaman, Spiritualist, Warpriest, Witch\
4: Arcanist, Bloodrager, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

**Sources:** Blood of the Beast pg 7

> _The following spell was created by [catfolk](ref/race/catfolk) and make use of their inherent
> luck._

You curse the target, making it incredibly unlucky. While affected by curse of befouled fortune, the
target can't receive luck bonuses or benefit from effects that grant it the ability to roll multiple
times and take the higher result (like the swashbuckler's charmed life ability). The target also
can't choose a die result, such as taking 10 or 20 in lieu of rolling (as per the bard's lore master
ability). Finally, the first time each turn the target would succeed at an attack, saving throw, or
skill check, it must roll twice and use the worse of the two results.

This curse cannot be dispelled, but it can be removed with a
[break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), [remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish)
spell.
