+++
id = "ref/arc-kineticist/blightburner"
kind = "archetype"
title = "Blightburner"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Blightburner"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blightburner", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "earth-focus", level = 1 },
  { anchor = "blightburn-manipulation" },
  { anchor = "radiation-absorption", level = 2 },
  { anchor = "blightburn-aura", level = 2 },
  { anchor = "radiation-resistance", level = 6 },
]
trades = [
  { replaces = "Basic geokinesis wild talent gained from elemental focus", feature = "elemental-focus", power = "basic utility wild talent", by = ["blightburn-manipulation"] },
  { replaces = "Utility wild talent gained at 2nd level", feature = "wild-talents", levels = [2], by = ["radiation-absorption"] },
  { replaces = "Ability score boosts granted by elemental overflow", feature = "elemental-overflow", by = ["blightburn-aura"] },
  { replaces = "earth's elemental defense", feature = "elemental-defense", by = ["blightburn-aura"] },
  { alters = "Elemental focus", feature = "elemental-focus", by = ["earth-focus"] },
  { alters = "Gather power", feature = "gather-power", by = ["radiation-resistance"] },
  { alters = "internal buffer", feature = "internal-buffer", by = ["radiation-resistance"] },
]
+++

Darklands geokineticists sometimes exhibit supernatural powers associated with
[blightburn](ref/eq-material/blightburn) crystals. Blightburner kineticists harness this
radioactivity in pyrotechnic displays, an unusual feat for those connected to the element of earth.

## Earth Focus {#earth-focus}

A blightburner must choose earth as her [elemental](ref/ability/elements) focus.

This alters elemental focus.

## Blightburn Manipulation (Su) {#blightburn-manipulation}

A blightburner can harness radiation for nondestructive purposes. A blightburner can channel
blightburn radiation as a standard action, causing herself to glow like a
[torch](ref/eq-misc/torch). This effect lasts until she dismisses it as a standard action.
Additionally, she can generate small amounts of heat with her hands. This radiation can slowly heat
unattended objects with a touch to a warm (but not painfully hot) temperature, or cook raw meat or
vegetable matter at a rate of 1 pound per minute. If used on a living creature, this ability deals 1
point of nonlethal damage per minute of contact, which manifests as reddened and blistering skin.

This ability replaces the basic geokinesis wild talent gained from elemental focus.

## Radiation Absorption (Su) {#radiation-absorption}

At 2nd level, whenever a blightburner would take [ability damage](ref/rule/ability-damage-drain)
from radiation, she can accept 1 point of burn to reduce the ability damage by 4 points. Any
remaining ability damage is applied normally.

This replaces the utility wild talent gained at 2nd level.

## Blightburn Aura (Su) {#blightburn-aura}

At 2nd level, a blightburner's body surges with a greenish, radioactive glow whenever she accepts
burn. This energy sheds light like a [candle](ref/eq-misc/candle). A creature that hits the
blightburner with a natural attack, unarmed strike, or non-reach melee weapon attack while she's
under the effect of her blightburn aura takes fire damage equal to her elemental overflow bonus
(minimum 1). By accepting 2 points of burn, she can increase this damage by an amount equal to her
elemental overflow bonus; she can increase the damage in this way up to four times. A blightburner
can temporarily suppress the visual effects of a blightburn aura by concentrating for 1 full round,
but doing so also suppresses all of this ability's other benefits. The next time she uses a wild
talent, the visual effects and benefits return instantly.

At 6th level, whenever the blightburner has at least 3 points of burn, the blightburn aura expands
to fill all adjacent squares. In addition to damaging creatures that hit the blightburner with melee
attacks, the aura also deals damage to other creatures that end their turns within the aura.

At 11th level, whenever the kineticist has at least 5 points of burn, the blightburn aura expands to
a 10-foot-radius aura, and any creature that takes damage from it must also succeed at a Fortitude
save (DC = 10 + half the blightburner's level + her Constitution bonus) or be
[sickened](ref/misc/sickened) for 1 round. This ability is a poison effect.

At 16th level, whenever a blightburner has at least 7 points of burn, any creature that takes damage
from the blightburn aura and fails its Fortitude save also become [fatigued](ref/misc/fatigued).

This ability replaces the ability score boosts granted by elemental overflow and earth's elemental
defense, but the blightburner can still gain elemental defenses from other elements with expanded
defense.

## Radiation Resistance (Su) {#radiation-resistance}

At 6th level, a blightburner becomes resistant to all forms of radiation, and can use the
radiation's energy as gathered power. She gains a bonus on saving throws to resist the effects of
radiation equal to her elemental overflow bonus. When she succeeds at a save against radiation, she
can reduce the total burn cost of a blast wild talent used before the end of her next turn as if she
had gathered power with a move action. Once she gains this benefit, she can't do so again for 1
minute, even if she's exposed to radiation again before that. She can't use this ability if she's
immune to poison or radiation. A blightburner gains an internal buffer at 11th level, and it has a
capacity as if she were 5 levels lower.

This ability alters gather power and internal buffer.
