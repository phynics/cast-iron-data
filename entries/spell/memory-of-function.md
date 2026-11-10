+++
id = "ref/spell/memory-of-function"
kind = "spell"
title = "Memory of Function"
aon = "SpellDisplay.aspx?ItemName=Memory%20of%20Function"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "memory_of_function", path = "json/spells14.json" },
]
[[sources]]
publication = "technology-guide"
page = "10"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (powdered skymetal worth 10,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "object or construct touched" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Cleric, Oracle, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (powdered skymetal worth 10,000 gp)
Range: touch
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: object or construct touched
:::

Even a broken object remembers what it means to be a functioning whole. You restore a broken object
or damaged construct to a functional state, as if it were new and intact. Any pieces missing from
the object or construct remain missing. Significant missing pieces may prevent proper functioning.
If the object uses charges, the object becomes fully charged. A timeworn object becomes fully
charged, but doesn't lose the timeworn condition (this spell is one of the few ways a timeworn item
can be recharged). For 1 hour after this spell is cast on a timeworn object, that object does not
suffer any chance of glitching. Other consumables such as ammunition are not restored.

When this spell is cast upon a damaged construct, all hit point damage dealt to that construct is
healed. When this spell is cast upon a destroyed construct, it is restored to full functionality and
full hit points, provided no significant portion of the destroyed construct (such as an entire limb)
is missing. Constructs brought back in this fashion regain their memories up to the moment of their
destruction and have no particular inclination to serve the caster.

If you attempt to cast this spell on an object or a construct that has been destroyed for more than
10 years per caster level you possess, the spell fails.
