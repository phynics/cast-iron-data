+++
id = "ref/subtype/blight"
kind = "rule"
title = "Blight"
source_ids = ["bestiary-6"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blight", path = "json/monster_subtypes.json" },
]

[fields]
kind = "none"
+++

## Subtype: Blight

**Sources:** Bestiary 6

A blight is an evil and intelligent [ooze](ref/type/ooze) that infects entire ecosystems. Unless
otherwise noted in a creature's entry, blights have the following traits.

- [Immunity](ref/umr/immunity) to acid, in addition to typical ooze immunities.
- **Favored Terrain (Ex):** A blight favors a specific type of terrain. Within its
  [favored terrain](ref/ability/favored-terrain), a blight gains a +2 bonus on initiative checks and
  on [Knowledge (geography)](ref/skill/knowledge-geography), [Perception](ref/skill/perception),
  [Stealth](ref/skill/stealth), and [Survival](ref/skill/survival) checks. A blight in its favored
  terrain leaves no trail and cannot be tracked (although it can choose to leave a trail). Outside
  of its favored terrain, a blight loses access to its domain of evil, rejuvenation,
  [spell-like abilities](ref/umr/spell-like-abilities), and telepathy; it also gains the
  [staggered](ref/misc/staggered) condition.
- **Cursed Domain (Su):** Blights are living epicenters for domains of evil. Once per year, a blight
  may infuse an area of its favored terrain, transforming it into a domain of evil with a radius of
  5 miles (this effect does not extend beyond the natural border of the terrain). The epicenter of
  the domain can be identified via [detect evil](ref/spell/detect-evil), for it radiates an aura of
  overwhelming evil in a 10-foot-radius. The epicenter of a blight's domain may be targeted by a
  [remove curse](ref/spell/remove-curse) effect to temporarily lift this affliction. The DC to
  remove a blight's cursed domain is equal to 10 + 1/2 the blight's Hit Dice + its Charisma
  modifier. If successful, the _[remove curse](ref/spell/remove-curse)_ effect suppresses the domain
  of evil for 1 hour per caster level, during which time the associated blight becomes
  [sickened](ref/misc/sickened). The cursed domains of multiple blights can overlap, but the effects
  do not stack-this simply makes it more difficult to remove the curse effect since there are
  multiple epicenters. Since all blights have at least 10 Hit Dice, these domains of evil always
  become strongly evil-aligned. A blight's cursed domain has open borders, and creatures can freely
  enter and leave. Unlike the typical domains of evil, animals are not particularly unsettled by a
  blight's domain of evil. While magic and time are not affected in this cursed domain, each blight
  infuses the domain with a specific hazard, as detailed in the blight's entry.
- **Rejuvenation (Su):** If a blight is slain within its cursed terrain, a new blight of the same
  type spontaneously forms in 1d10 days at the epicenter of the blight's cursed domain unless the
  blight's corpse is targeted with a _[remove curse](ref/spell/remove-curse)_ spell (DC = 10 + the
  blight's Hit Dice).
- **Spell-Like Abilities (Sp):** Once a blight establishes a cursed domain, it gains the ability to
  use a small suite of [spell-like abilities](ref/umr/spell-like-abilities) to issue commands to
  plants and animals within its domain. Once per day, a blight with a cursed domain can use the
  following spell-like abilities, once per day each, while within its domain:
  [blight](ref/spell/blight), [command plants](ref/spell/command-plants),
  [dominate monster](ref/spell/dominate-monster) (animals and magical beasts only),
  [greater curse terrain](ref/spell/curse-terrain-greater), and
  [hallucinatory terrain](ref/spell/hallucinatory-terrain). In addition, each type of blight gains
  an additional spell-like ability unique to its terrain, as indicated in the blight's stat block. A
  blight's caster level for these spell-like abilities always equals its CR.
- **Telepathy (Su):** Blights can communicate telepathically with any intelligent creature within
  their domain.
- **Vision (Ex):** Unlike most oozes, blights have eyes and can see normally. In addition, all
  blights have [blindsight](ref/umr/blindsight) to a range of 120 feet.
