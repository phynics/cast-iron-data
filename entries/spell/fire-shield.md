+++
id = "ref/spell/fire-shield"
kind = "spell"
title = "Fire Shield"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fire_shield", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "evocation [fire or cold]"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (phosphorus for the warm shield; a firefly or glowworm for the chill shield)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation \[fire or cold\]
Level: 3: Summoner\
4: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Occultist, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (phosphorus for the warm shield; a firefly or glowworm for the chill shield)
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** PRPG Core Rulebook pg 282

This spell wreathes you in flame and causes damage to each creature that attacks you in melee. The
flames also protect you from either cold-based or fire-based attacks, depending on if you choose
cool or warm flames for your fire shield.

Any creature striking you with its body or a handheld weapon deals normal damage, but at the same
time the attacker takes 1d6 points of damage + 1 point per caster level (maximum +15). This damage
is either cold damage (if you choose a chill shield) or fire damage (if you choose a warm shield).
If the attacker has [spell resistance](ref/rule/spell-resistance), it applies to this effect.
Creatures wielding melee weapons with reach are not subject to this damage if they attack you.

When casting this spell, you appear to immolate yourself, but the flames are thin and wispy,
increasing the light level within 10 feet by one step, up to normal light. The color of the flames
is blue or green if the chill shield is cast, violet or red if the warm shield is employed. The
special powers of each version are as follows.

_Chill Shield:_ The flames are cool to the touch. You take only half damage from fire-based attacks.
If such an attack allows a Reflex save for half damage, you take no damage on a successful saving
throw.

_Warm Shield:_ The flames are warm to the touch. You take only half damage from cold-based attacks.
If such an attack allows a Reflex save for half damage, you take no damage on a successful saving
throw.

### Mythic Fire Shield

**Sources:** Mythic Adventures pg 94\
The damage dealt to your attackers increases to 1d8 points of damage + 1 point per caster level
(maximum +15). A chill shield gives you fire immunity. A warm shield gives you cold immunity.
