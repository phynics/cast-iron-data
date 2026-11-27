+++
id = "ref/arc-occultist/psychodermist"
kind = "archetype"
title = "Psychodermist"
aon = "ArchetypeDisplay.aspx?FixedName=Occultist%20Psychodermist"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychodermist", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "trophies", level = 1 },
  { anchor = "monster-hunting-lore", level = 2 },
  { anchor = "discern-death", level = 2 },
  { anchor = "seek-prey", level = 5 },
  { anchor = "residual-hatred", level = 8 },
  { anchor = "manifest-abilities", level = 12 },
]
trades = [
  { replaces = "Magic item skill", feature = "magic-item-skill", by = ["monster-hunting-lore"] },
  { replaces = "Object reading", feature = "object-reading", by = ["discern-death"] },
  { replaces = "Aura sight", feature = "aura-sight", by = ["seek-prey"] },
  { replaces = "Outside contact", feature = "outside-contact", by = ["residual-hatred"] },
  { replaces = "Binding circles", feature = "binding-circles", by = ["manifest-abilities"] },
  { replaces = "fast circles", feature = "fast-circles", by = ["manifest-abilities"] },
  { alters = "Implements", feature = "implements", by = ["trophies"] },
  { alters = "Class skills" },
]
+++

Rather than tapping the psychic energy residing within esoteric items, psychodermists form
supernatural bonds with trophies taken from creatures they have slain. Through these mementos, these
occultists manifest not only their own magic, but also the unique powers of their fallen foes.

## Class Skills {#class-skills}

A psychodermist loses Disable Device, Knowledge (engineering), Knowledge (history), and Sleight of
Hand as class skills, and adds Heal, Knowledge (nature), Knowledge (local), and Survival as class
skills.

This alters the occultist's class skills.

## Trophies (Su) {#trophies}

At 1st level, a psychodermist learns how to siphon power from pieces of creatures he has slain. The
psychodermist gains [Harvest Parts](ref/feat/harvest-parts) as a bonus feat, and he can select one
monster part per implement school he knows to become a permanently preserved trophy so long as it
remains in his possession. Each trophy functions as the psychodermist's implement for its associated
implement school. A trophy that fits multiple implement categories, such as a hand with clawed
fingers, can function for only one implement school at a time. A trophy can be integrated into
another item, such as an ornament or a magic item, but otherwise does not take up a magic item slot,
even when worn. A psychodermist can replace trophies with new ones harvested from slain foes,
although doing so causes the old trophies to rot at their normal rate. In order to craft a trophy,
the psychodermist must have been present during the creature's death.

This ability alters implements.

### Trophies {#trophies-box}

Psychodermists use the following monster parts for each implement school.

**Abjuration:** Chitin, hides, scales, and other natural armor.

**Conjuration:** Gizzards, glands, hearts, livers, and other internal organs.

**Divination:** Ears, eyes, tongues, and other sensory organs.

**Enchantment:** Feathers, fur, hair, spines, and other decorative features.

**Evocation:** Claws, fangs, horns, and other natural weapons.

**Illusion:** Fingers, tendrils, toes, and other prehensile digits.

**Necromancy:** Bones, bile, and life-sustaining fluids, such as blood.

**Transmutation:** Feet, hands, paws, wings, and other appendages tied to locomotion.

## Monster Hunting Lore (Ex) {#monster-hunting-lore}

At 2nd level, a psychodermist gains a bonus equal to half his occultist level on skill checks made
to craft trophies and Knowledge checks made to identify the abilities and weaknesses of creatures.

This ability replaces magic item skill.

## Discern Death (Su) {#discern-death}

At 2nd level, as a full-round action that provokes attacks of opportunity, a psychodermist can glean
information from a creature's corpse. The psychodermist must study at least one drop of the
creature's blood, a small portion of its flesh, or a fragment of one of its bones as a part of this
action. This ability otherwise functions as _[blood biography](ref/spell/blood-biography)_, using
the psychodermist's occultist level as his caster level. The psychodermist can use this ability once
per day at 2nd level, plus one additional time per day for every 3 levels beyond 2nd.

This ability replaces object reading.

## Seek Prey (Su) {#seek-prey}

At 5th level, a psychodermist can supernaturally detect creatures around him as a standard action.
This functions as the spell _[aura sight](ref/spell/aura-sight)_, except the duration is 1 round and
the psychodermist learns the locations and power of all auras of a specific creature type, similar
to _[detect undead](ref/spell/detect-undead)_ except the psychodermist can choose any creature type
represented among the trophies he has selected for that day.

This ability replaces aura sight.

## Residual Hatred (Su) {#residual-hatred}

At 8th level, a psychodermist can tap into the psychic death throes of the monsters his trophies are
derived from, increasing his efficiency at slaying similar beasts. The psychodermist can spend
mental focus invested in a trophy to gain the ranger's [favored enemy](ref/ability/favored-enemy)
class feature against the kind of creature from which the trophy was crafted. The favored enemy
bonus applies against the specific creature variety, not the creature type; a psychodermist could
use a red dragon scale trophy to gain favored enemy (red dragon), but not favored enemy (dragon).
Each point of mental focus spent grants a cumulative +2 favored enemy bonus, with a maximum bonus
equal to +2 for every 5 psychodermist levels he has. This benefit lasts until the psychodermist
regains his mental focus.

This replaces outside contact.

## Manifest Abilities (Su) {#manifest-abilities}

At 12th level, a psychodermist can use the latent energy within his trophies to replicate his
victims' special abilities. As a standard action, he can spend 1 point of mental focus invested in a
trophy to gain one of that creature's special abilities that could be granted by the spell
_[monstrous physique III](ref/spell/monstrous-physique-3)_. At 16th level, the psychodermist adds
abilities offered by _[monstrous physique IV](ref/spell/monstrous-physique-4)_ to the options he can
select using this ability. The saving throw DC for these special abilities is equal to 10 + half the
psychodermist's level + his Intelligence modifier.

Alternatively, he can spend 1 point of mental focus as a standard action to add any two of the
creature's [spell-like abilities](ref/umr/spell-like-abilities) to his list of spells known. To
determine the spell's level for this ability, use the level as it appears on the spell list for an
occultist, wizard, or cleric, in that order; if it appears on none of those lists, use the spell's
highest spell level. For example, _[lesser restoration](ref/spell/restoration-lesser)_ would be a
2nd-level spell, despite appearing on the paladin's 1st-level list.

Both uses of this ability last for 1 minute per psychodermist level. He can instead spend 2 points
of mental focus to activate this ability as a move action, or 3 points to activate it as a swift
action.

This replaces binding circles and fast circles.
