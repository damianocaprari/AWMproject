export default ({ app, $axios }, inject) => {
    /* gets ID of the resource for the given URL:
      example gets '1' from 'http://localhost:8000/api/users/1/'
     */
    function getResourceId (url) {
        let lastSlash = url.lastIndexOf('/')
        if (lastSlash <= 0) return null
        url = url.substring(0, lastSlash)
        if (url.lastIndexOf('/') <= 0) return null
        return url.substring(url.lastIndexOf('/') + 1, url.length)
    }
    app.getResourceId = getResourceId

    /* used in /account/edit.vue.OLD */
    async function getMySpells (myId) {
        console.log("getMySpells")
        let retval = {my_spells: [], characterclasses: [], spelltags: []}
        try {
            let query_spell = await $axios.$get(`/spells/`);
            let query_spelltags = await $axios.$get(`/spelltags/`);
            let query_characterclasses = await $axios.$get(`/characterclasses/`);

            if (query_spell.count > 0) {
                retval.my_spells = query_spell.results.filter(spell => {
                    return myId == getResourceId(spell.author)
                })

                if (retval.my_spells.length <= 0) return retval
                // -- Add casting_time value
                retval.my_spells.forEach(spell => {
                    let casting_time = "" + spell.casting_time_amount + " " + spell.casting_time_unit.toLowerCase()
                    spell['casting_time'] = casting_time
                })
                // -- Add tags in spells
                retval.my_spells.forEach(spell => {
                    if (spell.spell_additional_info != null) {
                        if (spell.spell_additional_info.tags != null) {
                            let tag_list = ""
                            for (var cnt in spell.spell_additional_info.tags) {
                                tag_list = tag_list.concat(spell.spell_additional_info.tags[cnt].tag)
                                tag_list = tag_list.concat(" ")
                            }
                            spell['tag_list'] = tag_list
                        } else
                            spell['tag_list'] = '-'
                    } else {
                        spell['tag_list'] = '-'
                    }
                })
                // -- Add classes name in spells
                retval.my_spells.forEach(spell => {
                    if (spell.classes != null) {
                        let class_list = ""
                        for (var cnt in spell.classes) {
                            for (var cl in query_characterclasses.results) {
                                var a = query_characterclasses.results[cl].url
                                if (a.match(spell.classes[cnt])) {
                                    class_list = class_list.concat(query_characterclasses.results[cl].name)
                                    class_list = class_list.concat(" ")
                                }
                            }
                        }
                        spell['class_list'] = class_list
                    }
                })
            }
            if (query_spelltags.count > 0) {
                let v = {text: "All", value: null}
                retval.spelltags.push(v)
                for (var i = 0; i < query_spelltags.count; i++) {
                    let v = {text: query_spelltags.results[i].tag, value: query_spelltags.results[i].tag}
                    retval.spelltags.push(v)
                }
            }
            if (query_characterclasses.count > 0) {
                let v = {text: "All", value: null}
                retval.characterclasses.push(v)
                for (var i = 0; i < query_characterclasses.count; i++) {
                    let v = {
                        text: query_characterclasses.results[i].name,
                        value: query_characterclasses.results[i].name
                    }
                    retval.characterclasses.push(v)
                }
            }
        } catch (e) {
            console.log('plugins/utils.js getMySpells() catch(e)', e);
        }
        return retval
    }
    app.getMySpells = getMySpells


    // -----------------------
    // ----- per MONSTERS -----
    async function getMyMonsters (myId) {
        console.log("getMyMonsters")
        let retval = {my_monsters: []}
        try {
            let query_monster = await $axios.$get(`/monsters/`);

            if (query_monster.count > 0) {
                retval.my_monsters = query_monster.results.filter(monster => {
                    return myId == getResourceId(monster.author)
                })

                if (retval.my_monsters.length <= 0) return retval
            }
        } catch (e) {
            console.log('plugins/utils.js getMyMonsters() catch(e)', e);
        }
        return retval
    }
    app.getMyMonsters = getMyMonsters

}
