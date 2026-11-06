+++
id = "ref/spell/mnemonic-siphon"
kind = "spell"
title = "Mnemonic Siphon"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mnemonic_siphon", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "10 minutes"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "1 day/level or until discharged (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Magus, Occultist\
4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S
Range: touch
Duration: 1 day/level or until discharged (D)
Saving throw: none
Spell resistance: no
Target: object touched
:::

**Sources:** Blood of the Ancients pg 28

You inscribe a rune on the target object. The rune remains dormant until the object finds its way
into the hands of a spellcaster, at which point the rune steals one of that creature's spells and
passes the knowledge back to you. The stolen spell is selected randomly. An object inscribed with
this rune is affected as though by the spell [magic aura](ref/spell/magic-aura). Additionally, if a
creature in possession of the object casts a spell that appears on your spell list, there is a 10%
chance that the mnemonic siphon absorbs that spell, causing it to fail as though it had been
successfully countered. Whenever the mnemonic siphon absorbs a spell in this fashion, it causes the
knowledge of the absorbed spell to appear directly in your mind. You can use this knowledge to
prepare the spell if you have an unused spell slot capable of casting it. You can also use the
knowledge to write the spell into a spellbook or teach it to your familiar. This knowledge remains
in your mind for 24 hours, after which time it is lost. The mnemonic siphon is capable of absorbing
up to 1 spell per 2 caster levels you have before being discharged. If you are not capable of
learning a stolen spell normally, the knowledge is useless to you.
