+++
id = "ref/spell/invisibility-greater"
kind = "spell"
title = "Greater Invisibility"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invisibility_greater", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/invisibility" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal or touch"
effects = [
  { label = "Target", value = "you or creature touched" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Medium, Summoner\
4: Alchemist, Antipaladin, Arcanist, Bard, Inquisitor, Investigator, Magus, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Spiritualist, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal or touch
Target: you or creature touched
Duration: 1 round/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Glamer
Descriptors: glamer
:::

## Invisibility

**Sources:** PRPG Core Rulebook pg 301

The creature or object touched becomes invisible. If the recipient is a creature carrying gear, that
vanishes, too. If you cast the spell on someone else, neither you nor your allies can see the
subject, unless you can normally see invisible things or you employ magic to do so.

Items dropped or put down by an invisible creature become visible; items picked up disappear if
tucked into the clothing or pouches worn by the creature. Light, however, never becomes invisible,
although a source of light can become so (thus, the effect is that of a light with no visible
source). Any part of an item that the subject carries but that extends more than 10 feet from it
becomes visible.

Of course, the subject is not magically silenced, and certain other conditions can render the
recipient detectable (such as swimming in water or stepping in a puddle). If a check is required, a
stationary invisible creature has a +40 bonus on its Stealth checks. This bonus is reduced to +20 if
the creature is moving. The spell ends if the subject attacks any creature. For purposes of this
spell, an attack includes any spell targeting a foe or whose area or effect includes a foe. Exactly
who is a foe depends on the invisible character's perceptions. Actions directed at unattended
objects do not break the spell. Causing harm indirectly is not an attack. Thus, an invisible being
can open doors, talk, eat, climb stairs, summon monsters and have them attack, cut the ropes holding
a rope bridge while enemies are on the bridge, remotely trigger traps, open a portcullis to release
attack dogs, and so forth. If the subject attacks directly, however, it immediately becomes visible
along with all its gear. Spells such as bless that specifically affect allies but not foes are not
attacks for this purpose, even when they include foes in their area.

Invisibility can be made permanent (on objects only) with a [permanency](ref/spell/permanency)
spell.

### Mythic Invisibility

**Sources:** Mythic Adventures pg 99

The invisible target can't be detected with [detect magic](ref/spell/detect-magic) or other spells
that detect magic auras. The invisibility can't be penetrated, revealed, or dispelled by spells of
2nd level or lower (such as see invisibility or glitterdust), though true seeing and dust of
appearance can reveal the invisible target's presence.

_Augmented (3rd):_ If you expend two uses of mythic power, the invisible target is undetectable by
[blindsense](ref/rule/blindsight-and-blindsense), blindsight, scent, and
[tremorsense](ref/umr/tremorsense).

### Greater Invisibility

**Sources:** PRPG Core Rulebook pg 302

This spell functions like [invisibility](ref/spell/invisibility), except that it doesn't end if the
subject attacks.

### Mass Invisibility

**Sources:** PRPG Core Rulebook pg 302

This spell functions like invisibility, except that the effect moves with the group and is broken
when anyone in the group attacks. Individuals in the group cannot see each other. The spell is
broken for any individual who moves more than 180 feet from the nearest member of the group. If only
two individuals are affected, the one moving away from the other one loses its invisibility. If both
are moving away from each other, they both become visible when the distance between them exceeds 180
feet.
