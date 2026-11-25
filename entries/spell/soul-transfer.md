+++
id = "ref/spell/soul-transfer"
kind = "spell"
title = "Soul Transfer"
aon = "SpellDisplay.aspx?ItemName=Soul%20Transfer"
source_ids = ["book-of-the-damned", "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soul_transfer", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/trap-the-soul" },
]
[[sources]]
publication = "book-of-the-damned"
page = "186"
[[sources]]
publication = "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"
page = "39"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["summoning"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a gem worth 1,000 gp per HD of the targeted creature or soul)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one petitioner, incorporeal soul, or similar creature" },
]
duration = "permanent see text"
saving_throw = "Will negates"
spell_resistance = "yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Spiritualist\
7: Arcanist, Cleric, Oracle, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a gem worth 1,000 gp per HD of the targeted creature or soul)
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent see text
Saving throw: Will negates
Spell resistance: yes (see text)
Target: one petitioner, incorporeal soul, or similar creature
Subschool: summoning
:::

### Soul Transfer

This spell functions like [the spell completion option of trap the soul](ref/spell/trap-the-soul),
except it works only on bodiless souls (such as incorporeal undead or a soul trapped in a gem) and
creatures whose substance is a physical incarnation of a soul (such as a petitioner). It does not
work on creatures formed from souls or planar material (such as most outsiders). Soul transfer is
mainly used to transfer souls from one receptacle to another, but it can also be used to capture
vulnerable souls that aren't bound to mortal flesh (such as incorporeal creatures and petitioners).
When used to capture a petitioner, the petitioner's physical body vanishes, reappearing only when
its soul is released from the receptacle.
