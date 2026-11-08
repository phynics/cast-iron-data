+++
id = "ref/spell/soul-transfer"
kind = "spell"
title = "Soul Transfer"
source_ids = ["core-rulebook", "book-of-the-damned", "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soul_transfer", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/trap-the-soul" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action or see text"
components = "V, S, M (gem worth 1,000 gp per HD of the trapped creature)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent; see text"
saving_throw = "see text"
spell_resistance = "yes; see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 8: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action or see text
Components: V, S, M (gem worth 1,000 gp per HD of the trapped creature)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent; see text
Saving throw: see text
Spell resistance: yes; see text
Target: one creature
Subschool: Summoning
:::

## Trap the Soul

**Sources:** PRPG Core Rulebook pg 362

Trap the soul forces a creature's life force (and its material body) into a gem. The gem holds the
trapped entity indefinitely or until the gem is broken and the life force is released, which allows
the material body to reform. If the trapped creature is a powerful creature from another plane, it
can be required to perform a service immediately upon being freed. Otherwise, the creature can go
free once the gem imprisoning it is broken.

Depending on the version selected, the spell can be triggered in one of two ways.

_Spell Completion:_ First, the spell can be completed by speaking its final word as a standard
action as if you were casting a regular spell at the subject. This allows
[spell resistance](ref/rule/spell-resistance) (if any) and a Will save to avoid the effect. If the
creature's name is spoken as well, any spell resistance is ignored and the save DC increases by 2.
If the save or spell resistance is successful, the gem shatters.

_Trigger Object:_ The second method is far more insidious, for it tricks the subject into accepting
a trigger object inscribed with the final spell word, automatically placing the creature's soul in
the trap. To use this method, both the creature's name and the trigger word must be inscribed on the
trigger object when the gem is enspelled. A sympathy spell can also be placed on the trigger object.
As soon as the subject picks up or accepts the trigger object, its life force is automatically
transferred to the gem without the benefit of [spell resistance](ref/rule/spell-resistance) or a
save.

### Soul Transfer

**Sources:** Book of the Damned pg 186, Book of the Damned - Volume 3: Horsemen of the Apocalypse pg
39

This spell functions like [the spell completion option of trap the soul](ref/spell/trap-the-soul),
except it works only on bodiless souls (such as incorporeal undead or a soul trapped in a gem) and
creatures whose substance is a physical incarnation of a soul (such as a petitioner). It does not
work on creatures formed from souls or planar material (such as most outsiders). Soul transfer is
mainly used to transfer souls from one receptacle to another, but it can also be used to capture
vulnerable souls that aren't bound to mortal flesh (such as incorporeal creatures and petitioners).
When used to capture a petitioner, the petitioner's physical body vanishes, reappearing only when
its soul is released from the receptacle.
