+++
id = "ref/spell/possession-greater"
kind = "spell"
title = "Greater Possession"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "possession_greater", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/possession" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Occultist, Spiritualist\
8: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Target: one creature
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
:::

## Possession

**Sources:** Occult Adventures pg 180

You attempt to possess a creature by projecting your soul into its body. The target creature must be
within spell range and you must know where it is, though you do not need line of sight or line of
effect to it. When you transfer your soul upon casting, your body appears to be dead. Failure to
take over a host ends the spell.

If you are successful, your life force occupies the host body. The host's soul is imprisoned with
you, but can still use its own senses (though it can't assert any influence or use even purely
mental abilities). You can communicate telepathically with the host as if you shared a common
language, but only with your consent. You keep your Intelligence, Wisdom, Charisma, level, class,
base attack bonus, base save bonuses, alignment, and mental abilities. The body retains its
Strength, Dexterity, Constitution, hit points, natural abilities, and automatic abilities. A body
with extra limbs doesn't allow you to make more attacks (or more advantageous two-weapon attacks)
than normal. You can't activate the body's extraordinary or supernatural abilities, nor can you cast
any of its spells or [spell-like abilities](ref/umr/spell-like-abilities).

As a standard action, you can shift freely back to your own body regardless of range, so long as it
remains on the same plane. If the host's body is killed, you return to your own body and the life
force of the host departs (it is dead). If your body is slain, when the spell expires or the host's
body is killed, you are slain. It is possible to cast this spell on a new target from within another
creature's body; this resets the duration. You still return to your original body (not any
intermediate body) when you take a standard action to do so or the spell's duration expires.
Returning to your body ends the spell. Creatures whose souls are their bodies, such as incorporeal
undead and non-native outsiders, use the effects of greater possession instead.

#### Possession and Magic Jar

The old [magic jar](ref/spell/magic-jar) spell is unwieldy, particularly with respect to creatures
like ghosts and shadow demons that don't really use a jar at all. Consider replacing magic jar with
the new possession spells for both spellcasters and monsters. Likewise, consider using spells based
on possession rather than magic jar.

### Greater Possession

**Sources:** Occult Adventures pg 181

This spell functions as [possession](ref/spell/possession), but when you possess a host, you enter
the host's body and your physical body vanishes. You are ejected to the closest empty square upon
expiration of the spell or upon the host's death.
