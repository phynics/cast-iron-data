+++
id = "ref/spell/detect-scrying"
kind = "spell"
title = "Detect Scrying"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_scrying", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of mirror and a miniature brass hearing trumpet)"
range = "40 ft."
effects = [
  { label = "Area", value = "40-ft.-radius emanation centered on you" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Medium\
4: Arcanist, Bard, Inquisitor, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of mirror and a miniature brass hearing trumpet)
Range: 40 ft.
Duration: 24 hours
Saving throw: none
Spell resistance: no
Area: 40-ft.-radius emanation centered on you
:::

**Sources:** PRPG Core Rulebook pg 268

You immediately become aware of any attempt to observe you by means of a divination (scrying) spell
or effect. The spell's area radiates from you and moves as you move. You know the location of every
magical sensor within the spell's area.

If the scrying attempt originates within the area, you also know its location; otherwise, you and
the scrier immediately make opposed caster level checks (1d20 + caster level). If you at least match
the scrier's result, you get a visual image of the scrier and an accurate sense of his direction and
distance from you.

### Mythic Detect Scrying

**Sources:** Mythic Adventures pg 90\
This spell automatically gives you a visual image of the creature scrying you. If it's using a
non-mythic means of scrying, you also gain an accurate sense of its direction and distance from you.
You automatically succeed at caster level checks to overcome nondetection or similar effects (other
than mind blank) that block your ability to detect the creature.

If you learn the creature's direction and distance with this spell, you can, as an immediate action,
cast a mind-affecting spell through the scrying sensor to target the creature. This spell affects
only the scrying creature, even if the spell normally affects an area or multiple targets. You must
expend a number of uses of mythic power equal to the level of the spell you wish to cast against the
creature.

_Augmented (6th):_ If you expend two uses of mythic power, even mind blank doesn't prevent you from
detecting the scrying creature. If you teleport to the creature's location within 1 minute, you
arrive on target (with no chance of error) and bypass non-mythic effects that block teleportation.
Alternatively, you can compel the creature to attempt to teleport to you within 1 minute (Will
negates, DC equal to 10 plus double your tier). It must use its own means of teleportation to do so,
but you guarantee it arrives on target and bypasses non-mythic effects that block teleportation to
your location.
