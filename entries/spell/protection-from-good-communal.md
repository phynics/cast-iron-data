+++
id = "ref/spell/protection-from-good-communal"
kind = "spell"
title = "Communal Protection from Good"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protection_from_good_communal", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/protection-from-good" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Adept", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "no; see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Adept, Arcanist, Bloodrager, Cleric, Inquisitor, Medium, Oracle, Paladin, Shaman, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: no; see text
Target: creature touched
Descriptors: good
:::

## Protection from Evil

**Sources:** PRPG Core Rulebook pg 327

This spell wards a creature from attacks by evil creatures, from mental control, and from summoned
creatures. It creates a magical barrier around the subject at a distance of 1 foot. The barrier
moves with the subject and has three major effects.

First, the subject gains a +2 deflection bonus to AC and a +2 resistance bonus on saves. Both these
bonuses apply against attacks made or effects created by evil creatures.

Second, the subject immediately receives another saving throw (if one was allowed to begin with)
against any spells or effects that possess or exercise mental control over the creature (including
enchantment \[charm\] effects and enchantment \[compulsion\] effects, such as charm person, command,
and dominate person. This saving throw is made with a +2 morale bonus, using the same DC as the
original effect. If successful, such effects are suppressed for the duration of this spell. The
effects resume when the duration of this spell expires. While under the effects of this spell, the
target is immune to any new attempts to possess or exercise mental control over the target. This
spell does not expel a controlling life force (such as a [ghost](ref/template/ghost) or spellcaster
using [magic jar](ref/spell/magic-jar)), but it does prevent them from controlling the target. This
second effect only functions against spells and effects created by evil creatures or objects,
subject to GM discretion.

Third, the spell prevents bodily contact by evil summoned creatures. This causes the natural weapon
attacks of such creatures to fail and the creatures to recoil if such attacks require touching the
warded creature. Summoned creatures that are not evil are immune to this effect. The protection
against contact by summoned creatures ends if the warded creature makes an attack against or tries
to force the barrier against the blocked creature. [Spell resistance](ref/rule/spell-resistance) can
allow a creature to overcome this protection and touch the warded creature.

### Mythic Protection from Evil

**Sources:** Mythic Adventures pg 105

The bonuses to AC and on saves increase to +4. Any evil creature attempting to possess or exercise
mental control over the target must attempt a Will save against this spell. If it fails, the
creature takes 1d6 points of damage per 2 caster levels (maximum 5d6) from mental feedback. An evil
creature that uses [spell resistance](ref/rule/spell-resistance) to bypass the spell's protection
against contact must successfully save or take this damage once each round it attacks the protected
target.

### Communal Protection from Evil

**Sources:** Ultimate Combat pg 240

This spell functions like _[protection from good](ref/spell/protection-from-good),_ except you
divide the duration in 1-minute intervals among the creatures touched.

### Protection from Chaos

**Sources:** PRPG Core Rulebook pg 327

This spell functions like _[protection from evil](ref/spell/protection-from-evil),_ except that the
deflection and resistance bonuses apply to attacks made by chaotic creatures. The target receives a
new saving throw against control by chaotic creatures and chaotic summoned creatures cannot touch
the target.

### Mythic Protection from Chaos

**Sources:** Mythic Adventures pg 104

As mythic protection from evil, except against chaotic creatures.

### Communal Protection from Chaos

**Sources:** Ultimate Combat pg 240

This spell functions like
_[communal protection from evil](ref/spell/protection-from-evil-communal),_ except it behaves like
_[protection from chaos](ref/spell/protection-from-chaos)_ and you divide the duration in 1-minute
intervals among the creatures touched.

### Protection from Good

**Sources:** PRPG Core Rulebook pg 328

This spell functions like _[protection from evil](ref/spell/protection-from-evil),_ except that the
deflection and resistance bonuses apply to attacks made by good creatures. The target receives a new
saving throw against control by good creatures and good summoned creatures cannot touch the target.

### Mythic Protection from Good

**Sources:** Mythic Adventures pg 105

As _mythic protection from evil,_ except against good creatures.

### Communal Protection from Good

**Sources:** Ultimate Combat pg 240

This spell functions like _communcal protection from evil,_ except it behaves like
_[protection from good](ref/spell/protection-from-good)_ and you divide the duration in 1-minute
intervals among the creatures touched.

### Protection from Law

**Sources:** PRPG Core Rulebook pg 328

This spell functions like _[protection from evil](ref/spell/protection-from-evil),_ except that the
deflection and resistance bonuses apply to attacks made by lawful creatures. The target receives a
new saving throw against control by lawful creatures and lawful summoned creatures cannot touch the
target.

### Mythic Protection from Law

**Sources:** Mythic Adventures pg 105

As _mythic protection from evil,_ except against lawful creatures.

### Communal Protection from Law

**Sources:** Ultimate Combat pg 240

This spell functions like
_[communal protection from evil](ref/spell/protection-from-evil-communal),_ except it behaves like
_[protection from law](ref/spell/protection-from-law)_ and you divide the duration in 1-minute
intervals among the creatures touched.
