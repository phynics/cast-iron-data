+++
id = "ref/arc-kineticist/blightburner"
kind = "archetype"
title = "Blightburner"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blightburner", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]

[fields]
kind = "archetype"
replaces = ["Basic geokinesis wild talent", "Utility wild talent gained at 2nd level", "Ability score boosts granted by elemental overflow", "earth's elemental defense"]
alters = ["Elemental focus", "Gather power", "internal buffer"]
+++

**Sources:** Heroes of the Darklands pg 25\
Darklands geokineticists sometimes exhibit supernatural powers associated with
[blightburn](ref/eq-material/blightburn) crystals. Blightburner kineticists harness this
radioactivity in pyrotechnic displays, an unusual feat for those connected to the element of earth.

**Earth Focus**

**Alters:** Elemental focus

**Info:** A blightburner must choose earth as her [elemental](ref/ability/elements) focus.

**Blightburn Manipulation (Su)**

**Flavor:** A blightburner can harness radiation for nondestructive purposes.

**Replaces:** _Basic geokinesis_ wild talent

**Standard:** A blightburner can channel blightburn radiation, causing herself to glow like a
[torch](ref/eq-misc/torch). This effect lasts until she dismisses it as another standard action.
Additionally, she can generate small amounts of heat with her hands. This radiation can slowly heat
unattended objects with a touch to a warm (but not painfully hot) temperature, or cook raw meat or
vegetable matter at a rate of 1 pound per minute. If used on a living creature, this ability deals 1
point of nonlethal damage per minute of contact, which manifests as reddened and blistering skin.

**Radiation Absorption (Su)**

**Ability:** Whenever a blightburner would take [ability damage](ref/rule/ability-damage-drain) from
radiation, she can accept 1 point of burn to reduce the ability damage by 4 points. Any remaining
ability damage is applied normally.

**Gained:** At 2nd Level

**Replaces:** Utility wild talent gained at 2nd level

**Blightburn Aura (Su)**

**Ability:** A blightburner's body surges with a greenish, radioactive glow whenever she accepts
burn. This energy sheds light like a [candle](ref/eq-misc/candle). A creature that hits the
blightburner with a natural attack, unarmed strike, or non-reach melee weapon attack while she's
under the effect of her _blightburn aura_ takes fire damage equal to her _elemental overflow_ bonus
(minimum 1). By accepting 2 points of burn, she can increase this damage by an amount equal to her
_elemental overflow_ bonus; she can increase the damage in this way up to four times. A blightburner
can temporarily suppress the visual effects of a _blightburn aura_ by concentrating for 1 full
round, but doing so also suppresses all of this ability's other benefits. The next time she uses a
wild talent, the visual effects and benefits return instantly.

**At 11th Level:** Whenever the kineticist has at least 5 points of burn, the _blightburn aura_
expands to a 10-foot-radius aura, and any creature that takes damage from it must also succeed at a
Fortitude save (DC = 10 + half the blightburner's level + her Constitution bonus) or be
[sickened](ref/misc/sickened) for 1 round. This ability is a poison effect.

**At 16th Level:** Whenever a blightburner has at least 7 points of burn, any creature that takes
damage from the _blightburn aura_ and fails its Fortitude save also become
[fatigued](ref/misc/fatigued).

**At 6th Level:** Whenever the blightburner has at least 3 points of burn, the _blightburn aura_
expands to fill all adjacent squares. In addition to damaging creatures that hit the blightburner
with melee attacks, the aura also deals damage to other creatures that end their turns within the
aura.

**Gained:** At 2nd Level

**Replaces:** Ability score boosts granted by elemental overflow, earth's elemental defense

**Special:** The blightburner can still gain elemental defenses from other elements with _expanded
defense._

**Radiation Resistance (Su)**

**Ability:** A blightburner becomes resistant to all forms of radiation, and can use the radiation's
energy as gathered power. She gains a bonus on saving throws to resist the effects of radiation
equal to her _elemental overflow_ bonus. When she succeeds at a save against radiation, she can
reduce the total burn cost of a blast wild talent used before the end of her next turn as if she had
gathered power with a move action. Once she gains this benefit, she can't do so again for 1 minute,
even if she's exposed to radiation again before that. She can't use this ability if she's immune to
poison or radiation.

**Alters:** Gather power, internal buffer

**At 11th Level:** A blightburner gains an _internal buffer_ at 11th level, and it has a capacity as
if she were 5 levels lower.

**Gained:** At 6th Level
