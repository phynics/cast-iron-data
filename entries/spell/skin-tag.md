+++
id = "ref/spell/skin-tag"
kind = "spell"
title = "Skin Tag"
aon = "SpellDisplay.aspx?ItemName=Skin%20Tag"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "skin_tag", path = "json/spells9.json" },
]
[[sources]]
publication = "haunted-heroes-handbook"
page = "28"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["emotion", "fear", "haunted", "mind-affecting"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 minute"
components = "V, S, M (beverage or food item, plus special reagents worth 25 gp)"
range = "touch (object); 1 mile (remote effects)"
effects = [
  { label = "Target", value = "1 beverage or piece of food touched" },
]
duration = "1 day plus 1 day/level (D)"
saving_throw = "none (object), Fortitude negates; see text"
spell_resistance = "no (object), yes (creature)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Alchemist, Arcanist, Medium, Occultist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 minute
Components: V, S, M (beverage or food item, plus special reagents worth 25 gp)
Range: touch (object); 1 mile (remote effects)
Duration: 1 day plus 1 day/level (D)
Saving throw: none (object), Fortitude negates; see text
Spell resistance: no (object), yes (creature)
Target: 1 beverage or piece of food touched
Descriptors: emotion, fear, haunted, mind-affecting
:::

You mix a malign spirit into a piece of food, a drink, or some other item to be consumed (including
alchemical items, potions, elixirs, or similar items). The skin tag spell discharges when the item
is consumed, affecting the creature that used the item unless it succeeds at a Fortitude save. The
spirit embeds itself somewhere in the affected creature's skin, forming a painless set of wrinkles
and tags of skin that looks vaguely like a face when the haunt activates. You are considered to have
a body part from the affected creature for the purpose of scrying and similar divination spells.
Once per day as a standard action, you can remotely cause the spirit to make the affected creature's
skin crawl, causing the creature to become sickened for 1d4 rounds + 1 round per 2 caster levels you
have (to a maximum of 5 extra rounds at 10th level) unless it succeeds at a Fortitude save.
Alternatively, once per day you can remotely use a hex, a mind-affecting spell, or a necromancy
spell that causes disease or possession on the affected creature. Each time you use the remote
sickening or spell or hex effect, the spell's haunt-like manifestation occurs during that round.

#### Haunt Statistics

**Notice:** Perception DC 20 (to taste a hint of rot) or DC 25 (if the affected creature is wearing
armor or heavy clothing)

**Hit points:** 5

**Trigger:** conditional (using the item or the spell's remote effects)

**Reset:** none
