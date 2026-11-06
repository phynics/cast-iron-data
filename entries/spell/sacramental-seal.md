+++
id = "ref/spell/sacramental-seal"
kind = "spell"
title = "Sacramental Seal"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacramental_seal", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
]
casting_time = "1 round"
components = "V, S, F (an object worth at least 2,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 8: Cleric, Oracle
Casting time: 1 round
Components: V, S, F (an object worth at least 2,000 gp)
Range: touch
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
:::

**Sources:** Horror Adventures pg 126

You trap the target in an object decorated with the holy symbols of your god or faith. While trapped
in the object, the creature can't take any actions and is immune to spells and
[spell-like abilities](ref/umr/spell-like-abilities). The creature remains permanently trapped in
the object as long the object remains in your possession. Only a [freedom](ref/spell/freedom),
[miracle](ref/spell/miracle), or [wish](ref/spell/wish) spell can dispel the enchantment, though
destroying the object frees the creature.

If you relinquish your stewardship of the object (such as giving it away or leaving it in a remote
location or extradimensional space), the trapped creature begins to gain control over the object. It
immediately gains the ability to communicate telepathically with any creature now in possession of
the object. It still can't take any actions besides communicating but can use feats and skills
related to speaking (such as Bluff and Diplomacy).

After 1 week of the object being out of your presence, the creature can create a number of haunts
with a total CR (that is, the CR of the encounter with all of the haunts at once) equaling 1/4 the
creature's Hit Dice. These haunts are centered on the object. The creature can also communicate
telepathically up to a range of 100 feet at this point.

After 1 month of the object being out of your presence, the CR total of the haunts the trapped
creature can create increases to 1/2 its Hit Dice. In addition to telepathy, it can also impart
mental images of its choosing into the mind of any creature holding or carrying the object.

After 1 year of being out of your presence, in addition to the above abilities, the creature can
attempt to possess any living creature with an Intelligence score of 3 or higher that touches the
object, as per possession. However, the creature can't personally destroy the object, even while
possessing another creature.

Because the binding magic irrevocably weakens the longer you're away from the item, returning it to
your ownership doesn't reverse any of the effects. You must free the creature and impose another
sacramental seal if you want to restrict its abilities again.

If the object is placed in the stewardship of creatures or a location belonging to your faith, it
still counts as being out of your presence but it takes ten times longer for the creature to
manifest the above abilities (it would take 10 weeks for it to manifest the ability to create
haunts, for example).
