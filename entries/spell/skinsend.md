+++
id = "ref/spell/skinsend"
kind = "spell"
title = "Skinsend"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "skinsend", path = "json/spells9.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "238"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 minute"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Alchemist, Arcanist, Investigator, Occultist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 minute
Components: V, S
Range: personal
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

You cause your own skin to peel off your body and animate as a magical creature you control. You may
project your consciousness to your animated skin or return it to your actual body as a standard
action. When your consciousness is in your body, you are helpless (except for transferring your will
to your skin, or dismissing the spell).

Your possessed skin is identical to you in all ways, except the following: It has only half the
number of hit points you had at the time you cast the spell, and cannot be healed above this
maximum; construct type, traits, and immunities; Str 3, Con -; DR 10/piercing or slashing; and
[compression](ref/umr/compression). Your skin can take any actions you could normally take in your
own body (such as to fight or cast spells).

When your skin leaves your body, your body's hit points drop to 0. Your body cannot heal damage
naturally while you have no skin, nor do spells that cure hit point damage work on your body; only
regeneration (from a [regenerate](ref/spell/regenerate) spell,
[ring of regeneration](ref/magic-ring/ring-of-regeneration), the
[regeneration](ref/umr/regeneration) monster ability, or any other effect that can regrow missing
limbs) or heal can regrow your skin and allow you heal above 0 hit points.

If your body is regenerated before your skin returns to it, the skin dies and your consciousness
returns automatically to your body. Your skin can be preserved with
[gentle repose](ref/spell/gentle-repose) and is suitable for any purpose that requires some of your
flesh (such as a [resurrection](ref/spell/resurrection) spell) or any magic or ritual that requires
a creature's skin.

When your skin returns to your body, you regain hit points equal to your skin's remaining hit
points. If the spell ends before you reunite with your skin or if your skin is killed while you are
in your body, you remain helpless and at 0 hit points until your full body is restored to you
(requiring powerful magic, as described above). If your body dies while you are possessing your
skin, you die when the spell ends, regardless of how many hit points the skin has left. If your body
or skin is slain with your consciousness in it, the spell ends and you are instantly killed.

This spell leaves long scars on your skin where it split apart, although these fade normally with
the use of healing magic.
