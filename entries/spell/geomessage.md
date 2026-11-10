+++
id = "ref/spell/geomessage"
kind = "spell"
title = "Geomessage"
aon = "SpellDisplay.aspx?ItemName=Geomessage"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "geomessage", path = "json/spells13.json" },
]
[[sources]]
publication = "villain-codex"
page = "237"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 minute"
components = "V, S, M (a scrap of vellum)"
range = "touch"
effects = [
  { label = "Target", value = "surface touched" },
]
duration = "1 day/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Bard, Hunter, Medium, Occultist, Ranger, Skald\
4: Arcanist, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S, M (a scrap of vellum)
Range: touch
Duration: 1 day/level
Saving throw: none
Spell resistance: no
Target: surface touched
Subschool: Figment
:::

You create a written message of 50 words or fewer, or else an image, a drawing, or a similar
diagram. The figment hangs invisible and obscured upon the target surface for the duration of the
spell. Another casting of geomessage is needed to cause the figment to arrange itself into the
intended message.

When you cast the spell, you can choose to incorporate a passphrase into the spell. If you do so,
the message is protected as if nondetection had been cast on it for the full duration of the spell,
though creatures that cast geomessage on the surface and speak the passphrase ignore the
nondetection effect and cause the image to become visible until the caster speaks the passphrase
again.

Without a passphrase, the message simply remains invisible to those who cast geomessage. Detection
methods like detect magic and see invisibility indicate the message's presence but do not reveal its
contents.
