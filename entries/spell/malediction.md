+++
id = "ref/spell/malediction"
kind = "spell"
title = "Malediction"
source_ids = ["book-of-the-damned", "book-of-the-damned-volume-1-princes-of-darkness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "malediction", path = "json/spells6.json" },
]
[[sources]]
publication = "book-of-the-damned"
page = "184"
[[sources]]
publication = "book-of-the-damned-volume-1-princes-of-darkness"
page = "46"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse", "evil"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "1 creature touched" },
]
duration = "1 minute and instantaneous (see text)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin, Cleric, Oracle, Shaman, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute and instantaneous (see text)
Saving throw: Will negates
Spell resistance: yes
Target: 1 creature touched
Descriptors: curse, evil
:::

Channeling the blasphemy of fiends into your hand, you mark your target with a brief but fundamental
corruption, causing its soul to be irretrievably damned should it die within the next minute. If you
are lawful evil, souls are sent to Hell. If you are neutral evil, souls are sent to Abaddon. If you
are chaotic evil, souls are sent to the Abyss.

A target killed while under the effect of this spell cannot be resurrected by normal means. Only a
worshiper of a deity or demigod of your alignment can return a soul damned by malediction to life
without difficulty. Other spellcasters must succeed at a caster level check (DC = 10 + your caster
level) to restore to life a creature slain while under the effects of malediction. Miracle or wish
can return the victim of a malediction to life without requiring a caster level check.

A soul can also be freed by the efforts of someone bodily going to the appropriate plane, locating
the affected soul, and leading it out of the plane, which allows it to go to its intended
destination in the afterlife and be resurrected as normal. You can end the effects of your own
malediction by casting the spell again and concentrating on a past target. Doing so only frees the
past target to go to its rightful place in death; it does not return the target to life.

Spells such as [break enchantment](ref/spell/break-enchantment),
[dispel magic](ref/spell/dispel-magic), and [remove curse](ref/spell/remove-curse) negate this spell
if successfully cast before the target dies.
