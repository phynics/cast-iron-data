+++
id = "ref/spell/dispel-magic"
kind = "spell"
title = "Dispel Magic"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dispel_magic", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "272"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target or Area", value = "one spellcaster, creature, or object" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Antipaladin, Arcanist, Bard, Cleric, Inquisitor, Magus, Medium, Mesmerist, Occultist, Oracle, Paladin, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Witch, Wizard\
4: Druid, Hunter
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target or Area: one spellcaster, creature, or object
:::

You can use dispel magic to end one ongoing spell that has been cast on a creature or object, to
temporarily suppress the magical abilities of a magic item, or to counter another spellcaster's
spell. A dispelled spell ends as if its duration had expired. Some spells, as detailed in their
descriptions, can't be defeated by dispel magic. Dispel magic can dispel (but not counter)
spell-like effects just as it does spells. The effect of a spell with an instantaneous duration
can't be dispelled, because the magical effect is already over before the dispel magic can take
effect.

You choose to use dispel magic in one of two ways: a targeted dispel or a counterspell.

_Targeted Dispel:_ One object, creature, or spell is the target of the dispel magic spell. You make
one dispel check (1d20 + your caster level) and compare that to the spell with highest caster level
(DC = 11 + the spell's caster level). If successful, that spell ends. If not, compare the same
result to the spell with the next highest caster level. Repeat this process until you have dispelled
one spell affecting the target, or you have failed to dispel every spell.

For example, a 7th-level caster casts dispel magic, targeting a creature affected by stoneskin
(caster level 12th) and fly (caster level 6th). The caster level check results in a 19. This check
is not high enough to end the stoneskin (which would have required a 23 or higher), but it is high
enough to end the fly (which only required a 17). Had the dispel check resulted in a 23 or higher,
the stoneskin would have been dispelled, leaving the fly intact. Had the dispel check been a 16 or
less, no spells would have been affected.

You can also use a targeted dispel to specifically end one spell affecting the target or one spell
affecting an area (such as a wall of fire). You must name the specific spell effect to be targeted
in this way. If your caster level check is equal to or higher than the DC of that spell, it ends. No
other spells or effects on the target are dispelled if your check is not high enough to end the
targeted effect.

If you target an object or creature that is the effect of an ongoing spell (such as a monster
summoned by summon monster), you make a dispel check to end the spell that conjured the object or
creature.

If the object that you target is a magic item, you make a dispel check against the item's caster
level (DC = 11 + the item's caster level). If you succeed, all the item's magical properties are
suppressed for 1d4 rounds, after which the item recovers its magical properties. A suppressed item
becomes nonmagical for the duration of the effect. An interdimensional opening (such as a bag of
holding) is temporarily closed. A magic item's physical properties are unchanged: A suppressed magic
sword is still a sword (a masterwork sword, in fact). Artifacts and deities are unaffected by mortal
magic such as this.

You automatically succeed on your dispel check against any spell that you cast yourself.

_Counterspell:_ When dispel magic is used in this way, the spell targets a spellcaster and is cast
as a counterspell. Unlike a true counterspell, however, dispel magic may not work; you must make a
dispel check to counter the other spellcaster's spell.
