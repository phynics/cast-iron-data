+++
id = "ref/spell/lash-of-the-astradaemon"
kind = "spell"
title = "Lash of the Astradaemon"
aon = "SpellDisplay.aspx?ItemName=Lash%20of%20the%20Astradaemon"
source_ids = ["book-of-the-damned", "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lash_of_the_astradaemon", path = "json/spells6.json" },
]
[[sources]]
publication = "book-of-the-damned"
page = "184"
[[sources]]
publication = "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"
page = "38"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Magus", level = 5 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Magus\
6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: Fortitude negates (see text)
Spell resistance: yes
Effect: see text
Descriptors: evil
:::

You draw on the essence of astradaemons to cause one of your hands to elongate and sprout fearsome
translucent claws that radiate a cold phosphorescence. You gain one claw attack, which is a primary
natural attack that deals 1d6 points of slashing damage on a hit (1d4 for a Small spellcaster) and
forces the creature struck to succeed at a Fortitude save against the spell
([spell resistance](ref/rule/spell-resistance) applies) to resist gaining 1 negative level. Each
time you inflict a negative level with this spell, you gain 5 temporary hit points that persist for
1 hour. A creature that succeeds at the saving throw against your claw's negative level is immune to
further negative levels inflicted from this casting of lash of the astradaemon but not to the claw's
damage. The claw does not interfere with your ability to cast spells or perform other actions that
require hands. You can use your claw attack up to 1 time per 2 caster levels. Your claw reverts to a
normal hand once you've delivered all of your potential attacks or after 24 hours (whichever comes
first).
