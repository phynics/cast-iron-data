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
