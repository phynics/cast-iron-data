+++
id = "ref/spell/thorny-entanglement"
kind = "spell"
title = "Thorny Entanglement"
source_ids = ["core-rulebook", "mythic-adventures", "villain-codex", "advanced-class-guide", "legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thorny_entanglement", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "plants in a 40-ft.-radius spread" },
]
duration = "1 minute/level (D)"
saving_throw = "Reflex partial; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Druid, Hunter, Ranger, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: long (400 ft. + 40 ft./level)
Duration: 1 minute/level (D)
Saving throw: Reflex partial; see text
Spell resistance: no
Area: plants in a 40-ft.-radius spread
:::

## Entangle

**Sources:** PRPG Core Rulebook pg 278

This spell causes tall grass, weeds, and other plants to wrap around creatures in the area of effect
or those that enter the area. Creatures that fail their save gain the entangled condition. Creatures
that make their save can move as normal, but those that remain in the area must save again at the
end of your turn. Creatures that move into the area must save immediately. Those that fail must end
their movement and gain the entangled condition. Entangled creatures can attempt to break free as a
move action, making a Strength or Escape Artist check. The DC for this check is equal to the DC of
the spell. The entire area of effect is considered difficult terrain while the effect lasts.

If the plants in the area are covered in thorns, those in the area take 1 point of damage each time
they fail a save against the entangle or fail a check made to break free. Other effects, depending
on the local plants, might be possible at GM discretion.

### Mythic Entangle

**Sources:** Mythic Adventures pg 93

The spell functions in areas without any vegetation, causing plants to spring up out of the ground.
These plants can reach creatures that are up to 10 feet in the air. Plants affected or created by
the spell sprout thorns that deal 1d6 points of damage each round to creatures in the area.

### Burning Entanglement

**Sources:** Villain Codex pg 140

This spell functions as per entangle, except it sets the foliage on fire. A creature that begins its
turn entangled by the spell takes 4d6 points of fire damage (Reflex half), and a creature that
begins its turn in the area but is not entangled takes 2d6 points of fire damage (Reflex negates).
Smoke rising from the vines partially obscures visibility. Creatures can see things in the smoke
within 5 feet clearly, but attacks against anything farther away in the smoke must contend with
concealment (20% miss chance). When the spell's duration expires, the vines burn away entirely.

### Sickening Entanglement

**Sources:** Advanced Class Guide pg 192

This spell functions as entangle, except the plants are coated with an irritating sap that creates a
painful, itching rash on creatures that touch them. Any creature that enters the area or ends its
turn there must succeed at a Fortitude save or be sickened as long as it remains in the area and for
1d4 rounds afterward. This is a poison effect.

### Thirsting Entanglement

**Sources:** Legacy of the First World pg 17

This spell functions as entangle, except the plants latch on to targets and drain away their
vitality. Any creature that fails a save to avoid becoming entangled or fails a check to break free
takes 1d2 points of Constitution damage.

### Thorny Entanglement

**Sources:** Advanced Class Guide pg 196

This spell functions as entangle, except the plants also grow thorns and can fling them up to 15
feet. Any creature that moves within 15 feet of the spell's area is attacked once on its turn by the
animated plants. The plants use your caster level as their base attack bonus and add your
spellcasting ability score modifier (Intelligence for witches; Wisdom for druids, rangers, and
shamans) to the attack roll. A volley of thorns counts as a thrown weapon and deals 2d6 points of
piercing damage on a successful hit. A creature that enters the spell's area or ends its turn there
automatically takes 2d6 points of piercing damage.
